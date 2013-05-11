from teams.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User

# class TeamInline(admin.StackedInline):
#   model = Team
#   can_delete = False
#   verbose_name_plural= 'team'

class GroupInline(admin.StackedInline):
  model = Group
  # exclude = ('name',)
  can_delete = False
  verbose_name_plural= 'group'

# class GroupAdmin(GroupAdmin):
#   inlines = (TeamInline,)

class TeamAdmin(admin.ModelAdmin):
  pass
  #exclude = ('group',)
  # inlines = (GroupInline,)

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
# admin.site.unregister(Group)
# admin.site.register(Group, GroupAdmin)
admin.site.register(Robot, RobotAdmin)
admin.site.register(Team, TeamAdmin)