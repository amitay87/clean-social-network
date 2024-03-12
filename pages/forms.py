# yourappname/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from pages.models import CustomUser


class SignUpForm(UserCreationForm):
    # Add custom fields if needed
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

class LogInForm(AuthenticationForm):
    pass
