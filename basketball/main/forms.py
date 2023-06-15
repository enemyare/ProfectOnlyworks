from django import forms
from django.forms import ModelForm
from .models import userProfile, Myteam
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

class UserProfileForm(ModelForm):
    class Meta:
        model = userProfile
        fields = '__all__'
        exclude = ['user']


class UserMyteamForm(ModelForm):
    class Meta:
        model = Myteam
        fields = '__all__'
        exclude = ['user']
