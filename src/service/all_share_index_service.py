from decimal import Decimal
from functools import reduce


class AllShareIndexService:
    def __init__(self, stocks_in_index):
        self.stocks_in_index = stocks_in_index
        self.nth_root = len(self.stocks_in_index)

    def geometric_mean(self):
        product = reduce(
            (lambda x, y: x * y),
            [stock.volume_weighted_price for stock in self.stocks_in_index],
        )
        return product ** (Decimal(1 / self.nth_root))

    def calculate_index_price_by_geometric_mean(self):
        price = self.geometric_mean()
        return Decimal(price)
