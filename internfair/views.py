from django.shortcuts import render
from django.views import View
# Create your views here.

def index(request):
    return render(request, "StudentLanding.html")

def recruiter(request):
    return render(request, "RecruiterLanding.html")

def studentregistration(request):
    return render(request, "StudentRegistration.html")

def recruiteregistration(request):
    return render(request, "RecruiterRegistration.html")
    
def recruiteregistration(request):
    return render(request, "RecruiterRegistration.html")
