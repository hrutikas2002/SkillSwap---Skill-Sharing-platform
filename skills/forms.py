from django import forms
from .models import TeachSkill, LearnSkill, Skill


class TeachSkillForm(forms.ModelForm):
    class Meta:
        model = TeachSkill
        fields = ["skill", "experience_level"]


class LearnSkillForm(forms.ModelForm):
    class Meta:
        model = LearnSkill
        fields = ["skill", "priority_level"]
