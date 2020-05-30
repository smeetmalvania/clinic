from clinic_mgmt.models import Person
from django.contrib import admin
from django.apps import AppConfig

admin.site.register(Person)
class ClinicConfig(AppConfig):
    name = 'clinic_mgmt'