from django.db import models

class UnreadMessagesManager(models.Manager):
    """Manager to filter unread messages for a user, optimized with .only()."""
    def for_user(self, user):
        return self.get_queryset().filter(receiver=user, read=False).only('id', 'sender', 'content', 'timestamp')