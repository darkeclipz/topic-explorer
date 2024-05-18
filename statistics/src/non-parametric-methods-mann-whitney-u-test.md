---
title: Mann-Whitney U Test
---

[Back to index](index.html)

---
# Non-Parametric Methods
## Mann-Whitney U Test

The Mann-Whitney U Test, also known as the Wilcoxon rank-sum test, is a non-parametric test used to determine whether there is a significant difference between the distributions of two independent groups. Unlike parametric tests, it doesn't assume that the data comes from a particular distribution, such as the normal distribution, making it useful when dealing with non-normally distributed data or ordinal data.

### Key Concepts and Steps in the Mann-Whitney U Test:

1. **Hypotheses:**
   - **Null Hypothesis (H0):** The distributions of the two groups are identical. This implies that the probabilities of observing any value from one group are equal to the probabilities of observing values from the other group.
   - **Alternative Hypothesis (H1):** The distributions of the two groups are not identical.

2. **Assumptions:**
   - The observations are independent within and across groups.
   - The measurement scale is at least ordinal.

3. **Procedure:**
   1. **Combine and Rank Data:**
      - Combine data from both groups.
      - Rank the combined data from smallest to largest. In case of ties, assign the average rank to tied values.

   2. **Calculate U Values:**
      - Calculate the sum of ranks for each group (\( R1 \) and \( R2 \)).
      - Calculate the test statistic \( U \) for both groups:
        \[ U1 = n1 \cdot n2 + \frac{n1(n1 + 1)}{2} - R1 \]
        \[ U2 = n1 \cdot n2 + \frac{n2(n2 + 1)}{2} - R2 \]
        where \( n1 \) and \( n2 \) are the sample sizes for Group 1 and Group 2, respectively.
      - The smaller value between \( U1 \) and \( U2 \) is the test statistic \( U \).

4. **Determine Significance:**
   - Compare the calculated \( U \) value with the critical value from the Mann-Whitney U distribution table at a chosen significance level (alpha, usually 0.05).
   - Alternatively, compute the p-value (often available from statistical software) and compare it to the significance level.

5. **Conclusion:**
   - If \( U \) is less than or equal to the critical value (or if the p-value is less than the significance level), reject the null hypothesis. This implies that there is a significant difference between the two groups.
   - If \( U \) is greater than the critical value (or if the p-value is greater than the significance level), fail to reject the null hypothesis. This implies no significant difference between the two groups.

### Example:

Suppose we have two groups of students who took different teaching methods for learning math, and we want to compare their test scores.

- **Group A (Method 1):** 85, 90, 88
- **Group B (Method 2):** 78, 82, 85, 88

1. **Rank the combined data:**
   - Combined Scores: 78(1), 82(2), 85(3.5, 3.5), 85(3.5, 3.5), 88(6, 6), 90(7)
   - (Here, 85 has tied ranks, and 88 has tied ranks, so average ranks are used).

2. **Sum of ranks:**
   - Sum of ranks for Group A (\( R1 \)): 3.5 + 7 + 6 = 16.5
   - Sum of ranks for Group B (\( R2 \)): 1 + 2 + 3.5 + 6 = 12.5

3. **Calculate U:**
   - \( n1 = 3 \) (Group A)
   - \( n2 = 4 \) (Group B)
   - Calculate \( U \) values:
     \[ U1 = 3 \cdot 4 + \frac{3(3 + 1)}{2} - 16.5 = 12 + 6 - 16.5 = 1.5 \]
     \[ U2 = 3 \cdot 4 + \frac{4(4 + 1)}{2} - 12.5 = 12 + 10 - 12.5 = 9.5 \]
   - The smaller U value is 1.5.

4. **Determine significance:**
   - Check the U value in a Mann-Whitney U table or use statistical software to find the p-value.
   - If the computed U (1.5) is less than the critical value at the chosen significance level, conclude that there is a significant difference between the groups.

The Mann-Whitney U test is an important tool for statistical analysis when the data does not meet the assumptions of parametric tests.

---
[Back to index](index.html)
