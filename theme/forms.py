from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email','password1', 'password2',]
        
class CustomAuthenticationForm(AuthenticationForm):
     class Meta:
        model = CustomUser
        fields = ['email', 'password',]