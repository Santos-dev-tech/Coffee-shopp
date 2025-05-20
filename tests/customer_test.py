import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_name_validation():
    customer = Customer("Zara")
    assert customer.name == "Zara"
    with pytest.raises(TypeError):
        Customer(123)
    with pytest.raises(ValueError):
        Customer("A" * 16)

def test_orders():
    customer = Customer("Zara")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert len(customer.orders()) == 1
    assert customer.orders()[0].price == 5.0

def test_coffees():
    customer = Customer("Zara")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert customer.coffees() == [coffee]

def test_create_order():
    customer = Customer("Zara")
    coffee = Coffee("Latte")
    new_order = customer.create_order(coffee, 3.0)
    assert len(customer.orders()) == 1
    assert new_order.price == 3.0

def test_most_aficionado():
    customer = Customer("Zara")
    coffee = Coffee("Latte")
    Order(customer, coffee, 5.0)
    liam = Customer("Liam")
    Order(liam, coffee, 2.0)
    assert Customer.most_aficionado(coffee).name == "Zara"