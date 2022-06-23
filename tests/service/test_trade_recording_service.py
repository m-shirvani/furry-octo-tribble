from datetime import datetime
from unittest.mock import MagicMock

from src.domain.trade import Trade
from src.repository.trade_recording_repository import TradeRecordingRepository
from src.service.trade_recording_service import TradeRecordingService


def test_trade_recording_service():
    trade1 = Trade(datetime.utcnow().timestamp(), "TEA", 120, 56.89, "BUY")
    trade2 = Trade(datetime.utcnow().timestamp(), "TEA", 240, 56.89, "BUY")

    repo = TradeRecordingRepository()
    repo.store = MagicMock()
    service = TradeRecordingService(repo)

    service.store_trades(trade1, trade2)

    repo.store.assert_called_with(trade1, trade2)
