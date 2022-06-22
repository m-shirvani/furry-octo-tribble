import abc


class BaseStock(abc.ABC):
    def __init__(self, symbol, last_dividend, par_value, fixed_dividend):
        self.symbol = symbol
        self.last_dividend = last_dividend
        self.par_value = par_value
        self.fixed_dividend = fixed_dividend

    @abc.abstractmethod
    def calculate_dividend_yield(self, price):
        pass


class CommonStock(BaseStock):
    def __init__(self, symbol, last_dividend, par_value, fixed_dividend=0):
        super().__init__(symbol, last_dividend, par_value, fixed_dividend)

    def calculate_dividend_yield(self, price):
        return self.last_dividend / price


class PreferredStock(BaseStock):
    def __init__(self, symbol, last_dividend, par_value, fixed_dividend):
        super().__init__(symbol, last_dividend, par_value, fixed_dividend)

    def calculate_dividend_yield(self, price):
        return (self.fixed_dividend * self.par_value) / price
