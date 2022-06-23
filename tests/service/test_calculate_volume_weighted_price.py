from decimal import Decimal

from src.service.volume_weighted_price_service import VolumeWeightedServise


def test_it_calculates_volume_weighted_price(trades_in_five_mins):
    service = VolumeWeightedServise(trades_in_five_mins)

    vwp = service.calculate()

    assert vwp == Decimal("102.67")
