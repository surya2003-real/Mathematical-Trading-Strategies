import pandas as pd
import yfinance as yf

indexes=['^RUT', '^GSPC', 'AGG', '^BSESN', '^DJI']
data=yf.download(" ".join(indexes), start='2010-01-01', end='2023-05-01')
dt=pd.DataFrame(data)
print(dt.shape)

