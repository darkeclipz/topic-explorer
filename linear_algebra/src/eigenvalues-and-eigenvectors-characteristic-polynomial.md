---
title: Characteristic Polynomial
---

[Back to index](index.html)

---
# Eigenvalues and Eigenvectors
## Characteristic Polynomial

The characteristic polynomial is a crucial concept in the study of eigenvalues and eigenvectors in linear algebra. It is derived from a square matrix and is fundamental in determining the eigenvalues of that matrix. Here is a detailed explanation:

### Definition
The characteristic polynomial of an \( n \times n \) matrix \( A \) is defined as the polynomial \( p(\lambda) \) given by the determinant of \( A - \lambda I \), where \( \lambda \) is a scalar (typically representing eigenvalues), and \( I \) is the identity matrix of the same dimension as \( A \). Mathematically, it is expressed as:

\[ p(\lambda) = \text{det}(A - \lambda I) \]

### Steps to Find the Characteristic Polynomial

1. **Construct the Matrix \( A - \lambda I \)**:
   - Subtract \( \lambda \) times the identity matrix \( I \) from the matrix \( A \). If \( A \) is a \( 3 \times 3 \) matrix, \( A - \lambda I \) would look like this:
   \[
   A - \lambda I = 
   \begin{pmatrix}
   a_{11} - \lambda & a_{12} & a_{13} \\
   a_{21} & a_{22} - \lambda & a_{23} \\
   a_{31} & a_{32} & a_{33} - \lambda
   \end{pmatrix}.
   \]

2. **Compute the Determinant**:
   - Find the determinant of the resulting matrix \( A - \lambda I \). This step involves cofactor expansion, which can get computationally intense for larger matrices. For a \( 3 \times 3 \) matrix, the determinant is calculated as:
   \[
   \text{det}(A - \lambda I) = 
   \begin{vmatrix}
   a_{11} - \lambda & a_{12} & a_{13} \\
   a_{21} & a_{22} - \lambda & a_{23} \\
   a_{31} & a_{32} & a_{33} - \lambda
   \end{vmatrix}.
   \]

3. **Form the Polynomial**:
   - The result is a polynomial in \( \lambda \). This polynomial is called the characteristic polynomial of \( A \).

### Eigenvalues
The eigenvalues of the matrix \( A \) are the solutions to the equation obtained by setting the characteristic polynomial equal to zero:

\[ \text{det}(A - \lambda I) = 0 \]

Solving this equation gives the values of \( \lambda \) for which there are non-zero vectors \( \mathbf{v} \) such that:

\[ A \mathbf{v} = \lambda \mathbf{v} \]

### Example
Consider a \( 2 \times 2 \) matrix:

\[ A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix} \]

1. **Construct \( A - \lambda I \)**:
   \[
   A - \lambda I = \begin{pmatrix} 4 - \lambda & 1 \\ 2 & 3 - \lambda \end{pmatrix}
   \]

2. **Compute the Determinant**:
   \[
   \text{det}(A - \lambda I) = (4 - \lambda)(3 - \lambda) - (2 \cdot 1) = \lambda^2 - 7\lambda + 10
   \]

3. **Form the Characteristic Polynomial**:
   \[
   p(\lambda) = \lambda^2 - 7\lambda + 10
   \]

### Finding Eigenvalues
To find the eigenvalues, set the characteristic polynomial equal to zero and solve for \( \lambda \):

\[ \lambda^2 - 7\lambda + 10 = 0 \]

This factors to:

\[ (\lambda - 5)(\lambda - 2) = 0 \]

So, the eigenvalues are \( \lambda = 5 \) and \( \lambda = 2 \).

Understanding characteristic polynomials and computing eigenvalues is fundamental in many applications of linear algebra, including systems of differential equations, stability analysis, and various fields of engineering and physics.

---
[Back to index](index.html)
