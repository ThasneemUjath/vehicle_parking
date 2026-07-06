from django import forms
from .models import Parking

class ParkingForm(forms.ModelForm):
    class Meta:
        model = Parking
        fields = '__all__'

        labels = {
            'pid': 'Parking ID',
            'vehicle_type' : 'Vehicle Type',
            'vehicle_number' : 'Vehicle Number' ,
            'owner_name' : 'Owner Name' ,
            'parked_hours' : 'Parked Hours' ,
            'paid_hours' : 'paid Hours' ,
            'status' : 'Status'
        }

        widgets  ={
            'Pid': forms.NumberInput(attrs={'placeholder': 'eg. 101'}),
            'vehicle_Type': forms.TextInput(attrs={'placeholder': 'eg. Car/Bike'}),
            'vehicle_number': forms.TextInput(attrs={'placeholder': 'eg. TN 75 AK **'}),
            'owner_name': forms.TextInput(attrs={'placeholder': 'eg. John Henry'}),
            'parked_hours': forms.TextInput(attrs={'placeholder': 'eg. 2 hr'}),
            'paid_amount': forms.NumberInput(attrs={'placeholder': 'eg. $200'}),
            'status': forms.TextInput(attrs={'placeholder': 'eg. Active'}),
        }