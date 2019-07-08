from django.contrib import admin
from . models import User, ChatRoom, Message

@admin.register(User)
class ApiAdmin(admin.ModelAdmin):
    list_display = ('email', 'nickname')

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('user1', 'user2', 'roomname', 'channel_url')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('channel', 'sender', 'message', 'message_id')
