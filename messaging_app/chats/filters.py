import django_filters
from .models import Message, CustomUser

class MessageFilter(django_filters.FilterSet):
    # Filter messages that are part of a conversation involving a specific user (by user_id)
    conversation_participant = django_filters.ModelChoiceFilter(
        queryset=CustomUser.objects.all(),
        field_name='conversation__participants', # Checks if the user is in the message's conversation participants
        label='User ID of a participant in the conversation'
    )

    # Filter messages created after a certain datetime
    created_at_after = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    
    # Filter messages created before a certain datetime
    created_at_before = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Message
        fields = {
            'conversation': ['exact'], # Filter by exact conversation_id
            'sender': ['exact'],       # Filter by exact sender_id (user_id)
            # The custom filters are defined above
        }