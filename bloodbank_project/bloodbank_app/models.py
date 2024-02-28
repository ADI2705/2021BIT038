# bloodbank_app/models.py
from django.db import models

class Donor(models.Model):
    class Meta:
        db_table = 'donor'  
    name = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=5)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    date_of_birth = models.DateField()
    address = models.TextField()

class BloodBag(models.Model):
    class Meta:
        db_table = 'bloodbag'  
    blood_type = models.CharField(max_length=5)
    donation_date = models.DateField()
    expiry_date = models.DateField()
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)

class BloodTransfusion(models.Model):
    class Meta:
        db_table = 'bloodtransfusion'  
    bag = models.ForeignKey(BloodBag, on_delete=models.CASCADE)
    recipient_name = models.CharField(max_length=100)
    transfusion_date = models.DateField()
    doctor_name = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
class Recipient(models.Model):
    class Meta:
        db_table = 'recipient'  
    name = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=5)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    date_of_birth = models.DateField()
    address = models.TextField()
    medical_history = models.TextField()
