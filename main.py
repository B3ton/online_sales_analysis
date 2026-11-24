from product import Product
from product_manager import ProductManager


def main():
    manager = ProductManager()

    manager.add_product(Product("Gaming Laptop", 1099.99, 3))
    manager.add_product(Product("Pametni Telefon", 599.50, 6))
    manager.add_product(Product("Bluetooth Slusalice", 89.99, 10))


if __name__ == "__main__":
    main()
