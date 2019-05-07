from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Author ")
    title = models.CharField(max_length =10000,verbose_name = "Title")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Created on")
    article_image = models.FileField(blank = True,null = True,verbose_name="Add article photo")
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Article",related_name="comments")
    comment_author = models.CharField(max_length = 1000,verbose_name = "Name")
    comment_content = models.CharField(max_length = 10000,verbose_name = "comments")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)


