from django.contrib import admin

from skills.models import LearnSkill, Match, Skill, TeachSkill

admin.site.register(Skill)
admin.site.register(TeachSkill)
admin.site.register(LearnSkill)
admin.site.register(Match)