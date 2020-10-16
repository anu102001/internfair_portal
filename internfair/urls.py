from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recruiter/', views.recruiter, name='recruiter'),
    path('studentregistration/', views.studentregistration, name='studentregistration'),
    path('recruiteregistration/', views.recruiteregistration, name='recruiteregistration')
]
