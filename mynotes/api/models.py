from django.db import models

# Create your models here.
#This is where we create how our database must look like
# Every single class is going to represent a table in our database and attributes are going to represent colunms
# The instances of each model are going to represent the row

class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    # auto_now_add takes the timestamp of creation. It takes first creation timestamp while auto_now takes after creation and every time its updated
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # We just want the first 50 characters
        return self.body[0:50]
