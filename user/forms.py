from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(label = "User-name")
    password = forms.CharField(label = "Password",widget = forms.PasswordInput)


class RegisterForm(forms.Form):
    username  = forms.CharField(max_length = 100,label = "User-name")
    email = forms.EmailField(required=False,label='Email')
    password = forms.CharField(max_length=20,label = "Password",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label ="Confirm-Password",widget = forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Password Don't matched")

        values = {
            "username" : username,
            "email":email,
            "password" : password,
        }
        return values


class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField(required=False)
    
    class Meta:
        model = User
        fields = ['username','email',]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']    