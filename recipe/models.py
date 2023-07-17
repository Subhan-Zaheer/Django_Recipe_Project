from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    recipe_name = models.CharField(max_length=50)
    recipe_desc = models.TextField()
    recipe_image = models.FileField(upload_to='recipe/', max_length=250, null=True, default=None)

class my_user(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

