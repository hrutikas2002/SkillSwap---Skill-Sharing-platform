from django.db import models

from django.contrib.auth.models import User

from session_schedule.models import Session_Schedule


class Review(models.Model):
    session = models.OneToOneField(Session_Schedule, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for session {self.session.id}"

