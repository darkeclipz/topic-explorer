---
title: Gram-Schmidt Process
---

[Back to index](index.html)

---
# Orthogonality
## Gram-Schmidt Process

The Gram-Schmidt process is an algorithm used in linear algebra to take a set of linearly independent vectors and transform them into an orthogonal (or orthonormal) set of vectors that span the same subspace. This is particularly useful in various applications such as numerical methods, statistics, and signal processing.

Here's a step-by-step explanation of the Gram-Schmidt process:

### Step-by-Step Process

1. **Input Vectors:**
   - Start with a set of linearly independent vectors \(\{v_1, v_2, \ldots, v_n\}\) in an inner product space (usually \(\mathbb{R}^n\)).

2. **Initialization:**
   - Initialize the first orthogonal vector \(u_1\) such that \(u_1 = v_1\).

3. **Orthogonalization:**
   - For each vector \(v_k\) where \(2 \le k \le n\), compute the orthogonal components by subtracting the projections of \(v_k\) on all previously computed orthogonal vectors \(u_1, u_2, \ldots, u_{k-1}\).

   The formula for computing the orthogonal vector \(u_k\) is:
   \[
   u_k = v_k - \sum_{j=1}^{k-1} \text{proj}_{u_j}(v_k)
   \]
   where the projection of \(v_k\) onto \(u_j\) is given by:
   \[
   \text{proj}_{u_j}(v_k) = \frac{\langle v_k, u_j \rangle}{\langle u_j, u_j \rangle} u_j
   \]

4. **Normalization (Optional):**
   - If an orthonormal set is desired instead of just an orthogonal set, normalize each \(u_k\) to get \(e_k\):
   \[
   e_k = \frac{u_k}{\|u_k\|}
   \]
   where \(\|u_k\|\) is the norm of \(u_k\).

### Example

Let's illustrate the Gram-Schmidt process with an example. Consider the vectors \( \{v_1, v_2\} \) in \(\mathbb{R}^2\):
\[
v_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \quad v_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}
\]

1. **Step 1: Initialize**
   \[
   u_1 = v_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}
   \]

2. **Step 2: Orthogonalization**
   \[
   \text{proj}_{u_1}(v_2) = \frac{\langle v_2, u_1 \rangle}{\langle u_1, u_1 \rangle} u_1 = \frac{(1)(1) + (-1)(1)}{1^2 + 1^2} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = 0 \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
   \]

   \[
   u_2 = v_2 - \text{proj}_{u_1}(v_2) = \begin{pmatrix} 1 \\ -1 \end{pmatrix} - \begin{pmatrix} 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}
   \]

3. **Step 3: Normalization (if orthonormality is required)**
   \[
   e_1 = \frac{u_1}{\|u_1\|} = \frac{\begin{pmatrix} 1 \\ 1 \end{pmatrix}}{\sqrt{1^2 + 1^2}} = \frac{\begin{pmatrix} 1 \\ 1 \end{pmatrix}}{\sqrt{2}} = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix}
   \]

   \[
   e_2 = \frac{u_2}{\|u_2\|} = \frac{\begin{pmatrix} 1 \\ -1 \end{pmatrix}}{\sqrt{1^2 + (-1)^2}} = \frac{\begin{pmatrix} 1 \\ -1 \end{pmatrix}}{\sqrt{2}} = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{-1}{\sqrt{2}} \end{pmatrix}
   \]

### Result

The set of orthogonal vectors is:
\[
\{ \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \end{pmatrix} \}
\]

The orthonormal set is:
\[
\{ \begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix}, \begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{-1}{\sqrt{2}} \end{pmatrix} \}
\]

The Gram-Schmidt process ensures that vectors in the resulting set are orthogonal (or orthonormal if normalized), making it easier to work with them in various applications such as solving linear systems, performing projections, and more.

---
[Back to index](index.html)
