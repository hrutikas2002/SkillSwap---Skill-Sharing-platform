from django.db import models
from django.contrib.auth.models import User
from skills.models import Match, Skill
from django.utils import timezone

class Session_Schedule(models.Model):
    STATUS_CHOICES=(
        ("SCHEDULED","Scheduled"),
        ("COMPLETED","Completed"),
        ("CANCELLED","Cancelled")
    )

    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teacher_sessions")
    learner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="learner_sessions")
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    date_time = models.DateTimeField()
    meet_link = models.URLField()

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="SCHEDULED")

    created_at = models.DateTimeField(auto_now_add=True)

    cancel_reason = models.TextField(blank=True, null=True)

    CANCELLED_BY_CHOICES = (
        ("LEARNER", "Learner"),
        ("TEACHER", "Teacher"),
    )

    cancelled_by = models.CharField(
        max_length=10,
        choices=CANCELLED_BY_CHOICES,
        blank=True,
        null=True
    )

    def clean(self):
        from .models import LearnSkill
        if LearnSkill.objects.filter(user=self.user, skill=self.skill).exists():
            raise ValidationError("You cannot teach and learn the same skill.")

    def __str__(self):
        return f"Session: {self.skill} - {self.date_time}"