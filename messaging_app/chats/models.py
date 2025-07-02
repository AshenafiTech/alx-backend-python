import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Custom user model extending Django's AbstractUser with extra fields."""
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    # password, first_name, last_name are already included in AbstractUser

class Conversation(models.Model):
    """Tracks which users are involved in a conversation."""
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.pk} between {[user.username for user in self.participants.all()]}"

class Message(models.Model):
    """Message model containing sender and conversation."""
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} at {self.timestamp}"