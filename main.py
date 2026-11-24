from product import Product
from product_manager import ProductManager
from cart import Cart


def main():
    manager = ProductManager()

    manager.add_product(Product("Laptop", 899.99, 5))
    manager.add_product(Product("Telefon", 499.50, 8))
    manager.add_product(Product("Slusalice", 79.99, 15))

    print("Proizvodi u inventaru:")
    manager.display_products()
    print(f"Ukupna vrijednost inventara: {manager.total_inventory_value():.2f}")

    cart = Cart()
    cart.add_to_cart(Product("Laptop", 899.99, 1))
    cart.add_to_cart(Product("Slusalice", 79.99, 2))

    print("\nSadrzaj korpe:")
    cart.display_cart()
    print(f"Ukupna vrijednost korpe: {cart.total_cart_value():.2f}")


if __name__ == "__main__":
    main()
