import pytest

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
