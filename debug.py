from customer import Customer
from coffee import Coffee
from order import Order

# Sample usage to test functionality
def main():
    # Create customers
    zara = Customer("Zara")
    liam = Customer("Liam")

    # Create coffees
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")

    # Create orders
    order1 = zara.create_order(latte, 5.0)
    order2 = zara.create_order(espresso, 3.5)
    order3 = liam.create_order(latte, 4.5)

    # Test relationships
    print(f"Zara's orders: {len(zara.orders())}")  # Should be 2
    print(f"Zara's coffees: {[coffee.name for coffee in zara.coffees()]}")  # ['Latte', 'Espresso']
    print(f"Latte's customers: {[customer.name for customer in latte.customers()]}")  # ['Zara', 'Liam']
    print(f"Latte's number of orders: {latte.num_orders()}")  # 2
    print(f"Latte's average price: {latte.average_price()}")  # 4.75
    print(f"Most aficionado for Latte: {Customer.most_aficionado(latte).name}")  # Zara

if __name__ == "__main__":
    main()