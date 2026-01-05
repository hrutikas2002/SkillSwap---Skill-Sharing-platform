from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from notifications.utils import notify
from .forms import TeachSkillForm, LearnSkillForm
from .models import TeachSkill, LearnSkill, Skill
from skills.models import Match
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from reviews.models import Review
from session_schedule.models import Session_Schedule
from django.utils import timezone



@login_required
def select_skills(request):

    # Show current skills
    teach_skills = TeachSkill.objects.filter(user=request.user)
    learn_skills = LearnSkill.objects.filter(user=request.user)

    if request.method == "POST":

        if "teach_form" in request.POST:
            form = TeachSkillForm(request.POST)
            if form.is_valid():
                teach = form.save(commit=False)
                teach.user = request.user
                teach.save()
                return redirect("select_skills")

        if "learn_form" in request.POST:
            form = LearnSkillForm(request.POST)
            if form.is_valid():
                learn = form.save(commit=False)
                learn.user = request.user
                learn.save()
                return redirect("select_skills")

    teach_form = TeachSkillForm()
    learn_form = LearnSkillForm()

    return render(
        request,
        "skills/select_skills.html",
        {
            "teach_form": teach_form,
            "learn_form": learn_form,
            "teach_skills": teach_skills,
            "learn_skills": learn_skills,
        },
    )

@login_required
def edit_teach_skill(request, id):
    teach = get_object_or_404(TeachSkill, id=id, user=request.user)

    if request.method == "POST":
        form = TeachSkillForm(request.POST, instance=teach)
        if form.is_valid():
            form.save()
            messages.success(request, "Teach skill updated.")
            return redirect("select_skills")
    else:
        form = TeachSkillForm(instance=teach)

    return render(request, "skills/edit_teach.html", {"form": form})


@login_required
def edit_learn_skill(request, id):
    learn = get_object_or_404(LearnSkill, id=id, user=request.user)

    if request.method == "POST":
        form = LearnSkillForm(request.POST, instance=learn)
        if form.is_valid():
            form.save()
            messages.success(request, "Learn skill updated.")
            return redirect("select_skills")
    else:
        form = LearnSkillForm(instance=learn)

    return render(request, "skills/edit_learn.html", {"form": form})


@login_required
def delete_teach_skill(request, id):
    teach = get_object_or_404(TeachSkill, id=id, user=request.user)
    teach.delete()
    messages.info(request, "Teach skill removed.")
    return redirect("select_skills")

@login_required
def delete_learn_skill(request, id):
    learn = get_object_or_404(LearnSkill, id=id, user=request.user)
    learn.delete()
    messages.info(request, "Learn skill removed.")
    return redirect("select_skills")


@login_required
def matching(request):

    #skills user wants to learn 
    learn_skills = LearnSkill.objects.filter(user=request.user).values_list("skill",flat=True)

    #teachers who teach those skills
    matches = TeachSkill.objects.filter(skill__in=learn_skills).exclude(user=request.user)

    return render(request, "skills/matching.html",{"matches":matches})

@login_required
def view_teacher_profile(request, user_id):
    teacher = get_object_or_404(User, id=user_id)

    profile = teacher.userprofile

    teach_skills = TeachSkill.objects.filter(user=teacher)
    learn_skills = LearnSkill.objects.filter(user=teacher)

    reviews = Review.objects.filter(session__teacher=teacher)

    return render(
        request,
        "skills/teacher_profile.html",
        {
            "teacher": teacher,
            "profile": profile,
            "teach_skills": teach_skills,
            "learn_skills": learn_skills,
            "reviews": reviews,
        },
    )

@login_required
def request_session(request, teacher_id):
    teacher = get_object_or_404(User, id=teacher_id)

    # prevent requesting yourself
    if teacher == request.user:
        messages.error(request, "You cannot request a session from yourself.")
        return redirect("matching")

    # get the first skill that matches
    learn_skills = LearnSkill.objects.filter(user=request.user).values_list("skill", flat=True)

    match = TeachSkill.objects.filter(
        user=teacher,
        skill__in=learn_skills
    ).first()

    if not match:
        messages.error(request, "No matching skill found.")
        return redirect("matching")

    # create or update match entry
    Match.objects.update_or_create(
        learner=request.user,
        teacher=teacher,
        skill=match.skill,
        defaults={"status": "PENDING"},
    )

    notify(teacher, f"{request.user.first_name} {request.user.last_name} requested a session to learn {match.skill}.")

    messages.success(request, "Session request sent to teacher!")
    return redirect("view_teacher_profile", user_id=teacher_id)

@login_required
def session_requests(request):
    requests_list = Match.objects.filter(
        teacher=request.user,
        status="PENDING"
    )

    return render(
        request,
        "skills/session_requests.html",
        {"requests": requests_list},
    )

@login_required
def schedule_session(request, match_id):
    match = get_object_or_404(Match, id=match_id, teacher=request.user)

    if request.method == "POST":
        date_time = request.POST.get("date_time")
        meet_link = request.POST.get("meet_link")

        Session_Schedule.objects.create(
            match=match,
            teacher=match.teacher,
            learner=match.learner,
            skill=match.skill,
            date_time=date_time,
            meet_link=meet_link,
        )

        match.status = "ACCEPTED"
        match.save()

        notify(match.learner,f"Your session for {match.skill} has been scheduled on {date_time}.")

        messages.success(request, "Session scheduled!")
        return redirect("session_requests")

    return render(request, "skills/schedule_session.html", {"match": match})

@login_required
def reject_request(request, match_id):
    match = get_object_or_404(Match, id=match_id, teacher=request.user)
    match.status = "REJECTED"
    match.save()

    notify(
    match.learner,
    f"Your session request for {match.skill} was rejected."
    )

    messages.info(request, "Request rejected.")
    return redirect("session_requests")


@login_required
def my_requests(request):
    requests_list = Match.objects.filter(
        learner=request.user
    ).order_by("-created_at")

    return render(
        request,
        "skills/my_requests.html",
        {"requests": requests_list},
    )


@login_required
def reject_request(request, match_id):
    match = get_object_or_404(Match, id=match_id, teacher=request.user)

    if request.method == "POST":
        reason = request.POST.get("reason")

        match.status = "REJECTED"
        match.reject_reason = reason
        match.save()

        messages.info(request, "Request rejected with reason.")
        return redirect("session_requests")

    return render(request, "skills/reject_request.html", {"match": match})
