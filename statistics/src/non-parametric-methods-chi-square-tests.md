---
title: Chi-Square Tests
---

[Back to index](index.html)

---
# Non-Parametric Methods
## Chi-Square Tests

Chi-Square tests are a set of non-parametric statistical tests that are used to determine if there is a significant association between categorical variables or if the observed frequencies of events differ significantly from expected frequencies. There are two main types of Chi-Square tests:

### 1. Chi-Square Test of Independence
The Chi-Square Test of Independence is used to determine whether there is a significant association between two categorical variables in a contingency table. 

**Steps for conducting Chi-Square Test of Independence:**

1. **State the Hypotheses:**
   - Null Hypothesis (\(H_0\)): The two variables are independent (no association).
   - Alternative Hypothesis (\(H_A\)): The two variables are dependent (there is an association).

2. **Collect and Organize Data:**
   - Construct a contingency table with the observed frequencies.

3. **Calculate the Expected Frequencies:**
   - Use the formula: \[
   E_{ij} = \frac{(Row \, Total_i) \times (Column \, Total_j)}{Grand \, Total}
   \]
   
4. **Compute the Chi-Square Statistic:**
   - Use the formula: \[
   \chi^2 = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}}
   \]
   where \(O_{ij}\) is the observed frequency and \(E_{ij}\) is the expected frequency.

5. **Determine the Degrees of Freedom (df):**
   - Calculate the degrees of freedom using the formula: \[
   df = (Number \, of \, Rows - 1) \times (Number \, of \, Columns - 1)
   \]

6. **Compare to the Chi-Square Distribution:**
   - Compare the Chi-Square statistic to the critical value from the Chi-Square distribution table at the desired significance level (e.g., 0.05) and check the corresponding p-value.

7. **Make a Decision:**
   - If the Chi-Square statistic is greater than the critical value, or if the p-value is less than the significance level, reject the null hypothesis.

**Example Application:**
Suppose you want to see if there's an association between gender (male, female) and preference for a new product (like, dislike). You would collect data, put it into a contingency table, calculate the expected frequencies, compute the Chi-Square statistic, and compare against the Chi-Square distribution.

### 2. Chi-Square Goodness-of-Fit Test
The Chi-Square Goodness-of-Fit Test is used to determine if a sample data matches an expected distribution.

**Steps for conducting Chi-Square Goodness-of-Fit Test:**

1. **State the Hypotheses:**
   - Null Hypothesis (\(H_0\)): The observed frequencies match the expected frequencies.
   - Alternative Hypothesis (\(H_A\)): The observed frequencies do not match the expected frequencies.

2. **Collect and Organize Data:**
   - List the observed frequencies for each category.

3. **Define the Expected Frequencies:**
   - Specify the expected frequencies based on a given distribution or proportion.

4. **Compute the Chi-Square Statistic:**
   - Use the same formula as above: \[
   \chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}
   \]
   where \(O_i\) is the observed frequency and \(E_i\) is the expected frequency for each category.

5. **Determine the Degrees of Freedom (df):**
   - Calculate the degrees of freedom using the formula: \[
   df = (Number \, of \, Categories - 1)
   \]

6. **Compare to the Chi-Square Distribution:**
   - Compare the Chi-Square statistic to the critical value from the Chi-Square distribution table at the desired significance level and check the p-value.

7. **Make a Decision:**
   - If the Chi-Square statistic is greater than the critical value, or if the p-value is less than the significance level, reject the null hypothesis.

**Example Application:**
Suppose you roll a six-sided die 60 times and want to test whether the die is fair. You would calculate the expected frequency (10 rolls per face if fair), compare to observed frequencies, compute the Chi-Square statistic, and compare it to the Chi-Square distribution.

### Important Considerations:
- **Data Requirements:** Chi-Square tests require a sufficiently large sample size to ensure accurate results. Each expected frequency should ideally be 5 or more.
- **Assumptions:** The Chi-Square test assumes that the data is a random sample and that the categories are mutually exclusive.

Chi-Square tests are widely used in various fields such as biology, social sciences, economics, and marketing to analyze categorical data and test hypotheses.

---
[Back to index](index.html)
