from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent

# Dates:
end_date = "2026-09-30"
start_date = "2021-09-30"

# Asset universe:
asset_file = PROJECT_ROOT / "data" / "ibex_tickers.csv"

# Other
trading_days = 252
risk_free_rate = 0.041670 # 10Y Spain govt yield on 1/10/2026
num_random_portfolios = 5000
max_weight = 0.05 # for constrained optimisation
random_seed = 42
