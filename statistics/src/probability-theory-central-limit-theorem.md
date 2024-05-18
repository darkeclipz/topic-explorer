---
title: Central Limit Theorem
---

[Back to index](index.html)

---
# Probability Theory
## Central Limit Theorem

The Central Limit Theorem (CLT) is a fundamental theorem in probability theory and statistics. It states that, given a sufficiently large sample size, the sampling distribution of the sample mean will be normally distributed (i.e., it will approximate a normal distribution), regardless of the original distribution of the population from which the sample is drawn. Here are the key points to understand about the CLT:

### Key Concepts

1. **Population and Sample**:
   - **Population**: The entire set of possible observations.
   - **Sample**: A subset of observations drawn from the population.

2. **Sample Mean**: The average value of the observations in the sample. It is a statistic used to estimate the population mean.

3. **Sampling Distribution**: The probability distribution of a given statistic (e.g., the sample mean) based on a large number of samples drawn from the same population.

### Formal Statement

If \( X_1, X_2, ..., X_n \) are independent and identically distributed (i.i.d.) random variables drawn from any population with a finite mean \( \mu \) and finite variance \( \sigma^2 \), then the sampling distribution of the sample mean \( \bar{X} \) will approach a normal distribution as the sample size \( n \) becomes large. Mathematically, this can be expressed as:

\[ \bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i \]

As \( n \) approaches infinity:

\[ \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \rightarrow N(0,1) \]

Where \( N(0,1) \) denotes the standard normal distribution, with mean 0 and variance 1.

### Implications

1. **Normal Approximation**: For large sample sizes, the sample mean \( \bar{X} \) will be approximately normally distributed even if the underlying population is not normal.

2. **Estimations and Confidence Intervals**: The CLT allows statisticians to make inferences about population parameters (such as the mean) using the normal distribution. This is particularly useful for constructing confidence intervals and conducting hypothesis tests.

### Conditions

1. **Sample Size**: The sample size should be sufficiently large. In practice, a sample size of 30 or more is often considered adequate, although a larger sample size may be required if the population distribution is highly skewed or has heavy tails.

2. **Independence**: The samples must be independent. This means that the selection of one observation should not influence the selection of another.

3. **Identical Distribution**: The random variables should be identically distributed with the same mean and variance.

### Example

Suppose you want to estimate the average height of adult men in a city. You collect a random sample of 100 men and calculate the sample mean height. According to the CLT, if you repeat this process many times (drawing many samples of 100 men each time), the distribution of these sample means will approximate a normal distribution centered around the true population mean height, with a standard error \( \sigma / \sqrt{100} \).

### Conclusion

The Central Limit Theorem is a powerful tool in statistics because it justifies the use of the normal distribution for making probabilistic and statistical inferences about population parameters, even when the underlying population distribution is not normal. This theorem underpins many statistical methods and is essential for understanding how sample statistics relate to population parameters.

---
[Back to index](index.html)
