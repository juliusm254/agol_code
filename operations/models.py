from django.db import models

from django.contrib.auth.models import User
from django.db import models
from customers.models import Order, Customer

class ScannedOrders(models.Model):
    coid = models.ForeignKey(Order, on_delete=models.CASCADE)
    # customer_id = models.ForeignKey(Customer, related_name='id', on_delete=models.CASCADE)
    # status = models.CharField(max_length=25, choices=ORDERS_STATUS, default=PENDING)
    scanned_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 


class SafetyInspection(models.Model):
    coid = models.ForeignKey(Order, on_delete=models.CASCADE)
    # customer_id = models.ForeignKey(Customer, related_name='leads', on_delete=models.CASCADE)
    # status = models.CharField(max_length=25, choices=ORDERS_STATUS, default=PENDING)
    scanned_at = models.ForeignKey(ScannedOrders, on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)


class SafetyChecklist(models.Model):
    coid = models.ForeignKey(Order, on_delete=models.CASCADE)
    q1 = models.BooleanField(null=False)
    q2 = models.BooleanField(null=False) 
    q3 = models.BooleanField(null=False) 


class Labinspection(models.Model):
    coid = models.ForeignKey(Order, on_delete=models.CASCADE)
    pressure = models.FloatField(null=True)
    oxygen = models.FloatField(null=True)
    nitrogen = models.FloatField(null=True)
    methane = models.FloatField(null=True)
    
# Create your models here.
