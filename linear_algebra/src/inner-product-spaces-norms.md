---
title: Norms
---

[Back to index](index.html)

---
# Inner Product Spaces
## Norms

In the context of inner product spaces, norms are a way to measure the "size" or "length" of vectors. Essentially, norms provide a way to quantify the magnitude of a vector within an inner product space. Here's a detailed explanation:

### Definition of Norms
A norm is a function \(\|\cdot\|\) that assigns a non-negative scalar to each vector in such a way that certain properties (axioms) are satisfied. For a vector space \(V\) over the field \(\mathbb{R}\) or \(\mathbb{C}\), a function \(\|\cdot\| : V \rightarrow \mathbb{R}\) is called a norm if it satisfies the following properties for all vectors \( \mathbf{u}, \mathbf{v} \in V \) and all scalars \( \alpha \in \mathbb{R} \) or \( \mathbb{C} \):

1. **Non-negativity (Positivity)**: 
   \[
   \|\mathbf{v}\| \geq 0 \quad \text{and} \quad \|\mathbf{v}\| = 0 \iff \mathbf{v} = \mathbf{0}
   \]
2. **Scalar Multiplication**:
   \[
   \|\alpha \mathbf{v}\| = |\alpha| \|\mathbf{v}\|
   \]
3. **Triangle Inequality**:
   \[
   \|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|
   \]

### Norm Induced by an Inner Product
In inner product spaces, norms can be induced by an inner product. If \( \langle \cdot , \cdot \rangle \) denotes the inner product, the norm can be defined as:
   \[
   \|\mathbf{v}\| = \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle}
   \]
This definition satisfies the properties of a norm mentioned above. Let's ensure that these properties hold for this specific definition:

1. **Non-negativity**:
   Since \( \langle \mathbf{v}, \mathbf{v} \rangle \) is non-negative and equals zero if and only if \( \mathbf{v} \) is the zero vector, it follows that \(\|\mathbf{v}\|\) is non-negative and equals zero if and only if \( \mathbf{v} = \mathbf{0} \).

2. **Scalar Multiplication**:
   For a scalar \( \alpha \):
   \[
   \|\alpha \mathbf{v}\| = \sqrt{\langle \alpha \mathbf{v}, \alpha \mathbf{v} \rangle} = \sqrt{|\alpha|^2 \langle \mathbf{v}, \mathbf{v} \rangle} = |\alpha| \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle} = |\alpha| \|\mathbf{v}\|
   \]

3. **Triangle Inequality**:
   This property can be derived from the Cauchy-Schwarz inequality:
   \[
   \|\mathbf{u} + \mathbf{v}\|^2 = \langle \mathbf{u} + \mathbf{v}, \mathbf{u} + \mathbf{v} \rangle \leq \big(\|\mathbf{u}\| + \|\mathbf{v}\|\big)^2
   \]
Therefore, taking the square root of both sides yields:
   \[
   \|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|
   \]

### Common Examples of Norms
1. **Euclidean Norm (L2 Norm)**:
   \[
   \|\mathbf{v}\|_2 = \sqrt{v_1^2 + v_2^2 + \ldots + v_n^2}
   \]
   This is the most common norm, corresponding to the usual notion of distance in Euclidean space derived from the dot product.

2. **Manhattan Norm (L1 Norm)**:
   \[
   \|\mathbf{v}\|_1 = |v_1| + |v_2| + \ldots + |v_n|
   \]

3. **Max Norm (L∞ Norm)**:
   \[
   \|\mathbf{v}\|_\infty = \max (|v_1|, |v_2|, \ldots, |v_n|)
   \]

### Conclusion
Norms are crucial in both theoretical and applied mathematics as they provide a means to measure vector magnitudes, which is fundamental for convergences, optimizations, and numerical computations. In inner product spaces, norms induced by inner products provide an elegant and consistent way to measure vector lengths, harmonizing with the geometric intuition of distance and angle.

---
[Back to index](index.html)
