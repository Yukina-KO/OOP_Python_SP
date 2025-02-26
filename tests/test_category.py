from src.Classes.Category.category import Category
from src.Classes.Product.product import Product


def test_category_creation() -> None:
    product1 = Product("Tablet", "A lightweight tablet", 499.99, 7)
    product2 = Product("Monitor", "4K Ultra HD Monitor", 299.99, 3)
    category = Category("Electronics", "Devices and gadgets", [product1, product2])

    assert category.name == "Electronics"
    assert category.description == "Devices and gadgets"
    assert len(category.products) == 2
    assert category.products[0].name == "Tablet"
    assert category.products[1].name == "Monitor"


def test_category_count_increment() -> None:
    initial_category_count = Category.category_count
    Category("Appliances", "Home appliances", [])
    assert Category.category_count == initial_category_count + 1


def test_category_product_count() -> None:
    product1 = Product("Camera", "DSLR Camera", 799.99, 2)
    product2 = Product("Headphones", "Noise-canceling headphones", 199.99, 8)
    Category("Gadgets", "Wearable and portable devices", [product1, product2])
    assert Category.product_count == 2
