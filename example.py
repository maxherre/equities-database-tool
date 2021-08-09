import yfinance as yf

aapl = yf.Ticker("MSFT")
info = aapl.get_info("sector")
print(info)
