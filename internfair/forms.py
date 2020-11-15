from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Student, Recruiter, User
from django import forms

class studentsignupform(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    roll_number = forms.CharField(required=True)
    department = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()

        student = Student.objects.create(user=user)
        student.first_name = self.cleaned_data.get('first_name')
        student.last_name = self.cleaned_data.get('last_name')
        student.department = self.cleaned_data.get('department')
        student.roll_number = self.cleaned_data.get('roll_number')
        student.save()
        return user



class recruitersignupform(UserCreationForm):
    recruitername = forms.CharField(required=True)
    recruitercontact = forms.CharField(required=True)
    recruiterlocation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_recruiter = True
        user.is_staff = True
        user.save()

        recruiter = Recruiter.objects.create(user=user)
        recruiter.recruitername = self.cleaned_data.get('recruitername')
        recruiter.recruitercontact = self.cleaned_data.get('recruitercontact')
        recruiter.recruiterlocation = self.cleaned_data.get('recruiterlocation')
        recruiter.save()
        return user
