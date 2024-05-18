---
title: Random Variables
---

[Back to index](index.html)

---
# Probability Theory
## Random Variables

A random variable is a fundamental concept in probability theory that maps the outcomes of a random experiment to numerical values. It essentially allows us to quantify the results of probabilistic events.

**Types of Random Variables:**

1. **Discrete Random Variables:** These take on a countable number of distinct values. For example, the number of heads when flipping three coins.
  
    - **Probability Mass Function (PMF):** Defines the probability that a discrete random variable is exactly equal to some value. For example, the PMF for rolling a fair six-sided die is \( P(X = x) = \frac{1}{6} \) for \( x = 1, 2, 3, 4, 5, 6 \).

2. **Continuous Random Variables:** These take on an infinite number of possible values. For example, the exact height of students in a class.
  
    - **Probability Density Function (PDF):** Describes the likelihood of the random variable taking on a range of values, rather than a specific value. For example, the height of students might be modeled by a normal distribution with a specific mean and standard deviation.

**Key Concepts:**

1. **Cumulative Distribution Function (CDF):** For both discrete and continuous random variables, the CDF is a function \( F(x) = P(X \leq x) \) that gives the probability that the random variable \( X \) is less than or equal to \( x \). It provides a complete description of the distribution of the random variable.

2. **Expected Value:** The long-term average value of the random variable, denoted as \( E(X) \). For a discrete random variable, it is computed as:
   \[
   E(X) = \sum_{x} x \cdot P(X = x)
   \]
   For a continuous random variable, it is computed as:
   \[
   E(X) = \int_{-\infty}^{\infty} x \cdot f(x) \, dx
   \]
   where \( f(x) \) is the PDF of \( X \).

3. **Variance and Standard Deviation:** These measure the spread or dispersion of the random variable around its mean. The variance is denoted as \( \text{Var}(X) \) and is given by:
   \[
   \text{Var}(X) = E[(X - E(X))^2]
   \]
   The standard deviation is the square root of the variance.

4. **Moments:** Moments are quantitative measures related to the shape of the distribution's graph. The \( n \)-th moment of a random variable about the origin is \( E(X^n) \), and the \( n \)-th moment about the mean (central moment) is \( E[(X - E(X))^n] \).

**Examples of Random Variables:**

1. **Bernoulli Random Variable:** This is a simple type with only two outcomes, usually denoted as 1 (success) and 0 (failure) with a single probability parameter \( p \).

2. **Binomial Random Variable:** Represents the number of successes in a fixed number of \( n \) independent Bernoulli trials.

3. **Normal (Gaussian) Random Variable:** A continuous random variable with a bell-shaped probability density function, defined by its mean \( \mu \) and standard deviation \( \sigma \).

4. **Exponential Random Variable:** Used to model the time between events in a Poisson process, typically defined by its rate parameter \( \lambda \).

Understanding random variables is crucial for modeling and analyzing real-world scenarios in fields such as finance, engineering, and natural sciences. They provide the foundation for both theoretical and applied statistics.

---
[Back to index](index.html)
