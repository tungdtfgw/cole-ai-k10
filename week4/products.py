products = ['macbook air', 'iphone', 'macbook pro', 'ipad', 'apple watch']
prices = [1500, 1000, 2000, 800, 400]

def main():
    running = True
    while running:
        print_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print_products()
        elif choice == 2:
            add_product()
        elif choice == 3:
            remove_product()
        elif choice == 4:
            update_price()
        elif choice == 5:
            running = False
        else:
            print("Invalid choice. Please try again.")

def print_menu():
    print("Product Management System")
    print("1. Show products")
    print("2. Add product")
    print("3. Remove product")
    print("4. Update price")
    print("5. Exit")

def print_products():
    print("Products and prices:")
    for i in range(len(products)):
        print(f'\t{i+1}. {products[i]:>20} : {prices[i]:>8}$')

def add_product():
    print("Add a new product:")
    product = input("Enter product name: ")
    price = int(input("Enter product price: "))
    
    products.append(product)
    prices.append(price)

    print(f'Added {product} successfully.')

def remove_product():
    print('Remove a product:')
    position = int(input("Enter product position to remove: "))
    if position < 1 or position > len(products):
        print("Invalid position.")
        return

    product = products.pop(position - 1)
    price = prices.pop(position - 1)
    print(f'Removed {product} successfully.')

def update_price():
    print('Update product price:')
    position = int(input("Enter product position to update: "))
    if position < 1 or position > len(products):
        print("Invalid position.")
        return

    new_price = int(input("Enter new price: "))
    prices[position - 1] = new_price
    print(f'Updated price of {products[position - 1]} to ${new_price} successfully.')


if __name__ == "__main__":
    main()