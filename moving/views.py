from django.shortcuts import render ,redirect
from django.urls import reverse 
from .models import Moving
from django.core.paginator import Paginator
from .form import  MovingForm
from django.contrib.auth.decorators import login_required



def moving_detail(request):
    print('done')    
    moving_detail = Moving.objects.all()

    return render(request,'moving/moving.html', {'moving': moving_detail})
