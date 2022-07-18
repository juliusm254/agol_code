from . import CustomerFactory

customers = CustomerFactory.create_batch(10)

for customer in customers:
    print(customer)