from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = "User_name")
    password = forms.CharField(label = "Password",widget = forms.PasswordInput)


class RegisterForm(forms.Form):
    username  = forms.CharField(max_length = 50,label = "User_name")
    email = forms.EmailField(required=False,label='email')
    password = forms.CharField(max_length=20,label = "Password",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label ="Confirm_Password",widget = forms.PasswordInput)
    
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


