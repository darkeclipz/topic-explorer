---
title: LU Decomposition
---

[Back to index](index.html)

---
# Systems of Linear Equations
## LU Decomposition

LU Decomposition is a method used to solve systems of linear equations, find the determinant of a matrix, and compute the inverse of a matrix. It involves decomposing a given square matrix \( A \) into the product of two matrices: a lower triangular matrix \( L \) and an upper triangular matrix \( U \).

### Steps for LU Decomposition

1. **Decompose Matrix \( A \)**:
    - For a given matrix \( A \), decompose it such that \( A = LU \), where \( L \) is a lower triangular matrix and \( U \) is an upper triangular matrix.
    - \( L \) will have 1s on its diagonal and values \( l_{ij} \) below the diagonal, while \( U \) will have values \( u_{ij} \) above the diagonal and on the diagonal.

2. **Forward Elimination (Decompose into \( L \) and \( U \))**:
    - Start with the first row of \( U \) and use it to form \( L \). The (1,1) entry of \( A \) becomes the (1,1) entry of \( U \), and so on.
    - Subtract multiples of the first row from the subsequent rows to form zeros below the diagonal in \( U \), updating \( L \) accordingly.

3. **Solve for \( y \) in \( Ly = b \) (Forward Substitution)**:
    - Once \( A \) is decomposed into \( L \) and \( U \), substitute \( A = LU \) into the system \( Ax = b \) to obtain \( LUx = b \).
    - Let \( Ux = y \), which transforms the system into two simpler systems: \( Ly = b \) and \( Ux = y \).
    - Solve \( Ly = b \) using forward substitution.

4. **Solve for \( x \) in \( Ux = y \) (Back Substitution)**:
    - After finding \( y \) from the previous step, solve \( Ux = y \) using back substitution.

### Example

Let \( A \) be a \( 3 \times 3 \) matrix:
\[ A = \begin{pmatrix}
2 & 3 & 1 \\
4 & 7 & 9 \\
6 & 9 & 8
\end{pmatrix} \]

Find \( L \) and \( U \) such that \( A = LU \).

1. **Initialization**:
   - \( L = \begin{pmatrix}
1 & 0 & 0 \\
l_{21} & 1 & 0 \\
l_{31} & l_{32} & 1
  \end{pmatrix} \)
   - \( U = \begin{pmatrix}
2 & 3 & 1 \\
0 & u_{22} & u_{23} \\
0 & 0 & u_{33}
  \end{pmatrix} \)

2. **Decomposition**:
   - The first row remains the same for \( U \).
   - Eliminate the first column entries below the diagonal using the appropriate multipliers from \( L \).
    \[
    l_{21} = \frac{a_{21}}{a_{11}} = \frac{4}{2} = 2
    \]
    \[
    l_{31} = \frac{a_{31}}{a_{11}} = \frac{6}{2} = 3
    \]

   - Update the second row:
    \[
    U_{2,2} = a_{22} - l_{21} \times a_{12} = 7 - 2 \times 3 = 1
    \]
    \[
    U_{2,3} = a_{23} - l_{21} \times a_{13} = 9 - 2 \times 1 = 7
    \]

   - Update the third row using the same elimination process:
    \[
    l_{32} = \frac{a_{32} - l_{31} \times a_{12}}{u_{22}} = \frac{9 - 3 \times 3}{1} = 0
    \]
    \[
    U_{3,3} = a_{33} - l_{31} \times a_{13} - l_{32} \times u_{23} = 8 - 3 \times 1 = 5
    \]

Thus, the decomposed matrices are:
\[ L = \begin{pmatrix}
1 & 0 & 0 \\
2 & 1 & 0 \\
3 & 0 & 1
\end{pmatrix} \]
\[ U = \begin{pmatrix}
2 & 3 & 1 \\
0 & 1 & 7 \\
0 & 0 & 5
\end{pmatrix} \]

With \( L \) and \( U \) determined, you can solve \( Ax = b \) by performing forward and back substitution.

### Benefits and Applications

- **Efficiency**: Solving \( Ax = b \) for multiple different \( b \)-values can be done quickly once \( A \) is decomposed into \( L \) and \( U \).
- **Determinant**: The determinant of \( A \) can be found by multiplying the diagonal entries of \( U \) (since \( \det(A) = \det(L) \cdot \det(U) \)).
- **Inversion**: Computing the inverse of \( A \) can be done efficiently using \( L \) and \( U \).

LU Decomposition is widely used in numerical methods for solving large systems of linear equations and for other matrix computations in various engineering and scientific applications.

---
[Back to index](index.html)
