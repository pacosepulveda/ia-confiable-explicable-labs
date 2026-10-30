from pathlib import Path

import numpy as np
import pandas as pd


SEED = 42
ROWS = 3000
OUTPUT = Path("data/aurea_credit.csv.gz")


def generate_dataset(n: int = ROWS, seed: int = SEED) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    customer_group = rng.choice(["A", "B"], n, p=[0.62, 0.38])

    age = np.clip(rng.normal(42, 9.5, n), 21, 70).round().astype(int)

    annual_income = np.exp(rng.normal(np.log(43000), 0.35, n))
    annual_income = np.clip(annual_income, 16000, 140000).round().astype(int)

    employment_months = np.clip(rng.gamma(3.1, 23, n), 1, 360).round().astype(int)

    credit_history_months = np.clip(
        (age - 18) * 12 + rng.normal(0, 45, n), 6, 600
    ).round().astype(int)

    debt_ratio = np.clip(rng.beta(2.35, 4.25, n), 0.02, 0.92)

    late_lambda = np.clip(0.15 + 1.25 * debt_ratio, 0.03, 2.5)
    late_payments_12m = np.clip(rng.poisson(late_lambda), 0, 7)

    existing_debt = np.clip(
        annual_income * debt_ratio * rng.uniform(0.5, 1.0, n), 0, 90000
    ).round().astype(int)

    requested_amount = np.clip(
        np.exp(rng.normal(np.log(12000), 0.5, n)), 1000, 55000
    ).round().astype(int)

    savings_balance = np.clip(
        np.exp(rng.normal(np.log(7000), 0.75, n)), 100, 80000
    ).round().astype(int)

    request_ratio = requested_amount / annual_income

    # Internal latent factor used only to shape the synthetic default distribution.
    # It is deliberately not included in the output dataset.
    income_volatility = np.clip(
        rng.normal(np.where(customer_group == "A", 0.12, 0.42), 0.10),
        0,
        0.7,
    )

    logit = (
        -3.75
        + 3.2 * (debt_ratio - 0.32)
        + 0.48 * late_payments_12m
        + 1.35 * (request_ratio - 0.25)
        - 0.0042 * (employment_months - 48)
        - 0.0013 * (credit_history_months - 220)
        - 0.000013 * (annual_income - 42000)
        - 0.000012 * (savings_balance - 7000)
        + 2.35 * income_volatility
    )

    logit += 1.25 * (debt_ratio > 0.58)
    logit += 0.95 * ((late_payments_12m >= 2) & (debt_ratio > 0.45))
    logit += 0.75 * (request_ratio > 0.55)
    logit += 0.70 * ((employment_months < 18) & (late_payments_12m >= 1))
    logit += 0.55 * ((savings_balance < 2000) & (requested_amount > 18000))
    logit += rng.normal(0, 0.28, n)

    probability_default = 1 / (1 + np.exp(-logit))
    default = rng.binomial(1, probability_default)

    return pd.DataFrame(
        {
            "application_id": [f"AF-{i:06d}" for i in range(1, n + 1)],
            "age": age,
            "annual_income": annual_income,
            "debt_ratio": np.round(debt_ratio, 3),
            "employment_months": employment_months,
            "late_payments_12m": late_payments_12m,
            "credit_history_months": credit_history_months,
            "existing_debt": existing_debt,
            "requested_amount": requested_amount,
            "savings_balance": savings_balance,
            "customer_group": customer_group,
            "default": default,
        }
    )


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df = generate_dataset()
    df.to_csv(OUTPUT, index=False, compression="gzip")

    print(f"Generated: {OUTPUT}")
    print(f"Rows: {len(df)}")
    print(f"Default rate: {df['default'].mean():.3f}")
    print(df.groupby("customer_group")["default"].agg(["count", "mean"]))


if __name__ == "__main__":
    main()
