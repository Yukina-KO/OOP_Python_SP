from src.Classes.Product.product import Product


def test_product_creation() -> None:
    product = Product("Laptop", "A high-end gaming laptop", 1500.99, 10)

    assert product.name == "Laptop"
    assert product.description == "A high-end gaming laptop"
    assert product.price == 1500.99
    assert product.quantity == 10


def test_product_price_setter() -> None:
    product = Product("Phone", "Latest model smartphone", 999.99, 5)
    product.price = 1200.00
    assert product.price == 1200.00


def test_product_price_negative() -> None:
    product = Product("Tablet", "A lightweight tablet", 499.99, 7)
    product.price = -50
    assert product.price == 499.99


def test_new_product_with_duplicates() -> None:
    product1 = Product("Camera", "DSLR Camera", 800, 2)
    duplicates = [product1]
    new_product = Product.new_product(
        {"name": "Camera", "description": "DSLR Camera", "price": 750, "quantity": 3}, duplicates
    )
    assert new_product.quantity == 5
    assert new_product.price == 800
