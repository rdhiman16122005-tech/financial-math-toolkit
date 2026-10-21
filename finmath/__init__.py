
"""Functions for investment returns and volatility."""

import numpy as np


def simple_returns(prices):
    """Calculate simple returns between consecutive prices."""
    prices = np.asarray(prices, dtype=float)

    if prices.ndim != 1 or len(prices) < 2:
        raise ValueError("Provide at least two prices.")

    if not np.all(np.isfinite(prices)) or np.any(prices[:-1] == 0):
        raise ValueError("Prices must be finite and previous prices non-zero.")

    return np.diff(prices) / prices[:-1]


def annualized_volatility(returns, periods_per_year=252):
    """Estimate annualized volatility from periodic returns."""
    returns = np.asarray(returns, dtype=float)

    if returns.ndim != 1 or len(returns) < 2:
        raise ValueError("Provide at least two returns.")

    if not np.all(np.isfinite(returns)):
        raise ValueError("Returns must be finite.")

    if periods_per_year <= 0:
        raise ValueError("Periods per year must be positive.")

    return float(np.std(returns, ddof=1) * np.sqrt(periods_per_year))
