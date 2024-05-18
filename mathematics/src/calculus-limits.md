---
title: Limits
---

[Back to index](index.html)

---
# Calculus
## Limits

In calculus, the concept of a limit is fundamental and serves as the foundation for defining derivatives and integrals.

### What is a Limit?

A limit describes the value that a function (or sequence) approaches as the input (or index) approaches some value. In more intuitive terms, it’s about figuring out what value a function gets close to as the inputs get close to a certain point.

### Formal Definition

For a function \( f(x) \), the limit of \( f(x) \) as \( x \) approaches some value \( c \) is \( L \), written as:

\[ \lim_{{x \to c}} f(x) = L \]

This means that as \( x \) gets closer and closer to \( c \), \( f(x) \) gets closer and closer to \( L \).

### Left-Hand and Right-Hand Limits

- **Left-Hand Limit**: The value that \( f(x) \) approaches as \( x \) approaches \( c \) from the left (denoted as \( x \to c^- \)).
- **Right-Hand Limit**: The value that \( f(x) \) approaches as \( x \) approaches \( c \) from the right (denoted as \( x \to c^+ \)).

For a limit to exist, both the left-hand limit and the right-hand limit must exist and be equal.

### Properties of Limits

1. **Sum Rule**:
   \[ \lim_{{x \to c}} [f(x) + g(x)] = \lim_{{x \to c}} f(x) + \lim_{{x \to c}} g(x) \]

2. **Difference Rule**:
   \[ \lim_{{x \to c}} [f(x) - g(x)] = \lim_{{x \to c}} f(x) - \lim_{{x \to c}} g(x) \]

3. **Product Rule**:
   \[ \lim_{{x \to c}} [f(x) \cdot g(x)] = \lim_{{x \to c}} f(x) \cdot \lim_{{x \to c}} g(x) \]

4. **Quotient Rule**:
   \[ \lim_{{x \to c}} \left( \frac{{f(x)}}{g(x)} \right) = \frac{{\lim_{{x \to c}} f(x)}}{{\lim_{{x \to c}} g(x)}} \quad \text{(provided } \lim_{{x \to c}} g(x) \ne 0) \]

5. **Constant Multiple Rule**:
   \[ \lim_{{x \to c}} [k \cdot f(x)] = k \cdot \lim_{{x \to c}} f(x) \]

### Techniques for Evaluating Limits

1. **Direct Substitution**: Substitute \( x = c \) into the function.
   
2. **Factoring**: Factor the function and simplify before taking the limit.
   
3. **Rationalization**: Multiply by a conjugate if dealing with limits involving square roots.
   
4. **L'Hôpital's Rule**: When limits result in indeterminate forms like \( \frac{0}{0} \) or \( \frac{\infty}{\infty} \), L'Hôpital's Rule can be used:
   \[ \lim_{{x \to c}} \frac{f(x)}{g(x)} = \lim_{{x \to c}} \frac{f'(x)}{g'(x)} \]
   (provided certain conditions are met).

### Understanding Limits Graphically

You can often understand limits by looking at the graph of the function and seeing what value the function approaches as you get closer to \( c \). For example, if the function values get closer to \( 2 \) as \( x \) approaches \( 1 \), then the limit is \( 2 \).

### Examples

1. **Simple Polynomial**:
   \[ \lim_{{x \to 3}} (2x + 1) = 2(3) + 1 = 7 \]

2. **Indeterminate Form**:
   Evaluate \( \lim_{{x \to 2}} \frac{x^2 - 4}{x - 2} \):
   \[ \frac{x^2 - 4}{x - 2} = \frac{(x - 2)(x + 2)}{x - 2} = x + 2 \]
   So, \( \lim_{{x \to 2}} (x + 2) = 4 \).

Understanding limits is crucial for advanced calculus topics, including differentiation and integration.


---
[Back to index](index.html)
