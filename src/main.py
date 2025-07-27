# src/main.py

import click
from src.market_orders import execute_market_order
from src.limit_orders import execute_limit_order
from src.advanced.stop_limit import execute_stop_limit_order
from src.advanced.oco import execute_oco_order
from src.advanced.twap import execute_twap_order
from src.advanced.grid import execute_grid_order

@click.group()
def cli():
    """CLI Trading Bot - Supports Core & Advanced Orders"""
    pass

# --- Core Orders ---

@cli.command()
@click.argument('symbol')
@click.argument('quantity', type=float)
@click.argument('side', type=click.Choice(['buy', 'sell']))
def market(symbol, quantity, side):
    """Place a MARKET order"""
    execute_market_order(symbol, quantity, side)

@cli.command()
@click.argument('symbol')
@click.argument('quantity', type=float)
@click.argument('price', type=float)
@click.argument('side', type=click.Choice(['buy', 'sell']))
def limit(symbol, quantity, price, side):
    """Place a LIMIT order"""
    execute_limit_order(symbol, quantity, price, side)

# --- Advanced Orders ---

@cli.command()
@click.argument('symbol')
@click.argument('quantity', type=float)
@click.argument('stop_price', type=float)
@click.argument('limit_price', type=float)
@click.argument('side', type=click.Choice(['buy', 'sell']))
def stop_limit(symbol, quantity, stop_price, limit_price, side):
    """Place a STOP-LIMIT order"""
    execute_stop_limit_order(symbol, quantity, stop_price, limit_price, side)

@cli.command()
@click.argument('symbol')
@click.argument('quantity', type=float)
@click.argument('take_profit', type=float)
@click.argument('stop_loss', type=float)
@click.argument('side', type=click.Choice(['buy', 'sell']))
def oco(symbol, quantity, take_profit, stop_loss, side):
    """Place an OCO order (Take-Profit + Stop-Loss)"""
    execute_oco_order(symbol, quantity, take_profit, stop_loss, side)

@cli.command()
@click.argument('symbol')
@click.argument('quantity', type=float)
@click.argument('interval_secs', type=int)
@click.argument('slices', type=int)
@click.argument('side', type=click.Choice(['buy', 'sell']))
def twap(symbol, quantity, interval_secs, slices, side):
    """Place a TWAP order"""
    execute_twap_order(symbol, quantity, interval_secs, slices, side)

@cli.command()
@click.argument('symbol')
@click.argument('quantity', type=float)
@click.argument('lower_price', type=float)
@click.argument('upper_price', type=float)
@click.argument('grids', type=int)
@click.argument('side', type=click.Choice(['buy', 'sell']))
def grid(symbol, quantity, lower_price, upper_price, grids, side):
    """Place a GRID order (Buy low/Sell high)"""
    execute_grid_order(symbol, quantity, lower_price, upper_price, grids, side)

if __name__ == '__main__':
    cli()

