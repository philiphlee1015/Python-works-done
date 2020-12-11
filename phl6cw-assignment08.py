## File: phl6cw-assignment08.py 
## Topic:  Assignment 08 Solutions
## Name: Philip Lee

import pandas as pd
import glob


filelist = glob.glob('*.csv') 

df = pd.DataFrame()             ##reads in all of the stcok csvs and combines them into a giant dataframe
for f in filelist:                 ##Goes through all of the csvs
    newdf = pd.read_csv(f)         ##loads in all the csv files
    newdf['Ticker']=f.split('.')[0]     ##makes a new column called Ticker that corresponds to the stock name
    df = pd.concat([df,newdf])      ##makes all of the stocks into a one big dataframe



###1. Find the mean for the Open, High, Low, and Close entries for all records for all stocks.

df['Open'].mean()          ##Finds the mean for open, high, low, and close for all records for all stocks
df['High'].mean()
df['Low'].mean()
df['Close'].mean()

"""
1

50.86385220906213      ##mean for Open
51.459411725747884      ##mean for High
50.25336771426483     ##mean for Low
50.876481580135426      ##mean for Close
"""

### 2. Find the top-5 and bottom-5 stocks in terms of their average Close price. Give tables showing the
### stock ticker symbol and the average Close price

df['Close'].groupby(df.Ticker).mean().nlargest(5)        ##Finds the top-5 stocks in terms of avg Close price
df['Close'].groupby(df.Ticker).mean().nsmallest(5)      ##Finds the bottom-5 stocks in terms of avg Close price

"""
2

Ticker                    ## Top-5 avg Close price
CME     253.956017
AZO     235.951950
AMZN    185.140534
BLK     164.069088
GS      139.146781
-----------------
Ticker                       ##Bottom-5 avg Close price
FTR      8.969515
F       11.174158
XRX     11.291864
ETFC    12.808103
HBAN    13.697483
"""

### 3.Find the top-5 and bottom-5 stocks in terms of the day-to-day volatility of the price, which we define
### to be the mean of the daily differences High - Low for each stock. Give tables for each, as in the
### previous problem.

df['vol']=(df['High']-df['Low'])        ##makes a new column called vol that contains day-to-day volatility
df['vol'].groupby(df.Ticker).mean().nlargest(5)         ##gets the avg volatility for each stock and finds the top 5 stocks
df['vol'].groupby(df.Ticker).mean().nsmallest(5)        ##gets the avg volatility for each stock and finds the bottom 5 stocks

"""
3

Ticker
CME     7.697287
AMZN    4.691407
BLK     4.470693
AZO     4.330294
ICE     4.056189
--------------
Ticker
FTR     0.205275
XRX     0.308743
F       0.323567
HBAN    0.343893
NI      0.363250
"""

### 4.Repeat the previous problem, this time using the relative volatility, which we define to be the mean of
### High − Low/0.5(Open + Close) for each day. As above, provide tables.

df['rel']=((df['High']-df['Low'])/(0.5*(df['Open']+df['Close'])))     ##makes a new column that contains relative volatility for each record
df['rel'].groupby(df.Ticker).mean().nlargest(5)      ##gets the top-5 stocks for the relative volatility
df['rel'].groupby(df.Ticker).mean().nsmallest(5)    ##gets the bottom-5 stocks for the relative volatility

"""
4

Ticker
AAL     0.055533
LVLT    0.054870
EQIX    0.051295
REGN    0.048172
ETFC    0.045381
------------
Ticker
GIS    0.013966
PG     0.014192
K      0.014992
CL     0.015521
WEC    0.015761
"""

### 5. For each day the market was open in October 2008, find the average daily Open, High, Low, Close,
### and Volume for all stocks.
market=df.loc[df['Date'].str.contains('2008-10')==True]      ##finds and stores records for October 2008
(market.groupby(market.Date).mean()).round(3)[['Open','High','Low','Close','Volume']]     ##gets the avg daily Open,High,Low,Close, and Volume for each date in October 2008 and rounds them to the 3rd decimal place

