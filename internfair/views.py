from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.views.generic import CreateView
from .models import Student, Recruiter, User
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import studentsignupform, recruitersignupform
# Create your views here.




class student_register(CreateView):
    model = User
    form_class = studentsignupform
    template_name = "StudentRegistration.html"

    def form_valid(self, form):
        user = form.save()
        return redirect('../')


class recruiter_register(CreateView):
    model = User
    form_class = recruitersignupform
    template_name = "RecruiterRegistration.html"

    def form_valid(self, form):
        user = form.save()
        return redirect('../recruiter')


def index(request):
    if request.method=='POST':
        password = request.POST.get('password')
        username = request.POST.get('username')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_student == True:
                return redirect('../student/profile')
            else:
                return redirect('../student/profile')
        else:
            messages.info(request, 'Username OR password is incorrect')

    return render(request, "StudentLanding.html",
    context={'form': AuthenticationForm()} )
    '''
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                if user.is_recruiter == True:
                    login(request,user)
                    return redirect('/recruiter/profile')
                else:
                    login(request,user)
                    return redirect('/student/profile')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")

    return render(request, "StudentLanding.html",
    context={'form': AuthenticationForm()} )

    '''

def recruiterLanding(request):
    if request.method=='POST':
        password = request.POST.get('password')
        username = request.POST.get('username')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_recruiter == True:
                return redirect('../recruiter/profile')
            else:
                return redirect('../student/profile')
        else:
            messages.info(request, 'Username OR password is incorrect')

    return render(request, "RecruiterLanding.html",
    context={'form': AuthenticationForm()} )









def logout_view(request):
    logout(request)
    return redirect('')

def studentProfile1(request):
    return render(request, "StudentProfile1.html")

def availableInternships(request):
    return render(request, "AvailableInternships.html")

def studentProfile2(request):
    return render(request, "StudentProfile2.html")

def companyProfile(request):
    return render(request, "AvailableInterns.html")

def internStatic(request):
    return render(request, "CompanyProfile.html")
