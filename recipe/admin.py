from django.contrib import admin
from recipe.models import recipe

# Register your models here.
class my_recipe_admin(admin.ModelAdmin):
    list_display = ('recipe_name', 'recipe_desc', 'recipe_image')

admin.site.register(recipe, my_recipe_admin)

# @admin.register(recipe)
# class recipe_admin(admin.ModelAdmin):
    # pass              