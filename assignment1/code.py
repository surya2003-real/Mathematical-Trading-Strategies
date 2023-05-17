import pandas as pd
import yfinance as yf
from math import nan, sqrt
def cumulative_returns(dt):
    cr=[]
    daily_returns=((dt['Close']-dt['Open'])/dt['Open'])
    cr.append(((1+daily_returns).cumprod()-1).tail(1)*100)
    return cr

def volatility(dt):
    daily_returns=((dt['Close']-dt['Open'])/dt['Open'])
    return daily_returns.std()*sqrt(252)*100

def sharpe_ratio(dt):
    daily_returns=((dt['Close']-dt['Open'])/dt['Open'])
    annualized_avg_return=daily_returns.mean()
    print(annualized_avg_return)
    risk_free_return=[0]*5
    return annualized_avg_return#(annualized_avg_return-risk_free_return)/daily_returns.std()*sqrt(252)

def sortino_ratio(dt):
    daily_returns=((dt['Close']-dt['Open'])/dt['Open'])
    annualized_avg_return=daily_returns.mean()*252
    risk_free_return=[0]*5
    return daily_returns#(annualized_avg_return-risk_free_return)/[i  for i in daily_returns if i<0].std()*sqrt(252)

def maximum_drawdown(dt):
    return (dt['Close'].min()-dt['Close'].max())/dt['Close'].max()

indexes=['^DJI', '^GSPC','^IXIC', '^NSEI', '^RUT']
data=yf.download(" ".join(indexes), start='2010-01-01', end='2023-05-01')
dt=pd.DataFrame(data)
daily_returns=((dt['Close']-dt['Open'])/dt['Open'])
print(dt.tail())
print(dt.columns)
print(cumulative_returns(dt))
print(volatility(dt))
print(sharpe_ratio(dt))
print(sortino_ratio(dt))
print(maximum_drawdown(dt))