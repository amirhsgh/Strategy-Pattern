from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Season(Enum):
    WINTER = "winter"
    SPRING = "spring"
    SUMMER = "summer"
    AUTUMN = "autumn"


@dataclass
class ShoppingContext:
    is_member: bool = False
    quantity: int = 0
    season: Optional[Season] = None


class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price: int, context: ShoppingContext):
        pass
