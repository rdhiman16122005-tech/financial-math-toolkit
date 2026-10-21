
"""Demonstrate maximum drawdown and price plotting."""

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from finmath.risk import max_drawdown


def main():
    """Load sample data, calculate drawdown and plot prices."""
    root = Path(__file__).resolve().parents[1]
    data_file = root / "data" / "prices.csv"

    with data_file.open(newline="") as file:
        rows = list(csv.DictReader(file))

    dates = [row["date"] for row in rows]
    prices = np.array([float(row["close"]) for row in rows])

    drawdown = max_drawdown(prices)
    print(f"Maximum drawdown: {drawdown:.2%}")

    plt.plot(dates, prices, marker="o")
    plt.title("Prices for Drawdown Analysis")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
