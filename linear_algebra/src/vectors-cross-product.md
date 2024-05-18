---
title: Cross Product
---

[Back to index](index.html)

---
# Vectors
## Cross Product

The cross product, also known as the vector product, is a binary operation on two vectors in three-dimensional space. It results in a vector that is perpendicular to both of the vectors being multiplied, and thus normal to the plane containing them. Here are the key aspects of the cross product:

### Definition:
For two vectors \(\mathbf{a}\) and \(\mathbf{b}\) in 3-dimensional space, the cross product \(\mathbf{a} \times \mathbf{b}\) is defined as:
\[ \mathbf{a} \times \mathbf{b} = \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
a_1 & a_2 & a_3 \\
b_1 & b_2 & b_3
\end{vmatrix} \]

Where \(\mathbf{i}\), \(\mathbf{j}\), and \(\mathbf{k}\) are the unit vectors along the x, y, and z axes, respectively, and \(a_1, a_2, a_3\) and \(b_1, b_2, b_3\) are the components of vectors \(\mathbf{a}\) and \(\mathbf{b}\).

### Calculation:
Expanding the determinant, the cross product can be written as:
\[ \mathbf{a} \times \mathbf{b} = (a_2 b_3 - a_3 b_2) \mathbf{i} - (a_1 b_3 - a_3 b_1) \mathbf{j} + (a_1 b_2 - a_2 b_1) \mathbf{k} \]

### Geometric Interpretation:
1. **Direction**: The resulting vector \(\mathbf{a} \times \mathbf{b}\) is orthogonal (perpendicular) to both \(\mathbf{a}\) and \(\mathbf{b}\). The direction is determined by the right-hand rule: if you point the index finger of your right hand in the direction of \(\mathbf{a}\) and the middle finger in the direction of \(\mathbf{b}\), then your thumb will point in the direction of \(\mathbf{a} \times \mathbf{b}\).
   
2. **Magnitude**: The magnitude (length) of the cross product vector is given by:
\[ |\mathbf{a} \times \mathbf{b}| = |\mathbf{a}| |\mathbf{b}| \sin(\theta) \]
where \(\theta\) is the angle between \(\mathbf{a}\) and \(\mathbf{b}\). The magnitude represents the area of the parallelogram formed by \(\mathbf{a}\) and \(\mathbf{b}\).

### Properties of Cross Product:
1. **Anticommutative**: \(\mathbf{a} \times \mathbf{b} = -(\mathbf{b} \times \mathbf{a})\).
2. **Distributive**: \(\mathbf{a} \times (\mathbf{b} + \mathbf{c}) = \mathbf{a} \times \mathbf{b} + \mathbf{a} \times \mathbf{c}\).
3. **Scalar Multiplication**: \((k \mathbf{a}) \times \mathbf{b} = k (\mathbf{a} \times \mathbf{b})\) for any scalar \(k\).

### Applications:
- **Physics**: Used to calculate torque and angular momentum.
- **Engineering**: Used in computer graphics and CAD software to determine normals to surfaces.
- **Mathematics**: Helps in understanding geometrical and algebraic properties of space.

The cross product is specific to three-dimensional space and does not generalize directly to other dimensions. However, similar operations exist in higher dimensions under different names and with varying properties.

---
[Back to index](index.html)
