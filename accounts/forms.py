from django import forms
from django.contrib.auth.models import User
from .models import userProfile


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name","username", "email", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # remove username help text
        self.fields["username"].help_text = None

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # remove username help text
        self.fields["username"].help_text = None

class LoginForm(forms.Form):
    username_or_email = forms.CharField(label="Email or Username")
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ["education", "specialization" ,"bio", "certifications","linkedin","profile_picture"]
