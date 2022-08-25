from django.db import models

from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.db import models




class Customer(models.Model):
    # user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    location = models.CharField(max_length=255)
    # profile_picture = models.ImageField(null=True, blank=True, upload_to = 'profile_pictures/', default='../media/profile_pictures/default_pic.jpg')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    bulk_customer = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    registration = models.CharField(max_length=255)
    transporter = models.CharField(max_length=255)
    epra_no = models.CharField(max_length=255)
    def __str__(self):
        return self.registration


class Driver(models.Model):
    name = models.CharField(max_length=255)
    national_id = models.CharField(max_length=255)
    epra_no = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Order(models.Model):

    PENDING = 'PENDING'
    SAFETY = 'SAFETY'
    LAB = 'LAB'
    LABRESULTS = 'LABRESULTS'
    VENT = 'VENT'
    SEAL = 'SEAL'    
    LOADING = 'LOADING'
    LOADED = 'LOADED'
    RELEASED = 'RELEASED'
    CLOSED = 'CLOSED'
    REJECTED = 'REJECTED'
    STALE = 'STALE'
    
    ORDERS_STATUS = (
        (PENDING, 'Pending'),       
        (SAFETY, 'Safety'),
        (LAB, 'Lab'),
        (LABRESULTS, 'Labresults'),
        (VENT, 'Vent'),
        (SEAL, 'Seal'), 
        (LOADING, 'Loading'),
        (LOADED, 'Loaded'),
        (RELEASED, 'Released'),
        (CLOSED, 'Closed'),
        (REJECTED, 'Rejected'),
        (STALE, 'Stale')
    )

    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='order_customer', null=False)    
    destination = models.CharField(max_length=255)    
    order_quantity = models.IntegerField(null=False)    
    order_status = models.CharField(max_length=25, choices=ORDERS_STATUS, default=PENDING)
    driver = models.ForeignKey(Driver, related_name='order_driver', on_delete=models.CASCADE)
    truck = models.ForeignKey(Vehicle, related_name='order_truck', on_delete=models.CASCADE)
    trailer = models.ForeignKey(Vehicle, related_name='order_trailer', on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # created_by


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    # currency = models.FloatField(null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class BulkOrder(models.Model):
    description = models.CharField(max_length=200, null=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True)
    price = models.FloatField(null=True)
    # currency = models.FloatField(null=True)
    # description = models.CharField(max_length=200, null=True, blank=True)
    product = models.IntegerField(default=1)
    quantity = models.IntegerField(null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    # created_by
    
    def __str__(self):
        return self.description


class BulkOrderBalance(models.Model):
    class Meta:
        # db_table = 'customers_customerdriver'
        constraints = [
            models.UniqueConstraint(fields=['customer', 'product'], name='unique_bulk_balance')
        ]
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=False)
    product = models.IntegerField(default=1)
    quantity = models.IntegerField()


from django.core.exceptions import ObjectDoesNotExist

def bulk_order_balance_created(sender, instance, *args, **kwargs):
    print(args, kwargs)
    try:
        query = BulkOrderBalance.objects.get(pk=BulkOrderBalance.objects.get(customer=instance.customer, product=instance.product).id)
        order_quantity = instance.quantity
        balance_obj = query
        balance = balance_obj.quantity
        newquantity = int(order_quantity) + balance
        balance_obj.quantity = newquantity
        balance_obj.save()
    
    except ObjectDoesNotExist:
        obj = Customer.objects.filter(id=instance.customer.id).first()

        new_bulk_order = BulkOrderBalance (
                                customer = obj,
                                quantity = instance.quantity 
                                )
        new_bulk_order.save()    
    

pre_save.connect(bulk_order_balance_created, sender=BulkOrder)


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    loaded_quantity = models.CharField(max_length=255, null=True)
    loaded_date = models.DateTimeField(auto_now_add=True, null=True)
    # created_by = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, related_name='driver', on_delete=models.CASCADE)
    truck = models.ForeignKey(Vehicle, related_name='truck', on_delete=models.CASCADE)
    trailer = models.ForeignKey(Vehicle, related_name='trailer', on_delete=models.CASCADE)



# customer specific trucks
class CustomerTruck(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['customer', 'truck'], name='unique_customer_truck')
        ]
    customer = models.ForeignKey(
            Customer, on_delete=models.SET_NULL, null=True)
    registration = models.CharField(max_length=200, null=True)
    truck = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)

# customer specific driver
class CustomerDriver(models.Model):
    class Meta:
        db_table = 'customers_customerdriver'
        constraints = [
            models.UniqueConstraint(fields=['customer_id', 'driver'], name='unique_customer_driver')
        ]
    ''' table for Drivers specific to each customer account '''
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True) 
    name = models.CharField(max_length=200, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)    
    
    def __str__(self):
        return self.name

# customer specific trailer
class CustomerTrailer(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['customer', 'trailer'], name='unique_customer_trailer')
        ]
    
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    registration = models.CharField(max_length=200, null=True)
    trailer = models.ForeignKey(Vehicle, on_delete=models.CASCADE, 
                null=True, 
                related_name='customer_trailer')

    # def as_dict(self):
    #     return {
    #         "id": self.id,
    #         "customer": self.customer.id,
    #         "epra": self.trailer.epra_no

    #     }

