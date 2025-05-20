import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_name_validation():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"
    with pytest.raises(TypeError):
        Coffee(123)
    with pytest.raises(ValueError):
        Coffee("Ab")
    with pytest.raises(AttributeError):
        coffee.name = "NewName"

def test_orders():
    customer = Customer("Zara")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert len(coffee.orders()) == 1
    assert coffee.orders()[0].price == 5.0

def test_customers():
    customer = Customer("Zara")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert coffee.customers() == [customer]

def test_num_orders():
    customer = Customer("Zara")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert coffee.num_orders() == 1
    Order(customer, coffee, 4.0)
    assert coffee.num_orders() == 2

def test_average_price():
    customer = Customer("Zara")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert coffee.average_price() == 5.0
    Order(customer, coffee, 3.0)
    assert coffee.average_price() == 4.0