from django.contrib import admin
from .models import Profile, Project, Experience, Skill, Achievements

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1


class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [ProjectInline, ExperienceInline, SkillInline]