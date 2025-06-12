from django.contrib.auth import get_user_model
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Message

@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_user(request):
    user = request.user
    user.delete()
    return Response({"detail": "User account deleted."}, status=status.HTTP_204_NO_CONTENT)


def get_conversation_with_threads(conversation_id):
    # Fetch all messages in a conversation, with sender/receiver and replies prefetched
    messages = (
        Message.objects
        .filter(conversation_id=conversation_id, parent_message__isnull=True)
        .select_related('sender', 'receiver')
        .prefetch_related('replies__sender', 'replies__receiver')
    )
    return messages

def get_thread(message):
    """Recursively get all replies for a message."""
    thread = []
    for reply in message.replies.all():
        thread.append({
            'message': reply,
            'replies': get_thread(reply)
        })
    return thread