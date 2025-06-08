from rest_framework import permissions

class IsParticipantOrSender(permissions.BasePermission):
    """
    Custom permission to only allow participants of a conversation or sender of a message to access it.
    """

    def has_object_permission(self, request, view, obj):
        # For Conversation objects
        if hasattr(obj, 'participants'):
            return request.user in obj.participants.all()
        # For Message objects
        if hasattr(obj, 'sender'):
            return obj.sender == request.user or request.user in obj.conversation.participants.all()
        return False