class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_description(self):
        print(f'{self.item_name}: {self.item_description}')

    def print_item_cost(self):
        total_cost = self.item_quantity * self.item_price
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}')


class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, item_to_modify):
        found = False
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                item.item_quantity = item_to_modify.item_quantity
                found = True
                break
        if not found:
            print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        print("OUTPUT SHOPPING CART")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")

        if not self.cart_items:  
            print("Number of Items: 0")
            print("SHOPPING CART IS EMPTY")
            print("Total: $0")
        else:
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print("Item Descriptions")
            for item in self.cart_items:
                item.print_item_description()


def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")


def execute_menu(choice, cart):
    if choice == 'a':
        print("ADD ITEM TO CART")
        name = input("Enter the item name: ")
        description = input("Enter the item description: ")
        price = int(input("Enter the item price: "))
        quantity = int(input("Enter the item quantity: "))
        new_item = ItemToPurchase(name, price, quantity, description)
        cart.add_item(new_item)
    elif choice == 'r':
        print("REMOVE ITEM FROM CART")
        name = input("Enter name of item to remove: ")
        cart.remove_item(name)
    elif choice == 'c':
        print("CHANGE ITEM QUANTITY")
        name = input("Enter the item name: ")
        quantity = int(input("Enter the new quantity: "))
        modified_item = ItemToPurchase(item_name=name, item_quantity=quantity)
        cart.modify_item(modified_item)
    elif choice == 'i':
        print("\nOUTPUT ITEMS' DESCRIPTIONS")
        cart.print_descriptions()
    elif choice == 'o':
        cart.print_total()
    elif choice == 'q':
        return False
     

if __name__ == '__main__':
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    cart = ShoppingCart(customer_name, current_date)

    while True:
        print_menu()
        choice = input("Choose an option: ").lower()
        while choice not in ['a', 'r', 'c', 'i', 'o', 'q']:
            choice = input("Choose an option: ").lower()
        if choice == 'q':
            break
        execute_menu(choice, cart)