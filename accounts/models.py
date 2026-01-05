from django.db import models
from django.contrib.auth.models import User

# Django User model fields (built-in):
# id              -> Primary key (auto created)
# username        -> Unique name used for login
# password        -> Encrypted password (never store plain text)
# email           -> User email (optional by default)
# first_name      -> First name (optional)
# last_name       -> Last name (optional)
# is_active       -> True/False (deactivate account without deleting)
# is_staff        -> Can log into Django admin site
# is_superuser    -> Has all permissions (full control)
# date_joined     -> When the account was created
# last_login      -> Last time user logged in

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    education = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, null=True, blank=True)
    certifications = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField()
    timezone = models.CharField(max_length=50, default='Asia/Kolkata')
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)
    linkedin = models.URLField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username