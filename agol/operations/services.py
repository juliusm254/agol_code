from typing import List
from .models import Order, SafetyChecklist, SafetyChecklistQuestion
from django.shortcuts import get_object_or_404

def order_status_update(order, order_status):
    order.order_status = order_status
    order.save()



def checklist_create(*,order_id:str, question_id:str, checklist_choice:str ,**kwargs) -> SafetyChecklist:
    print(order_id)
    print('gets here create')
    question_obj = get_object_or_404(SafetyChecklistQuestion, id=question_id)
    order_obj = get_object_or_404(Order, id=order_id)
    SafetyChecklist.objects.create(order=order_obj, checklist_choice=checklist_choice, question=question_obj)
    order_status_update(order_obj, 'LAB')