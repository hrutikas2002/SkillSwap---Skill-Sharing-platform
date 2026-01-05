from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from reviews.models import Review
from skills.models import LearnSkill, TeachSkill
from .forms import RegisterForm, ProfileForm, LoginForm, UserForm
from accounts.models import userProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages 

def landing(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, "landing.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            userProfile.objects.create(user=user)

            login(request, user)
            return redirect("dashboard")

    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            identifier = form.cleaned_data["username_or_email"]
            password = form.cleaned_data["password"]

            # Try login by username first
            user = authenticate(request, username=identifier, password=password)

            # If not found → try email
            if user is None:
                try:
                    user_obj = User.objects.get(email=identifier)
                    user = authenticate(request, username=user_obj.username, password=password)
                except User.DoesNotExist:
                    user = None

            if user:
                login(request, user)
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid username/email or password.")

    return render(request, "accounts/login.html", {"form": form})

@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")

def dashboard(request):
    profile = request.user.userprofile

    profile_incomplete = (
        not profile.profile_picture
        or not profile.bio
        or not profile.education
        or not profile.specialization
        or not profile.certifications
        or not profile.linkedin
        or not TeachSkill.objects.filter(user=request.user).exists()
        or not LearnSkill.objects.filter(user=request.user).exists()
    )

    return render(
        request,
        "accounts/dashboard.html",
        {
            "profile_incomplete": profile_incomplete
        },
    )

@login_required
def my_profile(request):
    user = request.user
    profile = user.userprofile

    teach_skills = TeachSkill.objects.filter(user=user)
    learn_skills = LearnSkill.objects.filter(user=user)

    reviews = Review.objects.filter(session__teacher=user)

    return render(
        request,
        "accounts/my_profile.html",
        {
            "user_obj": user,
            "profile": profile,
            "teach_skills": teach_skills,
            "learn_skills": learn_skills,
            "reviews": reviews,
        },
    )

@login_required
def edit_profile(request):
    user = request.user
    profile = request.user.userprofile

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("dashboard")

    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    return render(
        request,
        "accounts/edit_profile.html",
        {"user_form": user_form, "profile_form": profile_form},
    )
