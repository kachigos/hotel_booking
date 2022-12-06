from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(forms.ModelForm):
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(), label='Введите пароль')
    password_confirmation = forms.CharField(min_length=8, widget=forms.PasswordInput(), label='Повторите пароль')

    class Meta:
        model = User
        fields = ['first_name', 'email', 'password', 'password_confirmation']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('User with such email already exists')
        return email

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password_confirm = data.pop('password_confirmation')
        if password != password_confirm:
            raise forms.ValidationError('Invalid password')
        return data

    def save(self, commit=True):
        user = User.objects.create(**self.cleaned_data)
        return user


# class UserLoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(),label='email')
#     password = forms.CharField(widget=forms.PasswordInput(),label='username')
