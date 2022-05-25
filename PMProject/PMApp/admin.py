from django.contrib import admin

from .models import Project
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name']
    date_hierarchy = 'creation_time'

admin.site.register(Project,ProjectAdmin)

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_filter = ['title']
    search_fields = ['title']
admin.site.register(Task, TaskAdmin)