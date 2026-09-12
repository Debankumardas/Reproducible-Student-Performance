# Research Question

Among students in the UCI Student Performance mathematics dataset, is greater weekly study time associated with higher final mathematics grades, after accounting for previous class failures and school absences?

## Hypotheses

## Population, Sample, and Exclusions

### Population

The target population is students represented by the UCI Student Performance dataset.

### Sample

The analysis sample will consist of students from the mathematics dataset (`student-mat.csv`), containing 395 observations.

### Exclusion Rules

## Variables and Measures

## Analysis Plan

## Data Transformations

The following transformations will be applied before the primary analysis:

- `studytime` will be retained using its original ordered coding from 1 to 4.
- `failures` will be retained as an integer count.
- `absences` will be retained as the recorded number of absences.
- `G3` will be retained on its original 0–20 scale.
- No logarithmic, standardization, normalization, or other mathematical transformation will be applied to the primary variables.
- No observations will be removed solely because they have extreme values.
- Rows with missing or invalid values in the variables required for the analysis will be excluded according to the predefined exclusion rules.

The processed dataset used for the final analysis will be generated from the raw dataset using a reproducible preprocessing procedure.

### Primary Analysis

A multiple linear regression model will be used to examine the association between weekly study time and final mathematics grade.

The model will be specified as:

G3 = β0 + β1(studytime) + β2(failures) + β3(absences) + ε

The primary effect of interest will be β1, representing the expected change in final mathematics grade associated with a one-category increase in weekly study time, after accounting for previous class failures and school absences.

### Statistical Inference

The primary analysis will use a two-sided significance level of α = 0.05.

The estimated coefficient for `studytime`, its 95% confidence interval, and p-value will be reported.

### Model Fit

Overall model fit will be reported using R² and adjusted R².

### Robustness Check

As a robustness analysis, `studytime` will also be treated as a categorical variable rather than an ordered numeric variable.

This will assess whether the estimated association depends on assuming that the difference between adjacent study-time categories is approximately equal.

### Model Diagnostics

The regression model will be checked for:

- Linearity between predictors and outcome
- Approximately normally distributed residuals
- Constant variance of residuals
- Influential observations

If assumptions are substantially violated, the findings will be reported with the relevant limitation rather than changing the primary analysis after seeing the results.

### Exposure Variable

**Weekly study time (`studytime`)**

Weekly study time is measured using four ordered categories:

- 1 = Less than 2 hours
- 2 = 2 to 5 hours
- 3 = 5 to 10 hours
- 4 = More than 10 hours

The primary analysis will treat `studytime` as an ordered numeric variable.

### Outcome Variable

**Final mathematics grade (`G3`)**

`G3` represents the student's final mathematics grade, measured on a scale from 0 to 20.

Higher values indicate higher final mathematics performance.

### Adjustment Variables

**Previous class failures (`failures`)**

The number of previous class failures, measured as an integer count.

**School absences (`absences`)**

The number of school absences recorded for each student.

### Variables Not Included as Adjustments

The earlier-period grades `G1` and `G2` will not be included as adjustment variables because they are closely related to the final grade and may provide information that occurs before the final outcome in a way that changes the research question.

Observations will be excluded if they:

- Have missing values in the research variables: `studytime`, `G3`, `failures`, or `absences`.
- Contain invalid or impossible values for these variables.

No observations will be excluded based on their final mathematics grade (`G3`) or study time merely because they have unusually high or low values.

### Null Hypothesis (H0)

There is no association between weekly study time and final mathematics grade after accounting for previous class failures and school absences.

### Alternative Hypothesis (H1)

Greater weekly study time is associated with higher final mathematics grades after accounting for previous class failures and school absences.

### Expected Direction

The expected association between weekly study time and final mathematics grade is positive.