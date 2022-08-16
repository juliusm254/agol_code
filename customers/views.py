# from django.shortcuts import render

# # Write a python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned below:
# # The ticket number should be generated as airline:src:dest:number
# # where :
# # 1. Consider AI as the value for airline
# # 2. src and dest should be the first three characters of the source and destination cities.
# # 3. number should be auto-generated starting from 101
# # The program should return the list of ticket numbers of last five passengers.
# # Note: If passenger count is less than 5, return the list of all generated ticket numbers.

# def generate_order(airline,source,destination,no_of_passengers):
#     ticket_number_list = []
#     i = 0
#     if no_of_passengers < 5:
#         while no_of_passengers != 0:
#             ticket_number_list.append(airline + ":" + source[:3] + ":" + destination[:3] + ":" + str(101+i))
#             i = i+1
#             no_of_passengers = no_of_passengers - 1
#     else:
#         for i in range(5):
#             ticket_number_list.append(airline + ":" + source[:3] + ":" + destination[:3] + ":" + str(100+no_of_passengers))
#             i = i+1
#             no_of_passengers = no_of_passengers - 1
#         ticket_number_list = ticket_number_list[::-1]

#     return ticket_number_list

# #Provide different values for airline,source,destination,no_of_passengers and test your program
# print(generate_ticket("AI","Bangalore","London",7))

from email.policy import default
from django.db.models import Prefetch, Count, Q
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import (BulkOrder, Order, 
                    Vehicle,
                    BulkOrderBalance, 
                    Driver, 
                    Customer, 
                    CustomerDriver,
                    CustomerTruck,
                    CustomerTrailer)
from .serializers import (  OrderSerializer, 
                            CustomerSerializer, 
                            VehicleSerializer, 
                            CustomerDriverSerializer, 
                            DriverSerializer, 
                            CustomerTruckSerializer,
                            CustomerTrailerSerializer,
                            BulkOrderSerializer,
                            )



def get_tokens_for_user(user):
    
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user' : user.id,
        'customer'  : user.customer_id.id
    }

def get_customer_id(self):
    customer_id = self.request.user.customer_id.id
    return customer_id


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        print(user)
        if user:
            return Response( get_tokens_for_user(user) )
        else:
            # return Response( get_tokens_for_user(user) )
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

from django.db.models import F
    
class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    # permission_classes = [IsAuthenticated,]
    serializer_class = OrderSerializer
    # queryset = Order.objects.all()
    # pagination_class =  LeadPagination
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('company', 'contact_person')
    
    def get_queryset(self):
        # customer_id = '3'
        # # customer_id = self.request.user.customer_id.id
        # queryset = Order.objects.filter(customer_id=customer_id).select_related('driver', 'truck', 'trailer', 'customer' )
        # # orders = []

        # # for order in queryset:
        # #     # orders.append({'id': order.id, 'customer': order.customer, 'driver': order.driver, 'created_at': order.created_at, 'modified_at': order.modified_at,'destination': order.destination, 'order_quantity': order.order_quantity, 'status': order.status, 'truck': order.truck, 'trailer': order.trailer})
        # #     orders.append({'id': order.id, 'driver': order.driver, })

        # # print(orders)     
        # return queryset
        pass

    def perform_create(self, serializer):
        truck = Vehicle.objects.filter(id=self.request.data['truck']).first()
        trailer = Vehicle.objects.filter(id=self.request.data['trailer']).first()
        driver = Driver.objects.filter(id=self.request.data['driver']).first()
        cust_obj = Customer.objects.get(id=self.request.user.customer_id.id)
        # truck = Vehicle.objects.get(id=1)
        # trailer = Vehicle.objects.get(id=1)
        # driver = Driver.objects.get(id=1)
        # cust_obj = Customer.objects.get(id=1)
        print(cust_obj)
        destination = self.request.data['destination'],
        order_quantity = self.request.data['order_quantity']

        if not cust_obj.bulk_customer:
        
            cust_order = Order(
                driver = driver,
                customer = cust_obj,
                trailer = trailer,
                truck = truck,
                destination = destination,
                order_quantity = order_quantity,
                
            )
            cust_order.save()

        else:
            # print('we got here')
            # try:
            #     # query = BulkOrderBalance.objects.get(customer_id=1)
            #     query = BulkOrderBalance.objects.get(customer_id=cust_obj.id)
            #     # order_quantity = self.request.data['order_quantity']
            #     balance_obj = query
            #     balance = balance_obj.quantity
            #     if balance > 0:
            #         print(balance)
            #         newquantity = balance - int(order_quantity)
            #         balance_obj.quantity = newquantity
            #         if newquantity > 0:
            #             print(balance_obj.quantity)
            #             balance_obj.save()
            #         else:
            #             print('else in')
            #     else:
            #             print('else out')

                
            # except:
            #     print('except')

            '''New Code To be reviewed'''

            print('we got here')
            balance_obj = BulkOrderBalance.objects.filter(customer_id=cust_obj.id)
            # order_quantity = self.request.data['order_quantity']
            balance_obj.update(quantity=F('quantity') - order_quantity)



                

            #     if balance > 0:
            #         print(balance)
            #         newquantity = balance - int(order_quantity)
            #         balance_obj.quantity = newquantity
            #         if newquantity > 0:
            #             print(balance_obj.quantity)
            #             balance_obj.save()
            #         else:
            #             print('else in')
            #     else:
            #             print('else out')

                
            # except:
            #     print('except')


