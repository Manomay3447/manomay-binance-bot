# src/market_orders.py
from src.utils import log_order, validate_order

def execute_market_order(symbol, quantity, side):
    if not validate_order(symbol, quantity):
        return
    # Simulate API call
    print(f"Placing {side} MARKET order for {quantity} of {symbol}")
    log_order("market", symbol, quantity, side)

