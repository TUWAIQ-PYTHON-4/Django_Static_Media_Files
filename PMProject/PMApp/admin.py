from django.contrib import admin
from .models import Task, Project


# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    date_hierarchy = 'creation_time'


class TaskAdmin(admin.ModelAdmin):
    list_filter = ('title', 'description', 'time_estimate')


admin.site.register(Task, TaskAdmin)

admin.site.register(Project, ProjectAdmin)
