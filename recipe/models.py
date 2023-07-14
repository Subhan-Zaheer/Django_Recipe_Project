from django.db import models

# Create your models here.

class recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    recipe_desc = models.TextField()
    recipe_image = models.FileField(upload_to='recipe/', max_length=250, null=True, default=None)
