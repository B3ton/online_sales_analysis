class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Proizvod: {self.name} | Cijena: {self.price:.2f} | Kolicina: {self.quantity}")

    def update_quantity(self, quantity):
        self.quantity = quantity
