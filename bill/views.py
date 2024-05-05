from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from.forms import myc,signp
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import *
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User

def land(request):
    return render(request,'bill/lanading.html')
@login_required(login_url='bill login')
def home(request):
    a=str(request.user)
    f= cosutomer_detailes.objects.all().filter(username=request.user)

    context={'a': a ,'f': f}
    return render(request,'bill/index.html',context)

@login_required()
def user_bill(request):

    f=cosutomer_detailes.objects.all().filter(username=request.user)
    r=reading.objects.all().filter(user=request.user)




    context={'a' : f,'q' : r}
    return render(request,'bill/Bill.html',context)

def pay(request):
    return render(request,'bill/payment.html')

def about(request):
    return render(request,'bill/about.html')



def login1(request):
    if request.method=='POST':
        
        form=myc(request.POST)
        
        if form.is_valid():
            
            username = request.POST['username']
            pass1 = request.POST['password']
            userr=authenticate(request,username=username,password=pass1)

            
            if username:
                login(request,userr)
                return redirect('index')


            else:
                messages.error(request,'invalid username or password')
                return redirect('bill login')
        else:
            messages.error(request,'Captcha is invalid')
            return redirect('bill login')
    
    

    form=myc()
    return render (request,'bill/login22.html',{'form':form})
  


def signup(request):

    if request.method=='POST':
        form = signp(request.POST)

        if form.is_valid():
            # user = form.save()

            uname=request.POST['username']
            email=request.POST['email']
            pass1=request.POST['password']
            pass2=request.POST['password1']

            if pass1!=pass2:
                messages.error(request, "Your password and confromation password are not Same!!")
            else:

                my_user=User.objects.create_user(username=uname,email=email,password=pass1)
                my_user.save()
                return redirect('bill login')

        else:
            messages.error(request,'Captcha is invalid')
            return redirect('bill login')

    form = signp()
    return render(request,'bill/signup.html',{'form':form})

def LogoutPage(request):
    logout(request)
    return redirect('bill login')

def entryy(request):
    if request.method == 'POST':

        meter_numm=request.POST.get('meter')
        username=request.POST.get('username')
        name=request.POST.get('name')
        add=request.POST.get('add')
        mail = request.POST.get('email')
        num=request.POST.get('mobile')
        pan=request.POST.get('pan')
        gst=request.POST.get('gst')
        ty=request.POST.get('ty')
        if request.user.email!=mail:
            messages.error(request, 'Please enter correct email ')

            return render(request, 'bill/bc.html')


        if str(request.user)!= username:


            messages.error(request,'Please enter correct username ')

            return render(request, 'bill/bc.html')

        else:
            ins=cosutomer_detailes(username=username,meter_num=meter_numm,name=name,address=add,email=mail,mobile_num=num,pan=pan,gst=gst,ty=ty)
            cosutomer_detailes.save(self=ins)

            return render(request, 'bill/index.html')

    return render(request, 'bill/bc.html')





