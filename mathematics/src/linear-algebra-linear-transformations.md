---
title: Linear Transformations
---

[Back to index](index.html)

---
# Linear Algebra
## Linear Transformations

Sure! Linear transformations are fundamental concepts in linear algebra. Let's break down the key points:

### Definition:
A **linear transformation** is a function between two vector spaces that preserves the operations of vector addition and scalar multiplication. Mathematically, a function \( T: V \rightarrow W \) (where \( V \) and \( W \) are vector spaces) is a linear transformation if for any vectors \( \mathbf{u}, \mathbf{v} \in V \) and any scalar \( c \):

1. **Additivity (or Superposition Principle)**: \( T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) \)
2. **Homogeneity (or Scalar Multiplication)**: \( T(c \mathbf{u}) = c T(\mathbf{u}) \)

### Examples:
1. **Scaling Transformation**: \( T(\mathbf{x}) = k \mathbf{x} \), where \( k \) is a scalar.
2. **Rotation Transformation** (in 2D): If \( T(\mathbf{x}) \) represents a rotation of \( \theta \) degrees counterclockwise, then:
   \[
   T\left( \begin{bmatrix} x \\ y \end{bmatrix} \right) = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}
   \]

### Matrix Representation:
Any linear transformation \( T: \mathbb{R}^n \rightarrow \mathbb{R}^m \) can be represented by a matrix. If \( A \) is an \( m \times n \) matrix, then the linear transformation \( T \) can be expressed as:
\[ T(\mathbf{x}) = A\mathbf{x} \]
where \( \mathbf{x} \) is a vector in \( \mathbb{R}^n \).

### Properties:
1. **Kernel (Null Space)**: The set of vectors that map to the zero vector \( \{ \mathbf{v} \in V : T(\mathbf{v}) = \mathbf{0} \} \). It provides insight into the solving of the homogeneous equation \( T(\mathbf{x}) = \mathbf{0} \).
2. **Image (Range)**: The set of all vectors that are the output of the transformation \( \{ \mathbf{w} \in W : \mathbf{w} = T(\mathbf{v}) \text{ for some } \mathbf{v} \in V \} \). It indicates the span of the transformed vectors.
3. **Rank-Nullity Theorem**: Relates the dimensions of the kernel and image. If \( V \) is finite-dimensional, then \( \text{dim}(V) = \text{rank}(T) + \text{nullity}(T) \).

### Applications:
1. **Computer Graphics**: Scaling, rotating, and translating images.
2. **Data Science**: Principal Component Analysis (PCA), where data is transformed into a new coordinate system.
3. **Engineering and Physics**: Solving systems of differential equations, time-invariant linear systems, etc.

### Visualization:
In 2D, imagine how transformations like rotations, scaling, and shearing can change the shape or orientation of vectors.

If you have more specific questions or examples you'd like to explore, feel free to ask!

---
[Back to index](index.html)
