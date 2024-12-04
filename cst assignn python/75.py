##75.	Build a simple e-commerce cart system using classes and functions.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})

    def total_price(self):
        return sum(item["product"].price *item["quantity"] for item in self.items)

    def show_cart(self):
        for item in self.items:
            print(f"{item['product'].name} x{item['quantity']} - ${item['product'].price * item['quantity']}")
        print(f"Total: ${self.total_price()}")

# Example usage
product1 = Product("Laptop", 104500)
product2 = Product("Headphones", 14500)

cart = Cart()
cart.add_product(product1, 1)
cart.add_product(product2, 2)
cart.show_cart()