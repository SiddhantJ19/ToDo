from django.db import models
from django.contrib.auth.models import User

class TodoList(models.Model):
    title  = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=500)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    task_content = models.TextField()
    done = models.BooleanField(default=False)