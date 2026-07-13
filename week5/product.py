class Product:
    def __init__(self, name, price):
        self.name = name # call setter
        self.price = price # call setter

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if new_name == '':
            raise ValueError('Name cannot be empty!')
        self.__name = new_name

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            raise ValueError('Price must be positive!')
        self.__price = new_price