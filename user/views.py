from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

from .forms import RegisterForm,LoginForm


from django.db import IntegrityError


# Create your views here.

def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        newUser = User(username =username,email=email)
        newUser.set_password(password)

        try:
            newUser.save()
        except IntegrityError as e: 
            if 'unique constraint' in str(e).lower(): # or e.args[0] from Django 1.10
                # login.error('Duplicated item')
                messages.info(request,"Sorry there is a user with the name '{}' ".format(newUser))
                return redirect("/user/register/")

        else:
            newUser.save()
            login(request,newUser)
        
            messages.info(request,"You have successfully Registered...")

            return redirect("/articles/dashboard")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)

    
    
def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"User_name or Password is incorrect")
            return render(request,"login.html",context)

        messages.success(request,"Log in successfully")
        login(request,user)
        return redirect("/articles")
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Logout Successfully ")
    return redirect("index")

