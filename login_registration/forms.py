from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        "class": "input",
        'required': True
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input",
        'required': True
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input",
        'required': True
    }))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_username(self):
        data = self.cleaned_data['username']
        return data.lower()



class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Логин"
        self.fields['password'].label = "Пароль"

    def clean_username(self):
        data = self.cleaned_data['username']
        return data.lower()
