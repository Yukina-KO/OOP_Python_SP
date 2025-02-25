class Product:
    product_count = 0

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name: str = name
        self.description: str = description
        self.price: float = price
        self.quantity: int = quantity

        Product.product_count += 1
