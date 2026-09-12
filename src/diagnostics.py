from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from scipy import stats


DATA_PATH = Path("data/processed/analysis_data.csv")


def load_data():
    return pd.read_csv(DATA_PATH)


def run_primary_model(df):
    X = df[["studytime", "failures", "absences"]]
    X = sm.add_constant(X)

    y = df["G3"]

    return sm.OLS(y, X).fit()


def run_diagnostics(model):
    residuals = model.resid
    fitted = model.fittedvalues

    # Residual normality
    shapiro_stat, shapiro_p = stats.shapiro(residuals)

    # Influence diagnostics
    influence = model.get_influence()
    cooks_distance = influence.cooks_distance[0]

    print("Diagnostic analysis completed.")
    print(f"Analysis rows: {len(residuals)}")
    print()

    print("Residual normality (Shapiro-Wilk):")
    print(f"Statistic: {shapiro_stat:.4f}")
    print(f"P-value: {shapiro_p:.4f}")
    print()

    print("Influential observations:")
    print(f"Maximum Cook's distance: {cooks_distance.max():.4f}")
    print(
        f"Observations with Cook's distance > 4/n: "
        f"{(cooks_distance > 4 / len(residuals)).sum()}"
    )

    # Residuals vs fitted values
    plt.figure()
    plt.scatter(fitted, residuals)
    plt.axhline(0, linestyle="--")
    plt.xlabel("Fitted values")
    plt.ylabel("Residuals")
    plt.title("Residuals vs Fitted Values")
    plt.show()

    # Q-Q plot
    plt.figure()
    sm.qqplot(residuals, line="45", fit=True)
    plt.title("Q-Q Plot of Residuals")
    plt.show()


if __name__ == "__main__":
    data = load_data()
    model = run_primary_model(data)
    run_diagnostics(model)