from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import serializers
from . models import User, ChatRoom, Message


class ChatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ('id', 'user1', 'user2', 'roomname', 'channel_url', 'created_at')
        depth=1

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('channel', 'sender', 'message', 'message_id', 'created_at')
        depth = 2
