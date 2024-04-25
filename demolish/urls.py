
from django.urls import path , include 
from . import views  
from . import api  

app_name = 'demolish'

urlpatterns = [
    path('',views.demolish_orders, name='demolish'),
    path('request_demolition/',views.request_demolition, name='request_demolition'),
    path('requests/',views.requests, name='requests'),
    path('requests/<int:id>',views.onerequest, name='onerequest'),
]
