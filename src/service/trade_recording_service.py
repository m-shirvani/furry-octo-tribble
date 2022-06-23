from src.repository.trade_recording_repository import TradeRecordingRepository


class TradeRecordingService:
    def __init__(self, repository: TradeRecordingRepository):
        self.repository = repository

    def store_trades(self, *trades):
        self.repository.store(*trades)
