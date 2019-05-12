from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from . import views


app_name = "article"

urlpatterns = [
    
    path('',views.articles,name = "articles"),
    
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('addarticle/',views.addArticle,name = "addarticle"),
    path('contact/',views.contact,name = "contact"),

    path('article/<int:id>',views.detail,name = "detail"),
    path('update/<int:id>',views.updateArticle,name = "update"),
    path('delete/<int:id>',views.deleteArticle,name = "delete"),
    path('comment/<int:id>',views.addComment,name = "comment"),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)