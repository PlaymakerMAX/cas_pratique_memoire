# todolist_app/admin.py
from django.contrib import admin
from .models import Task

admin.site.register(Task)