# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

print(" Simple Stock Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print(" Invalid stock symbol. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity < 0:
            print(" Quantity must be positive.")
            continue
    except ValueError:
        print(" Please enter a valid number.")
        continue

    # Save to portfolio and update total
    portfolio[stock] = portfolio.get(stock, 0) + quantity
    total_investment += stock_prices[stock] * quantity

# Display result
print("\n Investment Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    print(f"{stock} - Quantity: {qty}, Value: ${value}")
print("Total Investment: $", total_investment)

# Optional: Save to file
save = input("\nDo you want to save the result? (yes/no): ").lower()
if save == "yes":
    filename = input("Enter file name (e.g., portfolio.txt or portfolio.csv): ")
    try:
        with open(filename, "w") as f:
            f.write("Stock,Quantity,Value\n")
            for stock, qty in portfolio.items():
                value = stock_prices[stock] * qty
                f.write(f"{stock},{qty},{value}\n")
            f.write(f"Total Investment,,{total_investment}\n")
        print(f" Saved to {filename}")
    except Exception as e:
        print(" Error saving file:", e)
