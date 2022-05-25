from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100, help_text='The name of the project')
    creation_time = models.DateField(auto_now_add=True, help_text='The project creation time')
    completion_time= models.DateTimeField(null=True, help_text='The project completion time')
    project_logo = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100, help_text='The title of a task')
    description = models.TextField(help_text='The task description')
    time_estimate = models.IntegerField(help_text='Task time estimate')
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str__(self):
        return self.title



'''
x = Project.objects.create(name = 'projectx')

task = Task.objects.create(title='project plan', description='write out the project plan',time_estimate= 2, project= x)

 project = Project.objects.get(name='projectx')
 Task.objects.filter(title='project plan')

'''
