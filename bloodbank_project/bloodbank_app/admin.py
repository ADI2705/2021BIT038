# bloodbank_app/admin.py
from django.contrib import admin
from .models import Donor, BloodBag, BloodTransfusion,Recipient

admin.site.register(Donor)
admin.site.register(BloodBag)
admin.site.register(BloodTransfusion)
admin.site.register(Recipient)

