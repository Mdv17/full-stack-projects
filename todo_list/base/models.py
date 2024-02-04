from django.db import models
# To import table for users. The User model takes care of user information like email, password. This is how django handles authentication
from django.contrib.auth.models import User

# Create your models here.
# Models thats how we build our database table in django. There are simply classes that represent a table
# Basically the class is the table and all the attributes are the model columns
# Task is the database table. To make it a model we just have to inherit from models.Model
class Task(models.Model):
    # We want to create a many to 1 relationship. 1 user can have many items. This can be set with the Forein Key values
    # user is the model. First value is on_delete. on_delete means if the user gets deleted what happens to the task
    # If you want the tasks to stay after deletion. 
    # models.CASCADE means if the user gets deleted the child tasks get deleted. models.SET_NULL if user gets deleted te tasks remain 
    # null=True means the field could be empty. blank=True means that when submitting a form we want to allow the field to be blank
    # We set null=True and blank=True when starting the app and when testing so that we dont run to issues
    user = models.ForeignKey(User, models.CASCADE)
    # how long the title will be but here we will have 200characters. CharField is usually for headlines, name etc 
    title = models.CharField(max_length=200)
    # TextField, if this was a form gives us like box to write to like a message or something
    description = models.TextField(null=True, blank=True)
    # BooleanField is a true or false value. When item is first created it is false it means not completed
    complete = models.BooleanField(default=False)
    # If user is created automatically fill the date and time at that very moment
    create = models.DateTimeField(auto_now_add=True)

    #To close out. self is the name of the model
    def __str__(self):
        return self.title
    
    # This how to set ordering. Here we want everything complete to be in the bottom
    class Meta:
        ordering = ['complete']
