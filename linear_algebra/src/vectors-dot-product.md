---
title: Dot Product
---

[Back to index](index.html)

---
# Vectors
## Dot Product

The dot product, also known as the scalar product, is an algebraic operation that takes two equal-length sequences of numbers (usually coordinate vectors) and returns a single number. Here's a detailed explanation of the dot product:

### Definition
Given two vectors \( \mathbf{a} = [a_1, a_2, ... , a_n] \) and \( \mathbf{b} = [b_1, b_2, ..., b_n] \) in an n-dimensional space, the dot product is defined as:
\[ \mathbf{a} \cdot \mathbf{b} = a_1b_1 + a_2b_2 + ... + a_nb_n \]

### Geometric Interpretation
The dot product measures the cosine of the angle between two vectors and gives a result that is proportional to the product of their magnitudes and the cosine of the angle between them. Mathematically, this is expressed as:
\[ \mathbf{a} \cdot \mathbf{b} = \| \mathbf{a} \| \| \mathbf{b} \| \cos(\theta) \]
where:
- \( \| \mathbf{a} \| \) denotes the magnitude (or length) of vector \( \mathbf{a} \),
- \( \| \mathbf{b} \| \) denotes the magnitude of vector \( \mathbf{b} \),
- \( \theta \) is the angle between \( \mathbf{a} \) and \( \mathbf{b} \).

### Properties
1. **Commutative:**
   \[ \mathbf{a} \cdot \mathbf{b} = \mathbf{b} \cdot \mathbf{a} \]
   
2. **Distributive over vector addition:**
   \[ \mathbf{a} \cdot (\mathbf{b} + \mathbf{c}) = \mathbf{a} \cdot \mathbf{b} + \mathbf{a} \cdot \mathbf{c} \]
   
3. **Bilinear:**
   \[ k(\mathbf{a} \cdot \mathbf{b}) = (k\mathbf{a}) \cdot \mathbf{b} = \mathbf{a} \cdot (k\mathbf{b}) \]
   where \( k \) is a scalar.

4. **Orthogonality:**
   \[ \text{If } \mathbf{a} \cdot \mathbf{b} = 0, \text{ then } \mathbf{a} \text{ and } \mathbf{b} \text{ are orthogonal (perpendicular)}. \]
   
### Example
Consider two 3-dimensional vectors \( \mathbf{a} = [1, 2, 3] \) and \( \mathbf{b} = [4, -5, 6] \). The dot product is calculated as follows:
\[
\mathbf{a} \cdot \mathbf{b} = (1 \cdot 4) + (2 \cdot -5) + (3 \cdot 6)
= 4 - 10 + 18
= 12
\]
Thus, the dot product of \( \mathbf{a} \) and \( \mathbf{b} \) is 12.

The dot product is a fundamental tool in linear algebra, with applications in projection, determining orthogonality, and in various computations involving vectors and matrices.

---
[Back to index](index.html)
