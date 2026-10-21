
"""Demonstrate returns, volatility and price plotting."""

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from finmath.returns import simple_returns, annualized_volatility


def main():
    """Load sample data, calculate returns and plot prices."""
    root = Path(__file__).resolve().parents[1]
    data_file = root / "data" / "prices.csv"

    with data_file.open(newline="") as file:
        rows = list(csv.DictReader(file))

    dates = [row["date"] for row in rows]
    prices = np.array([float(row["close"]) for row in rows])

    returns = simple_returns(prices)
    volatility = annualized_volatility(returns)

    print("Daily returns (%):", np.round(returns * 100, 2))
    print(f"Annualised volatility: {volatility:.2%}")

    plt.plot(dates, prices, marker="o")
    plt.title("Illustrative Closing Prices")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()