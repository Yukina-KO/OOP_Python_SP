class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name: str = name
        self.description: str = description
        self.products: list = products

        Category.category_count += 1
        Category.product_count = len(self.products)
