from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models
from django.forms import ChoiceField
from customers.models import Order, Customer

# class OrderTerminalStatus(models.Model):

#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     status = models.CharField(Null=True, default=, max_length=25, choices=TERMINAL_STATUS)
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True) 
    
class ScanOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # customer_id = models.ForeignKey(Customer, related_name='id', on_delete=models.CASCADE)
    # status = models.CharField(max_length=25, choices=ORDERS_STATUS, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 
    # created_by = models.DateTimeField(auto_now_add=True)

class SafetyChecklistQuestion(models.Model):
    question_desc = models.CharField(max_length=255, null=False)
    # created_by = models.DateTimeField(auto_now_add=True)
    # inspection = models.ForeignKey
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 
    # created_by = models.DateTimeField(auto_now_add=True)



class SafetyChecklist(models.Model):
    YES = 'Yes'
    NO = 'No'


    CHECKLIST_CHOICES = (
        (YES, 'Yes'),
        (NO, 'No'),    
    )


    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    question = models.ForeignKey(SafetyChecklistQuestion, on_delete=models.CASCADE)    
    checklist_choice = models.CharField(max_length=25, null=False, choices=CHECKLIST_CHOICES)     
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.DateTimeField(auto_now_add=True)


class Labinspection(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    pressure = models.FloatField(null=True)
    oxygen = models.FloatField(null=True)
    nitrogen = models.FloatField(null=True)
    methane = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.DateTimeField(auto_now_add=True)

class LabResultsDecision(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    vent = models.BooleanField(null=False, default=False)
    seal = models.BooleanField(null=False, default=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.DateTimeField(auto_now_add=True)

class Loading(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    net_weight = models.FloatField(blank=False, null=True)
    tare_weight = models.FloatField(blank=False, null=True)
    gross_weight = models.FloatField(blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

#TO DO
# class BaseModel(models.Model)
#     created_at = models.DateTimeField(db_index=True, default=timezone.now)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True