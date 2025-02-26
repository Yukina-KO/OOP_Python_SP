from src.Classes.Product.product import Product


def test_product_creation() -> None:
    product = Product("Laptop", "A high-end gaming laptop", 1500.99, 10)

    assert product.name == "Laptop"
    assert product.description == "A high-end gaming laptop"
    assert product.price == 1500.99
    assert product.quantity == 10


def test_product_count_increment() -> None:
    initial_count = Product.product_count
    Product("Phone", "Latest model smartphone", 999.99, 5)
    assert Product.product_count == initial_count + 1
