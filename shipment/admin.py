from django.contrib import admin

from shipment.models import ShipmentDetails,TrackingDetails

# Register your models here.
admin.site.register(ShipmentDetails)
admin.site.register(TrackingDetails)