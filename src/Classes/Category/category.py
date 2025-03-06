from typing import List

from src.Classes.Order.base_entity import BaseEntity
from src.Classes.Product.product import Product

from .category_iterator import CategoryIterator


class Category(BaseEntity):
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        super().__init__(name, description)
        self.__products: List[Product] = products
        Category.category_count += 1
        Category.product_count = len(self.__products)

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты типа Product или его наследников")
        self.__products.append(product)
        Category.product_count = len(self.__products)

    @property
    def products(self) -> str:
        return "\n".join(str(product) for product in self.__products)

    def get_products(self) -> List[Product]:
        return self.__products

    def __iter__(self) -> "CategoryIterator":
        return CategoryIterator(self)
