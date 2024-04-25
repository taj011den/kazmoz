from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User



# Create your models here.



def image_upload(instance,filename):
    imagename,extension = filename.split(".")
    return "demolishs/%s.%s"%(instance.id,extension)



      
class Demolish(models.Model):   
    # New Address fields
    
    id = models.AutoField(primary_key=True)
   # street = models.CharField(max_length=200, verbose_name='Street and House Number')
   # zipcode = models.CharField(max_length=10, verbose_name='ZIP Code')
  #  city = models.CharField(max_length=100, verbose_name='City')
 #   country = models.CharField(max_length=100, verbose_name='Country')
    # Contact information fields
  #  payment_by = models.CharField(max_length=20, verbose_name='Who pays for the demolish?')
    full_name = models.CharField(max_length=200, verbose_name='First and Last Name')
    email = models.EmailField(verbose_name='Email Address')
    phone = models.CharField(max_length=20, verbose_name='Phone Number')
    created_at = models.DateTimeField(auto_now=True)
    note = models.CharField( max_length=1000 , verbose_name='Enter Your Notic')

    def __str__(self):
        return f"{self.full_name} ({self.created_at})"


    

