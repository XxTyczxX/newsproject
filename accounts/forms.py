# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # 含めるフィールドを明示的に指定
        fields = ('username', 'email', 'password1', 'password2')

