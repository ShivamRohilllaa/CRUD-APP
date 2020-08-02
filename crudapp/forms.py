from django.core import validators
from django import forms
from .models import User

#I make this using (Model Form Concept).
class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']    
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }
