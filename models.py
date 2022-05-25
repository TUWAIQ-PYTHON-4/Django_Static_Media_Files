from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length = 100, help_text = 'the name of the project')
    creation_time = models.DateTimeField(auto_now_add = True, help_text = 'this is creation time')
    completion_time = models.DateTimeField(null= True, help_text = 'this is completion time')

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100, help_text = 'this is task name')
    description = models.TextField(help_text = 'this is task description')
    time_estimate = models.IntegerField(help_text= 'this is the time a task might take')
    completed = models.BooleanField(default = False)
    task_logo = models.ImageField(upload_to='myImages')

    def __str__(self):
        return '{} {} {} {}'.format(self.title, self.description, self.time_estimate,self.completed)
