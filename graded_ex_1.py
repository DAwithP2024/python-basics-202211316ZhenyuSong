# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    if sort_order == "asc":
        return sorted(products_list, key=lambda x: x[1])
    elif sort_order == "desc":
        return sorted(products_list, key=lambda x: x[1], reverse=True)

def display_products(products_list):
    for index, (product, price) in enumerate(products_list):
        print(f"{index + 1}. {product} - ${price}")

def display_categories():
    for index, category in enumerate(products):
        print(f"{index + 1}. {category}")

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    total_cost = 0
    for product, price, quantity in cart:
        total_cost += price * quantity
        print(f"{product} - ${price} x {quantity} = ${price * quantity}")
    print(f"Total cost: ${total_cost}")

def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}\nEmail: {email}\nItems Purchased:\n")
    for product, price, quantity in cart:
        print(f"{quantity} x {product} - ${price} = ${price * quantity}")
    print(f"Total: ${total_cost}\nDelivery Address: {address}\nYour items will be delivered in 3 days.\nPayment will be accepted upon delivery.")

def validate_name(name):
    return name.replace(" ", "").replace("-", "").isalpha() and " " in name

def validate_email(email):
    return "@" in email

def main():
    name = input("Please enter your name: ")
    email = input("Please enter your email address: ")
    while not validate_name(name):
        name = input("Invalid name. Please enter your name: ")
    while not validate_email(email):
        email = input("Invalid email address. Please enter your email address: ")
    cart = []
    while True:
        display_categories()
        category_choice = input("Please select a category by entering the number: ")
        if category_choice.isdigit() and 1 <= int(category_choice) <= len(products):
            category = list(products.keys())[int(category_choice) - 1]
            display_products(products[category])
            product_choice = input("Please select a product by entering the number: ")
            if product_choice.isdigit() and 1 <= int(product_choice) <= len(products[category]):
                product = products[category][int(product_choice) - 1]
                quantity = input("Please enter the quantity: ")
                while not quantity.isdigit() or int(quantity) <= 0:
                    quantity = input("Invalid quantity. Please enter a valid quantity: ")
                add_to_cart(cart, product, int(quantity))
            else:
                print("Invalid product choice. Please try again.")
        else:
            print("Invalid category choice. Please try again.")
        
        print("\n1. Select a product to buy\n2. Sort the products according to the price.\n3. Go back to the category selection.\n4. Finish shopping")
        choice = input("Please enter your choice: ")
        if choice == '2':
            sort_order = input("Enter 1 for ascending or 2 for descending: ")
            sorted_products = display_sorted_products(products[category], sort_order)
            display_products(sorted_products)
        elif choice == '3':
            continue
        elif choice == '4':
            if cart:
                total_cost = sum(price * quantity for product, price, quantity in cart)
                address = input("Please enter your delivery address: ")
                generate_receipt(name, email, cart, total_cost, address)
            else:
                print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
            break
    

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
