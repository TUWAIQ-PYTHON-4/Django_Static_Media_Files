from django.contrib import admin
from .models import Project, Task

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'creation_time', 'completion_time')
    list_filter = ('name',)
    date_hierarchy = 'creation_time'
    search_fields = ('name',)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'time_estimate', 'completed', 'project')



admin.site.register(Project,ProjectAdmin)
admin.site.register(Task,TaskAdmin)


