from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.


Id = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
)


def image_upload(instance,filename):
    imagename,extension = filename.split(".")
    return "mains/%s.%s"%(instance.id,extension)


class Main(models.Model):   
    id = models.IntegerField(primary_key=True)
    serviceurl = models.CharField(max_length=100)
    title = models.CharField(max_length=100) 
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to=image_upload)
    

    def __str__ (self):
        return self.title
    
    
class About(models.Model):
    name = models.CharField(max_length=100) 
    
    phone = models.CharField(max_length=20, verbose_name='Phone Number')
    
    
    
    def __str__ (self):
        return self.name