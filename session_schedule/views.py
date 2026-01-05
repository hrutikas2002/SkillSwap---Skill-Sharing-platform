from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from notifications.utils import notify
from .models import Session_Schedule
from django.contrib import messages

@login_required
def my_sessions(request):
    sessions = Session_Schedule.objects.filter(
        learner=request.user
    ).order_by("-date_time")

    return render(
        request,
        "sessions/my_sessions.html",
        {"sessions": sessions},
    )

@login_required
def teaching_sessions(request):
    sessions = Session_Schedule.objects.filter(
        teacher=request.user
    ).order_by("-date_time")

    return render(
        request,
        "sessions/teaching_sessions.html",
        {"sessions": sessions},
    )

@login_required
def complete_session(request, session_id):
    session = get_object_or_404(Session_Schedule, id=session_id, teacher=request.user)

    session.status = "COMPLETED"
    session.save()

    messages.success(request, "Session marked as completed.")
    return redirect("teaching_sessions")

@login_required
def cancel_session_learner(request, session_id):
    session = get_object_or_404(Session_Schedule, id=session_id, learner=request.user)

    if request.method == "POST":
        reason = request.POST.get("reason")

        session.status = "CANCELLED"
        session.cancel_reason = reason
        session.cancelled_by = "LEARNER"
        session.save()

        notify(session.teacher,f"{request.user.username} cancelled the session for {session.skill}. Reason: {reason}")

        messages.info(request, "You cancelled the session.")
        return redirect("my_sessions")

    return render(request, "sessions/cancel_session.html", {"session": session})

@login_required
def cancel_session_teacher(request, session_id):
    session = get_object_or_404(Session_Schedule, id=session_id, teacher=request.user)

    if request.method == "POST":
        reason = request.POST.get("reason")

        session.status = "CANCELLED"
        session.cancel_reason = reason
        session.cancelled_by = "TEACHER"
        session.save()

        notify(session.learner,f"Your session for {session.skill} was cancelled by the teacher. Reason: {reason}")

        messages.info(request, "You cancelled the session.")
        return redirect("teaching_sessions")

    return render(request, "sessions/cancel_session.html", {"session": session})

