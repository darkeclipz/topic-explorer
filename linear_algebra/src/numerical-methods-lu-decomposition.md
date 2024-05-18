---
title: LU Decomposition
---

[Back to index](index.html)

---
# Numerical Methods
## LU Decomposition

LU Decomposition is a numerical method used to solve systems of linear equations, find the inverse of a matrix, and compute the determinant of a matrix. The key idea behind LU Decomposition is to factorize a given square matrix \( A \) into two simpler matrices: a lower triangular matrix \( L \) and an upper triangular matrix \( U \). This makes subsequent calculations more straightforward and computationally efficient.

Here’s the basic breakdown of LU Decomposition:

1. **Definition:**
   Given a square matrix \( A \), LU Decomposition finds matrices \( L \) and \( U \) such that:
   \[
   A = LU
   \]
   where:
   - \( L \) is a lower triangular matrix (all elements above the diagonal are zero).
   - \( U \) is an upper triangular matrix (all elements below the diagonal are zero).

2. **Procedure:**
   The process of LU Decomposition generally involves the following steps:
   - **Forward Elimination:** Transform the matrix \( A \) by eliminating elements below the diagonal to form the upper triangular matrix \( U \).
   - **Forming \( L \):** At the same time, record the multipliers used during the elimination process to form the lower triangular matrix \( L \).

To perform LU Decomposition, follow these steps:

### Step-by-Step Example:

Consider a 3x3 matrix \( A \):
\[
A = \begin{pmatrix}
2 & -1 & -2 \\
-4 & 6 & 3 \\
-4 & -2 & 8
\end{pmatrix}
\]

1. **Initialize \( L \) and \( U \):**
   \[
   L = \begin{pmatrix}
   1 & 0 & 0 \\
   0 & 1 & 0 \\
   0 & 0 & 1 
   \end{pmatrix},
   \quad
   U = \begin{pmatrix}
   2 & -1 & -2 \\
   0 & 0 & 0 \\
   0 & 0 & 0
   \end{pmatrix}
   \]

2. **Eliminate elements below \( U_{11} \):**
   - \( L_{21} = \frac{-4}{2} = -2 \)
   - Multiply the first row of \( U \) by \( -2 \) and add to the second row:
   \[
   U = \begin{pmatrix}
   2 & -1 & -2 \\
   0 & 4 & -1 \\
   0 & 0 & 0 
   \end{pmatrix}
   \]
   Update \( L \):
   \[
   L = \begin{pmatrix}
   1 & 0 & 0 \\
   -2 & 1 & 0 \\
   0 & 0 & 1 
   \end{pmatrix}
   \]

3. **Eliminate elements below \( U_{22} \):**
   - \( L_{31} = \frac{-4}{2} = -2 \)
   - Multiply the first row of \( U \) by \( -2 \) and add to the third row:
   \[
   U = \begin{pmatrix}
   2 & -1 & -2 \\
   0 & 4 & -1 \\
   0 & 0 & 4
   \end{pmatrix}
   \]
   Update \( L \):
   \[
   L = \begin{pmatrix}
   1 & 0 & 0 \\
   -2 & 1 & 0 \\
   -2 & 5 & 1
   \end{pmatrix}
   \]

4. **Finalize:**

Now you have matrices:
\[
L = \begin{pmatrix}
1 & 0 & 0 \\
-2 & 1 & 0 \\
-2 & 5 & 1
\end{pmatrix},
\quad
U = \begin{pmatrix}
2 & -1 & -2 \\
0 & 4 & -1 \\
0 & 0 & 4
\end{pmatrix}
\]

### Applications:
1. **Solving Systems of Equations:**
   To solve \( Ax = b \), where \( A = LU \):
   - Solve \( Ly = b \) for \( y \) using forward substitution.
   - Solve \( Ux = y \) for \( x \) using backward substitution.

2. **Finding the Inverse:**
   If you need to find \( A^{-1} \), rewrite \( A = LU \) and solve \( Ax = I \) column by column.

3. **Computing Determinants:**
   The determinant of \( A \) is the product of the diagonal elements of \( U \):
   \[
   \text{det}(A) = \text{det}(L) \times \text{det}(U) = 1 \times \left(2 \times 4 \times 4 \right)
   \]

LU Decomposition is particularly efficient for large matrices, making it a powerful tool in various numerical and engineering applications.

---
[Back to index](index.html)
