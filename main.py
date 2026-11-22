from product import Product
from product_manager import ProductManager


def main():
    manager = ProductManager()

    manager.add_product(Product("Laptop", 899.99, 5))
    manager.add_product(Product("Telefon", 499.50, 8))
    manager.add_product(Product("Slusalice", 79.99, 15))

    print("Proizvodi u inventaru:")
    manager.display_products()
    print(f"Ukupna vrijednost inventara: {manager.total_inventory_value():.2f}")


if __name__ == "__main__":
    main()
