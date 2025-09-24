 Ex02 Django ORM Web Application
## Date:18.9.2025 

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 5 Car 

## PROGRAM
```models.py
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
admin.py
from django.contrib import admin
from.models import StudentDetail, StudentDetailAdmin

# Register your models here.
admin.site.register(StudentDetail, StudentDetailAdmin)
```
## OUTPUT
![alt text](<Screenshot 2025-09-24 090637.png>) ![alt text](<Screenshot 2025-09-24 090704.png>) ![alt text](<Screenshot 2025-09-24 090716.png>)

## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
