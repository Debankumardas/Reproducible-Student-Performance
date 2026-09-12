from pathlib import Path

import pandas as pd
import statsmodels.api as sm


# File paths
DATA_PATH = Path("data/raw/student-mat.csv")
PROCESSED_PATH = Path("data/processed/analysis_data.csv")


# Required variables from the preregistration
REQUIRED_COLUMNS = [
    "studytime",
    "failures",
    "absences",
    "G3",
]


def load_data():
    """Load the raw mathematics student performance dataset."""
    return pd.read_csv(DATA_PATH, sep=";")


def prepare_data(df):
    """Apply the preregistered data exclusion rules."""

    analysis_df = df[REQUIRED_COLUMNS].copy()

    # Exclude rows with missing required variables.
    analysis_df = analysis_df.dropna(subset=REQUIRED_COLUMNS)

    # Exclude invalid or impossible values.
    analysis_df = analysis_df[
        analysis_df["studytime"].between(1, 4)
        & analysis_df["failures"].ge(0)
        & analysis_df["absences"].ge(0)
        & analysis_df["G3"].between(0, 20)
    ]

    return analysis_df


def run_primary_regression(df):
    """Run the preregistered multiple linear regression."""

    X = df[["studytime", "failures", "absences"]]
    X = sm.add_constant(X)

    y = df["G3"]

    model = sm.OLS(y, X).fit()

    return model


if __name__ == "__main__":
    # Load raw data
    data = load_data()

    # Apply preregistered exclusions
    analysis_data = prepare_data(data)

    # Save processed dataset for reproducibility
    analysis_data.to_csv(PROCESSED_PATH, index=False)

    # Run primary regression
    model = run_primary_regression(analysis_data)

    # Extract primary studytime result
    studytime_result = model.params["studytime"]
    confidence_interval = model.conf_int().loc["studytime"]

    print("Primary analysis completed.")
    print(f"Analysis rows: {len(analysis_data)}")
    print(f"Processed data saved to: {PROCESSED_PATH}")
    print(f"Studytime coefficient: {studytime_result:.4f}")
    print(
        f"95% CI: "
        f"{confidence_interval[0]:.4f} to "
        f"{confidence_interval[1]:.4f}"
    )
    print(f"P-value: {model.pvalues['studytime']:.4f}")
    print(f"R-squared: {model.rsquared:.4f}")
    print(f"Adjusted R-squared: {model.rsquared_adj:.4f}")