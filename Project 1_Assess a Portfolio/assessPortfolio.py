import datetime as dt
import pandas as pd
import yfinance as yf
import numpy as np

def assess_portfolio(sd, ed, syms, allocs, sv, rfr, sf, gen_plot):
    """
    Function for assessing the standard portfolio statistics.
    sd, ed: Start/End date
    syms: Symbols of stocks (Tickers)
    allocs: Allocated weights
    sv: Portfolio snding value
    rfr: Risk-free return
    sf: Sampling frequency per year
    gen_plot: If True, creates a time-series plot of cumulative returns
    """
    # Downloading stocks-data from Yahoo-finance
    df = yf.download(syms, start=sd, end=ed, group_by="ticker", progress=False)
    
    cr = 0                                  # Cumulative Return
    df['returns'] =  np.zeros(len(df[syms[0]]['Adj Close']))
    for i in range(len(syms)):
        df['returns'] += allocs[i]*((df[syms[i]]['Adj Close']/df[syms[i]]['Adj Close'].shift(1)) - 1)
        cr += allocs[i]*((df[syms[i]]['Adj Close'][-1]/df[syms[i]]['Adj Close'][0]) - 1)
    df['returns'] = df['returns'][1:]       # Portfolio daily returns
    adr = df['returns'].mean()              # Average Daily Return
    sddr = df['returns'].std()              # Volatility (stdev: daily returns)
    sr = sf**(0.5)*(adr - rfr) / sddr       # Sharpe Ratio
    ev = sv*(1 + cr)                        # Portfolio ending value
    
    df['cum_prod'] = (df['returns'] + 1).cumprod()
    
    if gen_plot == True:
        df['cum_prod'].plot()
    return cr, adr, sddr, sr, ev

if __name__ == "__main__":
    
    # Initialize portfolio inputs
#    start_date = dt.datetime(2010,1,1)
#    end_date = dt.datetime(2010,12,31)
#    symbols = ['GOOG', 'AAPL', 'GLD', 'XOM']
#    allocations = [0.2, 0.3, 0.4, 0.1]
#    start_val = 1000000  
#    risk_free_rate = 0.0
#    sample_freq = 252
    
    start_date = dt.datetime(2010,6,1)
    end_date = dt.datetime(2010,12,31)
    symbols = ['GOOG', 'AAPL', 'GLD', 'XOM']
    allocations = [0.2, 0.3, 0.4, 0.1]
    start_val = 1000000  
    risk_free_rate = 0.0
    sample_freq = 252
    
    # Assess the portfolio
    cr, adr, sddr, sr, ev = \
    assess_portfolio(sd = start_date, ed = end_date, \
    syms = symbols, \
    allocs = allocations, \
    sv = start_val, rfr = risk_free_rate, sf = sample_freq, \
    gen_plot = False)
    
    # Print portfolio-statistics
    print("Start Date:", start_date)
    print("End Date:", end_date)
    print("Symbols:", symbols)
    print("Allocations:", allocations)
    print("Sharpe Ratio:", sr)
    print("Volatility (stdev of daily returns):", sddr)
    print("Average Daily Return:", adr)
    print("Cumulative Return:", cr)