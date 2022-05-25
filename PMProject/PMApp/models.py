from django.db import models
from django.db import models


class Task(models.Model):
    title=models.CharField(max_length = 100, help_text = 'this is title')
    description=models.TextField(help_text='this is description')
    time_estimate=models.IntegerField(help_text ='time_estimate')
    completed=models.BooleanField(default = False )


    def __str__(self):
        return '{} {} {}'.format(self.title, self.description,self.time_estimate)

class Project(models.Model):
    name=models.CharField(max_length=100 , help_text ='this is name')
    creation_time=models.DateTimeField(auto_now_add=True , help_text='this is creation time')
    completion_time=models.DateTimeField(null= True, help_text='this is completiontime')
    Task = models.ForeignKey(Task, on_delete=models.CASCADE)
    project_logo = models.ImageField(upload_to='images/')

    def __str__(self):
        return '{} {}'.format(self.name, self.creation_time)