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
        return name + ' Case # ' + self.caseID 
