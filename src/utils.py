"""
Utility functions for data processing and financial calculations.
"""

import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

def fetch_stock_data(tickers: list, start_date: str = None, end_date: str = None) -> pd.DataFrame:
    """
    Fetch historical stock data from Yahoo Finance.
    
    Args:
        tickers (list): List of stock tickers
        start_date (str): Start date in 'YYYY-MM-DD' format
        end_date (str): End date in 'YYYY-MM-DD' format
        
    Returns:
        pd.DataFrame: DataFrame containing adjusted close prices
    """
    if not start_date:
        start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
    if not end_date:
        end_date = datetime.now().strftime('%Y-%m-%d')
        
    data = pd.DataFrame()
    
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(start=start_date, end=end_date)
        data[ticker] = hist['Adj Close']
        
    return data

def calculate_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate daily returns from price data.
    
    Args:
        prices (pd.DataFrame): DataFrame containing price data
        
    Returns:
        pd.DataFrame: DataFrame containing daily returns
    """
    return prices.pct_change().dropna()