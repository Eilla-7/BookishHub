from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class DiscussionRoom(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='discussion_rooms')

class Message(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='messages')
    discussion_room = models.ForeignKey(DiscussionRoom, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



