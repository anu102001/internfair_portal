from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/register', views.register, name='register'),
    path('recruiter/', views.recruiterLanding, name='recruiterLanding'),
    path('recruiter/register', views.recruiterRegistration, name='recruiterRegistration'),
    path('student/profile', views.studentProfile1, name='studentProfile1'),
    path('student/availableInternships', views.availableInternships, name='availableInternships'),
    path('studentProfile2', views.studentProfile2, name='studentProfile2'),
    path('recruiter/profile', views.companyProfile, name='companyProfile'),
    path('recruiter/internshipstatics', views.internStatic, name='internStatic'),


    
]
