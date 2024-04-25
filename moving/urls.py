
from django.urls import path , include 
from . import views  
from . import api  

app_name = 'moving'

urlpatterns = [
    path('',views.moving_detail, name='moving'),
]
