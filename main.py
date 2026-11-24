from product import Product
from product_manager import ProductManager
from cart import Cart


def main():
    manager = ProductManager()

    manager.add_product(Product("Gaming Laptop", 1099.99, 3))
    manager.add_product(Product("Pametni Telefon", 599.50, 6))
    manager.add_product(Product("Bluetooth Slusalice", 89.99, 10))

    cart = Cart()
    cart.add_to_cart(Product("Laptop", 899.99, 1))
    cart.add_to_cart(Product("Slusalice", 79.99, 2))

    print("\nSadrzaj korpe:")
    cart.display_cart()
    print(f"Ukupna vrijednost korpe: {cart.total_cart_value():.2f}")


if __name__ == "__main__":
    main()
