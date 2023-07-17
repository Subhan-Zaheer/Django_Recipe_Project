from django.contrib import admin
from recipe.models import recipe, my_user

# Register your models here.
class my_recipe_admin(admin.ModelAdmin):
    list_display = ('recipe_name', 'recipe_desc', 'recipe_image', 'user')

admin.site.register(recipe, my_recipe_admin)


class my_user_admin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user_name', 'password')

admin.site.register(my_user, my_user_admin)
# @admin.register(recipe)
# class recipe_admin(admin.ModelAdmin):
    # pass              