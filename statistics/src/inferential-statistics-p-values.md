---
title: P-values
---

[Back to index](index.html)

---
# Inferential Statistics
## P-values

Certainly! The p-value is a fundamental concept in inferential statistics used to determine the strength of evidence against the null hypothesis in hypothesis testing. Here’s a detailed explanation:

### What is a P-value?

The p-value is a probability measure that helps you understand whether your observed data would be considered extreme under the assumption that the null hypothesis is true. It essentially answers the question: "If the null hypothesis is true, what is the probability of obtaining a test statistic as extreme as the one observed, or more extreme?"

### Steps in Hypothesis Testing Using P-values:

1. **Formulate Hypotheses:**
    - **Null Hypothesis (H0):** The statement that there is no effect or no difference. It serves as a default or baseline assumption.
    - **Alternative Hypothesis (H1 or Ha):** The statement that there is an effect or a difference.

2. **Select a Significance Level (α):**
    - The significance level is the threshold for deciding whether to reject the null hypothesis. Common choices are 0.05, 0.01, or 0.10.

3. **Conduct the Test and Calculate the Test Statistic:**
    - Depending on the test (e.g., t-test, chi-square test), you will calculate a test statistic from your sample data.

4. **Calculate the P-value:**
    - The p-value is computed from the test statistic and it tells you the probability of obtaining a result at least as extreme as the one observed, given that the null hypothesis is true.

5. **Compare the P-value to the Significance Level (α):**
    - **If p-value ≤ α:** Reject the null hypothesis (H0). There is enough evidence to support the alternative hypothesis (H1).
    - **If p-value > α:** Do not reject the null hypothesis (H0). There isn't enough evidence to support the alternative hypothesis (H1).

### Interpretation of P-values:

- **Small P-values (≤ α):** Indicate strong evidence against the null hypothesis, so you reject the null hypothesis.
- **Large P-values (> α):** Indicate weak evidence against the null hypothesis, so you fail to reject the null hypothesis.

### Important Considerations:

- **P-value is not the probability that H0 is true:** A common misconception is that the p-value is the probability that the null hypothesis is true. Instead, it is the probability of the observed data (or more extreme) under the assumption that H0 is true.
- **P-value does not measure effect size:** A small p-value indicates statistical significance, but it does not convey the magnitude of the effect or its practical significance.
- **Interpretation depends on context:** A statistically significant result (small p-value) does not inherently mean the result is practically significant or important.
- **Multiple Comparisons:** When conducting multiple hypothesis tests, the risk of Type I error (false positive) increases. Adjustments (e.g., Bonferroni correction) may be necessary.

### Example:

Suppose you are testing whether a new drug is more effective than a placebo. Your null hypothesis (H0) is that the new drug has no effect compared to the placebo. After conducting a clinical trial, you obtain a test statistic and a corresponding p-value of 0.03. If you set your significance level (α) at 0.05, you would reject the null hypothesis because 0.03 < 0.05. This suggests that there is significant evidence against the null hypothesis, implying the new drug has an effect.

In summary, the p-value is a key component in hypothesis testing that helps determine whether to reject the null hypothesis based on the observed data. It quantifies the strength of evidence against the null hypothesis, guiding researchers in making informed decisions.

---
[Back to index](index.html)
