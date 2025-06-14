from rest_framework import serializers
from .models import CustomUser, Conversation, Message
from django.contrib.auth import get_user_model # It's good practice to use get_user_model

User = get_user_model() # Use User consistently

class CustomUserSerializer(serializers.ModelSerializer):
    # full_name is fine for reading, but not needed for registration input
    full_name = serializers.SerializerMethodField(read_only=True) 
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User # Use the User variable
        fields = [
            'user_id', 'username', 'email', 'password', # Add password here
            'first_name', 'last_name', 'phone_number', 
            'bio', 'profile_picture', 'full_name'
        ]
        extra_kwargs = {
            'user_id': {'read_only': True},
            'full_name': {'read_only': True}, # Ensure full_name is also read_only
            # 'profile_picture': {'required': False, 'allow_null': True} # Example if it's optional
        }

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def create(self, validated_data):
        password = validated_data.pop('password')
        # Remove fields that are not part of the CustomUser model directly 
        # or are handled by SerializerMethodField if they sneak into validated_data
        validated_data.pop('full_name', None) # full_name is read-only, not for creation

        user = User(**validated_data)
        user.set_password(password)  # Hashes the password
        user.save()
        return user

class MessageSerializer(serializers.ModelSerializer):
    sender = CustomUserSerializer(read_only=True)
    message_preview = serializers.SerializerMethodField()
    message_body = serializers.CharField()

    class Meta:
        model = Message
        fields = ['message_id', 'conversation', 'sender', 'message_body', 'sent_at', 'message_preview']

    def get_message_preview(self, obj):
        return obj.message_body[:20] + '...' if len(obj.message_body) > 20 else obj.message_body

    def validate_message_body(self, value):
        if not value.strip():
            raise serializers.ValidationError("Message body cannot be empty.")
        return value

class ConversationSerializer(serializers.ModelSerializer):
    participants = CustomUserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'created_at', 'messages']