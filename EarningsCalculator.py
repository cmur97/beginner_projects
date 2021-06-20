# Simple program that calculates earning from investments (non-compounding)
def earnings_calculator():
    initial_investment = int(input("Enter initial investment: "))
    num_trades = int(input("Enter the number of trades: "))
    percent_returns = float(input("Enter the percent return for each trade: "))
    earnings_per_trade = initial_investment * percent_returns
    print(f"You will earn ${earnings_per_trade} per trade")
    total = initial_investment
    
    for num in range(1, num_trades + 1):
        initial_investment += earnings_per_trade
        print(f"Trade {num}: {initial_investment}")
        print(f"Total earnings for trade {num}: {(initial_investment - total)}")

earnings_calculator()
