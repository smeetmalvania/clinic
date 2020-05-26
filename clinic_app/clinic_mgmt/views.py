from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'clinic_mgmt/home.html')

def contact(request):
    return render(request, 'clinic_mgmt/basic.html', {
        'content': ['You can contact me at: ', 'saunilmalvania@gmail.com']
        })