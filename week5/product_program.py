# syntax: from file_name import ClassName
from product import Product

class AppleShop:
    def __init__(self, name='FPTShop'):
        self.name = name
        self.__load()

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if new_name == '':
            raise ValueError('Name cannot be empty!')
        self.__name = new_name
    
    # private method
    def __load(self):
        macbook = Product('macbook air', 1500)
        iphone = Product('iphone', 1000)
        macpro = Product('macbook pro', 2000)
        ipad = Product('ipad', 800)
        watch = Product('apple watch', 400)

        self.__products = []
        self.__products.append(macbook)
        self.__products.append(iphone)
        self.__products.append(macpro)
        self.__products.append(ipad)
        self.__products.append(watch)
    # public method
    def operate(self):
        running = True
        while running:
            self.__print_menu()
            choice = int(input('Enter your choice: '))
            if choice == 1: 
                self.__show_products()
            elif choice == 2: 
                self.__add_product()
            elif choice == 3: 
                self.__remove_product()
            elif choice == 4: 
                self.__update_price()
            elif choice == 5: 
                running = False
            else: print('Invalid choice!')
    
    def __print_menu(self):
        print("Product Management System")
        print("1. Show products")
        print("2. Add product")
        print("3. Remove product")
        print("4. Update price")
        print("5. Exit")

    def __show_products(self):
        print('All product in store')
        for i in range(len(self.__products)):
            p = self.__products[i]
            print(f'{i+1}. {p.name}: {p.price}')

    def __add_product(self):
        print('Add a new product')
        name = input('Enter product name: ')
        price = int(input('Enter product price: '))
        p = Product(name, price)
        self.__products.append(p)
        print(f'{name} added to store!')
    
    def __remove_product(self):
        pass

    def __update_price(self):
        pass

### MAIN PROGRAM ###
shop = AppleShop()
shop.operate()