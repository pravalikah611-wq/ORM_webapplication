from django.db import models
from django.contrib import admin
# Create your models here.

class StudentDetail(models.model):
    name=models.CharField(max_length=250, help_text="Enter the student name")
    age=models.IntegerField(help_text="Enter age between 18 to 22")
    dob=models.DateField(help_text="Enter your Date of Birth")
    register_no=models.IntegerField(help_text="Enter your Register Number")

class StudentDetailAdmin(admin.ModelAdmin)
    list_display = ('name','age','dob','reg-no')
