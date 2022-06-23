import abc


class BaseStock(abc.ABC):
    @abc.abstractmethod
    def calculate_dividend_yield(self, price):
        pass

    def calculate_pe_ratio(self, price):
        try:
            return price / self.calculate_dividend_yield(price)
        except ZeroDivisionError:
            return 0


class Stock(BaseStock):
    def __init__(
        self, symbol, last_dividend, par_value, fixed_dividend, volume_weighted_price=0
    ):
        self.symbol = symbol
        self.last_dividend = last_dividend
        self.par_value = par_value
        self.fixed_dividend = fixed_dividend
        self.volume_weighted_price = volume_weighted_price

    def calculate_dividend_yield(self, price):
        raise NotImplementedError()


class CommonStock(Stock):
    def __init__(self, symbol, last_dividend, par_value, fixed_dividend=0):
        super().__init__(symbol, last_dividend, par_value, fixed_dividend)

    def calculate_dividend_yield(self, price):
        return self.last_dividend / price


class PreferredStock(Stock):
    def __init__(self, symbol, last_dividend, par_value, fixed_dividend):
        super().__init__(symbol, last_dividend, par_value, fixed_dividend)

    def calculate_dividend_yield(self, price):
        return (self.fixed_dividend * self.par_value) / price
