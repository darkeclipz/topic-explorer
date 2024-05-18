---
title: Cramer's Rule
---

[Back to index](index.html)

---
# Systems of Linear Equations
## Cramer's Rule

Cramer's Rule is a mathematical theorem used to solve systems of linear equations with as many equations as unknowns, provided that the system's coefficient matrix is invertible (i.e., it has a non-zero determinant). Here's a detailed explanation:

### Basic Concept

For an \( n \times n \) system of linear equations represented as:
\[ A\mathbf{x} = \mathbf{b} \]
where:
- \( A \) is an \( n \times n \) matrix of coefficients.
- \( \mathbf{x} \) is a column vector of \( n \) unknowns.
- \( \mathbf{b} \) is a column vector of \( n \) constants.

### Cramer's Rule

Cramer's Rule provides a method to find each unknown \( x_i \) by using determinants. The formula for each variable \( x_i \) is given by:

\[ x_i = \frac{\det(A_i)}{\det(A)} \]

Here:
- \( \det(A) \) is the determinant of the original coefficient matrix \( A \).
- \( \det(A_i) \) is the determinant of the matrix \( A \) with its \( i \)-th column replaced by the column vector \( \mathbf{b} \).

### Steps to Apply Cramer's Rule

1. **Compute \( \det(A) \)** - Calculate the determinant of the coefficient matrix \( A \). If \( \det(A) = 0 \), the system either has no unique solution or an infinite number of solutions.

2. **Form the Matrices \( A_i \)** - For each unknown \( x_i \), create a new matrix \( A_i \) by replacing the \( i \)-th column of \( A \) with the vector \( \mathbf{b} \).

3. **Compute \( \det(A_i) \)** - Calculate the determinant of each matrix \( A_i \).

4. **Solve for \( x_i \)** - Use the formula \( x_i = \frac{\det(A_i)}{\det(A)} \) to find the value of each unknown.

### Example

Consider the system of linear equations:
\[
\begin{cases}
a_{11}x_1 + a_{12}x_2 = b_1 \\
a_{21}x_1 + a_{22}x_2 = b_2 \\
\end{cases}
\]

This can be written in matrix form as:
\[ A\mathbf{x} = \mathbf{b} \]

Where:
\[ A = \begin{pmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{pmatrix}, \quad \mathbf{x} = \begin{pmatrix}
x_1 \\
x_2
\end{pmatrix}, \quad \mathbf{b} = \begin{pmatrix}
b_1 \\
b_2
\end{pmatrix} \]

To solve for \( x_1 \):
1. Compute \( \det(A) \):
\[ \det(A) = a_{11}a_{22} - a_{12}a_{21} \]

2. Form \( A_1 \) by replacing the 1st column with \( \mathbf{b} \):
\[ A_1 = \begin{pmatrix}
b_1 & a_{12} \\
b_2 & a_{22}
\end{pmatrix} \]

3. Compute \( \det(A_1) \):
\[ \det(A_1) = b_1a_{22} - b_2a_{12} \]

4. Solve for \( x_1 \):
\[ x_1 = \frac{\det(A_1)}{\det(A)} = \frac{b_1a_{22} - b_2a_{12}}{a_{11}a_{22} - a_{12}a_{21}} \]

Similarly, to solve for \( x_2 \):
1. Form \( A_2 \) by replacing the 2nd column with \( \mathbf{b} \):
\[ A_2 = \begin{pmatrix}
a_{11} & b_1 \\
a_{21} & b_2
\end{pmatrix} \]

2. Compute \( \det(A_2) \):
\[ \det(A_2) = a_{11}b_2 - a_{21}b_1 \]

3. Solve for \( x_2 \):
\[ x_2 = \frac{\det(A_2)}{\det(A)} = \frac{a_{11}b_2 - a_{21}b_1}{a_{11}a_{22} - a_{12}a_{21}} \]

Cramer's Rule is particularly useful for small systems and theoretical purposes, but for larger systems, numerical methods such as Gaussian elimination are usually more efficient.

---
[Back to index](index.html)
