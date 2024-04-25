from django.shortcuts import render ,redirect
from django.urls import reverse 
from .models import Main,About
from django.core.paginator import Paginator
from .form import  MainForm
from django.contrib.auth.decorators import login_required



def main_detail(request):
    print('done')    
    main_detail = Main.objects.all()

    return render(request,'main/main.html', {'main': main_detail})


def about(request):
    about=About.objects.all()
    return render(request,'main/about.html',{'about':about})