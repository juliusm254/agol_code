from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .services import checklist_create

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
            checklist_choice = question_list[2]
            question = question_list[0]
            serializer = self.InputSerializer(data={'order_id':order, 'question_id':question, 'checklist_choice':checklist_choice})
            serializer.is_valid(raise_exception=True)

            checklist_create(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)
