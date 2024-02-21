from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# For categories
class Category(models.Model):
    name = models.CharField(max_length=255)

    # To change categorys to Categories
    # When we want to order by name its done inside the Meta. Which is like options configuration for the model
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    #This is to show the names of their ctegories themselves i.e instead of Category object (3) to Toys
    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    #null = True in case the user dowsnt wanna provide the description
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    # If the user is deleted all item created by the user will be deleted
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name