from typing import List

from src.Classes.Product.product import Product


class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name: str = name
        self.description: str = description
        self.__products: List[Product] = products

        Category.category_count += 1
        Category.product_count = len(self.__products)

    def add_product(self, product: Product) -> None:
        """Метод для добавления нового товара в категорию."""
        self.__products.append(product)
        Category.product_count = len(self.__products)

    @property
    def products(self) -> str:
        """
        Геттер, возвращающий список товаров в виде строки.
        Формат строки: 'Название продукта, 80 руб. Остаток: 15 шт.'
        Каждая запись разделяется символом перевода строки.
        """
        lines: List[str] = []
        for prod in self.__products:
            line: str = f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт."
            lines.append(line)
        return "\n".join(lines)
