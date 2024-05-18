---
title: Wilcoxon Signed-Rank Test
---

[Back to index](index.html)

---
# Non-Parametric Methods
## Wilcoxon Signed-Rank Test

The Wilcoxon Signed-Rank Test is a non-parametric statistical test used to compare two related samples, matched samples, or repeated measurements on a single sample. The primary purpose of the test is to determine whether their population mean ranks differ (i.e., to test the median differences of paired observations).

### Key Concepts

1. **Non-parametric Nature**: Unlike parametric tests, the Wilcoxon Signed-Rank Test does not assume that the data are normally distributed. This makes it suitable for data that do not meet the assumptions of normality required by parametric tests such as the paired t-test.

2. **Paired Data**: The test is applied to paired data, meaning that each subject or entity is measured twice, resulting in two related measurements for each subject.

3. **Ranks**: Instead of comparing the actual values, the test compares the ranks of the differences between the paired observations.

### Steps to Perform the Wilcoxon Signed-Rank Test

1. **Calculate Differences**: For each pair of measurements, calculate the difference (d) between the two observations.

2. **Remove Zero Differences**: If any pairs have differences that are zero, they are discarded, as they do not contribute to the test.

3. **Rank the Differences**: Rank the absolute values of the differences. Assign ranks starting from 1 for the smallest absolute difference to n for the largest absolute difference. In the case of ties (identical absolute differences), assign the average of the ranks that the ties would have occupied.

4. **Assign Signs to the Ranks**: Assign a positive or negative sign to each rank based on the sign of the corresponding difference.

5. **Sum the Ranks**: Separate the ranks into positive and negative and then sum them. Let \( W^+ \) be the sum of ranks for the positive differences and \( W^- \) be the sum for the negative differences.

6. **Calculate the Test Statistic**: The test statistic is \( W = \min(W^+, W^-) \).

7. **Determine the P-Value or Critical Value**: Compare the test statistic to a critical value from the Wilcoxon signed-rank table or compute the p-value if using statistical software.

### Hypotheses

- **Null Hypothesis (\( H_0 \))**: The median difference between the pairs is zero. In other words, there is no significant difference between the paired observations.
- **Alternative Hypothesis (\( H_1 \))**: The median difference between the pairs is not zero.

### Interpretation

- If the p-value is less than the chosen significance level (e.g., 0.05), you reject the null hypothesis, concluding that there is a significant difference between the paired samples.
- If the p-value is greater than the significance level, you fail to reject the null hypothesis, suggesting that there is no significant difference between the paired samples.

### When to Use the Wilcoxon Signed-Rank Test

- **Non-normal Data**: When the assumption of normality is violated.
- **Ordinal Data**: When data are ordinal or ranked.
- **Small Sample Sizes**: When sample sizes are small, and the normality assumption cannot be confidently applied.

### Example

Suppose you have a group of patients' blood pressure measurements before and after a treatment. To see if the treatment had a significant effect, you can use the Wilcoxon Signed-Rank Test on the differences in blood pressure measurements before and after the treatment.

In summary, the Wilcoxon Signed-Rank Test is a useful non-parametric method for analyzing paired sample data, especially when the assumptions required by parametric tests are not met.

---
[Back to index](index.html)
