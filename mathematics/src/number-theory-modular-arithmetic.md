---
title: Modular Arithmetic
---

[Back to index](index.html)

---
# Number Theory
## Modular Arithmetic

Modular arithmetic is a system of arithmetic for integers, where numbers "wrap around" after reaching a certain value, called the modulus. It is a foundational concept in number theory and has many applications in computer science, cryptography, and coding theory.

### Key Concepts in Modular Arithmetic:

1. **Modulus**:
   - The modulus is a positive integer \( n \) that defines the range of numbers. In modular arithmetic, when you reach \( n \), you wrap around back to 0.
   - Example: In modulo 5 arithmetic, the numbers are 0, 1, 2, 3, and 4. After 4 comes 0 again.

2. **Congruence**:
   - Two integers \( a \) and \( b \) are said to be congruent modulo \( n \) if their difference \( a - b \) is divisible by \( n \).
   - This is written as \( a \equiv b \ (\text{mod} \ n) \).
   - Example: \( 17 \equiv 2 \ (\text{mod} \ 5) \) because \( 17 - 2 = 15 \) is divisible by 5.

3. **Addition, Subtraction, and Multiplication**:
   - The basic operations of addition, subtraction, and multiplication can be performed as usual and then the result is taken modulo \( n \).
   - Example (mod 7):
     - Addition: \( 4 + 5 \equiv 9 \equiv 2 \ (\text{mod} \ 7) \)
     - Subtraction: \( 4 - 5 \equiv -1 \equiv 6 \ (\text{mod} \ 7) \)
     - Multiplication: \( 3 \times 5 \equiv 15 \equiv 1 \ (\text{mod} \ 7) \)

4. **Inverse**:
   - An integer \( a \) has a multiplicative inverse modulo \( n \) if there exists an integer \( b \) such that \( a \times b \equiv 1 \ (\text{mod} \ n) \).
   - The inverse exists if and only if \( a \) and \( n \) are coprime (i.e., \( \gcd(a, n) = 1 \)).
   - Example: The inverse of 3 modulo 7 is 5 because \( 3 \times 5 \equiv 15 \equiv 1 \ (\text{mod} \ 7) \).

5. **Division**:
   - Division in modular arithmetic is performed by multiplying by the modular multiplicative inverse.
   - Example: To divide 3 by 2 modulo 7, first find the inverse of 2 modulo 7, which is 4, then compute \( 3 \times 4 \equiv 12 \equiv 5 \ (\text{mod} \ 7) \).

### Applications of Modular Arithmetic:

1. **Cryptography**:
   - Used in encryption algorithms like RSA, Diffie-Hellman key exchange, and elliptic curve cryptography.

2. **Computer Science**:
   - While working with cyclic data structures like circular buffers, hash tables, and for implementing random number generators.

3. **Algorithms**:
   - Used in algorithms for finding the greatest common divisor (Euclidean algorithm), solving linear congruences, and in modular exponentiation.

4. **Coding Theory**:
   - Essential in error detection and correction algorithms.

To summarize, modular arithmetic is a critical concept with widespread applications in various fields involving computations and helps in understanding the properties of integers under division, aiding in both theoretical and practical problems.

---
[Back to index](index.html)
