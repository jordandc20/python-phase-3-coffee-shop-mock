from classes.order import Order

class Coffee:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name
    
    def set_name(self,name):
        pass
    
    name = property (get_name, set_name)
    
    def orders(self):
        all_orders=Order.all_orders()
        return [order for order in all_orders if order.coffee == self]

    def customers(self):
        list_set = set([order.customer for order in self.orders()])
        return list(list_set)
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        sum_all_prices = sum([order.price for order in self.orders()])      
        return sum_all_prices/self.num_orders() 

# Coffee num_orders()
    # Returns the total number of times that coffee has been ordered
# Coffee average_price()
    # Returns the average price for a coffee based on its orders
    # Reminder: you can calculate the average by adding up all the orders prices and dividing by the number of orders
    
# Coffee orders()
    # Returns a list of all orders for that coffee
    # orders must be of type Order
    
# Coffee customers()
    # Returns a unique list of all customers who have ordered a particular coffee.
    # Customers must be of type Customer   
    
# Coffee __init__(self, name)
    # Coffees should be initialized with a name, as a string
# Coffee property name
    # Returns the coffee's name
    # Should not be able to change after the coffee is created
    # hint: hasattr()