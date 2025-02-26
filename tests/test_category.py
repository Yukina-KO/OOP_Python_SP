from src.Classes.Category.category import Category
from src.Classes.Product.product import Product


def test_category_creation() -> None:
    product1 = Product("Monitor", "4K Ultra HD Monitor", 299.99, 3)
    product2 = Product("Mouse", "Wireless Mouse", 29.99, 10)
    category = Category("Electronics", "Devices and gadgets", [product1, product2])
    assert category.name == "Electronics"
    assert category.description == "Devices and gadgets"
    assert Category.product_count == 2


def test_category_add_product() -> None:
    product = Product("Keyboard", "Mechanical keyboard", 99.99, 4)
    category = Category("Accessories", "Computer accessories", [])
    category.add_product(product)
    assert Category.product_count == 1


def test_category_products_format() -> None:
    product1 = Product("Smartwatch", "Fitness tracking watch", 199.99, 5)
    product2 = Product("Headphones", "Noise-canceling headphones", 149.99, 8)
    category = Category("Wearables", "Wearable tech devices", [product1, product2])
    expected_output = "Smartwatch, 199.99 руб. Остаток: 5 шт.\nHeadphones, 149.99 руб. Остаток: 8 шт."
    assert category.products == expected_output


def test_category_str() -> None:
    product1 = Product("Item1", "Desc1", 100, 5)
    product2 = Product("Item2", "Desc2", 200, 3)
    category = Category("TestCat", "Test Desc", [product1, product2])
    assert str(category) == "TestCat, количество продуктов: 8 шт."


def test_category_iteration() -> None:
    product1 = Product("Item1", "Desc1", 100, 5)
    product2 = Product("Item2", "Desc2", 200, 3)
    category = Category("TestCat", "Test Desc", [product1, product2])
    products = list(category)
    assert len(products) == 2
    assert products[0].name == "Item1"
    assert products[1].name == "Item2"
