from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponseForbidden
from django.db.models import Q

from .models import Message

User = get_user_model()

@login_required
def delete_user(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        return redirect('logout')
    return HttpResponseForbidden("Only POST allowed")

def get_thread(message):
    """Recursively get all replies to a message in a threaded format."""
    replies = Message.objects.filter(parent_message=message).select_related('sender', 'receiver')
    thread = []
    for reply in replies:
        thread.append({
            'message': reply,
            'replies': get_thread(reply)
        })
    return thread

def threaded_conversations_view(request):
    # Only show threads where the user is the sender or receiver
    messages = Message.objects.filter(
        Q(sender=request.user) | Q(receiver=request.user),
        parent_message__isnull=True
    ).select_related('sender', 'receiver') \
     .prefetch_related('replies__sender', 'replies__receiver')
    # Build threads for each top-level message
    threads = []
    for msg in messages:
        threads.append({
            'message': msg,
            'replies': get_thread(msg)
        })
    return render(request, "messaging/threaded_conversations.html", {"threads": threads})

@login_required
def unread_inbox(request):
    unread_messages = Message.unread.for_user(request.user)
    return render(request, "messaging/unread_inbox.html", {"unread_messages": unread_messages})

