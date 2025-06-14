from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponseForbidden
from django.shortcuts import render

User = get_user_model()

@login_required
def delete_user(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        return redirect('logout')
    return HttpResponseForbidden("Only POST allowed")
