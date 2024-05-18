---
title: Spectral Theorem
---

[Back to index](index.html)

---
# Eigenvalues and Eigenvectors
## Spectral Theorem

The Spectral Theorem is a fundamental result in linear algebra that applies to certain classes of matrices. It provides a structure for understanding how these matrices can be simplified using their eigenvalues and eigenvectors. Here's an explanation of the Spectral Theorem:

### The Spectral Theorem

**Statement**: The Spectral Theorem states that for any normal matrix \(A\) (i.e., \(A\) such that \(A A^* = A^* A\), where \(A^*\) is the conjugate transpose of \(A\)), there exists a unitary matrix \(U\) (a matrix \(U\) such that \(U U^* = U^* U = I\)) and a diagonal matrix \(D\) such that:

\[ A = U D U^* \]

In the special case when \(A\) is a real symmetric matrix (i.e., \(A = A^T\)), the matrix \(U\) can be chosen to be an orthogonal matrix (\(U^T U = U U^T = I\)) and the diagonal entries of \(D\) are real eigenvalues of \(A\).

### Key Points

1. **Normal Matrices**: A matrix \(A\) is normal if it commutes with its conjugate transpose, i.e., \(A A^* = A^* A\).
   - **Examples**: Hermitian (or self-adjoint) matrices (\(A = A^*\)), unitary matrices (\(U U^* = I\)), and real symmetric matrices (\(A = A^T\)) are all normal.

2. **Unitary and Orthogonal Matrices**:
   - A unitary matrix \(U\) satisfies \(U U^* = I\).
   - An orthogonal matrix is a special case of a unitary matrix where all entries are real and satisfies \(U^T U = I\).

3. **Diagonalization**: The theorem tells us that a normal matrix \(A\) can be diagonalized by a unitary matrix. This means that it can be written in the form \(A = U D U^*\), where \(D\) is a diagonal matrix containing the eigenvalues of \(A\) and the columns of \(U\) are the eigenvectors of \(A\).

### Implications

- **Simplifies Computation**: The Spectral Theorem is particularly useful because diagonal matrices are much easier to work with. For instance, powers of \(A\) or functions of \(A\) (like the matrix exponential) can be easily computed when \(A\) is diagonalized.
  
- **Positive Definite Matrices**: For a symmetric positive definite matrix \(A\), all eigenvalues are positive, which can be derived from the Spectral Theorem.

- **Quantum Mechanics**: The Spectral Theorem is a cornerstone in quantum mechanics, where Hermitian operators (representing physical observables) are diagonalized to find their eigenvalues (possible measurement outcomes).

### Example

Consider a real symmetric matrix:
\[ A = \begin{pmatrix} 4 & 1 \\ 1 & 3 \end{pmatrix} \]

1. **Find Eigenvalues and Eigenvectors**: Solve the characteristic equation \(\det(A - \lambda I) = 0\) to find the eigenvalues.
   
2. **Matrix \(U\)**: Construct \(U\) from the normalized eigenvectors.

3. **Matrix \(D\)**: Form \(D\) with the eigenvalues of \(A\).

4. **Verify**: Confirm that \(A = U D U^T\).

Thus, the Spectral Theorem provides insight into the structure and properties of normal matrices through their eigenvalues and eigenvectors.

---
[Back to index](index.html)
