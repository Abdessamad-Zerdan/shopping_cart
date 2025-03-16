products = {
    1: ("Apple", 2),
    2: ("Banana", 3),
    3: ("Orange", 2.5),
    4: ("Kiwi", 4),
    5: ("Lemon", 3),
    6: ("Ananas", 7),
}

def display_products(products):
    print("\nAvailable Products:")
    for number, (product, price) in products.items():
        print(f"{number}. {product}: ${price:.2f} per (kg)")

def get_quantity(product_name):
    while True:
        try:
            quantity = float(input(f"Enter the quantity of {product_name} you want (kg/units): "))
            if quantity > 0:
                return quantity
            else:
                print("Quantity must be greater than 0. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def view_cart(cart, total_cost):
    if not cart:
        print("\nYour cart is empty.")
    else:
        print("\nYour Cart:")
        for product_name, details in cart.items():
            quantity, subtotal = details
            print(f"{product_name} - {quantity} units - Subtotal: ${subtotal:.2f}")
        print(f"\nTotal Cost: ${total_cost:.2f}")

def shopping_program():
    total_cost = 0
    cart = {}
    print("Welcome to the Shopping Program!")

    while True:
        print("\nChoose an option:")
        print("1. Display products")
        print("2. Add products to cart")
        print("3. View cart")
        print("4. Proceed to payment")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            display_products(products)

        elif choice == "2":
            while True:
                display_products(products)
                try:
                    product_choice = int(input("\nEnter the number of the product you want to buy (or 0 to stop adding): "))
                    if product_choice == 0:
                        break
                    elif product_choice in products:
                        product_name, product_price = products[product_choice]
                        quantity = get_quantity(product_name)
                        subtotal = product_price * quantity
                        total_cost += subtotal
                        if product_name in cart:
                            cart[product_name][0] += quantity
                            cart[product_name][1] += subtotal
                        else:
                            cart[product_name] = [quantity, subtotal]
                        print(f"{quantity} units of {product_name} added to your cart. Current total: ${total_cost:.2f}")
                    else:
                        print("Invalid product number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        elif choice == "3":
            view_cart(cart, total_cost)

        elif choice == "4":
            if not cart:
                print("\nYour cart is empty. Add products before proceeding to payment.")
            else:
                print("\nProceeding to payment...")
                view_cart(cart, total_cost)
                print("Thank you for shopping with us! Goodbye!")
                break

        elif choice == "5":
            print(f"\nExiting the program. Your total is: ${total_cost:.2f}. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

shopping_program()
