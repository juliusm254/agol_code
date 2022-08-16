import json
from multiprocessing import context
from urllib import request
from django.core.exceptions import ImproperlyConfigured
from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, filters, status, generics
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from .models import Order, SafetyChecklist, Labinspection, SafetyChecklistQuestion
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import SafetyChecklistSerializer,ScanOrderSerializer, SafetyChecklistQuestionSerializer, LabinspectionSerializer, OrderSerializer
# from customers.serializers import OrderSerializer
from django.contrib.auth import authenticate
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def get_tokens_for_user(user):
    
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user' : user.id
    }

# Create your views here.
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
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     order = Order.objects.get(pk = self.kwargs['pk'])

    #     if not order:
    #         raise Http404

    #     # continue with the rest of the method populating the context
    #     return context

# class OrderDetailAPIView(
#     # UserQuerySetMixin, 
#     # StaffEditorPermissionMixin,
#     generics.RetrieveAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     lookup_field = 'pk'




# class ScanOrderViewset(viewsets.ModelViewSet):
class ScanOrder(generics.UpdateAPIView):
    permission_classes = ()

    def put(self, request, pk=None):
        data = json.loads(request.body.decode('utf-8'))
        instance = get_object_or_404(Order, id=pk)
        serializer = ScanOrderSerializer(instance, data=data)
        # if instance.order_status == data['order_status']:
        #     return Response(serializer.errors, status=400)
        # else:
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def checklist(request, pk):
    queryset = Order.objects.filter(id=pk)
    serializer = OrderSerializer
    questions =request.body.decode('utf-8')
    data = json.loads(questions)
    print(pk)
    print(data)
    checkist = SafetyChecklist(
        q1=data['q1'],
        q2=data['q2'],
        q3=data['q3'],
        coid=Order.objects.get(id=pk)
    )
    checkist.save()
    # return request.queryset.
    return Response(status=201)


class OrderUpdate(UpdateView):
    model = Order
    fields = ['status']

    def order_update(request, pk):    
        req = request.body.decode('utf-8')
        data = json.loads(req)
        print(pk)
        print(data)
        order = Order(
            status=data['status']
        )
        order.save()
        # return request.queryset.
        return Response(status=201)

# @api_view(['PUT'])
# def order_update(request, pk):    
#     req = request.body.decode('utf-8')
#     data = json.loads(req)
#     print(pk)
#     print(data)
#     order = Order(
#         status=data['status']
#     )
#     order.save()
#     # return request.queryset.
#     return Response(status=201)

class SafetyCheckListQuestionCreateAPIView(generics.ListCreateAPIView):
    
    serializer_class = SafetyChecklistQuestionSerializer
    queryset = SafetyChecklistQuestion.objects.all()
    # def get_queryset(self):
    #     # print(self.request.data)
    #     return self.queryset


class SafetyCheckListCreateAPIView(generics.ListCreateAPIView):
    
    serializer_class = SafetyChecklistSerializer
    queryset = Order.objects.filter(order_status='Scanned')
    # lookup_field = 'pk'
    # def get_queryset(self):
    #     # print(self.request.data)
    #     return self.queryset

    def perform_create(self, serializer):
        print(self.request.data['order'])
        dList = self.request.data['questions']
        order = Order.objects.get(id=self.request.data['order'])
        for index in range(len(dList)):
            questions_values_list=list(dList[index].values())
            # print(someweird[0])
            # print('Datatype : ',type(someweird))
            order = Order.objects.get(id=self.request.data['order'])
            checklist_choice = questions_values_list[2]
            question = SafetyChecklistQuestion.objects.get(id=questions_values_list[0])
            SafetyChecklist.objects.create(order=order, checklist_choice=checklist_choice, question=question)
            order.order_status = 'SAFETY'
            order.save()
            

class SafetyCheckListDetailAPIView(generics.RetrieveAPIView):
    
    serializer_class = SafetyChecklistSerializer
    queryset = Order.objects.filter(order_status='Scanned')
    lookup_field = 'pk'
    



class LabinspectionViewSet(viewsets.ModelViewSet):
    
    serializer_class = LabinspectionSerializer
    queryset = Labinspection.objects.all()
    # def get_queryset(self):
    #     # print(self.request.data)
    #     return self.queryset
   
            


class LabInspectionListCreateAPIView(generics.ListCreateAPIView):
    model = Labinspection
    serializer_class = LabinspectionSerializer
    queryset = Order.objects.filter(order_status='SAFETY')


    def perform_create(self, serializer):
        print(self.request.data)

        
