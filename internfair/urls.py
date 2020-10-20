<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('recruiterLanding', views.recruiterLanding, name='recruiterLanding'),
    path('recruiterRegistration', views.recruiterRegistration, name='recruiterRegistration'),
    path('studentProfile1', views.studentProfile1, name='studentProfile1'),
    path('availableInternships', views.availableInternships, name='availableInternships'),
]
=======
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('recruiterLanding', views.recruiterLanding, name='recruiterLanding'),
    path('recruiterRegistration', views.recruiterRegistration, name='recruiterRegistration'),
    path('studentProfile1', views.studentProfile1, name='studentProfile1'),
    path('availableInternships', views.availableInternships, name='availableInternships'),
]
>>>>>>> 52699643e89846ecad8860259f347e73e47ff765
