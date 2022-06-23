from dataclasses import dataclass
from decimal import Decimal
from enum import Enum


@dataclass(frozen=True)
class Trade:
    class Direction(Enum):
        BUY = "BUY"
        SELL = "SELL"

    timestamp: float
    symbol: str
    quantity: int
    price: float
    direction: Direction
