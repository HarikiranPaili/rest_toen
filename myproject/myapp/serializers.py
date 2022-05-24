from rest_framework import serializers
from .models import Message
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email")



class MessageSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    def get_created_by(self, Message):
        return UserSerializer(Message.created_by(), many=True).data

    class Meta:
        model = Message
        fields = [
            'id',
            'message',
            'created',
            'updated',
            'created_by',
        ]