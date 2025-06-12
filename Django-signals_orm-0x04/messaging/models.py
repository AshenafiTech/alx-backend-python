from django.db import models
from django.conf import settings
from .managers import UnreadMessagesManager

class Message(models.Model):
    """Model representing a message, supporting threads and edit tracking."""
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    edited_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='edited_messages',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    parent_message = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='replies',
        on_delete=models.CASCADE
    )
    read = models.BooleanField(default=False)

    objects = models.Manager()  # Default manager
    unread = UnreadMessagesManager()  # Custom manager

    def __str__(self):
        return f"From {self.sender} to {self.receiver} at {self.timestamp}"

class Notification(models.Model):
    """Stores notifications for users about messages."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='notifications', on_delete=models.CASCADE
    )
    message = models.ForeignKey(
        Message, related_name='notifications', on_delete=models.CASCADE
    )
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user} about message {self.message.id}"

class MessageHistory(models.Model):
    """Keeps a history of message edits."""
    message = models.ForeignKey(Message, related_name='history', on_delete=models.CASCADE)
    old_content = models.TextField()
    edited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History for message {self.message.id} at {self.edited_at}"