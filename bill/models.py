from django.db import models
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group

@receiver(post_save, sender=User)
def add_user_to_group(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        group = Group.objects.get(name='employee')
        instance.groups.add(group)
        if instance.is_superuser:
            instance.is_superuser = False
            instance.save()
            instance.is_staff = True
            instance.save()
class cosutomer_detailes(models.Model):

    username = models.CharField(max_length=20,default="",primary_key=True)
    meter_num=models.CharField(max_length=12)
    name=models.CharField(max_length=50,null=True)
    address=models.TextField(max_length=150,null=True)
    email=models.EmailField( max_length=254,null=True,default="")
    mobile_num=models.CharField(max_length=10,null=True)
    pan=models.CharField(max_length=10,null=True)
    gst=models.CharField(max_length=15,null=True)
    ty=models.CharField(max_length=10,null=True)

class employee_detailes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=False)
    employeee_id = models.CharField(max_length=12, primary_key="True")
    name = models.CharField(max_length=50, null=True)
    address = models.TextField(max_length=150, null=True)
    email = models.EmailField(max_length=254, null=True, default="")
    mobile_num = models.CharField(max_length=10, null=True)
    qualification = models.CharField(max_length=20, null=False)
    data_added = models.BooleanField(default=False)


@receiver(post_save, sender=employee_detailes)
def restrict_user_data_addition(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        if not user.is_superuser and not instance.data_added:
            instance.data_added = True

            instance.save()
        else:
            instance.data_added = False
            instance.save()

class reading(models.Model):
    bill_number = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=False)
    user_name = models.ForeignKey(cosutomer_detailes, on_delete=models.CASCADE,default="")
    r_date=models.DateField(default='dd-mm-yyyy',null=False)
    reading=models.FloatField()
    price=models.FloatField(default=True)
    total=models.FloatField(editable=False, null=True, blank=True)
    paid = models.BooleanField(default=False)


    def __str__(self):
        return (f'Bill number  {self.bill_number}   whos owner is    {self.user} whos total bill is {self.total} {self.paid} ')





