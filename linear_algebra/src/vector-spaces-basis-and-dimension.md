---
title: Basis and Dimension
---

[Back to index](index.html)

---
# Vector Spaces
## Basis and Dimension

### Basis and Dimension in Vector Spaces

#### Basis:
A **basis** of a vector space \( V \) is a set of vectors in \( V \) that are linearly independent and that span \( V \). This means that any vector in \( V \) can be written as a linear combination of the basis vectors.

**Key properties of a basis:**

1. **Linear Independence:** The vectors in the basis are linearly independent. This means no vector in the set can be written as a linear combination of the others.
2. **Spanning Set:** The vectors in the basis span the vector space, meaning any vector in the space can be expressed as a combination of the basis vectors.

For example, in the vector space \( \mathbb{R}^3 \), the standard basis is \( \{ \mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3 \} \), where:
\[ \mathbf{e}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \ \mathbf{e}_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \ \mathbf{e}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \]

#### Dimension:
The **dimension** of a vector space \( V \) is the number of vectors in any basis for \( V \). The dimension gives a measure of the "size" of the vector space.

**Key points about dimension:**

1. **Uniqueness:** All bases of a vector space \( V \) have the same number of elements, which is defined as the dimension of \( V \).
2. **Finite vs. Infinite:** If the basis has a finite number of elements, \( V \) is called a finite-dimensional vector space; otherwise, \( V \) is infinite-dimensional.

For example:
- The vector space \( \mathbb{R}^3 \) has dimension 3.
- The space of polynomials of degree at most \( n \) (denoted by \( \mathbb{P}_n \)) has dimension \( n+1 \).

### Determining a Basis and Dimension:
To find the basis and determine the dimension of a vector space:

1. **Span and Linear Independence:** Identify a set of vectors that span the vector space and check if they are linearly independent.
2. **Construct or Reduce:** Use techniques like the row reduction method (Gaussian elimination) to simplify the problem of identifying a basis, especially for spaces defined by systems of linear equations.

#### Examples:
1. **\( \mathbb{R}^2 \)**:
   - Standard Basis: \( \left\{ \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix} \right\} \)
   - Dimension: 2

2. **Polynomial Space \( \mathbb{P}_2 \)**:
   - Basis: \( \{1, x, x^2\} \)
   - Dimension: 3

3. **Subspace of \( \mathbb{R}^3 \) defined by \( x + y + z = 0 \)**:
   - Determine a basis by solving the equation and identifying the linearly independent vectors. For example:
     \[ \text{Solution in parametric form: } (x, y, z) = t \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix} + s \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} \]
   - Basis: \( \left\{ \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} \right\} \)
   - Dimension: 2

Understanding basis and dimension provides essential insight into the structure and properties of vector spaces, forming a foundational concept in linear algebra.

---
[Back to index](index.html)
