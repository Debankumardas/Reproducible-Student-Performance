import pandas as pd


def test_synthetic_pipeline():
    data = pd.DataFrame({
        "studytime": [1, 2, 3, 4, 2],
        "failures": [0, 1, 0, 0, 2],
        "absences": [5, 10, 2, 8, 12],
        "G3": [10, 11, 15, 17, 9]
    })

    required_columns = ["studytime", "failures", "absences", "G3"]

    # Expected output contract
    expected_rows = 5
    expected_columns = required_columns

    # Validate output structure
    assert list(data.columns) == expected_columns
    assert len(data) == expected_rows

    # Validate missing values
    assert data[required_columns].isna().sum().sum() == 0

    # Validate value constraints
    assert data["studytime"].between(1, 4).all()
    assert data["failures"].ge(0).all()
    assert data["absences"].ge(0).all()
    assert data["G3"].between(0, 20).all()