
from django.urls import path , include 
from . import views  
from . import api  

app_name = 'cleaning'

urlpatterns = [
    path('',views.cleaning_detail, name='cleaning'),
]
