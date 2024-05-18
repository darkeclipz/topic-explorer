---
title: QR Decomposition
---

[Back to index](index.html)

---
# Numerical Methods
## QR Decomposition

QR Decomposition, also known as QR Factorization, is a numerical method used in linear algebra to decompose a given matrix \( A \) into the product of two matrices: \( Q \) and \( R \).

### Definition:
For an \( m \times n \) matrix \( A \) with \( m \geq n \), QR Decomposition expresses \( A \) as:
\[ A = QR \]
where:
- \( Q \) is an \( m \times n \) orthogonal (if \( A \) is square) or unitary matrix (if \( A \) has complex entries).
- \( R \) is an \( n \times n \) upper triangular matrix.

### Properties:
- The columns of \( Q \) are orthonormal, meaning \( Q^T Q = I \) where \( I \) is the identity matrix.
- \( R \) being upper triangular means all its elements below the main diagonal are zero.

### Applications:
- **Solving linear systems**: Particularly useful for solving \( Ax = b \).
- **Computing eigenvalues**: Used in iterative methods like the QR algorithm.
- **Least squares problems**: Helps in finding the best fit solution to over-determined systems.

### Methods for QR Decomposition:
QR Decomposition can be performed using several methods:

1. **Gram-Schmidt Process**:
    - Applies the Gram-Schmidt orthogonalization to the columns of \( A \) to produce the orthogonal matrix \( Q \) and upper triangular matrix \( R \).

2. **Householder Reflections**:
    - Uses Householder transformations to zero out the sub-diagonal elements systematically, which is numerically stable and often preferred for practical implementations.

3. **Givens Rotations**:
    - Uses a series of rotations to introduce zeros below the diagonal, useful for sparse matrices.

### Example:
Given a matrix \( A \):

\[ A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 3 & 3 \\ 1 & 3 & 5 \end{pmatrix} \]

We aim to find matrices \( Q \) and \( R \) such that \( A = QR \).

Using the Gram-Schmidt process:

1. Compute \( Q \):
    - Normalize the first column: \( q_1 = a_1 / \|a_1\| \)
    - Orthogonalize the remaining columns with respect to \( q_1 \) and normalize, continue this process for each column.

2. Compute \( R \):
    - \( R = Q^T A \)

The resulting \( Q \) and \( R \) are:

\[ Q = \begin{pmatrix} 
\frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} & \frac{2}{\sqrt{2}} \\ 
\frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{2}} \\ 
\frac{1}{\sqrt{3}} & -\frac{4}{\sqrt{6}} & 0 
\end{pmatrix} \]

\[ R = \begin{pmatrix} 
\sqrt{3} & \frac{5}{\sqrt{3}} & \frac{9}{\sqrt{3}} \\ 
0 & \sqrt{\frac{2}{3}} & \frac{2\sqrt{6}}{3} \\ 
0 & 0 & \sqrt{2} 
\end{pmatrix} \]

Therefore, \( A = QR \) where \( Q \) and \( R \) are constructed as shown above.

### Summary:
QR Decomposition is a crucial tool in numerical linear algebra with applications that span solving linear systems, eigenvalue computations, and addressing least squares problems. The various methods for performing QR Decomposition, like Gram-Schmidt, Householder transformations, and Givens rotations, offer flexibility based on the structure and requirements of the problem at hand.

---
[Back to index](index.html)
