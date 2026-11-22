class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        if not self.products:
            print("Inventar je prazn.")
            return

        for product in self.products:
            product.display_info()

    def total_inventory_value(self):
        return sum(product.price * product.quantity for product in self.products)

    def remove_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                self.products.remove(product)
                print(f"Proizvod '{product.name}' je uklonjen.")
                return True

        print(f"Proizvod '{name}' nije pronadjen.")
        return False
