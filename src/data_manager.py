"""
Data management module for portfolio optimization.
Handles asset selection and data downloading from Yahoo Finance.
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import logging

class DataManager:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self._setup_logging()
        
    def _setup_logging(self):
        """Configure logging for the data manager."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    
    def download_data(self, tickers, start_date=None, end_date=None, period='5y'):
        """
        Download historical price data for given tickers.
        
        Args:
            tickers (list): List of stock tickers
            start_date (str, optional): Start date in 'YYYY-MM-DD' format
            end_date (str, optional): End date in 'YYYY-MM-DD' format
            period (str, optional): Time period to download (default '5y')
            
        Returns:
            pd.DataFrame: DataFrame containing adjusted close prices
        """
        try:
            # If dates are not provided, use period
            # Download data for each ticker individually to ensure robust handling
            all_data = pd.DataFrame()
            
            for ticker in tickers:
                self.logger.info(f"Downloading data for {ticker}")
                if start_date is None and end_date is None:
                    ticker_data = yf.download(ticker, period=period, progress=False)
                else:
                    ticker_data = yf.download(ticker, start=start_date, end=end_date, progress=False)
                
                if not ticker_data.empty:
                    all_data[ticker] = ticker_data['Close']  # Using 'Close' instead of 'Adj Close'
                else:
                    self.logger.warning(f"No data found for {ticker}")
            
            data = all_data
            
            # Check if we got data for all tickers
            missing_tickers = [ticker for ticker in tickers if ticker not in data.columns]
            if missing_tickers:
                self.logger.warning(f"No data found for tickers: {missing_tickers}")
            
            return data
            
        except Exception as e:
            self.logger.error(f"Error downloading data: {str(e)}")
            raise
    
    def calculate_returns(self, prices):
        """
        Calculate daily returns from price data.
        
        Args:
            prices (pd.DataFrame): DataFrame containing price data
            
        Returns:
            pd.DataFrame: DataFrame containing daily returns
        """
        try:
            returns = prices.pct_change().dropna()
            self.logger.info("Successfully calculated returns")
            return returns
        except Exception as e:
            self.logger.error(f"Error calculating returns: {str(e)}")
            raise

def main():
    """Example usage of the DataManager class."""
    # Initialize the data manager
    dm = DataManager()
    
    # Define sample assets from different sectors
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']  # Tech
    tickers.extend(['JPM', 'BAC'])               # Finance
    tickers.extend(['PFE', 'JNJ'])              # Healthcare
    tickers.extend(['XOM', 'CVX'])              # Energy
    
    # Download data for the last 5 years
    prices = dm.download_data(tickers)
    
    # Calculate returns
    returns = dm.calculate_returns(prices)
    
    # Display some basic statistics
    print("\nBasic Statistics:")
    print("\nAnnualized Returns:")
    print((returns.mean() * 252 * 100).round(2))  # 252 trading days
    print("\nAnnualized Volatility:")
    print((returns.std() * np.sqrt(252) * 100).round(2))

if __name__ == "__main__":
    import numpy as np
    main()