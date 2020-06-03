from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import VisitSearchForm, LogVisitForm, NewPatientForm, PatientSearchForm
from .models import Person, Visit

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
                outstanding_amt = 0

                # get outstanding amount due
                for visit in Visit.objects.filter(caseid_id=caseid):
                    outstanding_amt += visit.amt_due
                    outstanding_amt -= visit.amt_paid
                return render(request, 'clinic_mgmt/new_visit_entry.html', {
                    'caseid': caseid, 
                    'patient': patient,
                    'form': form,
                    'outstanding_amt': outstanding_amt,
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
            form.save()
            return render(request, 'clinic_mgmt/basic.html')
    # GET request
    return render(request, 'clinic_mgmt/basic.html')

def new_patient(request):
    if request.method == "POST":
        form = NewPatientForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'clinic_mgmt/basic.html')
    form = NewPatientForm
    return render(request, 'clinic_mgmt/new_patient.html', {'form': form})

def update_search(request):
    if request.method == "POST":
        form = PatientSearchForm(request.POST)
        if form.is_valid():
            caseid = form.cleaned_data['caseid']
            try:
                patient = Person.objects.filter(id=caseid).get(id=caseid)
                return redirect(r'/update/'+str(caseid)+'/')
            except:
                return render(request, 'clinic_mgmt/notfound.html', {'caseid': caseid})
        else:
            return render(request, 'clinic_mgmt/notfound.html')

    form = PatientSearchForm
    return render(request, 'clinic_mgmt/update_home.html', {'form': form})

def update_view(request, id):
    context = {}
    obj = get_object_or_404(Person, id=id)
    form = NewPatientForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return render(request, 'clinic_mgmt/saved.html')

    context['form'] = form
    return render(request, 'clinic_mgmt/update_person.html', context)