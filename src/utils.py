# src/utils.py
import logging

logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

def log_order(order_type, symbol, quantity, side, price=None, extra=None):
    log_entry = {
        "type": order_type,
        "symbol": symbol,
        "quantity": quantity,
        "side": side,
        "price": price,
        "extra": extra or {}
    }
    logging.info(log_entry)


def validate_order(symbol, quantity, price=None):
    if not symbol.isalpha():
        logging.error(f"Invalid symbol: {symbol}")
        return False
    if quantity <= 0:
        logging.error(f"Invalid quantity: {quantity}")
        return False
    if price is not None and price <= 0:
        logging.error(f"Invalid price: {price}")
        return False
    return True

