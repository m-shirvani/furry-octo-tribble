from decimal import Decimal

from src import TWOPLACES


class VolumeWeightedServise:
    def __init__(self, trades):
        self.trades_in_scope = trades

    def calculate(self):
        volume_weighted_price = sum(
            (trade.price * trade.quantity for trade in self.trades_in_scope)
        ) / sum((trade.quantity for trade in self.trades_in_scope))

        return Decimal(volume_weighted_price).quantize(TWOPLACES)