"""
5

              Open    High     Low   Close        Volume           ### Values rounded at the thousandth decimal place to allow all columns of the table to be visible
Date                                                    
2008-10-01  43.148  44.090  41.845  43.095  7.319004e+06
2008-10-02  43.033  43.444  40.642  41.127  9.555247e+06
2008-10-03  41.556  42.924  39.882  40.264  9.184641e+06
2008-10-06  39.409  40.564  36.731  39.177  1.176339e+07
2008-10-07  39.427  40.294  36.645  36.934  1.091851e+07
2008-10-08  36.107  38.785  35.062  36.677  1.378626e+07
2008-10-09  37.250  38.002  33.437  33.849  1.281094e+07
2008-10-10  32.581  35.953  30.432  33.992  1.820152e+07
2008-10-13  35.487  38.041  34.122  37.548  1.148344e+07
2008-10-14  38.581  39.627  35.513  36.785  1.240928e+07
2008-10-15  36.150  36.757  32.879  33.197  1.051697e+07
2008-10-16  33.486  35.097  31.415  34.599  1.258398e+07
2008-10-17  33.735  36.184  32.730  34.401  9.973754e+06
2008-10-20  34.989  36.358  33.968  35.909  7.657442e+06
2008-10-21  35.390  36.345  34.190  34.665  7.599813e+06
2008-10-22  33.752  34.345  31.386  32.373  9.425614e+06
2008-10-23  32.890  33.987  30.561  32.516  1.189890e+07
2008-10-24  30.046  32.498  29.404  31.395  9.726575e+06
2008-10-27  30.638  31.925  29.501  29.877  8.362392e+06
2008-10-28  30.860  33.145  29.345  32.956  1.091700e+07
2008-10-29  32.865  34.888  31.854  33.179  1.036944e+07
2008-10-30  34.274  35.292  32.884  34.285  8.928569e+06
2008-10-31  33.996  35.761  33.295  34.977  9.213693e+06
"""

### 6. For 2011, find the date with the maximum average relative volatility for all stocks and the date with
### the minimum average relative volatility for all stocks. (Consider only days when the market is open.)

market2=df.loc[df['Date'].str.contains('2011')==True]    ##finds and stores records from 2011
market2['rel'].groupby(market2.Date).mean().nlargest(1)      ##gets the maximum avg relative volatility
market2['rel'].groupby(market2.Date).mean().nsmallest(1)        ##gets the minimum avg relative volatility

"""
6

Date
2011-08-08    0.073087
----------------
Date
2011-12-30    0.014162
"""


### 7. For 2010-2012, for each day of the week, find the average relative volatility for all stocks. (Consider
### only days when the market is open.)

market3=df.loc[df['Date'].str.contains('2010|2011|2012')==True]       ##finds and stores records from 2010-2012
market3['Date']=pd.to_datetime(market3['Date']).dt.dayofweek        ##converts the Date column to day of the week
market3['rel'].groupby(market3.Date).mean()       ##gets the avg relative volatility for each day of the week from 2010-2012

"""
7

                ## 0 is Monday, 1 is Tuesday, 2 is Wednesday, 3 is Thursday, and 4 is Friday
Date
0    0.022109
1    0.023836
2    0.023443
3    0.024865
4    0.023018
"""

### 8. For each month of 2009, determine which stock had the maximum average relative volatility. Give a
### table with the month (number is fine), stock ticker symbol, and average relative volatility.
market4=df.loc[df['Date'].str.contains('2009')==True]         ##finds and store records from 2009
market4['Date']=pd.to_datetime(market4['Date']).dt.month         ##converts the Date column to contain just the months
market44=pd.DataFrame(market4['rel'].groupby([market4.Date,market4.Ticker]).mean())   ##gets the avg relative volatility based on the stock name and the date in a dataframe
market44['index']=market44.index  ##makes a new column called 'index'
market44.index=range(len(market44))   ##resets the index
market44['index']=market44['index'].astype(str).str.split('(').str[1].str.split(')').str[0]    ##removes the parenthesis from 'index'
market44['month']=market44['index'].str.split(',').str[0]     ##makes a new column called 'month' that contains the month values from 'index'
market44['stock']=market44['index'].str.split(',').str[1].str.split("'").str[1]     ##makes a new column called 'stock' that contains the stock names from 'index'
market44=market44.drop('index',axis=1)      ##removes the column 'index'
market44.sort_values('rel',ascending=False).drop_duplicates('month').sort_values('month')   ##sorts relative volatility values from highest to lowest and gets the only the first occurence of each month and sorts the months to be in order

"""
8

           rel month stock         
105   0.190686     1   GGP
2493  0.071610    10   AAL          
2875  0.089010    11   GGP
3153  0.112847    12   GGP
392   0.275587     2  HBAN
658   0.241744     3   GGP
935   0.212291     4   GGP
1212  0.187383     5   GGP
1489  0.131522     6   GGP
1671  0.121527     7   AIG
1948  0.141233     8   AIG
2320  0.103328     9   GGP
"""

### 9. The “Python Index” is designed to capture the collective movement of all of our stocks. For each date,
### this is defined as the average price for all stocks for which we have data on that day, weighted by the
### volume of shares traded for each stock. That is, for stock values S1, S2, . . . with corresponding sales
### volumes V1, V2, . . ., the average weighted by volume is
### S1V1 + S2V2 + · · ·
### V1 + V2 + · · ·
### Find the Open, High, Low, and Close for the Python Index for each day the market was open in
### January 2013. Give a table the includes the Date, Open, High, Low, and Close, with one date per row.

