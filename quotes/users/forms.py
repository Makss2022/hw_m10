from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))

    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password confirmation"}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = UsernameField(
        max_length=254,
        widget=forms.TextInput(attrs={
            'autofocus': True,
            "class": "form-control",
            "placeholder": "Username"}),
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}),
    )

    class Meta:
        model = User
        fields = ['username', 'password']
