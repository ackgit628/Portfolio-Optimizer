"""
Example script demonstrating how to use the Portfolio Optimizer.
This script shows how to download data and perform basic portfolio analysis.
"""

from src.data_manager import DataManager
from src.optimizer import PortfolioOptimizer
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Initialize the data manager
    dm = DataManager()
    
    # Define assets from different sectors for better diversification
    tickers = [
        'AAPL', 'MSFT', 'GOOGL', 'AMZN',  # Technology
        'JPM', 'BAC',                      # Finance
        'PFE', 'JNJ',                      # Healthcare
        'XOM', 'CVX'                       # Energy
    ]
    
    # Download historical data
    print("Downloading historical data...")
    prices = dm.download_data(tickers, period='5y')
    
    # Calculate returns
    print("Calculating returns...")
    returns = dm.calculate_returns(prices)
    
    # Display basic statistics
    print("\nBasic Statistics:")
    print("\nAnnualized Returns:")
    annual_returns = (returns.mean() * 252 * 100).round(2)
    print(annual_returns)
    
    print("\nAnnualized Volatility:")
    annual_vol = (returns.std() * (252 ** 0.5) * 100).round(2)
    print(annual_vol)
    
    # Create correlation heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(returns.corr(), annot=True, cmap='coolwarm', center=0)
    plt.title('Asset Correlation Matrix')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()