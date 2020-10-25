from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('recruiterLanding', views.recruiterLanding, name='recruiterLanding'),
    path('recruiterRegistration', views.recruiterRegistration, name='recruiterRegistration'),
    path('studentProfile1', views.studentProfile1, name='studentProfile1'),
    path('availableInternships', views.availableInternships, name='availableInternships'),
    path('studentProfile2', views.studentProfile2, name='studentProfile2'),
    path('companyProfile', views.companyProfile, name='companyProfile'),
    path('studentEditProfileCard', views.studentEditProfileCard, name='studentEditProfileCard'),
    path('applyToCompanyCard', views.applyToCompanyCard, name='applyToCompanyCard'),
    path('internshipQuestionsCard2', views.internshipQuestionsCard2, name='internshipQuestionsCard2'),
]
