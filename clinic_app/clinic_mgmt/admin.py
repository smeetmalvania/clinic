from django.contrib import admin

# Register your models here.
from .models import Person, Visit

class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Personal Particulars", {
            'fields': [
                'firstName', 'middleName', 'lastName',
                'aadhar', 'gender', 'birthDate', 'referral_type'
                ]
        }),
        ("Address", {
            'fields': [
                'address_line1', 'address_line2', 'address_line3',
                'city', 'state', 'country', 'pincode'
            ]
        }),
        ("Additional Notes for Consulting Doctor", {
            'fields': [
                'note1', 'note2'
            ]
        })
    ]
    search_fields = ['firstName', 'middleName', 'lastName', 'aadhar', 'id']
    
    def name(self, obj):
        return obj.firstName + ' ' + obj.middleName + ' ' + obj.lastName
    
    def case_ID(self, obj):
        return obj.id

    list_display = ['name', 'case_ID', 'aadhar', 'createdDateTime']

class VisitAdmin(admin.ModelAdmin):
    list_display = ['caseid', 'visit_type', 'amt_due', 'visitDate', 'visitDateTime']
    search_fields = ['caseid', 'visit_type', 'amt_due', 'visitDate', 'visitDateTime']

admin.site.register(Person, PersonAdmin)
admin.site.register(Visit, VisitAdmin)