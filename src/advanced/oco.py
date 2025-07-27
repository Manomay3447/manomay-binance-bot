# src/advanced/oco.py
from src.utils import log_order, validate_order

def execute_oco_order(symbol, quantity, take_profit, stop_loss, side):
    if not validate_order(symbol, quantity, take_profit) or not validate_order(symbol, quantity, stop_loss):
        return
    print(f"OCO: Place {side} TAKE-PROFIT at {take_profit} and STOP-LOSS at {stop_loss}")
    log_order("oco", symbol, quantity, side, extra={"take_profit": take_profit, "stop_loss": stop_loss})

