from decimal import Decimal
import pytest

from src.domain.stock import Stock
from src.domain.trade import Trade


@pytest.fixture()
def trades_in_five_mins():
    return [
        Trade(
            timestamp=1655715600.0,
            symbol="TEA",
            quantity=100,
            price=100,
            direction="BUY",
        ),
        Trade(
            timestamp=1655715660.0,
            symbol="TEA",
            quantity=200,
            price=101,
            direction="BUY",
        ),
        Trade(
            timestamp=1655715700.0,
            symbol="TEA",
            quantity=300,
            price=102,
            direction="BUY",
        ),
        Trade(
            timestamp=1655715800.0,
            symbol="TEA",
            quantity=400,
            price=103,
            direction="BUY",
        ),
        Trade(
            timestamp=1655715840.0,
            symbol="TEA",
            quantity=500,
            price=104,
            direction="BUY",
        ),
    ]


@pytest.fixture()
def all_stocks_with_volume_weighted_price():
    return [
        Stock("TEA", Decimal(0), 100, 0, Decimal("100")),
        Stock("POP", Decimal("0.08"), 100, 0, Decimal("200")),
        Stock("ALE", Decimal("0.23"), 60, 0, Decimal("300")),
        Stock("JOE", Decimal("0.13"), 250, 0, Decimal("400")),
        Stock("GIN", Decimal("0.08"), 100, 0.02, Decimal("500")),
    ]
