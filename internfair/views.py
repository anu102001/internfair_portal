from django.shortcuts import render
from django.views import View
# Create your views here.

def index(request):
    return render(request, "StudentLanding.html")

def register(request):
    return render(request, "StudentRegistration.html")

def recruiterLanding(request):
    return render(request, "RecruiterLanding.html")

def recruiterRegistration(request):
    return render(request, "RecruiterRegistration.html")

def studentProfile1(request):
    return render(request, "StudentProfile1.html")

def availableInternships(request):
    return render(request, "AvailableInternships.html")

def studentProfile2(request):
    return render(request, "StudentProfile2.html")

def companyProfile(request):
    return render(request, "CompanyProfile.html")

def studentEditProfileCard(request):
    return render(request, "StudentEditProfileCard.html")

def applyToCompanyCard(request):
    return render(request, "ApplyToCompanyCard.html")

def internshipQuestionsCard2(request):
    return render(request, "InternshipQuestionsCard2.html")




