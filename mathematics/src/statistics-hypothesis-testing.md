---
title: Hypothesis Testing
---

[Back to index](index.html)

---
# Statistics
## Hypothesis Testing

Hypothesis testing is a fundamental concept in statistics used to make inferences or draw conclusions about a population based on sample data. Here’s an explanation of the key components and steps involved in hypothesis testing:

### Key Components:
1. **Null Hypothesis (H0)**: The default assumption or statement that there is no effect or difference. It is what you aim to test against.
  
2. **Alternative Hypothesis (H1 or Ha)**: The statement that challenges the null hypothesis, indicating the presence of an effect or difference.

3. **Test Statistic**: A standardized value calculated from sample data, used to determine whether to reject the null hypothesis. Common test statistics include the Z-score, t-score, chi-square statistic, etc.

4. **Significance Level (α)**: The threshold for determining whether a result is statistically significant. Common choices are 0.05, 0.01, and 0.10.

5. **P-Value**: The probability of obtaining a test statistic at least as extreme as the one observed, assuming that the null hypothesis is true.

6. **Critical Value**: A value that defines the boundary for the rejection region. If the test statistic exceeds this value, the null hypothesis is rejected.

### Steps in Hypothesis Testing:

1. **State the Hypotheses**:
    - Null Hypothesis (H0): Example: H0: μ = μ0 (the population mean is equal to some specified value μ0).
    - Alternative Hypothesis (H1): Example: H1: μ ≠ μ0 (the population mean is not equal to μ0).

2. **Choose the Significance Level (α)**:
    - Common significance levels are 0.05, 0.01, or 0.10.

3. **Select the Appropriate Test and Calculate the Test Statistic**:
    - Choose based on the type of data and distribution (e.g., Z-test, t-test, chi-square test).
    - Calculate the test statistic using sample data.

4. **Determine the Critical Value or P-Value**:
    - For a critical value approach, find the critical value from statistical tables (e.g., Z-table, t-table).
    - For a p-value approach, calculate the p-value for the observed test statistic.

5. **Make the Decision**:
    - **Critical Value Approach**: Compare the test statistic to the critical value.
      - If it falls in the rejection region, reject H0.
      - If it doesn't, fail to reject H0.
    - **P-Value Approach**: Compare the p-value to the significance level.
      - If p-value ≤ α, reject H0.
      - If p-value > α, fail to reject H0.

6. **Draw Conclusions**:
    - Based on the decision, conclude whether there is sufficient evidence to support the alternative hypothesis.

### Example:
Suppose you want to test whether a new drug has an effect on blood pressure.

1. **State the Hypotheses**:
    - H0: The drug has no effect (mean change in blood pressure = 0).
    - H1: The drug has an effect (mean change in blood pressure ≠ 0).

2. **Choose Significance Level**: α = 0.05.

3. **Select Test and Calculate Test Statistic**: Assume we use a t-test, and from the sample data, we calculate a t-statistic of 2.5.

4. **Determine Critical Value or P-Value**:
    - Using a t-table for the corresponding degrees of freedom, we find the critical t-value for a two-tailed test at α = 0.05 is approximately ±2.0.
    - Or, calculate the p-value corresponding to a t-statistic of 2.5.

5. **Make the Decision**:
    - **Critical Value Approach**: Since 2.5 > 2.0, reject H0.
    - **P-Value Approach**: If the p-value < 0.05, reject H0.

6. **Draw Conclusions**:
    - There is sufficient evidence at the 0.05 level to conclude that the new drug has an effect on blood pressure.

Hypothesis testing provides a structured framework for making data-driven decisions and assessing whether observed patterns are likely due to random variation or a true effect.

---
[Back to index](index.html)
