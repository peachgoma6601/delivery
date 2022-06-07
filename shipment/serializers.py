from rest_framework import serializers

from shipment.models import ShipmentDetails,TrackingDetails

class ShipmentSeializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ShipmentDetails
    
class TrackingSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = TrackingDetails