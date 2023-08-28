import yfinance as yf
import matplotlib.pyplot as plt

# Get historical price data for Apple
data = yf.download("AAPL", start="2022-01-01", end="2023-01-01")

# Plot the closing price
plt.plot(data["Close"])
plt.show()
