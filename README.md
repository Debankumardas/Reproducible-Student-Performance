# Reproducible Student Performance Research

A preregistered and reproducible statistical research project investigating
whether weekly study time is associated with final mathematics grades, after
accounting for previous class failures and school absences.

## Research Question

Among students in the UCI Student Performance mathematics dataset, is greater
weekly study time associated with higher final mathematics grades, after
accounting for previous class failures and school absences?

## Dataset

**UCI Student Performance Dataset**

The analysis uses the mathematics dataset:

`student-mat.csv`

The dataset contains 395 student observations and 33 variables.

Primary variables used:

- `studytime` — weekly study time category (1–4)
- `failures` — number of previous class failures
- `absences` — number of school absences
- `G3` — final mathematics grade (0–20)

`G1` and `G2` were not included as adjustment variables because they are
closely related to the final grade and would substantially change the research
question.

## Preregistration

The research question, hypotheses, sample rules, variables, transformations,
analysis plan, robustness checks, and deviation policy were defined before
examining the real-data outcome patterns.

See:

`preregistration.md`

## Analysis

The primary analysis uses multiple linear regression:

`G3 = beta0 + beta1(studytime) + beta2(failures) + beta3(absences) + error`

The primary effect is the coefficient for `studytime`.

The analysis reports:

- Study-time coefficient
- 95% confidence interval
- P-value
- R-squared
- Adjusted R-squared

A categorical version of `studytime` is also used as a preregistered
robustness analysis.

## Results

The primary analysis produced:

- Studytime coefficient: **0.2158**
- 95% CI: **-0.2976 to 0.7292**
- P-value: **0.4091**
- R-squared: **0.1347**
- Adjusted R-squared: **0.1281**

The estimated association between study time and final grade was positive,
but the confidence interval included zero and the association was not
statistically significant at alpha = 0.05.

The categorical robustness analysis reached the same overall conclusion.

Detailed results and diagnostic findings are available in:

`reports/results.md`

## Reproducibility

The project includes:

- Raw data
- Processed analysis data
- Reproducible Python scripts
- Environment lockfile
- Synthetic pipeline validation
- Real-data validation
- Expected output contract
- Statistical analysis
- Robustness analysis
- Diagnostic checks
- Results report

The synthetic validation checks the expected structure and validity rules
before applying the workflow to the real dataset.

See:

`docs/output_contract.md`

## Repository Structure

```text
Reproducible-Student-Performance/
│
├── data/
│   ├── raw/
│   │   └── student-mat.csv
│   ├── interim/
│   └── processed/
│       └── analysis_data.csv
│
├── docs/
│   └── output_contract.md
│
├── notebooks/
│
├── reports/
│   └── results.md
│
├── src/
│   ├── validate_data.py
│   ├── analysis.py
│   ├── robustness.py
│   └── diagnostics.py
│
├── tests/
│   └── test_pipeline.py
│
├── preregistration.md
├── requirements.txt
├── README.md
└── .gitignore