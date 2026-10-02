# Portfolio Optimisation Analysis

## Overview

This project applies Modern Portfolio Theory to historical daily price data between 2021-09-30 and 2026-09-30 for 34 of the 35 equities in the IBEX 35 index. Puig Brands (PUIG.MC) is excluded because it only listed in May 2024 and has no price history for most of the period. It first creates randomly generated long-only portfolios and then constrained maximum-Sharpe-ratio portfolios.

The analysis calculates annualised returns, annualised volatility, and Sharpe ratios. It also plots the Capital Market Line (CML).

## Methods

- Calculated daily asset returns from historical adjusted closing prices.
- Annualised portfolio mean returns and standard deviations using 252 trading days.
- Generated 5,000 random long-only portfolios.
- Calculated each portfolio's Sharpe ratio using a risk-free rate of 4.1670%.
- Optimised portfolio weights with SciPy's SLSQP optimiser.
- Applied a full-investment constraint: portfolio weights sum to 1.
- Applied no-short-selling bounds: each asset weight lies between 0 and 1 or 0 and 0.05 (or equal-weighted).
- Compared the optimal portfolios: equal-weighted; no-short, no-leverage; and no-short, max-5%-weight.
- Plotted the CML using the risk-free rate and the market portfolio (constrained to 5% maximum asset weight).

## Key Results

- The market portfolio achieved an annualised return of 23.27%.
- Its annualised volatility was 15.15%.
- Its Sharpe ratio was 1.2609.
- The resulting allocation was diversified, with the largest weight assigned to a number of assets at 5%.

## Installation

Clone the repository and install the required Python packages:

```bash
git clone https://github.com/jamieterroba/ibex35-portfolio-optimisation
cd ibex35-portfolio-optimisation
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Usage

Run the notebook from Jupyter:

```bash
jupyter notebook
```

Then open and run:

```text
notebooks/main.ipynb
```

## Limitations

- Historical returns do not guarantee future performance.
- Optimised portfolio weights are sensitive to the selected date range and estimates of returns and covariance and can often lead to corner solutions.
- The analysis assumes that assets can be combined without transaction costs or taxes.
- The CML representation assumes that a risk-free asset is available at the stated risk-free rate.