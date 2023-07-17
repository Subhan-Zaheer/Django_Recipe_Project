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

class Department(models.Model):
    department_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department_name
    
    class Meta:
        ordering = ['department']

class StudentId(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self)  ->  str:
        return self.student_id

class Student(models.Model):
    student_id = models.OneToOneField(StudentId, related_name = 'studentID' , on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='department', on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50, default=None)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=None)
    student_address = models.TextField(default=None)

    def __str__(self) -> str:
        return self.student_name

    class Meta:
        ordering = ['student_name']
        verbose_name = 'student'


