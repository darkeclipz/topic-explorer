---
title: Orthogonal Complements
---

[Back to index](index.html)

---
# Inner Product Spaces
## Orthogonal Complements

Orthogonal complements are an important concept in the study of inner product spaces in linear algebra. Here is a detailed explanation:

### Inner Product Spaces
An inner product space is a vector space \( V \) equipped with an inner product, which is a function 
\[ \langle \cdot, \cdot \rangle: V \times V \to \mathbb{F} \]
where \( \mathbb{F} \) is the field of scalars (either the real numbers \( \mathbb{R} \) or the complex numbers \( \mathbb{C} \)). The inner product must satisfy the following properties for all vectors \( u, v, w \in V \) and all scalars \( c \in \mathbb{F} \):

1. **Conjugate Symmetry**: \( \langle u, v \rangle = \overline{\langle v, u \rangle} \)
2. **Linearity in the First Argument**: \( \langle cu + v, w \rangle = c \langle u, w \rangle + \langle v, w \rangle \)
3. **Positive Definiteness**: \( \langle v, v \rangle \geq 0 \) with equality if and only if \( v = 0 \)

### Orthogonality
Two vectors \( u \) and \( v \) are said to be orthogonal if their inner product is zero:
\[ \langle u, v \rangle = 0 \]
Orthogonality is a generalization of the concept of perpendicular vectors in Euclidean space.

### Orthogonal Complement
The orthogonal complement of a subspace \( W \subseteq V \), denoted \( W^\perp \), is the set of all vectors in \( V \) that are orthogonal to every vector in \( W \). Formally,
\[ W^\perp = \{ v \in V \mid \langle v, w \rangle = 0 \text{ for all } w \in W \} \]

### Properties
- **Subspace**: \( W^\perp \) itself is a subspace of \( V \).
- **Dimensionality**: If \( V \) is a finite-dimensional inner product space, then 
  \[ \dim(W) + \dim(W^\perp) = \dim(V) \]
  This implies that the dimensions of \( W \) and its orthogonal complement sum up to the dimension of the entire space \( V \).
- **Double Orthocomplement**: The orthogonal complement of the orthogonal complement of \( W \) is \( W \) itself, i.e., \((W^\perp)^\perp = W \).

### Examples
1. **Euclidean Space**: In \( \mathbb{R}^n \) with the standard dot product, the orthogonal complement of a plane through the origin is the line through the origin that is perpendicular to that plane.

2. **Column Space and Null Space**: In the context of linear transformations, the orthogonal complement of the column space of a matrix \( A \) (range of \( A \))  is the null space of \( A^T \) (transposed matrix \( A \)).

### Applications
Orthogonal complements are used in various applications, such as solving systems of linear equations, optimization problems, and more. For example, in the method of least squares, orthogonality plays a key role in finding the best approximation to an overdetermined system by projecting the data into a subspace and finding the orthogonal complement.

In summary, understanding orthogonal complements provides a deep insight into the geometry of inner product spaces and has extensive practical applications in both theoretical and applied linear algebra.

---
[Back to index](index.html)
