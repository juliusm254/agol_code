from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from customers.serializers import OrderSerializer
from .services import checklist_create
from .selectors import order_list, checklist_details
from .serializers import VehicleSerializer
class ChecklistCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        order_id = serializers.CharField()
        question_id = serializers.IntegerField()
        checklist_choice = serializers.CharField()

    def post(self, request):
        order = self.request.data['order']
        questions = self.request.data['questions']
        for index in range(len(questions)):
            question_list=list(questions[index].values())
            print(question_list)
            checklist_choice = question_list[2]
            print(checklist_choice)
            question = question_list[0]
            serializer = self.InputSerializer(data={'order_id':order, 'question_id':question, 'checklist_choice':checklist_choice})
            serializer.is_valid(raise_exception=True)

            checklist_create(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


class ChecklistListApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        trailer_details = VehicleSerializer(source="trailer", read_only=True)
        truck_details = VehicleSerializer(source="truck", read_only=True)


    def get(self, request):
        serializer = self.OutputSerializer(order_list('SAFETY'), many=True)
        print(serializer.data)
        return Response(serializer.data)


class ChecklistDetailApi(APIView):
    class OutputSerializer(serializers.Serializer):
        order_id = serializers.CharField()
        # truck = OrderSerializer(source="id", read_only=True)
        checklist_choice = serializers.CharField()
        question_id = serializers.IntegerField()
        trailer_details = OrderSerializer(source="trailer_id", read_only=True)
        # truck_id = serializers.PrimaryKeyRelatedField(read_only=True)
        # truck_id = VehicleSerializer( read_only=True)


    def get(self, request, pk=None):
        serializer = self.OutputSerializer(checklist_details(pk), many=True)
        print(serializer.data)
        return Response(serializer.data)

class ChecklistDetailApi(APIView):
    def get(self, request, pk=None):
        

        data = get_checklist_details(pk)

        return Response(data)

