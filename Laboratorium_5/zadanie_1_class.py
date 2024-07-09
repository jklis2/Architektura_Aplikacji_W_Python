class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_to_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        self.quantity += quantity

    def remove_from_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")
        self.quantity -= quantity

    def is_available(self):
        return self.quantity > 0