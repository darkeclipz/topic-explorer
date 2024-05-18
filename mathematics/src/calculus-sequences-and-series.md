---
title: Sequences and Series
---

[Back to index](index.html)

---
# Calculus
## Sequences and Series

Sequences and series are fundamental concepts in calculus and higher mathematics. They are essential for understanding various mathematical phenomena and for the analysis of functions and structures. Here's a detailed explanation of each:

### Sequences
#### Definition
A sequence is an ordered list of numbers written in a definite order. These numbers are called the terms of the sequence, and they can follow various rules.

#### Types of Sequences
1. **Arithmetic Sequence**:
   - Each term after the first is obtained by adding a constant difference, \(d\), to the previous term.
   - General form: \(a_n = a_1 + (n-1)d\), where \(a_n\) is the \(n\)-th term, and \(a_1\) is the first term.

2. **Geometric Sequence**:
   - Each term after the first is obtained by multiplying the previous term by a constant ratio, \(r\).
   - General form: \(a_n = a_1 \cdot r^{(n-1)}\)

3. **Fibonacci Sequence**:
   - Each term after the first two is the sum of the two preceding terms.
   - \(F_n = F_{n-1} + F_{n-2}\) with initial terms usually \(F_0 = 0\) and \(F_1 = 1\).

#### Convergence of Sequences
A sequence converges if the terms approach a specific value, called the limit, as \(n\) approaches infinity.

- A sequence \(\{a_n\}\) converges to \(L\) if, for every \(\epsilon > 0\), there exists a natural number \(N\) such that for all \(n \geq N\), \(|a_n - L| < \epsilon\).

### Series
#### Definition
A series is the sum of the terms of a sequence. More formally, if \(\{a_n\}\) is a sequence, then the series associated with it is expressed as:

\[ S = a_1 + a_2 + a_3 + \cdots + a_n + \cdots \]

#### Types of Series
1. **Arithmetic Series**:
   - The sum of the terms in an arithmetic sequence.
   - Sum of the first \(n\) terms: \(S_n = \frac{n}{2} (2a_1 + (n - 1)d)\)

2. **Geometric Series**:
   - The sum of the terms in a geometric sequence.
   - Sum of the first \(n\) terms: \(S_n = a_1 \frac{1 - r^n}{1 - r}\) for \(r \neq 1\)
   - Sum of an infinite geometric series (for \(|r| < 1\): \(S = \frac{a_1}{1 - r}\)

#### Convergence of Series
A series converges if the sequence of its partial sums converges to a particular value. 

- Partial sum of series: \(S_n = \sum_{i=1}^{n} a_i\)
- The series \(\sum_{i=1}^{\infty} a_i\) converges to \(S\) if the limit \(\lim_{n \to \infty} S_n = S\)

#### Tests for Convergence:
1. **n-th Term Test**:
   - If \(\lim_{n \to \infty} a_n \neq 0\), the series \(\sum a_n\) diverges.
   
2. **Integral Test**:
   - Relates the convergence of a series to an improper integral. If \(\int_{1}^{\infty} f(x) dx\) converges (or diverges), so does \(\sum f(n)\).
   
3. **Comparison Test**:
   - Compare \(\sum a_n\) with \(\sum b_n\). If \(0 \leq a_n \leq b_n\) and \(\sum b_n\) converges, then \(\sum a_n\) converges.

4. **Ratio Test**:
   - Evaluate \(\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = L\):
     - \(L < 1\), series converges.
     - \(L > 1\) or \(L\) is infinite, series diverges.
     - \(L = 1\), test is inconclusive.

5. **Root Test**:
   - Evaluate \(\lim_{n \to \infty} \sqrt[n]{|a_n|} = L\):
     - \(L < 1\), series converges.
     - \(L > 1\) or \(L\) is infinite, series diverges.
     - \(L = 1\), test is inconclusive.

#### Power Series
A power series is a series of the form:

\[ \sum_{n=0}^{\infty} c_n (x - a)^n \]

where \(c_n\) are coefficients and \(a\) is the center of the series. The series converges within a certain radius (the radius of convergence).

### Conclusion
Sequences and series are integral in advanced mathematics and calculus, forming the basis for further study in mathematical analysis, integration, and function approximation techniques. Understanding these concepts is crucial for a deeper grasp of many mathematical and scientific fields.


---
[Back to index](index.html)
