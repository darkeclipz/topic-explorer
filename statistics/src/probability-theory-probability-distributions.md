---
title: Probability Distributions
---

[Back to index](index.html)

---
# Probability Theory
## Probability Distributions

Probability distributions are essential concepts in probability theory and statistics, and they describe how the values of a random variable are distributed. They provide a function that gives the probabilities of occurrence of different possible outcomes in an experiment. Here are some key aspects to understand about probability distributions:

### Types of Probability Distributions

1. **Discrete Probability Distributions**:
    - Applicable to discrete random variables (variables that take on a finite or countable number of values).
    - **Examples**:
        - **Binomial Distribution**: Describes the number of successes in a fixed number of independent Bernoulli trials (e.g., flipping a coin a fixed number of times).
        - **Poisson Distribution**: Describes the number of events occurring within a fixed interval of time or space, provided these events happen with a known constant mean rate and independently of the time since the last event (e.g., number of emails received in an hour).

2. **Continuous Probability Distributions**:
    - Applicable to continuous random variables (variables that take on an infinite number of possible values).
    - **Examples**:
        - **Normal Distribution**: Often referred to as the bell curve due to its shape, it describes how the values of a variable are distributed around the mean. It is characterized by its mean (μ) and standard deviation (σ).
        - **Exponential Distribution**: Describes the time between events in a Poisson process (e.g., the time between arrivals of customers at a service point).

### Key Characteristics and Functions

1. **Probability Mass Function (PMF)** for Discrete Distributions:
    - Defines the probability that a discrete random variable is exactly equal to some value.
    - **Example (Binomial Distribution)**: 
        \[
        P(X = k) = \binom{n}{k} p^k (1-p)^{n-k} \, \text{for} \, k = 0, 1, 2, \ldots, n
        \]
        where \( n \) is the number of trials, \( k \) is the number of successes, and \( p \) is the probability of success on a single trial.

2. **Probability Density Function (PDF)** for Continuous Distributions:
    - Describes the probability of the random variable falling within a particular range of values, as opposed to taking any one value.
    - **Example (Normal Distribution)**:
        \[
        f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
        \]
        where \( \mu \) is the mean and \( \sigma \) is the standard deviation.

3. **Cumulative Distribution Function (CDF)**:
    - Describes the probability that a random variable will take a value less than or equal to a specific value.
    - For a discrete random variable, it is the sum of the PMF values.
    - For a continuous random variable, it is the integral of the PDF.
    - CDF for any random variable \( X \), \( F(x) = P(X \leq x) \).

### Moments of Distributions

1. **Mean (Expected Value)**:
    - The average or central value of a set of values.
    - Discrete: \( E(X) = \sum_{x} x \cdot P(X = x) \)
    - Continuous: \( E(X) = \int_{-\infty}^{\infty} x \cdot f(x) \, dx \)

2. **Variance**:
    - Measures the spread or dispersion of a set of values.
    - Discrete: \( \text{Var}(X) = \sum_{x} (x - E(X))^2 \cdot P(X = x) \)
    - Continuous: \( \text{Var}(X) = \int_{-\infty}^{\infty} (x - E(X))^2 \cdot f(x) \, dx \)

### Importance and Applications

- Probability distributions are used in a wide range of fields from finance and economics to engineering and the natural sciences. They provide the basis for statistical inference, allowing us to make predictions, conduct hypothesis tests, and estimate parameters.

Understanding and working with different types of probability distributions allows statisticians and data scientists to model and interpret real-world phenomena effectively.

---
[Back to index](index.html)
