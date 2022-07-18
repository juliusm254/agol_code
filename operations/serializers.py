from rest_framework import serializers
from .models import ScannedOrders
from customers.models import Order
from .models import SafetyChecklist, Labinspection

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        read_only_fields = (
            "created_at",
            "created_by",
        ),
        fields = '__all__'


class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafetyChecklist
        fields = '__all__'


class LabinspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labinspection
        fields = '__all__'


# class ScannedOrdersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ScannedOrders
#         fields = '__all__'


