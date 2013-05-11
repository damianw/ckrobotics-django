from django.contrib import admin
from blog.models import *

class BlogAdmin(admin.ModelAdmin):
  pass
class DescriptionAdmin(admin.ModelAdmin):
	pass
class CompetitionGameAdmin(admin.ModelAdmin):
	pass

admin.site.register(BlogPost, BlogAdmin)
admin.site.register(Description, DescriptionAdmin)
admin.site.register(CompetitionGame, CompetitionGameAdmin)