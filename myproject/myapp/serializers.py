from rest_framework import serializers
from .models import Message
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email")



class MessageSerializer(serializers.ModelSerializer):
    username = UserSerializer()
    class Meta:
        model = Message
        fields = ('id' ,'username')

