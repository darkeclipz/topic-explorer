---
title: Subspaces
---

[Back to index](index.html)

---
# Vector Spaces
## Subspaces

In linear algebra, a **subspace** is a subset of a vector space that is itself a vector space under the same addition and scalar multiplication operations. Understanding subspaces is fundamental when exploring the structure and properties of vector spaces.

### Definition of a Subspace:
A subset \( W \) of a vector space \( V \) is called a subspace if it satisfies the following three conditions:

1. **The Zero Vector**: The zero vector of \( V \) is in \( W \).
2. **Closed under Addition**: For any vectors \( u, v \in W \), the sum \( u + v \) is also in \( W \).
3. **Closed under Scalar Multiplication**: For any vector \( u \in W \) and any scalar \( c \), the product \( c \cdot u \) is also in \( W \).

These conditions ensure that the subset \( W \) inherits the structure of a vector space from \( V \).

### Examples of Subspaces:
1. **The Zero Subspace**: The set containing only the zero vector {0} is always a subspace.
2. **The Entire Space**: The vector space \( V \) itself is trivially a subspace of \( V \).
3. **Lines through the Origin**: In \( \mathbb{R}^2 \), any line passing through the origin is a subspace of \( \mathbb{R}^2 \).
4. **Planes through the Origin**: In \( \mathbb{R}^3 \), any plane passing through the origin is a subspace of \( \mathbb{R}^3 \).

### Properties of Subspaces:
- **Intersection of Subspaces**: The intersection of two subspaces \( W_1 \) and \( W_2 \) of \( V \) is also a subspace of \( V \).
- **Span of a Set**: Given a set of vectors in \( V \), the set of all linear combinations of these vectors forms a subspace, known as the **span** of the set.
- **Linear Independence and Basis**: A set of vectors is called a basis of a subspace \( W \) if the set is linearly independent and spans \( W \). The number of vectors in the basis is called the **dimension** of the subspace.

### Example Walkthrough:
Let's consider \( \mathbb{R}^3 \) and a subset \( W \) defined as \( W = \{ (x, y, z) \in \mathbb{R}^3 \mid x + y + z = 0 \} \).

1. **Zero Vector**: The zero vector \( (0, 0, 0) \) satisfies \( x + y + z = 0 \), so it is in \( W \).
2. **Closed under Addition**: Take any two vectors \( u = (x_1, y_1, z_1) \) and \( v = (x_2, y_2, z_2) \) in \( W \). Then \( x_1 + y_1 + z_1 = 0 \) and \( x_2 + y_2 + z_2 = 0 \). Adding them gives \( (x_1 + x_2, y_1 + y_2, z_1 + z_2) \). The sum \( (x_1 + x_2) + (y_1 + y_2) + (z_1 + z_2) = (x_1 + y_1 + z_1) + (x_2 + y_2 + z_2) = 0 + 0 = 0 \). So, the sum is in \( W \).
3. **Closed under Scalar Multiplication**: For vector \( (x, y, z) \in W \) and scalar \( c \), \( x + y + z = 0 \) implies \( c \cdot (x + y + z) = c \cdot 0 = 0 \). So, the product \( c(x, y, z) = (cx, cy, cz) \) is in \( W \).

Therefore, \( W \) is a subspace of \( \mathbb{R}^3 \).

### Conclusion:
Subspaces are a crucial concept in linear algebra as they help reveal the structure and dimensions within vector spaces. They are used in solving systems of linear equations, understanding transformations, and many other areas in mathematics and applied sciences.

---
[Back to index](index.html)
