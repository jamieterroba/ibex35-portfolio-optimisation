# Portfolio Optimisation Analysis

## Overview

This project applies Modern Portfolio Theory to historical daily price data between 2021-09-30 and 2026-09-30 for the 35 equities in the IBEX 35 index. It first creates randomly generated long-only portfolios and then constrained maximum-Sharpe-ratio portfolios.

The analysis calculates annualised returns, annualised volatility, and Sharpe ratios. It also plots the Capital Market Line (CML) and applies Ledoit-Wolf covariance shrinkage.

## Methods

- Calculated daily asset returns from historical adjusted closing prices.
- Annualised portfolio mean returns and standard deviations using 252 trading days.
- Generated 5,000 random long-only portfolios.
- Calculated each portfolio's Sharpe ratio using a risk-free rate of 4.1670%.
- Optimised portfolio weights with SciPy's SLSQP optimiser.
- Applied a full-investment constraint: portfolio weights sum to 1.
- Applied no-short-selling and no leverage bounds: each asset weight lies between 0 and 1 or 0 and 0.05 (or equal-weighted).
- Compared the optimal portfolios: equal-weighted; no-short; and no-short, max-5%-weight.
- Plotted the CML using the risk-free rate and the market portfolio (constrained to 5% maximum asset weight).
- Found an optimal portfolio along the CML with a target annualised return of 35%.
- Calculated the Ledoit-Wolf covariance matrix and applied it to find the optimal portfolio (no-short, no-leverage).
- Compared the Ledoit-Wolf optimal portfolio to the basic Markowitz optimal portfolio.

## Key Results

- The market portfolio achieved an in-sample annualised mean return of 33.09%. Its annualised volatility (STD) was 14.91% and its Sharpe ratio was 1.9406.
- The resulting allocation was diversified at 22 equities, with the largest weight assigned to a number of assets at 5%.
- The optimal portfolio under only no-short and no-leverage constraints outperformed the market portfolio, but represents an unlikely corner solution.
- The market portfolio heavily outperformed the equal-weighted portfolio.
- The portfolio along the CML which combines the risk-free asset and the market portfolio, with a target mean annual returns of 35% obtained an annual standard deviation of 15.89% and a Sharpe ratio of 1.94.
- The new optimal portfolio under Ledoit-Wolf covariance estimation obtained an in-sample annual mean return of 42.00%, an annual standard deviation of 14.14% and a Sharpe ratio of 2.68.
- The new optimal portfolio under Ledoit-Wolf covariance estimation had a covariance shrinkage factor of 0.036544.


## Installation

Clone the repository and install the required Python packages:

```bash
git clone https://github.com/jamieterroba/ibex35-portfolio-optimisation
cd https://github.com/jamieterroba/ibex35-portfolio-optimisation
python -m pip install -r requirements.txt
```

## Usage

Run the notebook from Jupyter:

```bash
jupyter notebook
```

Then open and run:

```text
main.ipynb
```

## Limitations

- Historical returns are not indicative of future performance and should not be used to drive investment decisions.
- Expected returns drive unstable weights: small changes in estimated mean returns can produce very different portfolio allocations (corner solutions). 
- Sample covariance is noisy and optimisation can amplify small estimation errors into concentrated and unstable weights.
- Volatility and the Sharpe ratio do not fully capture skewness, fat tails, drawdowns, liquidity shocks, or regime changes.
- No trading frictions: the current model omits transaction costs, taxes, bid-ask spreads, turnover, and liquidity constraints.
- It assumes investors can choose weights once and that inputs remain representative, rather than rebalancing through changing market regimes.
- We assume investors can borrow and lend at the same risk-free rate at no additional cost.