market5=df.loc[df['Date'].str.contains('2013-01')==True]   ##finds and stores records from January 2013
market5['open']=market5['Open']*market5['Volume']       ##makes a new column called 'open' that contains the numerator for the python index for the 'Open' column
market5['close']=market5['Close']*market5['Volume']     ##makes a new column called 'close' that contains the numerator for the python index for the 'Close' column
market5['high']=market5['High']*market5['Volume']       ##makes a new column called 'high' that contains the numerator for the python index for the 'High' column
market5['low']=market5['Low']*market5['Volume']     ##makes a new column called 'low' that contains the numerator for the python index for the 'Low' column
denom=market5['Volume'].groupby([market5.Date]).sum()      ##gets the sum of volume for each date
open=pd.DataFrame((market5['open'].groupby(market5.Date).sum())/denom) ##gets the sum of the numerator for the python index equation for 'open' based on each date and divides it by the sum of the volumes for each date and makes them into a dataframe
close=pd.DataFrame((market5['close'].groupby(market5.Date).sum())/denom) ##same thing as the above code but for 'close','high',and 'low'
high=pd.DataFrame((market5['high'].groupby(market5.Date).sum())/denom)
low=pd.DataFrame((market5['low'].groupby(market5.Date).sum())/denom)
first=pd.merge(open,high,on='Date')  ##merges the open and close python index values
second=pd.merge(low,close,on='Date')   ##merges the high and low python index values
alldat=pd.merge(first,second,on='Date')      ##merges all of the values
alldat.columns=['open','high','low','close']       ##renames the columns
print(alldat)

"""
9

                 open       high        low      close
Date                                                  
2013-01-02  37.218240  37.669825  36.804244  37.394700
2013-01-03  36.683928  37.175883  36.309854  36.730561
2013-01-04  37.735301  38.197961  37.471489  37.969676
2013-01-07  39.433973  39.952425  39.087880  39.596959
2013-01-08  39.403554  39.748143  38.922081  39.354890
2013-01-09  35.033924  35.411876  34.651302  35.014333
2013-01-10  37.137210  37.527043  36.757483  37.295754
2013-01-11  37.932903  38.256677  37.579063  37.991448
2013-01-14  38.348330  38.759699  37.980530  38.388938
2013-01-15  38.323527  38.880771  38.003460  38.487561
2013-01-16  39.353471  39.731879  38.887220  39.347620
2013-01-17  35.884004  36.233690  35.551895  35.877188
2013-01-18  40.277388  40.652477  39.865453  40.376961
2013-01-22  40.567323  41.068261  40.241281  40.851074
2013-01-23  44.417554  45.121563  44.065735  44.770209
2013-01-24  48.814446  49.728573  48.237470  49.174833
2013-01-25  58.340138  62.089706  58.052795  61.453043
2013-01-28  50.844625  51.450083  49.590466  50.007070
2013-01-29  41.631649  42.499318  41.221507  42.174208
2013-01-30  45.212780  45.587135  44.354852  44.792994
2013-01-31  44.310451  45.061372  43.789490  44.518366
"""

### 10. For the years 2007-2012 determine the top-5 months and years in terms of average relative volatility
### of the Python Index. Give a table with the month, year, and average relative volatility

market6=df.loc[df['Date'].str.contains('2007|2008|2009|2010|2011|2012')==True]    ##finds and stores records from 2007-2012
market6['open']=market6['Open']*market6['Volume']    ##makes a new column called 'open' that contains the numerator for the python index equation.
market6['close']=market6['Close']*market6['Volume']    ##same thing for the next 3 codes but for 'Close', 'High', and 'Low'
market6['high']=market6['High']*market6['Volume']
market6['low']=market6['Low']*market6['Volume']
denom2=market6['Volume'].groupby([market6.Date]).sum()    ##gets the sum of volume by Date
open2=pd.DataFrame((market6['open'].groupby(market6.Date).sum())/(denom2)) ##gets the sum of the numerator for the python index equation for 'open' based on each date and divides it by the sum of the volumes for each date and makes them into a dataframe
close2=pd.DataFrame((market6['close'].groupby(market6.Date).sum())/(denom2))  ##same thing as the above code but for 'close','high',and 'low'
high2=pd.DataFrame((market6['high'].groupby(market6.Date).sum())/(denom2))
low2=pd.DataFrame((market6['low'].groupby(market6.Date).sum())/(denom2))
first2=pd.merge(open2,close2,on='Date')     ##merges the open and close python index values
second2=pd.merge(high2,low2,on='Date')      ##merges the high and low python index values
alldat2=pd.merge(first2,second2,on='Date')      ##merges all of the values
alldat2.columns=['open','close','high','low']       ##renames the columns
alldat2['rel']=(alldat2['high']-alldat2['low'])/(0.5*(alldat2['open']+alldat2['close'])) ##calculates the relative volatility from the python index
alldat2['month']=alldat2.index.str.split('-').str[1]       ##creates a new column called month based on the month of the row
alldat2['year']=alldat2.index.str.split('-').str[0]       ##creates a new column called year based on the year of the row
alldat2['rel'].groupby([alldat2.year,alldat2.month]).mean().nlargest(5)    ##finds the mean relative volatility for each year and month and displays the top 5

"""
10

year  month
2008  10       0.100923
      11       0.081326
      09       0.067881
2009  03       0.066229
2008  12       0.062545
"""