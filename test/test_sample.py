import unittest
from discount_interfaces import Season, ShoppingContext
from discount_strategies import *


class TestDiscountStrategies(unittest.TestCase):
    def setUp(self):
        self.price = 100
    
    def test_all_strategies_exist(self):
        try:
            from discount_strategies import NoDiscount
            from discount_strategies import SeasonalDiscount
            from discount_strategies import BulkPurchaseDiscount
            from discount_strategies import MemberDiscount
        except:
            self.fail('all discounting strategies should be implemented')

    def test_no_discount(self):
        strategy = NoDiscount()
        context = ShoppingContext()
        discounted_price = strategy.apply_discount(self.price, context)
        self.assertEqual(discounted_price, 100)
