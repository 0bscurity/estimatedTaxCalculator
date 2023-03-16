from django.contrib.auth.models import User
from django.db import models


class Vehicle(models.Model):
    year = models.IntegerField(null=True)
    make = models.CharField(max_length=56)
    model = models.CharField(max_length=56)
    gas_mileage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(f'{self.make} {self.model}')


class MileageEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.RESTRICT)

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    miles_driven = models.DecimalField(max_digits=5, decimal_places=2)
    purpose = models.CharField(max_length=56)
    estimated_expense = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(f'{self.user} {self.miles_driven}')
