from django.db import models


class ChatList(models.Model):
    room = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