class BulkOrderViewSet(viewsets.ModelViewSet):
    # permission_classes = ()
    # permission_classes = [IsAuthenticated,]
    serializer_class = BulkOrderSerializer
    # queryset = Order.objects.all()
    # pagination_class =  LeadPagination
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('company', 'contact_person')

    '''Below query passes UserID who created Lead without team line'''

    def perform_create(self, serializer):
        print(self)
        cust_obj = Customer.objects.get(id=self.request.data['customer']).id
        
        cust_order = BulkOrder(
            customer_id = cust_obj,
            description = self.request.data['description'],
            quantity = self.request.data['quantity'],
            
        )
        print('gets here pre save perform_create in view')
        cust_order.save(self)

    def get_queryset(self):
        customer_id = self.request.user.customer_id.id
        return BulkOrderBalance.objects.filter(customer_id=customer_id)


class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    serializer_class = CustomerSerializer
    queryset = Order.objects.all()
    # pagination_class =  LeadPagination
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('company', 'contact_person')

    '''Below query passes UserID who created Lead without team line'''

    def perform_create(self, serializer):
        serializer.save()

    # def get_queryset(self, ):
    #     return self.queryset.filter() 


class VehicleViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    # pagination_class =  LeadPagination
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('company', 'contact_person')

    '''Below query passes UserID who created Lead without team line'''

    def perform_create(self, serializer):
        '''below connects team to the lead'''
        # order = Order.objects.filter(members__in=[self.request.user]).first()
        serializer.save() 

class DriverViewSet(viewsets.ModelViewSet):
    # permission_classes = ()
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()
    # pagination_class =  LeadPagination
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('company', 'contact_person')

    '''Below query passes UserID who created Lead without team line'''

    def perform_create(self, serializer):
        serializer.save() 


class CustomerDriverViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    model = CustomerDriver
    serializer_class = CustomerDriverSerializer
    # queryset = Driver.objects.all()
    # pagination_class =  LeadPagination
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('company', 'contact_person')

    def get_queryset(self):
        # customer_id = 2
        customer_id = self.request.user.customer_id.id
        return CustomerDriver.objects.filter(customer_id=customer_id).prefetch_related(
            Prefetch('driver',
            queryset=Driver.objects.all())
        )

        return CustomerDriver.objects.filter(customer_id=customer_id)

    def perform_create(self, request):
        national_id = self.request.data['national_id']
        obj = Driver.objects.filter(national_id=national_id).first()
        cust = Customer.objects.get(id=self.request.data['customer_id'])
        cust_driver = CustomerDriver(
            name = self.request.data['name'],
            customer_id = cust,
            driver = obj
        )
        cust_driver.save(self)

class VehicleViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    # pagination_class =  LeadPagination
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('company', 'contact_person')

    

    '''Below query passes UserID who created Lead without team line'''

    def perform_create(self, serializer):
        '''below connects team to the lead'''
        # order = Order.objects.filter(members__in=[self.request.user]).first()
        serializer.save() 


class CustomerTruckViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    model = CustomerTruck
    serializer_class = CustomerTruckSerializer    

    def get_queryset(self):
        # customer_id = 3
        customer_id = self.request.user.customer_id.id
        return CustomerTruck.objects.filter(customer_id=customer_id)

    def perform_create(self, request):
        registration = self.request.data['registration']
        
        obj = Vehicle.objects.filter(registration=registration).first()
        cust = get_customer_id(self)
        cust_truck = CustomerTruck(
            registration = registration,
            customer_id = cust,
            truck = obj
        )
        print(cust_truck)
        cust_truck.save(self)  


class CustomerTrailerViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated,]
    model = (CustomerTrailer)
    serializer_class = CustomerTrailerSerializer
        

    def get_queryset(self):
        # customer_id = '2'
        customer_id = self.request.user.customer_id.id
        return CustomerTrailer.objects.filter(customer_id=customer_id).prefetch_related(
            Prefetch('trailer',
            queryset=Vehicle.objects.all())
        )

       
    def perform_create(self, request):
        registration = self.request.data['registration']
        
        obj = Vehicle.objects.filter(registration=registration).first()
        cust = get_customer_id(self)
        cust_trailer = CustomerTrailer(
            registration = registration,
            customer_id = cust,
            trailer = obj
        )        
        cust_trailer.save(self)
        