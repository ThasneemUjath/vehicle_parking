from rest_framework import serializers
from .models import Parking

class ParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = ['Pid', 'vehicle_type', 'vehicle_number', 'owner_name', 'parked_hours', 'paid_amount','status']