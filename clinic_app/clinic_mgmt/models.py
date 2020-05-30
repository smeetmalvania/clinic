from django.db import models

class Person(models.Model):

    # Personal Particulars
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

    aadhar = models.IntegerField()
    createdDate = models.DateField(auto_now=True)
    createdDateTime = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=6, choices=[('Male', 'Male'), ('Female', 'Female')])
    birthDate = models.DateField()

    # Referral Type Capture
    REFERRAL_CHOICES = [
        ('Doctor', 'Doctor'),
        ('Patient', 'Patient'),
        ('Friend', 'Friend'),
        ('Other', 'Other'),
    ]
    referral_type = models.CharField(max_length=7, choices=REFERRAL_CHOICES, blank=True)
    
    # Address
    address_line1 = models.CharField(max_length=200, blank=True)
    address_line2 = models.CharField(max_length=200, blank=True)
    address_line3 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)

    # Patient Notes (for other Doctors' reference)
    note1 = models.TextField(blank=True)
    note2 = models.TextField(blank=True)

    def __str__(self):
        name = self.firstName+' '+self.middleName+' '+self.lastName
        return name + ' Case # ' + str(self.id)

class Visit(models.Model):

    # case ID
    caseid = models.ForeignKey(Person, on_delete=models.CASCADE)

    # Visit type
    VISIT_CHOICES = [
        ('First Consultation', 'First Consultation'),
        ('Routine Checkup', 'Routine Checkup'),
        ('Medicine Only', 'Medicine Only')
    ]
    visit_type = models.CharField(max_length=20, choices=VISIT_CHOICES, default='Routine Checkup')

    # Amount Due
    amt_due = models.IntegerField()
    PAYMENT_CHOICES = [
        ('Cash', 'Cash'),
        ('Credit', 'Credit')
    ]
    payment_method = models.CharField(max_length=6, choices=PAYMENT_CHOICES, default='Cash')
    visitDate = models.DateField(auto_now=True)
    visitDateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        dt = str(self.visitDateTime)
        # person = self.caseid.Person
        name = self.caseid.firstName+' '+self.caseid.middleName+' '+self.caseid.lastName
        return  name + ' visited on ' + dt 
    