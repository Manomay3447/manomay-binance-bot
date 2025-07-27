#TRADING BOT CLI (SIMULATOR)
A Command-Line Interface (CLI) simulator that mimics real-world trading behavior using various order types such as Market, Limit, Stop-Limit, OCO (One Cancels the Other), TWAP (Time-Weighted Average Price), and Grid trading.
This tool is designed to help understand the internal logic of modern trading systems and strategies without needing a live API, real funds, or exchange integration.

#PROJECT OVERVIEW
This trading simulator supports:
1.Basic orders (Market, Limit)	
2.Advanced strategies (Stop-Limit, OCO, TWAP, Grid)
3.Logging of all trades and actions
4.Modular Python structure for easy extensibility
5.Validation of input formats, side types, price ranges, and other critical fields

#HOW TO RUN THE PROJECT:
1.Navigate to the project directory:
	cd trading_bot_cli
	
2.Run the bot using:
	python3 -m src.main <order_type> <symbol> <amount> [parameters] <side>

	Each order type has a specific format:

		ORDER TYPES & EXAMPLES
		1.Market Order
		Description: Instantly buys or sells at market price.
		Syntax:
			python3 -m src.main market BTC 1 buy

		2.Limit Order
		Description: Places an order only if the target price is hit.
		Syntax:
			python3 -m src.main limit ETH 2 1800 sell
			Arguments: <symbol> <amount> <limit_price> <side>

		3.Stop-Limit Order
		Description: Triggers a limit order when the stop price is reached.
		Syntax:
			python3 -m src.main stop-limit XRP 100 210 220 buy
			Arguments: <symbol> <amount> <stop_price> <limit_price> <side>

		4.OCO (One Cancels the Other)
		Description: Combines take-profit and stop-loss. When one executes, the other is canceled.
		Syntax:
			python3 -m src.main oco DOGE 50 0.09 0.12 0.07 sell
			Arguments: <symbol> <amount> <entry_price> <take_profit> <stop_loss> <side>

		5.TWAP (Time-Weighted Average Price)
		Description: Splits a large order into smaller chunks over time.
		Syntax:
			python3 -m src.main twap BTC 5 5 10 buy
			Arguments: <symbol> <total_amount> <chunks> <interval_seconds> <side>

		6.Grid Trading
		Description: Creates a series of buy and sell limit orders between a price range.
		Syntax:
			python3 -m src.main grid ETH 10 1500 1800 5 sell
			Arguments: <symbol> <total_amount> <lower_price> <upper_price> <levels> <side>

		7.Logging
		Description: You can monitor real time activity with:
		Syntax:
			cat bot.log

#KEY FEATURES
1.Pure Python, no external API or database dependency
2.CLI-based, lightweight and portable
3.Clean logging and modular structure
4.Good for practicing logic of algorithmic/automated trading

