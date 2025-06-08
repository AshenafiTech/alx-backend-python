from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        participants = request.data.get('participants', [])
        if not participants:
            return Response({'error': 'Participants are required.'}, status=status.HTTP_400_BAD_REQUEST)
        conversation = Conversation.objects.create()
        conversation.participants.set(participants)
        conversation.save()
        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        conversation_id = request.data.get('conversation')
        message_body = request.data.get('message_body')
        if not conversation_id or not message_body:
            return Response({'error': 'conversation and message_body are required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            conversation = Conversation.objects.get(pk=conversation_id)
        except Conversation.DoesNotExist:
            return Response({'error': 'Conversation does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        message = Message.objects.create(
            conversation=conversation,
            sender=request.user,
            message_body=message_body
        )
        serializer = self.get_serializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)