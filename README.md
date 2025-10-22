# Portfolio Optimizer

A Python-based portfolio optimization tool that uses mathematical principles to construct the best possible portfolio from a given set of assets. "Best" is defined by finding the asset allocation that offers the highest expected return for a specific level of risk, or the lowest risk for a given level of return.

## Objective and Methodology

### Objective 🎯

The primary objective is to maximize a portfolio's risk-adjusted return through diversification. It's not just about picking winning stocks; it's about combining them in a way that their individual risks partially cancel each other out, giving you a smoother overall ride.

### Methodology: Modern Portfolio Theory (MPT)

The optimizer is built on the Nobel Prize-winning Modern Portfolio Theory (MPT). The core ideas are:

1. **The Efficient Frontier**: For any group of assets, there's a set of "optimal" portfolios that form a curve called the Efficient Frontier. Any portfolio on this curve offers the highest possible expected return for its level of risk. Any portfolio below the curve is suboptimal because you could get a higher return for the same risk or the same return for less risk.

2. **Diversification is Key**: MPT mathematically proves that mixing assets that don't move perfectly in sync (i.e., have low correlation) reduces the overall portfolio's volatility without sacrificing an equivalent amount of return.

3. **The Sharpe Ratio**: This is the metric we use to find the single "best" portfolio on the Efficient Frontier. It measures the return of a portfolio over and above the risk-free rate, per unit of risk (volatility). Our goal is to find the portfolio with the highest possible Sharpe Ratio.

```
Sharpe Ratio = (Expected Portfolio Return − Risk Free Rate) / Portfolio Volatility
```

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