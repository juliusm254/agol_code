from django.db.models.query import QuerySet
from django.db.models import Prefetch, Count, Q
from operations.models import SafetyChecklist
from customers.models import Order
from django.shortcuts import get_object_or_404

def order_list(order_status) -> QuerySet[Order]:
    return(Order.objects.filter(order_status=order_status))



def checklist_details(pk) -> QuerySet[SafetyChecklist]:
    return(SafetyChecklist.objects.select_related('order').filter(order_id=pk))

    return(Order.objects.get(id=pk).prefetch_related(
            Prefetch('order_id',
            queryset=SafetyChecklist.objects.all())
        ))

