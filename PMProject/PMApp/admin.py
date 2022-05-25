from django.contrib import admin

# Register your models here.
from .models import Project, Task


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'creation_time', 'completion_time',)
    list_filter = ('name',)
    search_fields = ('creation_time',)
    date_hierarchy = 'creation_time'


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'time_estimate', 'completed', 'project')
    list_filter = ('project',)
    search_fields = ('title',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
