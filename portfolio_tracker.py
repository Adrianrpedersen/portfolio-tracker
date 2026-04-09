import yfinance as yf

ticker = input("Enter stock ticker: ")
shares = float(input("Enter number of shares: "))
buy_price = float(input("Enter purchase price: "))

stock = yf.Ticker(ticker)
current_price = stock.info["currentPrice"]

total_value = current_price * shares
profit_loss = (current_price - buy_price) * shares

print("\n--- Portfolio Summary ---")
print(f"Current Price: {current_price}")
print(f"Total Value: {total_value}")
print(f"Profit/Loss: {profit_loss}")