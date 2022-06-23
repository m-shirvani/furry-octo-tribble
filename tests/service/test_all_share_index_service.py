from decimal import Decimal
from src.service.all_share_index_service import AllShareIndexService


def test_it_calculates_all_share_index(all_stocks_with_volume_weighted_price):
    service = AllShareIndexService(all_stocks_with_volume_weighted_price)
    price = service.calculate_index_price_by_geometric_mean()

    assert price == Decimal("260.52")
