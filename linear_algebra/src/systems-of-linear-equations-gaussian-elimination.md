---
title: Gaussian Elimination
---

[Back to index](index.html)

---
# Systems of Linear Equations
## Gaussian Elimination

Gaussian Elimination is a systematic method used for solving systems of linear equations. It transforms the system into an upper triangular matrix form (Row Echelon Form), from which the solutions can be easily obtained through back substitution. Below are the key steps involved in Gaussian Elimination:

### Step-by-Step Process

1. **Form the Augmented Matrix:**
   - Combine the coefficients of the variables and the constants on the right-hand side of the equations into a single matrix.

   For a system of linear equations:

     \[
     \begin{cases}
     a_{11}x + a_{12}y + a_{13}z = b_1 \\
     a_{21}x + a_{22}y + a_{23}z = b_2 \\
     a_{31}x + a_{32}y + a_{33}z = b_3 \\
     \end{cases}
     \]

   The augmented matrix is:

     \[
     \begin{pmatrix}
     a_{11} & a_{12} & a_{13} & | & b_1 \\
     a_{21} & a_{22} & a_{23} & | & b_2 \\
     a_{31} & a_{32} & a_{33} & | & b_3 \\
     \end{pmatrix}
     \]

2. **Forward Elimination (Transform to Row Echelon Form):**
   - Use elementary row operations to form zeros below the main diagonal of the matrix.
     1. **Pivoting:**
        - Swap rows, if necessary, to place the largest absolute value of the column at the diagonal position to reduce numerical errors (partial pivoting).
     2. **Eliminate Elements Below Pivot:**
        - For each row \(i\) from \(1\) to \(n-1\), for each row \(j\) from \(i+1\) to \(n\):
          - Subtract a multiple of row \(i\) from row \(j\) to make the element below the pivot (pivot element at position \(a_{ii}\)) zero.
          - The multiple is \( m_{ji} = \frac{a_{ji}}{a_{ii}} \).
          - Update row \(j\): \( \text{Row}_j = \text{Row}_j - m_{ji} \times \text{Row}_i \).

3. **Back Substitution:**
   - Once the matrix is in upper triangular form, solve for variables starting from the last row (equation) and moving upwards.
   - For the \(i\)-th equation: \( a_{ii}x_i = b_i - \sum_{j=i+1}^{n} a_{ij}x_j \).
   - \( x_i = \frac{b_i - \sum_{j=i+1}^{n} a_{ij}x_j}{a_{ii}} \).

### Example

Solve the system of equations:

\[
\begin{cases}
2x + 3y + z = 1 \\
4x + y - 2z = -2 \\
-6x + 2y + z = 10 \\
\end{cases}
\]

1. Form the Augmented Matrix:

\[
\begin{pmatrix}
2 & 3 & 1 & | & 1 \\
4 & 1 & -2 & | & -2 \\
-6 & 2 & 1 & | & 10 \\
\end{pmatrix}
\]

2. Use Forward Elimination:

- Make the element in the first column of the second row zero:

\[
\text{Row}_2 = \text{Row}_2 - 2 \times \text{Row}_1 \rightarrow (4 - 4, 1 - 6, -2 - 2, -2 - 2) = (0, -5, -4, -4)
\]

- Make the element in the first column of the third row zero:

\[
\text{Row}_3 = \text{Row}_3 + 3 \times \text{Row}_1 \rightarrow (-6 + 6, 2 + 9, 1 + 3, 10 + 3) = (0, 11, 4, 13)
\]

The matrix becomes:

\[
\begin{pmatrix}
2 & 3 & 1 & | & 1 \\
0 & -5 & -4 & | & -4 \\
0 & 11 & 4 & | & 13 \\
\end{pmatrix}
\]

- Now, eliminate the element in the second column of the third row:

\[
\text{Row}_3 = \text{Row}_3 + \frac{11}{-5} \times \text{Row}_2 \rightarrow (0, 0, \frac{-44}{-5} + 4, \frac{-44}{5} + 13) = (0, 0, \frac{20}{5}, \frac{21}{5})
\]

The matrix becomes:

\[
\begin{pmatrix}
2 & 3 & 1 & | & 1 \\
0 & -5 & -4 & | & -4 \\
0 & 0 & 4.4 & | & 4.6 \\
\end{pmatrix}
\]

3. Perform Back Substitution:

- From the third row: \( 4.4z = 4.6 \rightarrow z = \frac{4.6}{4.4} \approx 1 \)
- From the second row: \( -5y - 4z = -4 \rightarrow -5y - 4 \times 1 = -4 \rightarrow -5y - 4 = -4 \rightarrow y = 0 \)
- From the first row: \( 2x + 3y + z = 1 \rightarrow 2x + 1 = 1 \rightarrow x = 0 \)

Therefore, \( x = 0 \), \( y = 0 \), \( z \approx 1 \).

### Conclusion

Gaussian elimination, with its forward elimination and back substitution steps, systematically reduces a system of linear equations to a form that is easily solvable. The method, when combined with partial pivoting, is very robust and widely used for computational solutions of linear systems.

---
[Back to index](index.html)
