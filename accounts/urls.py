from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("my-profile/", views.my_profile, name="my_profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
]
