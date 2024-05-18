---
title: One-Way ANOVA
---

[Back to index](index.html)

---
# ANOVA (Analysis of Variance)
## One-Way ANOVA

One-Way Analysis of Variance (ANOVA) is a statistical method used to compare the means of three or more independent groups to determine if there is a statistically significant difference among them. It helps to understand if the observed differences among group means are likely to have occurred by random chance or if there is an underlying effect caused by some factor.

### Key Concepts:
1. **Null Hypothesis (H0):** The means of all groups are equal (μ1 = μ2 = μ3 = ... = μk).
2. **Alternative Hypothesis (H1):** At least one group mean is different from the others.
3. **Between-Group Variability:** Variation due to the interaction between the samples. This measures how much the group means differ from the overall mean.
4. **Within-Group Variability:** Variation within each group. This measures how much individual observations within each group differ from their respective group means.
5. **F-Statistic:** Ratio of the between-group variability to the within-group variability. Higher values of the F-statistic indicate a greater likelihood that the null hypothesis can be rejected.

### Steps for Performing One-Way ANOVA:
1. **Assumptions Check:**
   - **Normality:** Data in each group should be approximately normally distributed.
   - **Homogeneity of Variances:** Variances among groups should be approximately equal.
   - **Independence:** Observations should be independent of each other.

2. **Calculate Group Means:**
   - Compute the mean for each group as well as the overall mean of all the data combined.

3. **Compute Sums of Squares:**
   - **Total Sum of Squares (SST):** Measures the total variation in the data.
   - **Between-Group Sum of Squares (SSB):** Measures the variation due to the interactions between the groups.
   - **Within-Group Sum of Squares (SSW):** Measures the variation within each group.

4. **Calculate Mean Squares:**
   - **Mean Square Between (MSB):** SSB divided by the degrees of freedom between the groups (k-1, where k is the number of groups).
   - **Mean Square Within (MSW):** SSW divided by the degrees of freedom within the groups (N-k, where N is the total number of observations).

5. **Compute the F-Statistic:**
   - F = MSB / MSW

6. **Determine the P-value:**
   - Compare the computed F-statistic against the F-distribution with appropriate degrees of freedom to find the p-value.

7. **Decision Rule:**
   - If the p-value is less than the significance level (typically 0.05), reject the null hypothesis, indicating that at least one of the group means is significantly different from the others. Otherwise, fail to reject the null hypothesis.

### Example:
Suppose you have test scores from three different teaching methods and you want to see if there is a significant difference in the mean scores among these methods.

1. **Group 1 (Method A):** Scores = [85, 90, 88]
2. **Group 2 (Method B):** Scores = [78, 82, 80]
3. **Group 3 (Method C):** Scores = [92, 95, 93]

**Step-by-Step Calculation:**

- **Means:** Method A = 87.67, Method B = 80, Method C = 93.33
- **Overall Mean:** (85 + 90 + 88 + 78 + 82 + 80 + 92 + 95 + 93) / 9 = 87

**Sum of Squares Calculations:**
- **SSB**: Sum of squared differences between the group means and the overall mean.
- **SSW**: Sum of squared differences within each group.

**ANOVA Table:**
```
Source    |  Sum of Squares  |  Degrees of Freedom  |  Mean Square  |  F
Between   |        SSB       |         k-1          |     MSB       |  F = MSB/MSW
Within    |        SSW       |         N-k          |     MSW       |
Total     |        SST       |         N-1          |               |
```

If the p-value corresponding to the calculated F is less than 0.05, it indicates that the means of test scores from different teaching methods are statistically significantly different.

One-Way ANOVA is robust, effective, and commonly used in various fields such as psychology, education, and business to compare more than two groups at the same time, providing a powerful tool for statistical analysis and decision-making.

---
[Back to index](index.html)
