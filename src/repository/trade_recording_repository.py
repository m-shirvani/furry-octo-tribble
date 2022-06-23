from src.domain.trade import Trade


class TradeRecordingRepository:
    def __init__(self):
        self.trade_records = []

    def store(self, *trades):
        for trade in trades:
            if isinstance(trade, Trade):
                self.trade_records.append(trade)
