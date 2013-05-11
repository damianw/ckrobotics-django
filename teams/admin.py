from teams.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User

class TeamAdmin(GroupAdmin):
  exclude = ('name',)

class MemberInline(admin.StackedInline):
  model = Member
  can_delete = False
  verbose_name_plural = 'member'

class UserAdmin(UserAdmin):
  inlines = (MemberInline, )

class RobotAdmin(admin.ModelAdmin):
  fieldsets = [
      (None,  {'fields': ['name']}),
      (None,  {'fields': ['description']}),
  ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Robot, RobotAdmin)
admin.site.register(Team, TeamAdmin)