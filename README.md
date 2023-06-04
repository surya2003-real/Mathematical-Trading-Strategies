# Mathematical-Trading-Strategies
### This is a repository for keeping track of my project. I have added all my assignments in different folders.
## Formulaes for Understanding the content:
## 1. Cumulative Returns
> ## $[\prod_{i=1}^{n}(1+\frac {dailyreturns_i}{100})]-1$
>
## 2. Volatilty ($\sigma$ is standard Deviation)
> ## $\sigma _{dailyreturns}\times \sqrt {252}$
>
## 3. Sharpe Ratio
>## $\frac {(annualizedavgreturn-riskfreereturn)}{(\sigma_{dailyreturn}\times\sqrt{252})}$
> ### $annualizedavgreturn= \sum_{i=1}^{n}(\frac {dailyreturns_i} n)\times \sqrt{252}$
## 4. Sortino Ratio
>## $\frac {(annualizedavgreturn-riskfreereturn)}{(\sigma_{(dailyreturn<0)}\times\sqrt{252})}$
> ### $annualizedavgreturn= \sum_{i=1}^{n}(\frac {dailyreturns_i} n)\times \sqrt{252}$
>We take standard deviation of negative returns.
## 5. Maximum Drawdown
> The maximum observed loss from a peak to a trough of a portfolio, before a new peak is attained divided by peak value.
>
## 6. Exponential Moving Average(EMA)
>$EMA = Closing price\times multiplier + EMA (previous day)\times(1-multiplier)$  
>>$multiplier=\frac {Smoothing}{1+Days}$  
>>Usually Smoothing factor is taken as 2.  
>>Days can be 10, 12, 20, 26 depending on the indicator
## 7. Keltner Channel
> ### True Range(TR)=MAX [{HIGH - LOW}, {HIGH - P.CLOSE}, {P.CLOSE - LOW}]  
where,  
MAX = Maximum values  
HIGH = Market High  
LOW = Market Low  
P.CLOSE = Previous market close
> ### Average True Range
>ATR N = EMA N [ TR ] - 1 * 2  

where,  
ATR N = Average True Range of 'N' period  
SMA N = Simple Moving Average of 'N' period  
TR = True Range
> ### Keltner Kernel Channels
>### MIDDLE LINE 20 = EMA 20 [ C.STOCK ]  
where,  
EMA 20 = 20-day Exponential Moving Average   
C.STOCK = Closing price of the stock  
>### UPPER BAND 20 = EMA 20 [ C.STOCK ] + MULTIPLIER * ATR 10  
>### LOWER BAND 20 = EMA 20 [ C.STOCK ] - MULTIPLIER * ATR 10  
where,  
EMA 20 = 20-day Exponential Moving Average   
C.STOCK = Closing price of the stock  
MULTIPLIER = 2  
ATR 10 = 10-day Average True Range  
## 8. Bollinger Bands
>BOLU=MA(TP,n)+m∗σ[TP,n]  
>BOLD=MA(TP,n)−m∗σ[TP,n]  

where:  
BOLU=Upper Bollinger Band  
BOLD=Lower Bollinger Band  
MA=Moving average  
TP (typical price)=(High+Low+Close)÷3  
n=Number of days in smoothing period (typically 20)  
m=Number of standard deviations (typically 2)  
σ[TP,n]=Standard Deviation over last n periods of TP  
## 9. MACD indicators
>MACDline=12-Period EMA − 26-Period EMA  
>Signal line=EMA MACD  
>MACD histogram = MACD line - Signal line



## Some basic codes:
    .cumprod() //calculating cumulative product
    .cummax()  //calculating cumulative maximum
    .corr()    //calculating correlation
    .rolling(window_size).mean //calculating Simple Moving Average(SMA)
    .ewm(span=40,adjust=False).mean() //calculating Exponential Moving Average(EMA)



​
