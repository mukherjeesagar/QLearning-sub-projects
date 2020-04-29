"""Market simulator"""

import pandas as pd
import numpy as np
import datetime as dt
import yfinance as yf
#from assessPortfolio import assess_portfolio
from util import get_data, plot_data

def compute_portvals(orders_file = "./orders/orders.csv", start_val = 1000000):
    # TODO: Your code here
    ordersData = pd.read_csv(orders_file, index_col='Date', parse_dates=True)
    sdate = ordersData.index[0]
    edate=ordersData.index[-1]
    stocksList = []
    
    for index, ordersRow in ordersData.iterrows():
        if ordersRow['Symbol'] not in stocksList:
            stocksList.append(ordersRow['Symbol'])
            
    stocksData = yf.download(stocksList, start=sdate, end=edate+dt.timedelta(1), progress=False, group_by="Ticker")
    
    for stock in stocksList:
        stocksData[stock + ' Shares'] = pd.Series(0, index=stocksData.index)
    
    stocksData['Portolio Value'] = pd.Series(start_val, index=stocksData.index)
    stocksData['Cash'] = pd.Series(start_val, index=stocksData.index)
    
    for index, orderRow in ordersData.iterrows():
        symbol = orderRow['Symbol']
        if orderRow['Order'] == 'BUY':
            stocksData.loc[index:, symbol + ' Shares'] = stocksData.loc[index:, symbol + ' Shares'] + orderRow['Shares']
            stocksData.loc[index:, 'Cash'] -= stocksData.loc[index, symbol] * orderRow['Shares']
        if orderRow['Order'] == 'SELL':
            stocksData.loc[index:, symbol + ' Shares'] = stocksData.loc[index:, symbol + ' Shares'] - orderRow['Shares']
            stocksData.loc[index:, 'Cash'] += stocksData.loc[index, symbol] * orderRow['Shares']
    
    for index, orderRow in stocksData.iterrows():
        sharesVal = 0
        for stock in stocksList:
            sharesVal += stocksData.loc[index, stock + ' Shares'] * orderRow[stock]
        stocksData.loc[index, 'Portolio Value'] = stocksData.loc[index, 'Cash'] + sharesVal
    
    return stocksData.loc[:, 'Portolio Value']

#    # In the template, instead of computing the value of the portfolio, we just
#    # read in the value of IBM over 6 months
#    start_date = dt.datetime(2008,1,1)
#    end_date = dt.datetime(2008,6,1)
#    portvals = get_data(['IBM'], pd.date_range(start_date, end_date))
#    portvals = portvals[['IBM']]  # remove SPY

#    return portvals

def test_code():
    # Helper function: tests our code
    
    # Input parameters
    of = "./orders/orders.csv"
    sv = 1000000

    # Process orders
    portvals = compute_portvals(orders_file = of, start_val = sv)
    if isinstance(portvals, pd.DataFrame):
#        portvals = portvals[portvals.columns[0]] # just get the first column
        print(portvals)
    else:
        print("warning, code did not return a DataFrame")
        print(portvals)
    
#    # Get portfolio stats
#    # Here we just fake the data. you should use your code from previous assignments.
#    start_date = dt.datetime(2008,1,1)
#    end_date = dt.datetime(2008,6,1)
#    cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = [0.2,0.01,0.02,1.5]
#    cum_ret_SPY, avg_daily_ret_SPY, std_daily_ret_SPY, sharpe_ratio_SPY = [0.2,0.01,0.02,1.5]

    # Compare portfolio against $SPX
#    print ("Date Range: {} to {}".format(start_date, end_date), '\n')
#    
#    print ("Sharpe Ratio of Fund: {}".format(sharpe_ratio))
#    print ("Sharpe Ratio of SPY : {}".format(sharpe_ratio_SPY), '\n')
#    
#    print ("Cumulative Return of Fund: {}".format(cum_ret))
#    print ("Cumulative Return of SPY : {}".format(cum_ret_SPY), '\n')
#    
#    print ("Standard Deviation of Fund: {}".format(std_daily_ret))
#    print ("Standard Deviation of SPY : {}".format(std_daily_ret_SPY), '\n')
#    
#    print ("Average Daily Return of Fund: {}".format(avg_daily_ret))
#    print ("Average Daily Return of SPY : {}".format(avg_daily_ret_SPY), '\n')
#    
#    print ("Final Portfolio Value: {}".format(portvals[-1]))

if __name__ == "__main__":
#    test_code()
    of = "./orders/orders.csv"
    sv = 1000000
    
    
    #####
    orders_file = of
    start_val = sv
    ordersData = pd.read_csv(orders_file, index_col='Date', parse_dates=True)
    sdate = ordersData.index[0]
    edate=ordersData.index[-1]
    stocksList = []
    
    for index, ordersRow in ordersData.iterrows():
        if ordersRow['Symbol'] not in stocksList:
            stocksList.append(ordersRow['Symbol'])
            
    stocksData = yf.download(stocksList, start=sdate, end=edate+dt.timedelta(1), progress=False, group_by="Ticker")
    
    for stock in stocksList:
        stocksData[stock + ' Shares'] = pd.Series(0, index=stocksData.index)
    
    stocksData['Portolio Value'] = pd.Series(start_val, index=stocksData.index)
    stocksData['Cash'] = pd.Series(start_val, index=stocksData.index)
    
    for index, orderRow in ordersData.iterrows():
        symbol = orderRow['Symbol']
        if orderRow['Order'] == 'BUY':
            stocksData.loc[index:, symbol + ' Shares'] = stocksData.loc[index:, symbol + ' Shares'] + orderRow['Shares']
            stocksData.loc[index:, 'Cash'] -= stocksData.loc[index, symbol] * orderRow['Shares']
        if orderRow['Order'] == 'SELL':
            stocksData.loc[index:, symbol + ' Shares'] = stocksData.loc[index:, symbol + ' Shares'] - orderRow['Shares']
            stocksData.loc[index:, 'Cash'] += stocksData.loc[index, symbol] * orderRow['Shares']
    
    for index, orderRow in stocksData.iterrows():
        sharesVal = 0
        for stock in stocksList:
            sharesVal += stocksData.loc[index, stock + ' Shares'] * orderRow[stock]
        stocksData.loc[index, 'Portolio Value'] = stocksData.loc[index, 'Cash'] + sharesVal
    
    portvals = stocksData.loc[:, 'Portolio Value']
    #####
    if isinstance(portvals, pd.DataFrame):
#        portvals = portvals[portvals.columns[0]] # just get the first column
        print(portvals)
    else:
        print("warning, code did not return a DataFrame")
        print(portvals)
