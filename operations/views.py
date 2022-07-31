import json
from multiprocessing import context
from urllib import request
from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, filters, status
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from .models import Order, SafetyChecklist, Labinspection
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import SafetySerializer, LabinspectionSerializer
from customers.serializers import OrderSerializer
from django.contrib.auth import authenticate

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



class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    serializer_class = OrderSerializer
    # queryset = Order.objects.all()
    # pagination_class =  LeadPagination
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('status')
    def get_queryset(self):
        # print(self.request.data)
        pass
   
    


    # def perform_update(self,serializer):  

    #     print(request)      
    #     serializer.save(status='Scanned')
    #     return self.queryset.filter(status='Pending')

    

    # def partial_update(self, request, *args, **kwargs):
    #     instance = self.queryset.get(pk=kwargs.get('pk'))
    #     serializer = self.serializer_class(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)


# def order_update(request, pk):
#     req = request.body.decode('utf-8')
#     data = json.loads(req)
#     print(pk)
#     order = get_object_or_404(Order, id=pk)
#     order_update = order(
#         status=data['status']
#     )
#     order_update.save()
#     return Response(status=201)


# @csrf_exempt
# def order_update(request, pk):    
#     req = request.body.decode('utf-8')
#     data = json.loads(req)
#     print(pk)
#     print(data)
#     order = get_object_or_404(Order, id=pk)
#     order = Order(
#         status=data['status']
#     )
#     order.save()
#     # return request.queryset.
#     return Response(status=201)

class ScanOrderViewset(viewsets.ModelViewSet):
    permission_classes = ()
    model = Order
    serializer_class = OrderSerializer  
    # queryset = Order.objects.all()
    def get_queryset(self):
        # print(self.request.data)
        pass

    def update(self, request, pk=None):
        req = request.body.decode('utf-8')
        data = json.loads(req)
        order = get_object_or_404(Order, id=pk)
        serializer = self.serializer_class(order, data, partial=True)
        
        # Improver Validation for already processed orders 
        if order.status == data['status']:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
           
            order = Order(
                status=data['status']
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            # return request.queryset.
            return Response(serializer.data)



class SafetyViewSet(viewsets.ModelViewSet):
       
    serializer_class = SafetySerializer
    queryset = Order.objects.all()
    def get_queryset(self):
        # print(self.request.data)
        return self.queryset.filter(status='Scanned')


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

class ChecklistViewSet(viewsets.ModelViewSet):
    
    # serializer_class = ChecklistSerializer
    queryset = SafetyChecklist.objects.all()
    # def get_queryset(self):
    #     # print(self.request.data)
    #     return self.queryset
   
class LabinspectionViewSet(viewsets.ModelViewSet):
    
    serializer_class = LabinspectionSerializer
    queryset = Labinspection.objects.all()
    # def get_queryset(self):
    #     # print(self.request.data)
    #     return self.queryset
   
            

    
    
        
