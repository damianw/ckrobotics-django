from django.contrib import admin
from teams.models import Team

class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['number']}),
    ]

admin.site.register(Team, TeamAdmin)