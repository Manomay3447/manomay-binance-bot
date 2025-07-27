# src/advanced/stop_limit.py
from src.utils import log_order, validate_order

def execute_stop_limit_order(symbol, quantity, stop_price, limit_price, side):
    if not validate_order(symbol, quantity, stop_price) or not validate_order(symbol, quantity, limit_price):
        return
    print(f"STOP-LIMIT: Trigger at {stop_price}, then place {side} LIMIT at {limit_price}")
    log_order("stop-limit", symbol, quantity, side, price=limit_price, extra={"stop_price": stop_price})

