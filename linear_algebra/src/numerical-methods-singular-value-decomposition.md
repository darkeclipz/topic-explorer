---
title: Singular Value Decomposition
---

[Back to index](index.html)

---
# Numerical Methods
## Singular Value Decomposition

Singular Value Decomposition (SVD) is a powerful factorization method used in numerical linear algebra. It generalizes the eigendecomposition of a square matrix to any \( m \times n \) matrix. Here’s an in-depth explanation:

### Definition:
Singular Value Decomposition decomposes a matrix \( A \) into three other matrices, \( U \), \( \Sigma \), and \( V^T \), such that:
\[ A = U \Sigma V^T \]
where:
- \( A \) is an \( m \times n \) matrix.
- \( U \) is an \( m \times m \) orthogonal matrix (columns are orthonormal vectors, meaning \(U^TU = I\)).
- \( \Sigma \) is an \( m \times n \) diagonal matrix with non-negative real numbers on the diagonal (these are the singular values).
- \( V^T \) (the transpose of \( V \)) is an \( n \times n \) orthogonal matrix (columns are orthonormal vectors, meaning \( V^TV = I \)).

### Steps to Calculate SVD:
1. **Compute Eigenvalues and Eigenvectors:**
   - Compute the eigenvalues and eigenvectors of both \( A^T A \) and \( AA^T \).
   - The eigenvalues of \( A^T A \) (or \( AA^T \)) are the squares of the singular values of \( A \).

2. **Form Matrices \( U \) and \( V \):**
   - The columns of \( V \) are the eigenvectors of \( A^T A \).
   - The columns of \( U \) are the eigenvectors of \( AA^T \).

3. **Construct \( \Sigma \):**
   - Place the square roots of the eigenvalues (the singular values) on the diagonal of \( \Sigma \).
   - \( \Sigma \) will be an \( m \times n \) matrix with non-negative real numbers in descending order along the diagonal and zeros elsewhere.

### Properties:
- The singular values in \( \Sigma \) provide insight into the rank and stability of the matrix \( A \).
- If \( A \) is a square matrix, the singular values can also give information about the invertibility of \( A \).
- The columns of \( U \) are called the left singular vectors, and the columns of \( V \) are called the right singular vectors.

### Applications:
- **Dimensionality Reduction:** In Principal Component Analysis (PCA) for reducing the number of variables in high-dimensional data.
- **Signal Processing:** SVD is used to filter noise and improve signal quality.
- **Image Compression:** Compressing image data by reducing the number of singular values used to reconstruct the image.
- **Solving Linear Systems:** Especially useful for solving systems of linear equations that are ill-conditioned or singular.

### Example:
Consider a \( 3 \times 2 \) matrix \( A \):
\[ A = \begin{pmatrix}
3 & 2 \\ 
2 & 3 \\
1 & 1
\end{pmatrix} \]

1. **Compute \( A^T A \):**
\[ A^T A = \begin{pmatrix}
3 & 2 & 1 \\ 
2 & 3 & 1
\end{pmatrix}
\begin{pmatrix}
3 & 2 \\ 
2 & 3 \\
1 & 1
\end{pmatrix} = \begin{pmatrix}
14 & 11 \\ 
11 & 14
\end{pmatrix} \]

2. **Eigenvalues of \( A^T A \):**
\[ \lambda_1 = 25, \quad \lambda_2 = 3 \]
(Note: Eigenvalues \( \lambda_i \) are the squares of the singular values \( \sigma_i \))

3. **Singular Values:**
\[ \sigma_1 = \sqrt{25} = 5, \quad \sigma_2 = \sqrt{3} \approx 1.73 \]

4. **Construct \( \Sigma \):**
\[ \Sigma = \begin{pmatrix}
5 & 0 \\ 
0 & 1.732 \\ 
0 & 0 
\end{pmatrix} \]

5. **Find \( U \) and \( V \):**
   - Eigenvectors of \( A^T A \) will form \( V \).
   - Eigenvectors of \( AA^T \) will form \( U \).

Putting these pieces together yields the SVD of matrix \( A \).

In practice, numerical software and libraries such as MATLAB, NumPy, and others provide algorithms to compute SVD efficiently, making it a widely used tool in various fields.

---
[Back to index](index.html)
