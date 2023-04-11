
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.price = price
        self.customer = customer
        self.coffee = coffee
        Order.all.append(self)  
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,price):
        if 1<= price <= 10:
            self._price = price
    
    @classmethod
    def all_orders(cls):
        return cls.all
    


# Order __init__(self, customer, coffee, price)
    # Orders should be initialized with a customer, coffee, and a price (a number)
# Order property price
    # Returns the price for a coffee
    # Price must be a number between 1 and 10, inclusive