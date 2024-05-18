---
title: Integrals
---

[Back to index](index.html)

---
# Calculus
## Integrals

Integrals are a fundamental concept in calculus, often used in various branches of mathematics, physics, engineering, and other sciences. Integrals are broadly classified into definite and indefinite integrals. Here’s an overview of each:

### Indefinite Integrals

**Indefinite integral**:
- The indefinite integral of a function represents a family of functions whose derivative is the given function.
- It is essentially the reverse process of differentiation.
- The notation for an indefinite integral is ∫f(x)dx, which is read as "the integral of f of x with respect to x."

**Example**:
- If f(x) = 2x, an indefinite integral of 2x with respect to x is ∫2x dx = x² + C, where C is the constant of integration.

**Integration rules**:
- **Constant Rule**: ∫a dx = ax + C
- **Power Rule**: ∫xn dx = (xn+1)/(n+1) + C (for n ≠ -1)
- **Sum Rule**: ∫[f(x) + g(x)] dx = ∫f(x) dx + ∫g(x) dx
- **Difference Rule**: ∫[f(x) - g(x)] dx = ∫f(x) dx - ∫g(x) dx
- **Substitution Rule**: Used when integrating composite functions.

### Definite Integrals

**Definite integral**:
- The definite integral of a function over an interval [a, b] gives the net area under the curve of the function from x = a to x = b.
- It is represented by ∫[a, b] f(x) dx, where a and b are the limits of integration.

**Example**:
- If you want to find the area under the curve of f(x) = x² from x = 1 to x = 3, you calculate ∫[1, 3] x² dx.
  
  ∫[1, 3] x² dx = [x³/3] from 1 to 3
                = [(3³/3) - (1³/3)]
                = (27/3) - (1/3)
                = 9 - 1/3
                = 8.67

### Fundamental Theorem of Calculus

The Fundamental Theorem of Calculus links the concept of differentiation and integration in two parts:

1. If F is an antiderivative of f on an interval [a, b], then:
   ∫[a, b] f(x) dx = F(b) - F(a)
   
2. If f is continuous on [a, b] and F is defined by F(x) = ∫[a, x] f(t) dt, then F is differentiable, and F'(x) = f(x).

### Applications of Integrals

1. **Area under a curve**: Calculating the area between the x-axis and the curve of a function.
2. **Volume**: Determining the volume of solids of revolution using methods such as the disk, washer, and shell methods.
3. **Work**: Computing the work done when a force is applied over a distance.
4. **Center of mass**: Finding the center of mass of a system with continuous mass distribution.
5. **Probability**: In statistics, the integral of a probability density function over an interval represents the probability of the variable falling within that interval.

Understanding integrals requires practice and familiarity with various techniques and rules of integration, but they are a powerful tool in solving many real-world problems.

---
[Back to index](index.html)
