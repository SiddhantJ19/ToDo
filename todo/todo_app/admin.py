from django.contrib import admin

# Register your models here.
from .models import TodoList, Task

admin.site.register(TodoList)
admin.site.register(Task)
