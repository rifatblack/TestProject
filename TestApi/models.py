
from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)
   

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    

class Device(models.Model):
    name = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
   

class Checkout(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    checked_out = models.DateTimeField()
    checked_in = models.DateTimeField(null=True, blank=True)
    condition_when_checked_out = models.CharField(max_length=100)
    condition_when_checked_in = models.CharField(max_length=100, null=True, blank=True)
