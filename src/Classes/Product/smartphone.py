from .product import Product


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory  # в ГБ
        self.color = color

    def __str__(self) -> str:
        return f"{self.name} ({self.model}, {self.memory}GB, {self.color}), {self.price} руб. Остаток: {self.quantity} шт."
