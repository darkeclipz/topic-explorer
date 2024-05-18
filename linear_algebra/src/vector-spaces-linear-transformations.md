---
title: Linear Transformations
---

[Back to index](index.html)

---
# Vector Spaces
## Linear Transformations

Linear transformations are a fundamental concept in linear algebra, especially within the study of vector spaces. Here's an explanation broken down into key components:

### Definition
A **linear transformation** is a function \( T: V \to W \) between two vector spaces \( V \) and \( W \) that preserves the operations of vector addition and scalar multiplication. Formally, for all vectors \( \mathbf{u}, \mathbf{v} \in V \) and all scalars \( c \in \mathbb{R} \) (or \( \mathbb{C} \), if working in complex vector spaces), a transformation \( T \) is linear if the following two properties hold:

1. **Additivity (or Superposition Principle):**
   \[
   T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})
   \]

2. **Homogeneity (or Scalar Multiplication Compatibility):**
   \[
   T(c \mathbf{u}) = c T(\mathbf{u})
   \]

### Examples
1. **Identity Transformation:**
   \[
   T(\mathbf{x}) = \mathbf{x} 
   \]
   This transformation maps each vector to itself.

2. **Zero Transformation:**
   \[
   T(\mathbf{x}) = \mathbf{0} 
   \]
   This maps every vector to the zero vector.

3. **Scaling Transformation:**
   \[
   T(\mathbf{x}) = c \mathbf{x}
   \]
   This scales all vectors by a constant \( c \).

4. **Rotation (in \(\mathbb{R}^2\)):**
   \[
   T(\begin{bmatrix} x \\ y \end{bmatrix}) = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}
   \]
   This rotates vectors by an angle \(\theta\).

5. **Projection:**
   \[
   T(\begin{bmatrix} x \\ y \\ z \end{bmatrix}) = \begin{bmatrix} x \\ y \\ 0 \end{bmatrix}
   \]
   This projects vectors onto a plane.

### Properties
1. **Kernel (or Null Space):**
   The set of all vectors \(\mathbf{v} \in V\) such that \(T(\mathbf{v}) = \mathbf{0}\). It is a subspace of \(V\).
   \[
   \text{Ker}(T) = \{ \mathbf{v} \in V \, | \, T(\mathbf{v}) = \mathbf{0} \}
   \]

2. **Image (or Range):**
   The set of all vectors \(\mathbf{w} \in W\) such that \( \mathbf{w} = T(\mathbf{v}) \) for some \(\mathbf{v} \in V\). It is a subspace of \(W\).
   \[
   \text{Im}(T) = \{ \mathbf{w} \in W \, | \, \mathbf{w} = T(\mathbf{v}) \text{ for some } \mathbf{v} \in V \}
   \]

3. **Rank-Nullity Theorem:**
   States that for a linear transformation \(T: V \to W\),
   \[
   \text{dim}(\text{Ker}(T)) + \text{dim}(\text{Im}(T)) = \text{dim}(V)
   \]

### Matrix Representation
A linear transformation \( T: \mathbb{R}^n \to \mathbb{R}^m \) can be represented by an \(m \times n\) matrix \( A \) such that
\[
T(\mathbf{x}) = A \mathbf{x}
\]
For example, if \( T(\mathbf{x}) = A \mathbf{x} \) where \( \mathbf{x} \in \mathbb{R}^n \):

- **Input Vector** \(\mathbf{x}\) has \( n \) components.
- **Output Vector** \(T(\mathbf{x})\) (or \( A \mathbf{x} \)) has \( m \) components.
- **Transformation Matrix** \( A \) has \( m \) rows and \( n \) columns.

### Basis and Coordinate Systems
To fully understand linear transformations, one often considers the action of \(T\) on the basis vectors of \(V\). If \( \{ \mathbf{e}_1, \mathbf{e}_2, \ldots, \mathbf{e}_n \} \) is a basis for \( V \), then:

\[
T(\mathbf{e}_i) = \sum_{j=1}^{m} a_{ji} \mathbf{f}_j
\]

Where \( \{ \mathbf{f}_1, \mathbf{f}_2, \ldots, \mathbf{f}_m \} \) is a basis for \( W \), and the coefficients \( a_{ji} \) form the columns of the matrix representation of \(T\).

### Conclusion
Linear transformations are essential in understanding the structure of vector spaces and their interactions. They provide the foundation for many advanced topics in linear algebra and its applications to diverse fields such as physics, computer science, and engineering.

---
[Back to index](index.html)
