from rest_framework import serializers
from . models import ChatList

class ChatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatList
        fields = ('room', 'created_at')

class ChatListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatList
        fields = ('room', 'created_at')

    def __init__(self, request, *args, **kwargs):
        super(ChatListCreateSerializer, self).__init__(self, request, *args, **kwargs)

        return print(self.context['request'])
    

