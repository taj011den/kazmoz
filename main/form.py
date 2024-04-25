from django import forms

from .models import  Main,About






class MainForm(forms.ModelForm):
    class Meta:
        model = Main
        fields='__all__'
        
        
class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields='__all__'