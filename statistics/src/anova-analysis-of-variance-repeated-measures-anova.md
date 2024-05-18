---
title: Repeated Measures ANOVA
---

[Back to index](index.html)

---
# ANOVA (Analysis of Variance)
## Repeated Measures ANOVA

Repeated Measures ANOVA is a statistical technique used to analyze data where the same subjects are measured multiple times under different conditions or over different time points. This type of ANOVA is particularly useful in situations where you want to determine if there are statistically significant differences in means across multiple conditions or time points within the same group of subjects.

### Key Concepts

1. **Within-Subjects Design**: In a repeated measures design, the same subjects participate in every condition of the experiment, allowing researchers to control for inter-subject variability. This design increases statistical power because the variability due to individual differences is removed.

2. **Factor and Levels**: The repeated measures factor refers to the different conditions or time points being tested. Each condition or time point is called a level of the factor.

3. **Sphericity**: One crucial assumption of Repeated Measures ANOVA is sphericity, which means the variances of the differences between all combinations of conditions (levels) should be the same. If this assumption is violated, it can lead to incorrect conclusions.

4. **Subjects as Their Own Control**: Since the same subjects are measured under all conditions, each subject serves as their own control. This reduces the error variance associated with individual differences, enhancing statistical power.

### Steps in Repeated Measures ANOVA

1. **Formulate the Hypotheses**:
   - Null Hypothesis (\(H_0\)): There are no differences in the means across the different conditions or time points.
   - Alternative Hypothesis (\(H_A\)): There are significant differences in the means across the different conditions or time points.

2. **Check Assumptions**:
   - **Normality**: The data should be approximately normally distributed.
   - **Sphericity**: This can be tested using Mauchly's test for sphericity. If sphericity is violated, adjustments like Greenhouse-Geisser or Huynh-Feldt corrections can be applied.

3. **Calculate the F-Statistic**:
   - The F-statistic in Repeated Measures ANOVA compares the variance explained by the conditions to the variance within the conditions (residual variance).

4. **Compare to Critical Value**:
   - If the calculated F-statistic is greater than the critical value from the F-distribution table, or if the p-value is less than the chosen significance level (commonly 0.05), we reject the null hypothesis.

5. **Post-Hoc Tests** (if needed):
   - If you find a significant effect, you may need to conduct post-hoc tests to determine which specific conditions are different from each other.

### Example Scenario

Imagine a scenario where researchers want to test the effect of different types of diets on weight loss. The same group of participants follows each diet for a specific period, and their weights are measured at the end of each diet period. The repeated measures ANOVA can be used to determine if there are significant weight differences across the different diet conditions.

### Advantages

1. **Increased Statistical Power**: By controlling for individual variability, repeated measures designs often provide more statistical power.
2. **Efficiency and Economy**: Fewer subjects are needed since the same subjects provide multiple measurements.

### Disadvantages

1. **Carryover Effects**: The effect of a previous condition can carry over to subsequent conditions.
2. **Sphericity Violation**: Violations of the sphericity assumption can complicate the analysis.

### Conclusion

Repeated Measures ANOVA is a powerful tool for analyzing experiments where the same subjects experience multiple conditions. By controlling for individual variability, it enhances the ability to detect true differences between conditions, provided that the key assumptions are met.

---
[Back to index](index.html)
