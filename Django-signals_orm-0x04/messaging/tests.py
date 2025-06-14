from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Message, Notification, MessageHistory

User = get_user_model()

class MessagingSignalTest(TestCase):
    def setUp(self):
        self.alice = User.objects.create_user(username='alice', password='pass', email='alice@example.com')
        self.bob = User.objects.create_user(username='bob', password='pass', email='bob@example.com')

    def test_notification_created_on_message(self):
        msg = Message.objects.create(sender=self.alice, receiver=self.bob, content="Hello Bob!")
        notif = Notification.objects.get(user=self.bob, message=msg)
        self.assertFalse(notif.is_read)

    def test_message_edit_creates_history(self):
        msg = Message.objects.create(sender=self.alice, receiver=self.bob, content="Original")
        msg.content = "Edited"
        msg.save()
        history = msg.history.first()
        self.assertIsNotNone(history)
        self.assertEqual(history.old_content, "Original")
        self.assertTrue(msg.edited)

    def test_user_deletion_cleans_up_related_data(self):
        msg = Message.objects.create(sender=self.alice, receiver=self.bob, content="Bye")
        notif = Notification.objects.create(user=self.bob, message=msg)
        history = MessageHistory.objects.create(message=msg, old_content="Old")
        self.alice.delete()
        self.assertFalse(Message.objects.filter(pk=msg.pk).exists())
        self.assertFalse(Notification.objects.filter(pk=notif.pk).exists())
        self.assertFalse(MessageHistory.objects.filter(pk=history.pk).exists())
