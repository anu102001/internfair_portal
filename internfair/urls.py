from django.urls import path
from . import views
from .views import student_register

urlpatterns = [
    path('', views.index, name='index'),
    path('student/register', views.student_register.as_view(), name='student_register'),
    path('', views.logout_view, name='logout'),
    path('recruiter/', views.recruiterLanding, name='recruiterLanding'),
    path('recruiter/register', views.recruiter_register.as_view(), name='recruiterRegistration'),
    path('student/profile', views.studentProfile1, name='studentProfile1'),
    path('student/availableInternships', views.availableInternships, name='availableInternships'),
    path('studentProfile2', views.studentProfile2, name='studentProfile2'),
    path('recruiter/profile', views.companyProfile, name='companyProfile'),
    path('recruiter/internshipstatics', views.internStatic, name='internStatic'),



]
