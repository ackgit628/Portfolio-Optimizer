# Portfolio Optimizer

A Python-based portfolio optimization tool that helps investors find optimal asset allocations based on the Modern Portfolio Theory (MPT).

## Features

- Calculate efficient frontier for a given set of assets
- Optimize portfolio weights for maximum Sharpe ratio
- Historical data fetching from Yahoo Finance
- Risk and return metrics calculation
- Portfolio performance analysis

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd portfolio-optimizer
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Basic example:

```python
from src.optimizer import PortfolioOptimizer
from src.utils import fetch_stock_data, calculate_returns

# Initialize the optimizer
optimizer = PortfolioOptimizer()

# Fetch data for some stocks
tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']
prices = fetch_stock_data(tickers)
returns = calculate_returns(prices)

# Set the data for optimization
optimizer.set_data(returns)

# Calculate portfolio metrics for equal weights
import numpy as np
weights = np.array([0.25, 0.25, 0.25, 0.25])
expected_return, volatility = optimizer.calculate_portfolio_metrics(weights)
print(f"Expected Return: {expected_return:.2%}")
print(f"Volatility: {volatility:.2%}")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.