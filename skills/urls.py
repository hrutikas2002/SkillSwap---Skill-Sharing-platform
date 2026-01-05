from django.urls import path
from . import views

urlpatterns = [
    path("select/", views.select_skills, name="select_skills"),
    # teach skill actions
    path("teach/<int:id>/edit/", views.edit_teach_skill, name="edit_teach_skill"),
    path("teach/<int:id>/delete/", views.delete_teach_skill, name="delete_teach_skill"),

    # learn skill actions
    path("learn/<int:id>/edit/", views.edit_learn_skill, name="edit_learn_skill"),
    path("learn/<int:id>/delete/", views.delete_learn_skill, name="delete_learn_skill"),

    #path to match skills
    path("matching/",views.matching, name="matching"),

    #view profile for the matching teacher
    path("profile/<int:user_id>/", views.view_teacher_profile, name="view_teacher_profile"),

    #request session navigation 
    path("request/<int:teacher_id>/", views.request_session, name="request_session"),

    path("requests/", views.session_requests, name="session_requests"),

    path("schedule/<int:match_id>/", views.schedule_session, name="schedule_session"),
    path("reject/<int:match_id>/", views.reject_request, name="reject_request"),

#view requested sessions
    path("my-requests/", views.my_requests, name="my_requests"),


]
