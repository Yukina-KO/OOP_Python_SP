from typing import List

from src.Classes.Product.product import Product


class CategoryIterator:
    def __init__(self, category: "Category") -> None:
        self.products: List[Product] = category.get_products()
        self.index: int = 0

    def __iter__(self) -> "CategoryIterator":
        return self

    def __next__(self) -> Product:
        if self.index >= len(self.products):
            raise StopIteration
        product = self.products[self.index]
        self.index += 1
        return product
