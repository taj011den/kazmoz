from django import forms
from .models import  Demolish






class DemolishForm(forms.ModelForm):
    class Meta:
        model = Demolish
        fields='__all__'
        exclude = ('id',)
        
        

