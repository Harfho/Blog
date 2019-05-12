from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from . import views

# from django.contrib.auth import views as auth_view

app_name = "user"

urlpatterns = [
    path('register/',views.register,name = "register"),
    path('login/',views.loginUser,name = "login"),
    path('logout/',views.logoutUser,name = "logout"),
    path('profile/',views.profile,name = "profile"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)