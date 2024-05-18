---
title: Vector Operations
---

[Back to index](index.html)

---
# Vectors
## Vector Operations

Vector operations are fundamental concepts in linear algebra that allow us to manipulate and compute with vectors. Here are the primary vector operations:

1. **Vector Addition**:
   - Vector addition involves adding corresponding components of two vectors.
   - For example, if you have two vectors \( \mathbf{u} = [u_1, u_2, \ldots, u_n] \) and \( \mathbf{v} = [v_1, v_2, \ldots, v_n] \), their sum \( \mathbf{w} \) is given by:
     \[
     \mathbf{w} = \mathbf{u} + \mathbf{v} = [u_1 + v_1, u_2 + v_2, \ldots, u_n + v_n]
     \]

2. **Scalar Multiplication**:
   - Scalar multiplication involves multiplying each component of a vector by a scalar (a single number).
   - For a scalar \( c \) and a vector \( \mathbf{v} = [v_1, v_2, \ldots, v_n] \), the result \( \mathbf{w} \) is:
     \[
     \mathbf{w} = c \mathbf{v} = [c \cdot v_1, c \cdot v_2, \ldots, c \cdot v_n]
     \]

3. **Dot Product (Inner Product)**:
   - The dot product is a measure of the cosine of the angle between two vectors and is a scalar.
   - For two vectors \( \mathbf{u} = [u_1, u_2, \ldots, u_n] \) and \( \mathbf{v} = [v_1, v_2, \ldots, v_n] \), the dot product is:
     \[
     \mathbf{u} \cdot \mathbf{v} = u_1 v_1 + u_2 v_2 + \ldots + u_n v_n
     \]

4. **Cross Product** (only in 3 dimensions):
   - The cross product of two 3-dimensional vectors results in another vector that is perpendicular to both.
   - For two vectors \( \mathbf{u} = [u_1, u_2, u_3] \) and \( \mathbf{v} = [v_1, v_2, v_3] \), the cross product \( \mathbf{w} \) is:
     \[
     \mathbf{w} = \mathbf{u} \times \mathbf{v} = \left( u_2 v_3 - u_3 v_2, u_3 v_1 - u_1 v_3, u_1 v_2 - u_2 v_1 \right)
     \]

5. **Vector Subtraction**:
   - Subtracting one vector from another involves subtracting corresponding components.
   - For vectors \( \mathbf{u} = [u_1, u_2, \ldots, u_n] \) and \( \mathbf{v} = [v_1, v_2, \ldots, v_n] \), the difference \( \mathbf{w} \) is:
     \[
     \mathbf{w} = \mathbf{u} - \mathbf{v} = [u_1 - v_1, u_2 - v_2, \ldots, u_n - v_n]
     \]

6. **Magnitude (Norm) of a Vector**:
   - The magnitude or Euclidean norm of a vector \( \mathbf{v} = [v_1, v_2, \ldots, v_n] \) is:
     \[
     \|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2 + \ldots + v_n^2}
     \]

Understanding these operations is crucial for performing more complex computations and analyses in linear algebra.

---
[Back to index](index.html)
