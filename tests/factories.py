import factory
from faker import Faker
fake = Faker()

from django.contrib.auth.models import User
from customers.models import models


# class UserFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = User

#     username = fake.name()
#     is_staff = 'True'


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Customer

    name = 'Fake Customer'
    phone = '123456'
    email = fake.email()
    location = 'NBI'


class VehicleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Vehicle

    registration = fake.vehicle.vrm()
    transporter = fake.company.companyName()
    epra_no = 'EPRA/55478516/1212'


class CustomerTrailerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.CustomerTrailer

    customer = factory.SubFactory(CustomerFactory)
    registration = fake.vehicle.vrm()
    trailer = factory.SubFactory(VehicleFactory)


class DriverFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Driver

    name = fake.name()
    national_id = '55478516'
    epra_no = 'EPRA/55478516/1212'


class CustomerDriverFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.CustomerDriver

    customer_id = factory.SubFactory(CustomerFactory)
    name = models.CharField(max_length=200, null=True)
    driver = factory.SubFactory(DriverFactory)


# class ProductFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = models.Product

#     title = 'product_title'
#     category = factory.SubFactory(CategoryFactory)
#     description = fake.text()
#     slug = 'product_slug'
#     regular_price = '9.99'
#     discount_price = '4.99'