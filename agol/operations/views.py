import json
from rest_framework import viewsets, filters, status, generics
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from .models import Order, SafetyChecklist, Labinspection, SafetyChecklistQuestion, LabResultsDecision
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import    (LabResultsDecisionSerializer, 
                            LabResultsDecisionSerializer,
                            LabResultsSerializer, 
                            # SafetyChecklistSerializer,
                            ScanOrderSerializer, 
                            SafetyChecklistQuestionSerializer, 
                            LabinspectionSerializer, 
                            OrderSerializer, 
                            LoadingSerializer)
# from customers.serializers import OrderSerializer
from django.contrib.auth import authenticate


def order_status_update(order, order_status):
    order.order_status = order_status
    order.save()

def get_tokens_for_user(user):
    
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user' : user.id
    }


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        # type = request.POST['type']
        print(request.data['username'])
        # if type == 'OPERATIONS':
        # username = request.data.get("username")
        # password = request.data.get("password")
        
        user = authenticate(username=request.data['username'], password=request.data['password'])
        # print(user + '2')
        if user.type=='OPERATIONS':
            return Response( get_tokens_for_user(user) )
        else:
            # return Response( get_tokens_for_user(user) )
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)




class OrderDetailView(APIView):
    serializer_class = OrderSerializer
    model = Order

    def get(self, request, pk=None):
        print(pk)
        queryset = Order.objects.get(id=pk)
        serializer = OrderSerializer(queryset)
        print(serializer.data)
        return Response(serializer.data)
    

class ScanOrder(generics.UpdateAPIView):
    permission_classes = ()

    def put(self, request, pk=None):
        data = json.loads(request.body.decode('utf-8'))
        instance = get_object_or_404(Order, id=pk)
        serializer = ScanOrderSerializer(instance, data=data)        
        if instance.order_status == 'PENDING':
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=200)
        else:
            return Response(status=400)




class SafetyCheckListQuestionCreateAPIView(generics.ListCreateAPIView):
    
    serializer_class = SafetyChecklistQuestionSerializer
    queryset = SafetyChecklistQuestion.objects.all()
    # def get_queryset(self):
    #     # print(self.request.data)
    #     return self.queryset


# class SafetyCheckListCreateAPIView(generics.ListCreateAPIView):
    
#     serializer_class = SafetyChecklistSerializer
#     queryset = Order.objects.filter(order_status='SAFETY')
#     # lookup_field = 'pk'
#     # def get_queryset(self):
#     #     # print(self.request.data)
#     #     return self.queryset

#     def perform_create(self, serializer):
#         print(self.request.data)
#         dList = self.request.data['questions']
#         order = get_object_or_404(Order, id=self.request.data['order'])
#         # order = Order.objects.get(id=self.request.data['order'])
#         for index in range(len(dList)):
#             questions_values_list=list(dList[index].values())
#             checklist_choice = questions_values_list[2]
#             question = SafetyChecklistQuestion.objects.get(id=questions_values_list[0])
#             update_order = order_status_update(order, 'LAB')
#             SafetyChecklist.objects.create(order=order, checklist_choice=checklist_choice, question=question)
                        

# class SafetyCheckListDetailAPIView(generics.RetrieveAPIView):
    
#     serializer_class = SafetyChecklistSerializer
#     queryset = Order.objects.filter(order_status='Scanned')
#     lookup_field = 'pk'   



class LabinspectionViewSet(viewsets.ModelViewSet):
    
    serializer_class = LabinspectionSerializer
    queryset = Labinspection.objects.all()
    # def get_queryset(self):
    #     # print(self.request.data)
    #     return self.queryset
   
            


class LabInspectionListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LabinspectionSerializer
    queryset = Order.objects.filter(order_status='LAB')


    def perform_create(self, serializer):
        print(self.request.data)
        order = get_object_or_404(Order, id=self.request.data['order'])
        pressure = self.request.data['truck_pressure']
        oxygen = self.request.data['oxygen_content']
        methane = self.request.data['methane_content']
        update_order = order_status_update(order, 'LABRESULTS')        
        return serializer.save(order=order, pressure=pressure, oxygen=oxygen, methane=methane)

class LabResultsListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LabinspectionSerializer
    queryset = Order.objects.filter(order_status='LABRESULTS')

    # def get(self, pk, *args, **kwargs):
        # print(self.request.data)
        # print(pk)


    def perform_create(self, serializer):
        print(self.request.data)
        order = get_object_or_404(Order, id=self.request.data['order'])
        update_order = order_status_update(order, self.request.data['status'])
        return Response(status=202)

class LabResultsDetailView(APIView):
    serializer_class = LabResultsSerializer    

    model = Labinspection

    def get(self, request, pk=None):
        queryset = Labinspection.objects.filter(order_id=pk).first()
        serializer = LabResultsSerializer(queryset)
        return Response(serializer.data)    


class LabResultsVentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LabinspectionSerializer
    queryset = Order.objects.filter(order_status='VENT')

    # def get(self, pk, *args, **kwargs):
        # print(self.request.data)
        # print(pk)


    def perform_create(self, serializer):
        print(self.request.data)
        order = get_object_or_404(Order, id=self.request.data['order'])
        update_order = order_status_update(order, 'LOADING')
        return Response(status=202)


class LoadingListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LoadingSerializer
    queryset = Order.objects.filter(order_status='LOADING')

    # def get(self, pk, *args, **kwargs):
        # print(self.request.data)
        # print(pk)


    def perform_create(self, serializer):
        print(self.request.data)
        order = get_object_or_404(Order, id=self.request.data['order'])
        net_weight = self.request.data['net_weight']
        tare_weight = self.request.data['tare_weight']
        gross_weight = self.request.data['gross_weight']
        update_order = order_status_update(order, 'LOADED')        
        return serializer.save(order=order, tare_weight=tare_weight, net_weight=net_weight, gross_weight=gross_weight)
