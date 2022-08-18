from rest_framework import serializers
from .models import ScanOrder
from customers.serializers import VehicleSerializer, DriverSerializer, CustomerSerializer
from customers.models import Order
from .models import SafetyChecklist, Labinspection, SafetyChecklistQuestion, LabResults


class SafetyChecklistSerializer(serializers.ModelSerializer):
    trailer_details = VehicleSerializer(source="trailer", read_only=True)
    truck_details = VehicleSerializer(source="truck", read_only=True)
    
    # questions = SafetyChecklistQuestionSerializer()
    class Meta:
        model = Order
        fields = ['id', 'truck', 'truck_details', 'trailer', 'trailer_details']


class LabinspectionSerializer(serializers.ModelSerializer):
    trailer_details = VehicleSerializer(source="trailer", read_only=True)
    truck_details = VehicleSerializer(source="truck", read_only=True)
    read_only_fields = (
            'truck', 'truck_details', 'trailer', 'trailer_details'
        )
    
    class Meta:
        model = Labinspection
        fields = [
                'id', 
                'truck_details', 
                'trailer_details',        
                'oxygen',
                'pressure',
                'nitrogen',
                'methane'

                ]

    
        
        
class ScanOrderSerializer(serializers.ModelSerializer):
    driver_details = DriverSerializer(source="driver", read_only=True)
    truck_details = VehicleSerializer(source="truck", read_only=True)
    trailer_details = VehicleSerializer(source="trailer", read_only=True)
    customer_details = CustomerSerializer(source="customer",  read_only=True)
    
    class Meta:
        model = Order
        fields = [
                    'id',
                    'driver_details',
                    'trailer_details',
                    'truck_details',
                    'order_status',
                    'customer_details'
                ]

    def update(self, instance, validated_data, *args, **kwargs):
        request_status = validated_data.pop("order_status")
        if instance.order_status != request_status:
            instance.order_status = request_status
            instance.save()
            return instance
        else:
            raise serializers.ValidationError( f'Order No. {instance.id} NOT Valid.')
        
class SafetyChecklistQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafetyChecklistQuestion
        fields = ['id', 'question_desc']


class OrderSerializer(serializers.ModelSerializer):
    driver_details = DriverSerializer(source="driver", read_only=True)
    truck_details = VehicleSerializer(source="truck", read_only=True)
    trailer_details = VehicleSerializer(source="trailer", read_only=True)
    # customer_details = CustomerSerializer(source="customer",  read_only=True)
    


    class Meta:
        model = Order
        read_only_fields = (
            "created_at",
            "created_by",
        ),
        fields = '__all__'

class LabResultsSerializer(serializers.ModelSerializer):
    # oxygen = LabinspectionSerializer(read_only=True)
    # pressure = LabinspectionSerializer(read_only=True)
    # nitrogen = LabinspectionSerializer(read_only=True)
    # methane = LabinspectionSerializer(read_only=True)
    
    # read_only_fields = (
    #     'id', 'truck', 'truck_details', 'trailer', 'trailer_details'
    #     )
    
    class Meta:
        model = Labinspection
        fields = [
                    'id',
                    'oxygen',
                    'pressure',
                    'nitrogen',
                    'methane',                    
                    
                ]
