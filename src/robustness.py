from pathlib import Path

import pandas as pd
import statsmodels.formula.api as smf


DATA_PATH = Path("data/processed/analysis_data.csv")


def load_data():
    return pd.read_csv(DATA_PATH)


def run_categorical_analysis(df):
    model = smf.ols(
        "G3 ~ C(studytime) + failures + absences",
        data=df
    ).fit()

    return model


if __name__ == "__main__":
    data = load_data()
    model = run_categorical_analysis(data)

    print("Categorical studytime robustness analysis completed.")
    print(f"Analysis rows: {len(data)}")
    print()
    print("Model coefficients:")
    print(model.params)
    print()
    print("P-values:")
    print(model.pvalues)
    print()
    print(f"R-squared: {model.rsquared:.4f}")
    print(f"Adjusted R-squared: {model.rsquared_adj:.4f}")