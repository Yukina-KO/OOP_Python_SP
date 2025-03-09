from src.Classes.Order.order import Order
from src.Classes.Product.product import Product


def test_order_creation() -> None:
    product = Product("Laptop", "Gaming laptop", 1500.0, 10)
    order = Order("Заказ 1", "Тестовый заказ", product, 2)
    assert order.name == "Заказ 1"
    assert order.description == "Тестовый заказ"
    assert order.product == product
    assert order.quantity == 2
    assert order.total_price == 3000.0


def test_order_str() -> None:
    product = Product("Laptop", "Gaming laptop", 1500.0, 10)
    order = Order("Заказ 1", "Тестовый заказ", product, 2)
    assert str(order) == "Заказ: Заказ 1, Товар: Laptop, Количество: 2, Итоговая стоимость: 3000.0 руб."
