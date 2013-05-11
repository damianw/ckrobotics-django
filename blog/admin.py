from django.contrib import admin
from blog.models import *

class BlogAdmin(admin.ModelAdmin):
  fieldsets = [
      (None,               {'fields': ['name']}),
      (None,               {'fields': ['text']}),
  ]
  list_display = ('name',)

class CompetitionGameAdmin(admin.ModelAdmin):
	fieldsets = [
			(None, {'fields': ['name']}),
			(None, {'fields': ['season_start']}),
			(None, {'fields': ['season_end']}),
			(None, {'fields': ['league']}),
			(None, {'fields': ['current']}),
			(None, {'fields': ['description']}),
			(None, {'fields': ['teams']}),
			(None, {'fields': ['rules']}),
	]

admin.site.register(Description, BlogAdmin)
admin.site.register(CompetitionGame, CompetitionGameAdmin)