from django.contrib import admin
from django.urls import path
from . import views

# from django.contrib.auth import views as auth_view

app_name = "user"

urlpatterns = [
    path('register/',views.register,name = "register"),
    path('login/',views.loginUser,name = "login"),
    path('logout/',views.logoutUser,name = "logout"),
    
    # path('password-reset',
    #         auth_view.PasswordResetDoneView.as_view(
    #                 template_name='articles/password_reset.html'), 
    #         name = "password_reset"),

    
    # path('password-reset/done',
    #         auth_view.PasswordResetDoneView.as_view(
    #                 template_name='articles/password_reset_done.html'), 
    #         name = "password_reset_done"),

]
