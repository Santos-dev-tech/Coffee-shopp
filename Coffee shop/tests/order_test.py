import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_price_validation():
    customer = Customer("Zara")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert order.price == 5.0
    with pytest.raises(TypeError):
        Order(customer, coffee, "5.0")
    with pytest.raises(ValueError):
        Order(customer, coffee, 11.0)
    with pytest.raises(AttributeError):
        order.price = 6.0

def test_customer():
    customer = Customer("Zara")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer

def test_coffee():
    customer = Customer("Zara")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert order.coffee == coffee

def test_type_validation():
    customer = Customer("Zara")
    coffee = Coffee("Latte")
    with pytest.raises(TypeError):
        Order("not a customer", coffee, 5.0)
    with pytest.raises(TypeError):
        Order(customer, "not a coffee", 5.0)