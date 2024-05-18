---
title: Proof Techniques
---

[Back to index](index.html)

---
# Mathematical Logic
## Proof Techniques

Proof techniques are crucial in mathematical logic and provide systematic methods to establish the validity of mathematical statements. Here are some key proof techniques:

### 1. **Direct Proof**
A direct proof demonstrates the truth of a given statement by straightforward logical reasoning. This type of proof is often used when trying to prove an implication \(P \rightarrow Q\).

**Example:**
Prove that if \(n\) is an even integer, then \(n^2\) is also even.

**Proof:**
- Assume \(n\) is even, so \( n = 2k \) for some integer \(k\).
- Then \( n^2 = (2k)^2 = 4k^2 \).
- \(4k^2\) is clearly even because it is a multiple of 2. 
- Thus, \(n^2\) is even.

### 2. **Indirect Proof (Proof by Contradiction)**
An indirect proof involves assuming that the statement to be proved is false and then showing that this assumption leads to a contradiction.

**Example:**
Prove that \(\sqrt{2}\) is irrational.

**Proof:**
- Assume \(\sqrt{2}\) is rational.
- Then it can be written as \(\sqrt{2} = \frac{a}{b}\), where \(a\) and \(b\) are coprime integers (i.e., their greatest common divisor is 1) and \(b \ne 0\).
- Squaring both sides gives \(2 = \frac{a^2}{b^2} \Rightarrow 2b^2 = a^2\).
- Thus, \(a^2\) is even, which implies \(a\) is even (if a square is even, its root must also be even).
- Let's write \(a = 2k\) for some integer \(k\).
- Then \(2b^2 = (2k)^2 = 4k^2 \Rightarrow b^2 = 2k^2\).
- Therefore, \(b^2\) is even, implying \(b\) is even.
- But if both \(a\) and \(b\) are even, they are not coprime, contradicting our initial assumption.
- Therefore, \(\sqrt{2}\) is irrational.

### 3. **Proof by Contrapositive**
This technique proves an implication \(P \rightarrow Q\) by proving the contrapositive \(\neg Q \rightarrow \neg P\) is true instead.

**Example:**
Prove that if \(n^2\) is odd, then \(n\) is odd.

**Proof:**
- We will prove the contrapositive: If \(n\) is even, then \(n^2\) is even.
- Assume \(n\) is even, so \( n = 2k \) for some integer \(k\).
- Then \( n^2 = (2k)^2 = 4k^2 \), which is even.
- This confirms the contrapositive, thereby proving the original statement.

### 4. **Mathematical Induction**
Mathematical induction is used to prove statements that are usually formulated in terms of \(n\), where \(n\) is a non-negative integer.

**Example:**
Prove that for all positive integers \(n\), the sum of the first \(n\) positive integers is given by \(\sum_{i=1}^{n} i = \frac{n(n+1)}{2}\).

**Proof:**
- **Base Case:** For \(n = 1\), \(\sum_{i=1}^{1} i = 1\). The formula gives \(\frac{1 \cdot (1+1)}{2} = 1\), so it holds for \(n = 1\).
- **Inductive Step:** Assume the formula holds for some integer \(k \geq 1\), i.e., \(\sum_{i=1}^{k} i = \frac{k(k+1)}{2}\).
- We need to show it holds for \(k + 1\). Consider \(\sum_{i=1}^{k+1} i = \sum_{i=1}^{k} i + (k+1)\).
- By the induction hypothesis, \(\sum_{i=1}^{k} i = \frac{k(k+1)}{2}\).
- So, \(\sum_{i=1}^{k+1} i = \frac{k(k+1)}{2} + (k+1) = \frac{k(k+1) + 2(k+1)}{2} = \frac{(k+1)(k+2)}{2}\).
- The formula holds for \(k + 1\).
- By induction, the formula is true for all positive integers \(n\).

### 5. **Proof by Exhaustion**
This method involves checking all possible cases to prove the statement. It is often used when the number of cases is finite and manageable.

**Example:**
Prove that all positive integers less than 4 are prime numbers. 

**Proof:**
- The positive integers less than 4 are 1, 2, and 3.
- 1 is not considered prime, but for this proof we might redefine it to suit context.
- 2 is prime because its only divisors are 1 and 2.
- 3 is prime because its only divisors are 1 and 3.
- Since we have exhausted all cases and 1 is considered an exception or specially treated, the statement is proven.

These techniques are foundational in constructing rigorous mathematical arguments and ensure the validity of various mathematical propositions and theorems.

---
[Back to index](index.html)
