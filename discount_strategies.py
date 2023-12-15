from discount_interfaces import DiscountStrategy, Season, ShoppingContext


class NoDiscount(DiscountStrategy):
    def apply_discount(self, price, context):
        return price


# Implement other discount strategies too.
class SeasonalDiscount(DiscountStrategy):
    def apply_discount(self, price: int, context: ShoppingContext):
        if context.season == Season.WINTER:
            return price - (price * (10/100))
        
        return price
    
class BulkPurchaseDiscount(DiscountStrategy):
    def apply_discount(self, price: int, context: ShoppingContext):
        if context.quantity > 9:
            return price - (price * (15/100))
        
        return price
    
class MemberDiscount(DiscountStrategy):
    def apply_discount(self, price: int, context: ShoppingContext):
        if context.is_member:
            return price - (price * (20/100))
    
        return price
    
