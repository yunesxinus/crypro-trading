import pandas
import pandas_ta as ta
import yfinance as yf

rs = []
df = yf.download('DOGE-USD', start='2022-8-3', end='2022-9-3')
x = ta.rsi(df['Close'], length=14)

for k, v in x.items():
    rs.append(v)

print(rs[-1])

if shart > 50:
    print('Sell')
else:
    print('Buy')
