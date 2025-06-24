from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class UserModel(models.Model):
    FirstName=models.CharField(max_length=100,null=False)
    LastName=models.CharField(max_length=100,null=False)
    EmailId=models.CharField(max_length=100,null=False,primary_key=True)
    PhoneNo=models.CharField(max_length=100,null=False,unique=True)
    Password=models.CharField(max_length=100,null=False)

class AdminModel(models.Model):
    adminEmailId=models.CharField(max_length=100,primary_key=True)
    adminPassword=models.CharField(max_length=100,null=False)
    adminName=models.CharField(max_length=100)
    adminPhoneno=models.CharField(max_length=20,null=False)

class PostModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)