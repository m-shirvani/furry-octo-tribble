from decimal import Decimal

import pytest

from src.domain.stock import CommonStock, PreferredStock


@pytest.mark.parametrize(
    "symbol, last_dividend, par_value, price, expected",
    [
        ("TEA", Decimal(0), 100, 10, 0),
        ("POP", Decimal("0.08"), 100, 10, Decimal("1250")),
        ("ALE", Decimal("0.23"), 60, 10, Decimal("434.78")),
        # # ("GIN", StockType.PREFERRED, Decimal("0.08"), 100, Decimal('0.02'), 10, Decimal("434.78")),
        ("JOE", Decimal("0.13"), 250, 10, Decimal("769.23")),
    ],
)
def test_it_calculates_common_pe_ratio(
    symbol, last_dividend, par_value, price, expected
):
    common_stock = CommonStock(
        symbol=symbol,
        last_dividend=last_dividend,
        par_value=par_value,
    )
    pe_ratio = common_stock.calculate_pe_ratio(price)
    assert pe_ratio == expected


def test_it_calculates_preferred_pe_ratio():
    preferred_stock = PreferredStock(
        symbol="GIN",
        last_dividend=Decimal("0.08"),
        par_value=100,
        fixed_dividend=Decimal("0.02"),
    )
    dividend_yield = preferred_stock.calculate_pe_ratio(price=10)
    assert dividend_yield == Decimal("50")
