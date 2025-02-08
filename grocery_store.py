# Grocery Store management

class Store:
    def __init__(self, Owners_name, Store_name, address, time):
        self.Owners_name = Owners_name
        self.Store_name = Store_name
        self.address = address
        self.time = time

class Products:
    def __init__(self):
        self.items = []

    def add_item(self, item, price, availability):
        self.items.append({"item": item, "price": price, "availability": availability})

    def get_items(self):
        return self.items        

class Price:
    def __init__(self,price):
        self.price = price

class Avail_not:
    def __init__(self,availability):
        self.availability= availability
    
    def get_availability(self):
        return self.availability

class Display:
    def get_store_details(Store):
        print(f"\t\nStore Details: \nStore owners name: {Store.Owners_name}\nStore name: {Store.Store_name}\nStore address : {Store.address} 403802\nStore timings are: {Store.time}")

    def get_product_details(Products):
        if not Products.get_items():
            print("\nNo Items is available in store")
        else:
            for product in Products.get_items():
                print(f"Item: {product['item']}, Price: {product['price']}, Availability: {product['availability']}")

my_store = Store("Rahul","General Store","Opposite to kharewada vasco da gama Goa","10am to 8pm")

my_products = Products()
while True:
    print("\n\t\t\t    ----STORE IS OPEN NOW----")
    print(f"\n\t\t------------WELCOME TO MY {my_store.Store_name}------------")
    print("\nCheck for your option")
    print("1) Add Items")
    print("2) Check Store Details")
    print("3) Check store Address")
    print("4) Check store timings")
    print("5) Display Total Items")
    print("6) Exit")

    user_input = input()

    if user_input == '6':
        print("Store is closing...")
        break
    elif user_input == '1':
        item = input("Enter your items name:\n")
        price = int(input(f"Enter price for {item}\n"))
        availability = input(f"Enter avail for {item} (In stock/Out of stock)\n")
        my_products.add_item(item,price,availability)
        print(f"\n{item} added in list\n")

    elif user_input == '2':
        Display.get_store_details(my_store)

    elif user_input == '3':
        print(f"\nStore Address is: {my_store.address}")

    elif user_input == '4':
        print(f"\nStore timings are: {my_store.time}")

    elif user_input == '5':
        Display.get_product_details(my_products)    

    else:
        print("Invalid Option Choose option between (1-5)")