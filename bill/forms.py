from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from captcha.fields import CaptchaField
from .models import cosutomer_detailes
class myc(forms.Form):

    username = forms.CharField(max_length=100,required=True,)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)
    captcha=CaptchaField(required=True)

class signp(forms.Form):
    username = forms.CharField(max_length=100,required=True,)
    email=forms.EmailField( max_length=254,required=True,)
    password = forms.CharField(widget=forms.PasswordInput(),required=True,)
    password1 = forms.CharField(widget=forms.PasswordInput(),required=True,)
    captcha = CaptchaField(required=True)


