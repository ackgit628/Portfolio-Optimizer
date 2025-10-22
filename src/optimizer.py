"""
Portfolio optimization module for efficient frontier calculations and portfolio analysis.
"""

import numpy as np
import pandas as pd

class PortfolioOptimizer:
    def __init__(self):
        self.returns = None
        self.weights = None
        self.assets = None
        
    def set_data(self, returns_data: pd.DataFrame):
        """
        Set the asset returns data for optimization.
        
        Args:
            returns_data (pd.DataFrame): DataFrame containing asset returns
        """
        self.returns = returns_data
        self.assets = returns_data.columns.tolist()
        
    def calculate_portfolio_metrics(self, weights: np.ndarray) -> tuple:
        """
        Calculate portfolio return and risk metrics.
        
        Args:
            weights (np.ndarray): Array of portfolio weights
            
        Returns:
            tuple: (expected_return, volatility)
        """
        if self.returns is None:
            raise ValueError("Returns data not set. Call set_data first.")
            
        portfolio_return = np.sum(self.returns.mean() * weights) * 252  # Annualized return
        portfolio_volatility = np.sqrt(
            np.dot(weights.T, np.dot(self.returns.cov() * 252, weights))
        )
        
        return portfolio_return, portfolio_volatility