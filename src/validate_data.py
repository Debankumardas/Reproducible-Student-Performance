from pathlib import Path

import pandas as pd


DATA_PATH = Path("data/raw/student-mat.csv")

REQUIRED_COLUMNS = [
    "studytime",
    "failures",
    "absences",
    "G3",
]


def load_data():
    df = pd.read_csv(DATA_PATH, sep=";")
    return df


def validate_data(df):
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    if df[REQUIRED_COLUMNS].isna().any().any():
        raise ValueError("Missing values found in required variables.")

    if not df["studytime"].between(1, 4).all():
        raise ValueError("Invalid studytime values found.")

    if not df["failures"].ge(0).all():
        raise ValueError("Invalid failures values found.")

    if not df["absences"].ge(0).all():
        raise ValueError("Invalid absences values found.")

    if not df["G3"].between(0, 20).all():
        raise ValueError("Invalid G3 values found.")

    return True


if __name__ == "__main__":
    data = load_data()
    validate_data(data)

    print("Data validation passed.")
    print(f"Rows: {len(data)}")
    print(f"Columns: {len(data.columns)}")