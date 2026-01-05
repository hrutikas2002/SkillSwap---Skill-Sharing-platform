from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from session_schedule.models import Session_Schedule
from .forms import ReviewForm

@login_required
def add_review(request, session_id):
    session = get_object_or_404(Session_Schedule, id=session_id, learner=request.user)

    # allow review only if session completed
    if session.status != "COMPLETED":
        messages.error(request, "You can review only after the session is completed.")
        return redirect("my_sessions")

    # prevent duplicate review
    if hasattr(session, "review"):
        messages.info(request, "You already submitted a review.")
        return redirect("my_sessions")

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.session = session
            review.reviewer = request.user
            review.save()

            messages.success(request, "Review submitted successfully.")
            return redirect("my_sessions")
    else:
        form = ReviewForm()

    return render(request, "reviews/add_review.html", {"form": form, "session": session})