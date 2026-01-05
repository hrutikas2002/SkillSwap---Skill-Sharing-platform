from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class TeachSkill(models.Model):
    LEVEL_CHOICES = (
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Expert", "Expert"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    experience_level = models.CharField(max_length=20, choices=LEVEL_CHOICES)

    class Meta:
        unique_together = ('user', 'skill')

    def clean(self):
        from .models import LearnSkill
        if self.user_id and LearnSkill.objects.filter(user_id=self.user_id, skill=self.skill).exists():
            raise ValidationError("You cannot teach and learn the same skill.")

    def __str__(self):
        return f"{self.user} teaches {self.skill}"


class LearnSkill(models.Model):
    PRIORITY_CHOICES = (
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    priority_level = models.CharField(max_length=20, choices=PRIORITY_CHOICES)

    class Meta:
        unique_together = ('user', 'skill')

    def __str__(self):
        return f"{self.user} learns {self.skill}"


class Match(models.Model):
    STATUS_CHOICES = (
        ("AVAILABLE", "Available"),
        ("PENDING", "Pending"),
        ("ACCEPTED", "Accepted"),
        ("REJECTED", "Rejected"),
    )

    learner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="learner_matches")
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teacher_matches")
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="AVAILABLE")
    created_at = models.DateTimeField(auto_now_add=True)

    reject_reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.learner} ↔ {self.teacher} ({self.skill})"