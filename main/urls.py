
from django.urls import path , include 
from . import views  
from . import api  

app_name = 'main'

urlpatterns = [
    path('',views.main_detail, name='main'),
    path('about/',views.about, name='about'),
]
