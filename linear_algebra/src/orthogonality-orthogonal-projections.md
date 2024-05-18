---
title: Orthogonal Projections
---

[Back to index](index.html)

---
# Orthogonality
## Orthogonal Projections

Orthogonal projections are a fundamental concept in linear algebra, particularly in understanding the structure of vector spaces and subspaces. Here’s a detailed breakdown:

### Orthogonal Projections

**Definition:**
An orthogonal projection of a vector onto a subspace is the "shadow" or "footprint" the vector creates when dropped perpendicularly onto that subspace. Mathematically, if you have a vector \( \mathbf{v} \) and a subspace \( W \), the orthogonal projection of \( \mathbf{v} \) onto \( W \) is denoted as \( \mathbf{proj}_W(\mathbf{v}) \).

**Key Concepts:**

1. **Subspace:** A subspace \( W \) is a subset of a vector space that is itself a vector space. Common subspaces include the span of a set of vectors.

2. **Orthogonal Complement:** For a given subspace \( W \), the orthogonal complement \( W^\perp \) is the set of all vectors that are orthogonal to every vector in \( W \).

3. **Orthogonal Projection Theorem:** Any vector \( \mathbf{v} \) in a vector space \( V \) can be uniquely decomposed as the sum of two components: one that lies in a subspace \( W \) and one that lies in \( W^\perp \). Formally:
   \[ \mathbf{v} = \mathbf{v}_W + \mathbf{v}_{W^\perp} \]
   where \( \mathbf{v}_W \in W \) and \( \mathbf{v}_{W^\perp} \in W^\perp \).

### Calculation of Orthogonal Projection

To calculate the orthogonal projection of a vector \( \mathbf{v} \) onto a subspace \( W \), follow these steps:

1. **Basis of Subspace:** Find an orthogonal (or orthonormal) basis \( \{\mathbf{w}_1, \mathbf{w}_2, \dots, \mathbf{w}_k\} \) for the subspace \( W \).

2. **Using Orthonormal Basis:** If the basis is orthonormal, the projection can be computed easily as:
   \[ \mathbf{proj}_W(\mathbf{v}) = \sum_{i=1}^{k} \langle \mathbf{v}, \mathbf{w}_i \rangle \mathbf{w}_i \]
   where \( \langle \cdot, \cdot \rangle \) denotes the inner product.

3. **Using Orthogonal Basis:** If the basis is only orthogonal but not normalized, normalize the basis vectors first or use a modified formula:
   \[ \mathbf{proj}_W(\mathbf{v}) = \sum_{i=1}^{k} \frac{\langle \mathbf{v}, \mathbf{w}_i \rangle}{\langle \mathbf{w}_i, \mathbf{w}_i \rangle} \mathbf{w}_i \]

### Example

Suppose we have a vector \( \mathbf{v} \) and we want to project it onto the line spanned by a single vector \( \mathbf{u} \). If \( \mathbf{u} \) is an orthonormal vector, then:
\[ \mathbf{proj}_{\text{span}(\mathbf{u})}(\mathbf{v}) = \langle \mathbf{v}, \mathbf{u} \rangle \mathbf{u} \]
If \( \mathbf{u} \) is not unit length:
\[ \mathbf{proj}_{\text{span}(\mathbf{u})}(\mathbf{v}) = \frac{\langle \mathbf{v}, \mathbf{u} \rangle}{\langle \mathbf{u}, \mathbf{u} \rangle} \mathbf{u} \]

### Properties of Orthogonal Projections

1. **Idempotence:** Applying the projection operator twice yields the same result as applying it once:
   \[ \mathbf{proj}_W(\mathbf{proj}_W(\mathbf{v})) = \mathbf{proj}_W(\mathbf{v}) \]

2. **Linearity:** The projection operator is linear:
   \[ \mathbf{proj}_W(a \mathbf{v} + b \mathbf{u}) = a \mathbf{proj}_W(\mathbf{v}) + b \mathbf{proj}_W(\mathbf{u}) \]
   for any scalars \( a \) and \( b \).

3. **Orthogonality:** The difference between a vector and its projection lies in the orthogonal complement of the subspace:
   \[ \mathbf{v} - \mathbf{proj}_W(\mathbf{v}) \perp W \]

Understanding orthogonal projections is crucial in diverse fields such as computer graphics, optimization, signal processing, and statistics, particularly in techniques like Principal Component Analysis (PCA).

---
[Back to index](index.html)
