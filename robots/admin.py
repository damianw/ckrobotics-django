from django.contrib import admin
from teams.models import Robot

class RobotAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['number']}),
    ]

admin.site.register(Robot, RobotAdmin)