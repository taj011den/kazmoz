from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Moving

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moving
        fields = '__all__'




