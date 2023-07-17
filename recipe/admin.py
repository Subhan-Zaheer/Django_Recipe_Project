from django.contrib import admin
from recipe.models import recipe, my_user, Department, StudentId, Student

# Register your models here.
class my_recipe_admin(admin.ModelAdmin):
    list_display = ('recipe_name', 'recipe_desc', 'recipe_image', 'user')

admin.site.register(recipe, my_recipe_admin)


class my_user_admin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user_name', 'password')

admin.site.register(my_user, my_user_admin)

class my_department(admin.ModelAdmin):
    list_display = ('department_name',)

admin.site.register(Department, my_department)

class my_studentid(admin.ModelAdmin):
    list_display = ('student_id', )

admin.site.register(StudentId, my_studentid)

class my_student(admin.ModelAdmin):
    list_display = ('student_id', 'department', 'student_name', 'student_email', 'student_age', 'student_address')

admin.site.register(Student, my_student)
# @admin.register(recipe)
# class recipe_admin(admin.ModelAdmin):
    # pass              