from django.contrib import admin
from .models import Task

# Register your models here.
# We are registering our model with our admin panel
admin.site.register(Task)
