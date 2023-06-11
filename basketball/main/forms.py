from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        try:
            self.user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError(f'Пользователь с именем {username} не существует')

        if not self.user.check_password(password):
            raise forms.ValidationError(f'Пароля для пользователя с именем {username} не существует')


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['email'].required = True
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'enter'
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }

# class UserLoginForm(UserCreationForm):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'}))
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}))
#     class Meta:
#         model = User
#         fields = ('email','username','password1', 'password2')


