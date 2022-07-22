from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
from customers.models import Order, BulkOrder, Customer, Vehicle, CustomerTrailer, CustomerDriver, CustomerTruck, Driver
import random

class Command(BaseCommand):
    help="Command information"

    def handle(self, *args, **kwargs):
        
        fake = Faker()

        print(fake.address())

        # for _ in range(10):
        #     name =  fake.company()
        #     phone = random.randint(22155541, 554544541)
        #     email = fake.email()
        #     location = 'KSM'
        #     bulk_customer = random.randint(0, 1)
        #     Customer.objects.create(name=name, phone=phone, email=email, location=location, bulk_customer=bulk_customer)

        # for _ in range(30):
        #     registration = 'KAC 112'
        #     transporter = fake.company()
        #     epra_no = 'EPRA/1554'
        #     Vehicle.objects.create(registration=registration, transporter=transporter, epra_no=epra_no)

        # for _ in range(10):
        #     customer = Customer.objects.get(pk=2)
        #     registration = 'ZE 001'
        #     trailer = Vehicle.objects.get(pk=random.randint(0, 80))
        #     CustomerTrailer.objects.create(registration=registration, customer=customer, trailer=trailer)

        # for _ in range(50):
        #     name = fake.name()
        #     national_id = random.randint(22155541, 554544541)
        #     epra_no = random.randint(2215, 554544)
        #     Driver.objects.create(name=name, national_id=national_id, epra_no=epra_no)


        for _ in range(30):
            customer = Customer.objects.get(pk=random.randint(1, 2))    
            destination = 'KSM'    
            order_quantity = random.randint(25000, 30000)  
            
            driver = Driver.objects.get(id=random.randint(1, 30))
            truck = Vehicle.objects.get(id=random.randint(1, 30))
            trailer = Vehicle.objects.get(id=random.randint(1, 30))  
            Order.objects.create(customer=customer, destination=destination, order_quantity=order_quantity, driver=driver, truck=truck, trailer=trailer)


        # for _ in range(30):
        #     customer = Customer.objects.get(pk=2)
        #     name = fake.name()
        #     driver = Driver.objects.get(pk=random.randint(80, 100))
        #     CustomerDriver.objects.create(customer=customer, name=name, driver=driver)

        # for _ in range(30):
        #     customer = Customer.objects.get(pk=random.randint(1, 5))
        #     quantity = random.randint(2215, 554544)
        #     BulkOrder.objects.create(customer=customer, quantity=quantity)