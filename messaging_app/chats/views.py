from django.shortcuts import render
from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied # For HTTP_403_FORBIDDEN
from django_filters.rest_framework import DjangoFilterBackend # Import DjangoFilterBackend

from .models import Conversation, Message, CustomUser
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsParticipantOrSender
from .filters import MessageFilter # Import your custom filter
from .pagination import StandardMessagePagination # Import your custom pagination

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated, IsParticipantOrSender]
    filter_backends = [filters.SearchFilter]
    search_fields = ['participants__username', 'participants__email']

    def create(self, request, *args, **kwargs):
        participant_ids = request.data.get('participants', [])
        if not participant_ids:
            return Response({'detail': 'Participants are required.'}, status=status.HTTP_400_BAD_REQUEST)
        conversation = Conversation.objects.create()
        users = CustomUser.objects.filter(user_id__in=participant_ids)
        conversation.participants.set(users)
        conversation.save()
        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return user.conversations.all()
        return Conversation.objects.none()

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-sent_at') # Change 'created_at' to 'sent_at'
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOrSender]
    
    # Pagination
    pagination_class = StandardMessagePagination # Apply your custom pagination

    # Filtering and Searching
    filter_backends = [DjangoFilterBackend, filters.SearchFilter] # Add DjangoFilterBackend
    filterset_class = MessageFilter # Specify your custom filter class
    search_fields = ['message_body', 'sender__username'] # Keep existing search functionality

    def create(self, request, *args, **kwargs):
        conversation_id = request.data.get('conversation')
        message_body = request.data.get('message_body')
        if not conversation_id or not message_body:
            return Response({'detail': 'conversation and message_body are required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            conversation = Conversation.objects.get(conversation_id=conversation_id)
        except Conversation.DoesNotExist:
            return Response({'detail': 'Conversation not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.user not in conversation.participants.all():
            raise PermissionDenied("You are not a participant in this conversation and cannot send messages here.")

        message = Message.objects.create(
            conversation=conversation,
            sender=request.user,
            message_body=message_body
        )
        serializer = self.get_serializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Message.objects.filter(conversation__participants=user).distinct().order_by('-sent_at') # This one was likely changed correctly
        return Message.objects.none()

    def perform_create(self, serializer):
        conversation = serializer.validated_data.get('conversation')
        if self.request.user not in conversation.participants.all():
            raise PermissionDenied("You are not a participant in this conversation.")
        serializer.save(sender=self.request.user)
