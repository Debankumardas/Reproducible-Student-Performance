\# Results Report



\## 1. Research Question



Among students in the UCI Student Performance mathematics dataset, is greater weekly study time associated with higher final mathematics grades, after accounting for previous class failures and school absences?



\## 2. Dataset and Sample



The analysis used the UCI Student Performance mathematics dataset (`student-mat.csv`).



\- Initial observations: 395

\- Variables in the original dataset: 33

\- Final analysis observations: 395

\- Outcome: `G3` (final mathematics grade, 0-20)

\- Exposure: `studytime` (1-4)

\- Adjustment variables:

&#x20; - `failures`

&#x20; - `absences`



No observations were excluded because of extreme values alone.



\## 3. Primary Analysis



The preregistered primary analysis used multiple linear regression:



G3 = beta0 + beta1(studytime) + beta2(failures) + beta3(absences) + error



The primary effect of interest was the coefficient for `studytime`.



\### Primary Results



\- Studytime coefficient: \*\*0.2158\*\*

\- 95% confidence interval: \*\*-0.2976 to 0.7292\*\*

\- P-value: \*\*0.4091\*\*

\- R-squared: \*\*0.1347\*\*

\- Adjusted R-squared: \*\*0.1281\*\*



The estimated association between studytime and final mathematics grade was positive, but it was not statistically significant at the preregistered alpha = 0.05 level.



The confidence interval included zero, so the analysis does not provide sufficient evidence of an association between greater weekly study time and higher final mathematics grades after accounting for failures and absences.



\## 4. Robustness Analysis



As preregistered, a robustness analysis treated `studytime` as a categorical variable rather than assuming a linear effect across categories.



`studytime = 1` was used as the reference category.



\### Results



| Variable | Coefficient | P-value |

|---|---:|---:|

| Intercept | 10.9997 | <0.001 |

| Studytime = 2 | -0.3749 | 0.4714 |

| Studytime = 3 | 0.7457 | 0.2739 |

| Studytime = 4 | 0.1884 | 0.8402 |

| Failures | -2.2248 | <0.001 |

| Absences | 0.0370 | 0.1722 |



\- R-squared: \*\*0.1408\*\*

\- Adjusted R-squared: \*\*0.1298\*\*



None of the studytime categories differed significantly from the reference category.



The categorical specification therefore does not provide evidence of a statistically significant studytime association and does not change the conclusion of the primary analysis.



\## 5. Diagnostic Checks



\### Residual Normality



The Shapiro-Wilk test gave:



\- Statistic: \*\*0.9575\*\*

\- P-value: \*\*<0.001\*\*



This indicates that the residuals were not normally distributed.



The Q-Q plot also showed noticeable departures from the reference line, particularly in the tails.



\### Linearity



The residuals-versus-fitted plot did not show a strong systematic curved pattern. There was no obvious major violation of linearity.



\### Constant Variance



The residuals-versus-fitted plot showed variation in the spread of residuals across fitted values. This suggests some departure from the constant-variance assumption.



\### Influential Observations



\- Maximum Cook's distance: \*\*0.0838\*\*

\- Observations with Cook's distance > 4/n: \*\*30\*\*



These observations were treated as diagnostic flags rather than automatically removed.



No observations were removed solely because they appeared influential or extreme, consistent with the preregistered analysis plan.



\## 6. Interpretation



The primary analysis estimated a small positive association between weekly study time and final mathematics grade after accounting for previous failures and absences.



However, the association was not statistically significant:



\*\*beta = 0.2158, 95% CI \[-0.2976, 0.7292], p = 0.4091.\*\*



The categorical robustness analysis produced the same overall conclusion, with no studytime category showing a statistically significant difference from the reference category.



Therefore, this analysis does not provide sufficient evidence that greater weekly study time is associated with higher final mathematics grades in this sample after accounting for failures and absences.



The results should not be interpreted as proof that study time has no effect. The analysis estimates an association within this dataset and is subject to the limitations of the observational study design and model assumptions.



\## 7. Limitations



The regression diagnostics indicated departures from residual normality and some evidence of non-constant variance.



The study is observational, so the estimated association should not be interpreted as a causal effect of increasing study time.



The dataset also represents the students included in the UCI Student Performance dataset and may not generalize to all student populations.



\## 8. Deviations



No deviations from the preregistered primary analysis were made.



The primary regression model was retained despite the diagnostic findings.



No post-result transformations, outlier removals, or changes to the primary model were introduced to improve statistical results.



Any exploratory analysis not specified in the preregistration should be clearly labeled as exploratory and should not replace the preregistered primary analysis.



\## 9. Reproducibility



The project includes:



\- Research preregistration

\- Reproducible Python environment lockfile

\- Raw dataset

\- Processed analysis dataset

\- Real-data validation script

\- Primary analysis script

\- Categorical robustness analysis

\- Diagnostic analysis

\- Synthetic pipeline validation

\- Version-controlled Git history



The processed analysis dataset was generated reproducibly from the raw dataset using the analysis pipeline.


