import pytest
from rest_framework.test import APIClient
from backend.models import Product, Order, Contact, User
from model_bakery import baker

@pytest.fixture()
def client():
    return APIClient()

@pytest.fixture()
def product_factory():
    def factory(*args, **kwargs):
        return baker.make(Product, *args, **kwargs)
    return factory

@pytest.fixture()
def contact_factory():
    def factory(*args, **kwargs):
        return baker.make(Contact, *args, **kwargs)
    return factory

@pytest.fixture()
def order_factory():
    def factory(*args, **kwargs):
        return baker.make(Order, *args, **kwargs)
    return factory

@pytest.fixture()
def user():
    return User.objects.create_user('admin')

@pytest.mark.django_db
def test_get_products(client, product_factory):
    products = product_factory(_quantity=5)
    response = client.get(path='/api/v1/products')
    assert response.status_code == 200
    data = response.json()
    for i, m in enumerate(data):
        assert m['name'] == products[i].name

@pytest.mark.django_db
def test_get_contacts(client, user, contact_factory):
    contacts = contact_factory(_quantity=5)
    response = client.get(path='/api/v1/user/contact')
    assert response.status_code == 200
    data = response.json()
    # for i, m in enumerate(data):
    #     assert m['name'] == contacts[i].name