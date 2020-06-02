from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import VisitSearchForm, LogVisitForm, NewPatientForm
from .models import Person

def index(request):
    return render(request, 'clinic_mgmt/home.html')

def contact(request):
    return render(request, 'clinic_mgmt/basic.html', {
        'content': ['You can contact me at: ', 'saunilmalvania@gmail.com']
        })

def visit_search(request):
    if request.method == "POST":
        form = VisitSearchForm(request.POST)
        if form.is_valid():
            caseid = form.cleaned_data['caseid']
            try:
                patient = Person.objects.filter(id=caseid).get(id=caseid)
                form = LogVisitForm
                return render(request, 'clinic_mgmt/new_visit_entry.html', {
                    'caseid': caseid, 
                    'patient': patient,
                    'form': form
                    })
            except:
                return render(request, 'clinic_mgmt/notfound.html', {'caseid': caseid})
        else:
            return render(request, 'clinic_mgmt/notfound.html')
    
    # For the GET request (by default)
    form = VisitSearchForm
    return render(request, 'clinic_mgmt/visit_home.html', {"form": form})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            return redirect("clinic_mgmt:index")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserCreationForm
    return render(request, 
                "clinic_mgmt/register.html", 
                {"form": form})

def visit_log(request):
    if request.method == "POST":
        form = LogVisitForm(request.POST)
        if form.is_valid():
            visit = form.save()
            return render(request, 'clinic_mgmt/basic.html')
    # GET request
    return render(request, 'clinic_mgmt/basic.html')

def new_patient(request):
    if request.method == "POST":
        form = NewPatientForm(request.POST)
        if form.is_valid():
            person = form.save()
            return render(request, 'clinic_mgmt/basic.html')
    form = NewPatientForm
    return render(request, 'clinic_mgmt/new_patient.html', {'form': form})