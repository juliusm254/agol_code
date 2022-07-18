from attr import fields
from django.forms import CharField
from rest_framework import serializers
from .models import (BulkOrder, 
                    Order, 
                    Customer, 
                    Vehicle, 
                    Driver, 
                    CustomerDriver, 
                    CustomerTruck, 
                    CustomerTrailer)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['name', 'national_id']

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class CustomerTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerTruck
        fields = '__all__'

class CustomerTrailerSerializer(serializers.ModelSerializer):
    trailer = VehicleSerializer()
    class Meta:
        model = CustomerTrailer
        
        fields = ['trailer','customer_id']


class CustomerDriverSerializer(serializers.ModelSerializer):  
    driver = DriverSerializer()
    class Meta:
        model = CustomerDriver
        fields = ['driver', 'customer']


class OrderSerializer(serializers.ModelSerializer):
    driver = DriverSerializer()
    truck = VehicleSerializer()
    trailer = VehicleSerializer()
    customer = CustomerSerializer()

    class Meta:
        
        model = Order
        fields = [
                    'id',
                    'driver',
                    'trailer', 
                    'truck', 
                    'created_at', 
                    'destination',
                    'order_quantity',
                    'status',
                    'customer'
                ]

                    
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class BulkOrderSerializer(serializers.ModelSerializer):
    # customer = serializers.StringRelatedField(many=False)
    class Meta:
        model = BulkOrder
        # fields = ['customer', 'quantity', 'description']
        fields = '__all__'