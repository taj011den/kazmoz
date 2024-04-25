from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Demolish

class DemolishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demolish
        fields = '__all__'




