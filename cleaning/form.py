from django import forms

from .models import  Cleaning






class CleaningForm(forms.ModelForm):
    class Meta:
        model = Cleaning
        fields='__all__'