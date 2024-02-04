from django.contrib import admin

# Register your models here.
# If you want to use your models inside the admin panel you need to register them here

from .models import Note


admin.site.register(Note)