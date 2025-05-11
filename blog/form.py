from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser# forms.py




class CustomUserForm(forms.ModelForm):
    class Meta:
        fields = ['username', 'email', 'password']



class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'address', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass  # No need to override, Django handles login validation

