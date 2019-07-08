from django.db import models

class User(models.Model):
    email = models.CharField(max_length=225, unique=True)
    nickname = models.CharField(max_length=225, unique=True)

    def __str__(self):
        return self.email


class ChatRoom(models.Model):
    user1 = models.ForeignKey(User, related_name='user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='user2', on_delete=models.CASCADE)
    roomname = models.CharField(max_length=225)
    channel_url = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.roomname


class Message(models.Model):
    channel = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    message = models.TextField()
    message_id = models.CharField(max_length=225)

    
    def __str__(self):
        return self.message_id