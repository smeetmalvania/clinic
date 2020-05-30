from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from clinic_mgmt.models import Person

app_name = "clinic_mgmt"
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    # path('registration/', 
    #         ListView.as_view(queryset=Person.objects.all().order_by("-createdDateTime")[:20], 
    #         template_name = 'clinic_mgmt/recents.html')),
    path('register/', views.register, name="register"),
    path('new_visit/', views.visit_search, name="search"),
    path('visit_log/', views.visit_log, name="visitlog")
]