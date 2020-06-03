from django import forms
from .models import Visit, Person
from django.forms import ModelForm, widgets
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class DateInput(forms.DateInput):
    input_type = 'date'

class VisitSearchForm(forms.Form):
    caseid = forms.IntegerField(
        label="Case ID"
        )

    def clean_data(self):
        data = self.cleaned_data['caseid']
        if data < 1:
            raise ValidationError(_('Invalid Entry!'))
        return data

class LogVisitForm(ModelForm):
    class Meta:
        model = Visit
        fields = ['caseid', 'visit_type', 'amt_due', 'amt_paid', 'payment_method']
        labels = {
            'caseid': _("Confirm Case #"),
            'visit_type': _("Visit Type"),
            'amt_due': _("Amount Due for Visit"),
            'payment_method' : _("Mode of Payment"),
            'amt_paid': ("Amount Paid for Visit")
        }

class NewPatientForm(ModelForm):
    class Meta:
        model = Person
        exclude = ['createdDate']
        widgets = {'birthDate': DateInput()}
        
class PatientSearchForm(forms.Form):
    caseid = forms.IntegerField(
        label="Case ID"
        )



