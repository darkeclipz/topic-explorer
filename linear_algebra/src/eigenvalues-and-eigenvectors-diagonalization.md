---
title: Diagonalization
---

[Back to index](index.html)

---
# Eigenvalues and Eigenvectors
## Diagonalization

Diagonalization is a key concept in linear algebra involving eigenvalues and eigenvectors. It refers to the process of transforming a given matrix into a diagonal matrix, making many matrix operations simpler and more computationally efficient. Here's a detailed explanation:

### What is Diagonalization?
Diagonalization involves finding a diagonal matrix \( D \) and an invertible matrix \( P \) such that a square matrix \( A \) can be expressed as:
\[ A = PDP^{-1} \]

### Why is Diagonalization Important?
Diagonalization simplifies matrix computations, particularly for raising matrices to higher powers and solving systems of linear differential equations.

### Steps for Diagonalization:

1. **Find Eigenvalues:**
   - Compute the eigenvalues of matrix \( A \). These are the roots of the characteristic polynomial \( \det(A - \lambda I) = 0 \), where \( I \) is the identity matrix and \( \lambda \) represents eigenvalues.

2. **Find Eigenvectors:**
   - For each eigenvalue \( \lambda \), solve \( (A - \lambda I)x = 0 \) to find the corresponding eigenvectors.

3. **Form the Matrix \( P \):**
   - Construct matrix \( P \) using the eigenvectors as columns. \( P \) should be invertible, which is possible if and only if \( A \) has \( n \) linearly independent eigenvectors (where \( n \) is the size of \( A \)).

4. **Form the Diagonal Matrix \( D \):**
   - Construct \( D \) as a diagonal matrix with eigenvalues \( \lambda_1, \lambda_2, \ldots, \lambda_n \) on the diagonal.

### Conditions for Diagonalization:
A matrix \( A \) is diagonalizable if:
- \( A \) has \( n \) linearly independent eigenvectors.
- This condition holds if the algebraic multiplicity of each eigenvalue (the number of times each eigenvalue appears as a root of the characteristic polynomial) equals its geometric multiplicity (the dimension of its corresponding eigenspace, i.e., the number of linearly independent eigenvectors associated with it).

### Example:
Suppose we have a matrix \( A \):

\[ A = \begin{pmatrix}
4 & 1 \\
2 & 3
\end{pmatrix} \]

1. **Find Eigenvalues:**
   - The characteristic polynomial is given by \( \det(A - \lambda I) \):
     \[
     \det \begin{pmatrix}
     4 - \lambda & 1 \\
     2 & 3 - \lambda
     \end{pmatrix}
     = (4 - \lambda)(3 - \lambda) - 2 = \lambda^2 - 7\lambda + 10 = 0
     \]
   - Solve for \( \lambda \): \( (\lambda - 5)(\lambda - 2) = 0 \) gives eigenvalues \( \lambda_1 = 5 \) and \( \lambda_2 = 2 \).

2. **Find Eigenvectors:**
   - For \( \lambda_1 = 5 \):
     \[
     (A - 5I)\vec{v} = 0 \quad\Rightarrow\quad \begin{pmatrix}
     -1 & 1 \\
     2 & -2
     \end{pmatrix}\begin{pmatrix}
     v_1 \\
     v_2
     \end{pmatrix} = \begin{pmatrix}
     0\\
     0
     \end{pmatrix}
     \]
     - Simplified, \( v_1 = v_2 \), so one eigenvector is \( \vec{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix} \).

   - For \( \lambda_2 = 2 \):
     \[
     (A - 2I)\vec{v} = 0 \quad\Rightarrow\quad \begin{pmatrix}
     2 & 1 \\
     2 & 1
     \end{pmatrix}\begin{pmatrix}
     v_1 \\
     v_2
     \end{pmatrix} = \begin{pmatrix}
     0 \\ 0 
     \end{pmatrix}
     \]
     - Simplified, \( v_1 = -v_2/2 \), so one eigenvector is \( \vec{v}_2 = \begin{pmatrix} 1 \\ -2 \end{pmatrix} \).

3. **Form the Matrix \( P \):**
   \[
   P = \begin{pmatrix} 
   1 & 1 \\ 
   1 & -2 
   \end{pmatrix}
   \]

4. **Form the Diagonal Matrix \( D \):**
   \[
   D = \begin{pmatrix} 
   5 & 0 \\ 
   0 & 2 
   \end{pmatrix}
   \]

Thus, we have:
\[ A = PDP^{-1} \]

This diagonalization of matrix \( A \) makes many operations more straightforward.

### Summary
Diagonalization is a profound and useful concept in linear algebra, making complex matrix operations more manageable. By utilizing eigenvalues and their respective eigenvectors, matrices can be transformed into a simpler diagonal form.

---
[Back to index](index.html)
