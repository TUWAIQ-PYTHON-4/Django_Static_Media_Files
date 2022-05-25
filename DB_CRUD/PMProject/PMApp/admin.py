from django.contrib import admin
from .models import Project, Task


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'time_estimate')
    search_fields = ('title',)
    list_filter = ('time_estimate',)


class ProjectAdmin(admin.ModelAdmin):
    date_hierarchy = 'creation_time'


admin.site.register(Task, TaskAdmin)
admin.site.register(Project, ProjectAdmin )

