# src/advanced/grid.py
from src.utils import log_order, validate_order

def execute_grid_order(symbol, total_quantity, lower_price, upper_price, grids, side):
    price_step = (upper_price - lower_price) / (grids - 1)
    qty_per_grid = total_quantity / grids
    for i in range(grids):
        grid_price = lower_price + i * price_step
        if not validate_order(symbol, qty_per_grid, grid_price):
            return
        print(f"GRID [{i+1}/{grids}]: Place {side} LIMIT order at {grid_price} for {qty_per_grid}")
        log_order("grid", symbol, qty_per_grid, side, price=grid_price, extra={"grid_index": i+1})

