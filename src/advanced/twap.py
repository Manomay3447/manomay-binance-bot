# src/advanced/twap.py
from src.utils import log_order, validate_order
import time

def execute_twap_order(symbol, quantity, interval_secs, slices, side):
    slice_qty = quantity / slices
    for i in range(slices):
        if not validate_order(symbol, slice_qty):
            return
        print(f"TWAP: Executing {side} {slice_qty} of {symbol} [Slice {i+1}/{slices}]")
        log_order("twap", symbol, slice_qty, side, extra={"interval": interval_secs, "slice": i+1})
        time.sleep(interval_secs)

