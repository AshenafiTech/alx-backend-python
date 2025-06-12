from django.contrib.auth import get_user_model
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Message

@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_user(request):
    """Allow a user to delete their own account."""
    user = request.user
    user.delete()
    return Response({"detail": "User account deleted."}, status=status.HTTP_204_NO_CONTENT)

def get_conversation_with_threads(conversation_id):
    """
    Fetch all top-level messages in a conversation, with sender/receiver and replies prefetched.
    """
    messages = (
        Message.objects
        .filter(conversation_id=conversation_id, parent_message__isnull=True)
        .select_related('sender', 'receiver')
        .prefetch_related('replies__sender', 'replies__receiver')
    )
    return messages

def get_thread_queryset(message):
    """
    Recursively fetch all replies to a message using Django ORM.
    """
    replies = Message.objects.filter(parent_message=message).select_related('sender', 'receiver')
    thread = []
    for reply in replies:
        thread.append({
            'message': reply,
            'replies': get_thread_queryset(reply)
        })
    return thread

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def send_message(request):
    """
    Send a message, optionally as a reply (threaded).
    """
    content = request.data.get('content')
    receiver_id = request.data.get('receiver')
    parent_message_id = request.data.get('parent_message')
    if not content or not receiver_id:
        return Response({'error': 'Content and receiver are required.'}, status=status.HTTP_400_BAD_REQUEST)
    message = Message.objects.create(
        sender=request.user,
        receiver_id=receiver_id,
        content=content,
        parent_message_id=parent_message_id if parent_message_id else None
    )
    return Response({'detail': 'Message sent.', 'message_id': message.id}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def unread_messages(request):
    """
    Display only unread messages for the authenticated user, optimized with .only().
    """
    unread = Message.unread.for_user(request.user)
    data = [
        {
            "id": msg.id,
            "sender": msg.sender_id,
            "content": msg.content,
            "timestamp": msg.timestamp,
        }
        for msg in unread
    ]
    return Response(data)