from classes.order import Order

class Customer:
    def __init__(self, name):
        self._name = name
            
    def get_name(self):
        return self._name
    
    def set_name(self,name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
    
    name = property(get_name, set_name)    

    def orders(self):
        all_orders=Order.all_orders()
        return [order for order in all_orders if order.customer == self]

    
    def coffees(self):
        list_set = set([order.coffee for order in self.orders()])
        return list(list_set)
    
    def create_order(self,coffee, price):
        Order(self,coffee,price)
#Customer create_order(coffee, price)
    #given a coffee object and a price(as an integer), creates a new order and associates it with that customer and coffee.    
# Customer orders()
    # Returns a list of all orders a customer has ordered
    # orders must be of type Order
# Customer coffees()
    # Returns a unique list of all coffees a customer has ordered
    # Coffees must be of type Coffee

# Customer __init__(self, name)
    # Customer should be initialized with a name
# Customer property name
    # Return name
    # Names must be of type str
    # Names must be between 1 and 15 characters, inclusive