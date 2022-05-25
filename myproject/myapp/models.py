from django.db import models
from django.contrib.auth.models import User
from rest_framework.response import Response
# Create your models here.

class Message(models.Model):
    message = models.CharField(max_length=2000,null=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE,related_name='name')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def created_by(self):
        username= self.username.username
        id = self.username.id
        email = self.username.email
        create= {
             id,
             username,
             email
        }
        return self.username


