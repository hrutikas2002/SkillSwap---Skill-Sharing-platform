from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from notifications.models import Notification

@login_required
def my_notifications(request):
    notifications = Notification.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(
        request,
        "notifications/my_notifications.html",
        {"notifications": notifications},
    )