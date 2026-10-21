"""Functions for investment returns and volatility."""

import numpy as np


def simple_returns(prices):
    """Calculate returns between consecutive prices."""
    prices = np.asarray(prices, dtype=float)

    if prices.ndim != 1 or len(prices) < 2:
        raise ValueError("Provide at least two prices.")

    if not np.all(np.isfinite(prices)):
        raise ValueError("Prices must be finite.")

    if np.any(prices[:-1] == 0):
        raise ValueError("Previous prices must be non-zero.")

    returns = np.diff(prices) / prices[:-1]
    return returns


def annualized_volatility(returns, periods_per_year=252):
    """Calculate annualised volatility from periodic returns."""
    returns = np.asarray(returns, dtype=float)

    if returns.ndim != 1 or len(returns) < 2:
        raise ValueError("Provide at least two returns.")

    if not np.all(np.isfinite(returns)):
        raise ValueError("Returns must be finite.")

    if periods_per_year <= 0:
        raise ValueError("Periods per year must be positive.")

    volatility = np.std(returns, ddof=1) * np.sqrt(periods_per_year)
    return float(volatility)