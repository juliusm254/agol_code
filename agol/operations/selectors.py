from django.db.models.query import QuerySet
from customers.models import Order
from django.shortcuts import get_object_or_404

def order_list(order_status) -> QuerySet[Order]:
    return(Order.objects.filter(order_status=order_status))



def checklist_details(pk) -> QuerySet[Order]:
    return(get_object_or_404(Order, id=pk))

