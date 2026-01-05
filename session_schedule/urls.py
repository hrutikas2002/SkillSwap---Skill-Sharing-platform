from django.urls import path
from . import views

urlpatterns = [
    path("my/", views.my_sessions, name="my_sessions"),
    path("teaching/", views.teaching_sessions, name="teaching_sessions"),
    path("complete/<int:session_id>/", views.complete_session, name="complete_session"),
    path("cancel/learner/<int:session_id>/", views.cancel_session_learner, name="cancel_session_learner"),
    path("cancel/teacher/<int:session_id>/", views.cancel_session_teacher, name="cancel_session_teacher"),
]
