from django import forms
from django.forms import ModelForm
from .models import Register

class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = [
            'firstname', 'lastname', 'email', 'programe_option',
        ]

