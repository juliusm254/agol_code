import pytest

from pytest_factoryboy import register
from tests.factories import CustomerFactory, ProductFactory, CategoryFactory

register(CustomerFactory)
register(ProductFactory)  
register(CategoryFactory)  

@pytest.fixture
def new_user1(db, customer_factory):
    user = customer_factory.create()
    return user