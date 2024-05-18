---
title: Linear Independence
---

[Back to index](index.html)

---
# Vector Spaces
## Linear Independence

Linear independence is a fundamental concept in linear algebra, particularly within the context of vector spaces. It refers to a set of vectors that are not linearly dependent on each other. Here's a detailed explanation:

### Definition:
A set of vectors \(\{v_1, v_2, \ldots, v_n\}\) in a vector space \(V\) is said to be **linearly independent** if the only solution to the equation

\[ c_1 v_1 + c_2 v_2 + \cdots + c_n v_n = 0 \]

is \(c_1 = c_2 = \cdots = c_n = 0\), where \(c_1, c_2, \ldots, c_n\) are scalars (constants).

Conversely, if there exists a non-trivial solution (at least one \(c_i \neq 0\)) to this equation, then the vectors are said to be **linearly dependent**.

### Geometry Intuition:
- In \(\mathbb{R}^2\) (2-dimensional space), two vectors are linearly independent if they do not lie on the same line through the origin. For example, the vectors \(\begin{pmatrix} 1 \\ 0 \end{pmatrix}\) and \(\begin{pmatrix} 0 \\ 1 \end{pmatrix}\) are linearly independent.
- In \(\mathbb{R}^3\) (3-dimensional space), three vectors are linearly independent if they do not lie in the same plane through the origin. For example, the vectors \(\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}\), \(\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}\), and \(\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}\) are linearly independent.

### Why It's Important:
- **Basis:** A basis for a vector space \(V\) is a maximal linearly independent set of vectors in \(V\). This is crucial because a basis provides a way to uniquely represent every vector in the space as a linear combination of basis vectors.
- **Dimension:** The dimension of a vector space is the number of vectors in a basis for that space. For example, \(\mathbb{R}^3\) has dimension 3, meaning any basis of \(\mathbb{R}^3\) will consist of exactly three linearly independent vectors.
- **Span:** The span of a set of vectors is the collection of all linear combinations of those vectors. If the vectors are linearly independent, they span the vector space without redundancy.

### Example:
Consider the vectors \(\mathbf{v}_1 = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}\) and \(\mathbf{v}_2 = \begin{pmatrix} 4 \\ 5 \\ 6 \end{pmatrix}\) in \(\mathbb{R}^3\).

To determine if they are linearly independent, set up the equation:
\[ c_1 \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + c_2 \begin{pmatrix} 4 \\ 5 \\ 6 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} \]

This gives us the system of equations:
\[ c_1 + 4c_2 = 0 \]
\[ 2c_1 + 5c_2 = 0 \]
\[ 3c_1 + 6c_2 = 0 \]

Solving this system, we find \(c_1 = 0\) and \(c_2 = 0\), indicating that the vectors are linearly independent.

### Conclusion:
Understanding linear independence is crucial for many applications in linear algebra, including solving systems of linear equations, transforming matrices, and more advanced topics like eigenvalues and eigenvectors. It serves as a foundation for building and working with vector spaces.

---
[Back to index](index.html)
