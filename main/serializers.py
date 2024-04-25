from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Main

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = '__all__'




