---
title: Eigenvalues and Eigenvectors
---

[Back to index](index.html)

---
# Linear Algebra
## Eigenvalues and Eigenvectors

Eigenvalues and eigenvectors are fundamental concepts in linear algebra, playing a significant role in various applications including stability analysis, quantum mechanics, vibration analysis, facial recognition, and more. Here's a detailed explanation:

### Eigenvectors:
An eigenvector of a square matrix \( A \) is a nonzero vector \( v \) such that when \( v \) is multiplied by \( A \), the resultant vector is a scalar multiple of \( v \). In mathematical terms, \( v \) is an eigenvector if:

\[ A \mathbf{v} = \lambda \mathbf{v} \]

Here:
- \( A \) is an \( n \times n \) matrix.
- \( \mathbf{v} \) is the eigenvector.
- \( \lambda \) is the eigenvalue corresponding to the eigenvector \( \mathbf{v} \).

### Eigenvalues:
An eigenvalue \( \lambda \) of a matrix \( A \) is a scalar such that there exists a nonzero vector \( \mathbf{v} \) (the corresponding eigenvector) for which the above equation holds.

### Finding Eigenvalues and Eigenvectors:

1. **Eigenvalues:**
   To find the eigenvalues of a matrix \( A \), we solve the characteristic equation. This is done by following these steps:
   - Compute the determinant of \( A - \lambda I \), where \( I \) is the identity matrix of the same dimension as \( A \).
   
   \[ \text{det}(A - \lambda I) = 0 \]
   
   - The values of \( \lambda \) that satisfy this equation are the eigenvalues of \( A \).

2. **Eigenvectors:**
   Once the eigenvalues \( \lambda \) are found, the corresponding eigenvectors can be determined by solving the equation:
   
   \[ (A - \lambda I) \mathbf{v} = 0 \]
   
   This involves finding the null space of the matrix \( A - \lambda I \). The nontrivial solutions to this homogeneous system are the eigenvectors corresponding to the eigenvalue \( \lambda \).

### Example:
Consider the matrix \( A \):
\[ A = 
 \begin{pmatrix}
4 & 1 \\
2 & 3
 \end{pmatrix}
\]
   
1. **Finding the Eigenvalues:**
   The characteristic equation is obtained by solving \( \text{det}(A - \lambda I) = 0 \):
   \[ \text{det}
    \begin{pmatrix}
    4-\lambda & 1 \\
    2 & 3-\lambda
    \end{pmatrix}
    = (4-\lambda)(3-\lambda) - (2 \cdot 1) = \lambda^2 - 7\lambda + 10 = 0
   \]
   Solving this quadratic equation:
   \[ \lambda^2 - 7\lambda + 10 = 0 \]
   \[ (\lambda - 5)(\lambda - 2) = 0 \]
   Thus, the eigenvalues are \( \lambda_1 = 5 \) and \( \lambda_2 = 2 \).

2. **Finding the Eigenvectors:**
   For \( \lambda_1 = 5 \):
   \[ 
   (A - 5I) \mathbf{v} = 
   \begin{pmatrix}
   4-5 & 1 \\
   2 & 3-5
   \end{pmatrix}
   \mathbf{v} =
   \begin{pmatrix}
   -1 & 1 \\
   2 & -2
   \end{pmatrix}
   \mathbf{v} = 0 
   \]
   Solving, we get:
   \[ -v_1 + v_2 = 0 \]
   Therefore, \( v_2 = v_1 \), and one possible eigenvector is \( \mathbf{v}_1 = (1, 1)^T \).

   For \( \lambda_2 = 2 \):
   \[ 
   (A - 2I) \mathbf{v} = 
   \begin{pmatrix}
   4-2 & 1 \\
   2 & 3-2
   \end{pmatrix}
   \mathbf{v} = 
   \begin{pmatrix}
   2 & 1 \\
   2 & 1
   \end{pmatrix}
   \mathbf{v} = 0 
   \]
   Solving, we find:
   \[ 2v_1 + v_2 = 0 \]
   Therefore, \( v_2 = -2v_1 \), and one possible eigenvector is \( \mathbf{v}_2 = (1, -2)^T \).

In summary, eigenvalues and eigenvectors provide significant insights into the structure of linear transformations represented by matrices, helping to simplify complex systems and understanding their behavior in various applications.

---
[Back to index](index.html)
