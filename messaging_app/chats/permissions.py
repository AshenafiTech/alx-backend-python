class IsOwnerOrParticipant(permissions.BasePermission):
    """
    Custom permission to only allow users to access their own messages or conversations.
    """
    def has_object_permission(self, request, view, obj):
        # For Message: sender or receiver
        if hasattr(obj, 'sender') and hasattr(obj, 'receiver'):
            return obj.sender == request.user or obj.receiver == request.user
        # For Conversation: participant
        if hasattr(obj, 'participants'):
            return request.user in obj.participants.all()
        return False
from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.participants.all()

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class IsMessageParticipantAndSafeOrUnsafe(permissions.BasePermission):
    """
    Only participants in a conversation can send, view, update, or delete messages.
    """
    def has_object_permission(self, request, view, obj):
        # Only allow if user is a participant in the conversation
        is_participant = request.user in obj.conversation.participants.all()
        if request.method in ["GET", "PUT", "PATCH", "DELETE", "POST"]:
            return is_participant
        return False