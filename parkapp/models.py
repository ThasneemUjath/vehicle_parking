from django.db import models


# Create your models here.
class Parking(models.Model):
    Pid = models.IntegerField(primary_key=True)
    vehicle_type = models.CharField(max_length=20)
    vehicle_number = models.CharField(max_length=20)
    owner_name = models.CharField(max_length=20)
    parked_hours = models.TextField()
    paid_amount = models.FloatField()
    status = models.CharField(max_length=50)




# Create your models here.
