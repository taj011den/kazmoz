from django import forms

from .models import  Moving






class MovingForm(forms.ModelForm):
    class Meta:
        model = Moving
        fields='__all__'