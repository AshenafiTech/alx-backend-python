import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    Adds extra fields: user_id (UUID primary key), phone_number.
    """
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    # email, password, first_name, last_name are already included in AbstractUser

    def __str__(self):
        return self.username

class Conversation(models.Model):
    """
    Model to track which users are involved in a conversation.
    """
    conversation_id = models.AutoField(primary_key=True)
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        usernames = ', '.join([user.username for user in self.participants.all()])
        return f"Conversation {self.conversation_id} between {usernames}"

class Message(models.Model):
    """
    Message model containing sender and conversation.
    """
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} at {self.timestamp}"