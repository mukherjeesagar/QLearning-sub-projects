"""A basic Linear regression based learner"""

from LinRegLearner import LinRegLearner as LR
import pandas as pd
import numpy as np
import datetime as dt
import yfinance as yf
#from assessPortfolio import assess_portfolio

def compute_portvals(orders_file = "./orders/orders.csv", start_val = 1000000):
    

if __name__ == "__main__":
    stock = 'IBM'
    sd = dt.datetime(2015,12,31)
    ed = dt.datetime(2019,12,31)
    df = yf.download(stock, start=sd, end=ed+dt.timedelta(1), progress=False)
    lr = LR()