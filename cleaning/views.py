from django.shortcuts import render ,redirect
from django.urls import reverse 
from .models import Cleaning
from django.core.paginator import Paginator
from .form import  CleaningForm
from django.contrib.auth.decorators import login_required



def cleaning_detail(request):
    print('done')    
    cleaning_detail = Cleaning.objects.all()

    return render(request,'cleaning/cleaning.html', {'cleaning': cleaning_detail})
