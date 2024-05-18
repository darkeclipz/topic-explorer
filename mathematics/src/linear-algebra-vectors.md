---
title: Vectors
---

[Back to index](index.html)

---
# Linear Algebra
## Vectors

Vectors are fundamental objects in linear algebra and are used to represent quantities that have both magnitude and direction. They are an essential tool in many areas of mathematics, physics, engineering, and computer science. Let's delve into some of the key concepts related to vectors:

### 1. **Definition of Vectors**
- **Geometric Interpretation**: In 2D or 3D space, a vector can be represented as an arrow pointing from one point to another. The length of the arrow represents the magnitude, and the direction in which the arrow points represents the direction of the vector.
- **Algebraic Representation**: Vectors can be represented as an ordered list of numbers, for example, \(\mathbf{v} = [v_1, v_2, v_3]\) in 3D space, where \(v_1, v_2,\) and \(v_3\) are the vector components.

### 2. **Vector Notation and Basics**
- **Notation**: Vectors are commonly denoted using bold letters like \(\mathbf{v}\) or with an arrow over the letter like \(\vec{v}\).
- **Zero Vector**: The vector with all components equal to zero, denoted as \(\mathbf{0} = [0, 0, 0]\).

### 3. **Vector Operations**
- **Addition**: Vectors can be added together by adding their corresponding components. If \(\mathbf{u} = [u_1, u_2]\) and \(\mathbf{v} = [v_1, v_2]\), then \(\mathbf{u} + \mathbf{v} = [u_1 + v_1, u_2 + v_2]\).
- **Scalar Multiplication**: A vector can be multiplied by a scalar (a real number) by multiplying each component of the vector by the scalar. For example, if \(k\) is a scalar and \(\mathbf{v} = [v_1, v_2]\), then \(k\mathbf{v} = [kv_1, kv_2]\).

### 4. **Dot Product (Scalar Product)**
- The dot product of two vectors \(\mathbf{u} = [u_1, u_2, u_3]\) and \(\mathbf{v} = [v_1, v_2, v_3]\) is given by:
  \[
  \mathbf{u} \cdot \mathbf{v} = u_1v_1 + u_2v_2 + u_3v_3
  \]
- The dot product is a scalar and measures the extent to which two vectors are aligned. It is zero if the vectors are orthogonal (perpendicular).

### 5. **Cross Product (Vector Product)**
- The cross product is defined only in 3D space and produces a vector that is perpendicular to both of the vectors being multiplied. For \(\mathbf{u} = [u_1, u_2, u_3]\) and \(\mathbf{v} = [v_1, v_2, v_3]\), the cross product \(\mathbf{u} \times \mathbf{v}\) is given by:
  \[
  \mathbf{u} \times \mathbf{v} = \begin{vmatrix}
  \mathbf{i} & \mathbf{j} & \mathbf{k} \\
  u_1 & u_2 & u_3 \\
  v_1 & v_2 & v_3 \\
  \end{vmatrix}
  \]
  This yields:
  \[
  \mathbf{u} \times \mathbf{v} = [(u_2v_3 - u_3v_2), (u_3v_1 - u_1v_3), (u_1v_2 - u_2v_1)]
  \]

### 6. **Magnitude (Norm)**
- The magnitude or length of a vector \(\mathbf{v} = [v_1, v_2, v_3]\) is given by the Euclidean norm:
  \[
  \|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2 + v_3^2}
  \]

### 7. **Unit Vectors**
- A unit vector is a vector with a magnitude of 1, typically used to denote direction. A vector \(\mathbf{v}\) can be converted to a unit vector by dividing it by its magnitude:
  \[
  \hat{\mathbf{v}} = \frac{\mathbf{v}}{\|\mathbf{v}\|}
  \]

### 8. **Vector Projections**
- The projection of vector \(\mathbf{u}\) onto vector \(\mathbf{v}\) is given by:
  \[
  \text{proj}_{\mathbf{v}} \mathbf{u} = \left( \frac{\mathbf{u} \cdot \mathbf{v}}{\mathbf{v} \cdot \mathbf{v}} \right) \mathbf{v}
  \]

### 9. **Applications**
- **Physics**: Vectors are used to represent forces, velocities, and other physical quantities.
- **Computer Graphics**: Vectors represent points, directions, and transformations in 2D and 3D space.
- **Engineering**: Vectors are used in statics and dynamics to analyze forces and movements.

Understanding vectors and their properties is crucial for advancing in more complex topics in linear algebra and its applications in various fields.

---
[Back to index](index.html)
