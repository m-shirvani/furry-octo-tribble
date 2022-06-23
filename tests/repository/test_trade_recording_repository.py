from datetime import datetime
from src.domain.trade import Trade
from src.repository.trade_recording_repository import TradeRecordingRepository


def test_it_stores_trade_records():
    trade1 = Trade(datetime.utcnow().timestamp(), "TEA", 120, 56.89, "BUY")
    trade2 = Trade(datetime.utcnow().timestamp(), "TEA", 240, 56.89, "BUY")
    repo = TradeRecordingRepository()

    repo.store(trade1, trade2)

    assert trade1 in repo.trade_records
    assert trade2 in repo.trade_records
