from src.Classes.Order.base_entity import BaseEntity
from src.Classes.Product.product import Product


class Order(BaseEntity):
    def __init__(self, name: str, description: str, product: Product, quantity: int) -> None:
        super().__init__(name, description)
        self.product = product
        self.quantity = quantity
        self.total_price = self.product.price * self.quantity

    def __str__(self) -> str:
        return (
            f"Заказ: {self.name}, Товар: {self.product.name}, "
            f"Количество: {self.quantity}, Итоговая стоимость: {self.total_price} руб."
        )
