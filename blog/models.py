from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

# Create your models here.

class User(AbstractUser):
    pass

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    contents = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Article, default=None, on_delete=models.CASCADE)

class Reading_List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    savedpost = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['user', 'savedpost']]