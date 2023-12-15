from discount_strategies import DiscountStrategy, NoDiscount
from discount_interfaces import ShoppingContext


class ShoppingCart:
    def __init__(self, discount_strategy: DiscountStrategy = None):
        self.discount_strategy = discount_strategy or NoDiscount()
        self.items = []

    def add_item(self, item, price):
        self.items.append((item, price))

    def calculate_total(self):
        total = sum(price for _, price in self.items)
        return total

    def apply_discount(self, context: ShoppingContext):
        if not self.items:
            return 0
        total = self.calculate_total()
        return self.discount_strategy.apply_discount(total, context)
