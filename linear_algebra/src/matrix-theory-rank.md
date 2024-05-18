---
title: Rank
---

[Back to index](index.html)

---
# Matrix Theory
## Rank

The rank of a matrix is a fundamental concept in linear algebra that provides key insights into the properties of a matrix and the linear system it represents. Here's an explanation of the rank of a matrix:

### Definition
- **Rank**: The rank of a matrix is the maximum number of linearly independent rows or columns in the matrix. It essentially measures the dimension of the vector space spanned by its rows or columns.

### Key Points
1. **Column Rank**: The column rank of a matrix is the number of linearly independent columns.
2. **Row Rank**: The row rank of a matrix is the number of linearly independent rows.
3. **Equivalence**: For any matrix, the row rank is always equal to the column rank. This common rank is simply referred to as the rank of the matrix.

### How to Determine Rank
There are several methods to determine the rank of a matrix:
1. **Gaussian Elimination**: Convert the matrix to its row echelon form (REF) or reduced row echelon form (RREF) using row operations. The number of non-zero rows in the resulting form is the rank of the matrix.
2. **Column Reduction**: Similarly, you can apply column operations to reduce the matrix and count the number of non-zero columns.
3. **Submatrices**: The rank can also be determined by finding the largest square submatrix with a non-zero determinant.

### Properties of Rank
- The rank of an \(m \times n\) matrix \(A\) is a non-negative integer and is at most \(\min(m, n)\).
- A matrix is said to be of **full rank** if its rank is equal to the smallest dimension, \(\min(m, n)\). 
  - For an \(m \times n\) matrix, if \(m \leq n\), full rank means the rank is \(m\); if \(m \geq n\), full rank means the rank is \(n\).

### Applications
- **Solving Linear Systems**: The rank helps to determine whether a system of linear equations has a solution and whether the solution is unique. 
  - **Unique Solution**: A system has a unique solution if the rank of the augmented matrix (matrix of coefficients with an extra column for the constants) is equal to the rank of the coefficient matrix and both are equal to the number of variables.
  - **Infinite Solutions**: If the rank of the coefficient matrix is less than the number of variables but equal to the rank of the augmented matrix, there are infinitely many solutions.
  - **No Solution**: If the rank of the augmented matrix is greater than the rank of the coefficient matrix, the system is inconsistent and has no solution.
- **Linear Transformations**: The rank provides information about the dimension of the range (or image) of a linear transformation.
- **Matrix Inversion**: A square matrix is invertible (non-singular) if and only if it has full rank, meaning its rank is equal to its dimension.

### Example
Consider the matrix \(A\):
\[ A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} \]

To find the rank of \(A\), we can perform row operations to reduce it to its row echelon form:
\[ \begin{pmatrix} 1 & 2 & 3 \\ 0 & -3 & -6 \\ 0 & 0 & 0 \end{pmatrix} \]

Here, there are 2 non-zero rows, so the rank of \(A\) is 2.

### Summary
The rank of a matrix is crucial in understanding the solutions to linear equations, the properties of linear transformations, and the invertibility of matrices. It encapsulates the idea of the maximum number of linearly independent vectors in the rows or columns of a matrix.

---
[Back to index](index.html)
