---
title: Kruskal-Wallis Test
---

[Back to index](index.html)

---
# Non-Parametric Methods
## Kruskal-Wallis Test

The Kruskal-Wallis test is a non-parametric method used to determine whether there are statistically significant differences between the medians of three or more independent groups. It is the non-parametric equivalent of the one-way ANOVA, and it is used when the assumptions of the one-way ANOVA are not met, particularly the assumption of normality.

Here’s a detailed explanation of the Kruskal-Wallis Test:

### Key Concepts:
1. **H0 (Null Hypothesis)**: The populations from which the samples originate have the same median.
2. **H1 (Alternative Hypothesis)**: At least one of the populations has a different median.

### Steps to Conduct the Kruskal-Wallis Test:

1. **Combine and Rank Data**:
    - Combine all data from the groups into a single dataset.
    - Assign ranks to the combined data. If there are ties (duplicate values), assign the average of the ranks that these values span.

2. **Sum of Ranks**:
    - Calculate the sum of ranks for each group.

3. **Test Statistic Calculation**:
    - The test statistic for the Kruskal-Wallis test is given by:
      \[
      H = \left( \frac{12}{N(N+1)} \sum \frac{R_i^2}{n_i} \right) - 3(N+1)
      \]
      where:
      - \(N\) = total number of observations across all groups
      - \(R_i\) = sum of the ranks of the \(i\)-th group
      - \(n_i\) = number of observations in the \(i\)-th group

4. **Degrees of Freedom**:
    - The degrees of freedom (df) for the Kruskal-Wallis test is \(k - 1\), where \(k\) is the number of groups.

5. **Compare to Critical Value**:
    - Compare the calculated H value to the critical value from the chi-square distribution table with \(k - 1\) degrees of freedom to determine the significance.

6. **Decision**:
    - If \(H\) is greater than the critical value, reject the null hypothesis (there is a significant difference between the groups' medians).
    - If \(H\) is less than the critical value, do not reject the null hypothesis (no significant difference between the groups' medians).

### Assumptions:

1. **Independence**: Observations within each group must be independent of each other.
2. **Ordinal or Continuous Data**: The test is appropriate for ordinal or continuous data.
3. **Same Shape Distribution**: The distributions of the populations should have the same shape (not necessarily normal) so that differences in central tendency can be inferred directly from differences in ranks.

### Example:

Suppose you have three different groups of plants treated with different fertilizers, and you want to determine whether the height of plants differs significantly across the three groups. You would collect plant height data for each group and perform the Kruskal-Wallis test to determine if there are significant differences in median height across the groups.

### When to Use:

- When you have three or more independent groups.
- When the data violates the assumptions necessary for a one-way ANOVA, particularly normality.
- When dealing with ordinal data or small sample sizes.

The Kruskal-Wallis test is a robust alternative for comparing medians across multiple groups, especially under non-normal conditions, making it a valuable tool in non-parametric statistics.

---
[Back to index](index.html)
