from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Message, Notification, MessageHistory

User = get_user_model()

@receiver(post_save, sender=Message)
def create_notification_on_message(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.receiver,
            message=instance
        )

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:
        old_message = Message.objects.get(pk=instance.pk)
        if old_message.content != instance.content:
            # Save old content to history
            MessageHistory.objects.create(
                message=instance,
                old_content=old_message.content
            )
            instance.edited = True

@receiver(post_delete, sender=User)
def cleanup_user_related_data(sender, instance, **kwargs):
    # Delete messages where user is sender or receiver or editor
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()
    Message.objects.filter(edited_by=instance).delete()
    # Delete notifications for this user
    Notification.objects.filter(user=instance).delete()
    # Delete message histories for messages that belonged to this user
    MessageHistory.objects.filter(message__sender=instance).delete()
    MessageHistory.objects.filter(message__receiver=instance).delete()