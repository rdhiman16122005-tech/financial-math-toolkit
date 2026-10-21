
"""Functions for measuring investment risk."""

import numpy as np


def max_drawdown(prices):
    """Calculate the largest percentage decline from a running peak."""
    prices = np.asarray(prices, dtype=float)

    if prices.ndim != 1 or len(prices) < 2:
        raise ValueError("Provide at least two prices.")

    if not np.all(np.isfinite(prices)) or np.any(prices <= 0):
        raise ValueError("Prices must be finite and positive.")

    running_peaks = np.maximum.accumulate(prices)
    drawdowns = prices / running_peaks - 1

    return float(np.min(drawdowns))