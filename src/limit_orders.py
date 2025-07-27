# src/limit_orders.py
from src.utils import log_order, validate_order

def execute_limit_order(symbol, quantity, price, side):
    if not validate_order(symbol, quantity, price):
        return
    print(f"Placing {side} LIMIT order for {quantity} of {symbol} at {price}")
    log_order("limit", symbol, quantity, side, price)

