from django import forms
from .models import *



class StorageForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        
        
class LoginForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = '__all__'
