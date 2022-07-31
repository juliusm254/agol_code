from rest_framework import serializers
from .models import ScanOrder
from customers.serializers import VehicleSerializer
from customers.models import Order
from .models import SafetyChecklist, Labinspection

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        read_only_fields = (
            "created_at",
            "created_by",
        ),
        fields = '__all__'


class SafetySerializer(serializers.ModelSerializer):
    trailer_details = VehicleSerializer(source="trailer", read_only=True)
    class Meta:
        model = Order
        fields = ['id','trailer', 'truck', 'trailer_details']


class LabinspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labinspection
        fields = '__all__'


class ScanOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScanOrder
        fields = '__all__'


