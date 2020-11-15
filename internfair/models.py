from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
import os


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_recruiter = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    roll_number = models.CharField(max_length=100)
    department = models.CharField(max_length=150)

class Recruiter(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(max_length=150)
    recruitername = models.CharField(max_length=150)
    recruitercontact = models.CharField(max_length=150)
    recruiterlocation = models.CharField(max_length=100)
