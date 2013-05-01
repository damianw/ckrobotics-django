from django.contrib import admin
from blog.models import Description

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['text']}),
    ]
    list_display = ('name',)

admin.site.register(Description, BlogAdmin)