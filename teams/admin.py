from teams.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class TeamAdmin(admin.ModelAdmin):
  fieldsets = [
    (None,	{'fields': ['name']}),
    (None,	{'fields': ['number']}),
    (None,	{'fields': ['founded_date']}),
    (None,	{'fields': ['league']})
  ]

class MemberInline(admin.StackedInline):
  model = Member
  can_delete = False
  verbose_name_plural = 'member'

class UserAdmin(UserAdmin):
  inlines = (MemberInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Team, TeamAdmin)