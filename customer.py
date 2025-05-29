class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        self._orders = []
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(name) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = name

    def orders(self):
        """Returns a list of all orders made by this customer"""
        return self._orders

    def coffees(self):
        """Returns a unique list of all coffees ordered by this customer"""
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        """Creates a new order and associates it with this customer"""
        if not isinstance(coffee, Coffee):
            raise TypeError("Must provide a Coffee instance")
        if not isinstance(price, float):
            raise TypeError("Price must be a float")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
            
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        """
        Returns the customer who has spent the most on the given coffee
        Returns None if no orders exist for that coffee
        """
        if not isinstance(coffee, Coffee):
            raise TypeError("Must provide a Coffee instance")
            
        max_spender = None
        max_amount = 0.0
        
        for customer in cls.all_customers:
            total_spent = sum(
                order.price 
                for order in customer.orders() 
                if order.coffee == coffee
            )
            
            if total_spent > max_amount:
                max_amount = total_spent
                max_spender = customer
                
        return max_spender if max_amount > 0 else None

    def __repr__(self):
        return f"<Customer name='{self.name}'>"


# Import at bottom to avoid circular imports
from coffee import Coffee
from order import Order