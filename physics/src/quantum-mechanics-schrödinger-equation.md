---
title: Schrödinger Equation
---

[Back to index](index.html)

---
# Quantum Mechanics
## Schrödinger Equation

The Schrödinger Equation is a fundamental equation in quantum mechanics that describes how the quantum state of a physical system changes over time. Named after the physicist Erwin Schrödinger, who formulated it in 1925, it is one of the key components of quantum theory and provides a way to predict the behavior of particles at the microscopic level.

### Forms of the Schrödinger Equation

There are two main forms of the Schrödinger Equation: the time-dependent Schrödinger Equation and the time-independent Schrödinger Equation.

#### 1. Time-Dependent Schrödinger Equation
The time-dependent Schrödinger Equation describes how the quantum state of a system evolves over time. It is given by:

\[ i\hbar \frac{\partial \psi(\mathbf{r}, t)}{\partial t} = \hat{H} \psi(\mathbf{r}, t) \]

- \( i \) is the imaginary unit.
- \( \hbar \) (h-bar) is the reduced Planck's constant.
- \( \psi(\mathbf{r}, t) \) is the wave function of the system, which depends on position \( \mathbf{r} \) and time \( t \).
- \( \hat{H} \) is the Hamiltonian operator, which represents the total energy of the system (the sum of kinetic and potential energies).

#### 2. Time-Independent Schrödinger Equation
The time-independent Schrödinger Equation is used when the system's Hamiltonian does not depend on time. It is typically used to find the stationary states of a system (i.e., states with definite energy). It is given by:

\[ \hat{H} \psi(\mathbf{r}) = E \psi(\mathbf{r}) \]

- \( E \) is the energy eigenvalue associated with the wave function \( \psi(\mathbf{r}) \).

### Interpretation of the Wave Function

The wave function \( \psi(\mathbf{r}, t) \) contains all the information about the system's state. Its squared magnitude, \( |\psi(\mathbf{r}, t)|^2 \), represents the probability density of finding a particle at position \( \mathbf{r} \) at time \( t \).

### Hamiltonian Operator

The Hamiltonian operator \( \hat{H} \) often includes kinetic and potential energy terms:

\[ \hat{H} = \hat{T} + \hat{V} \]

- \( \hat{T} \) represents the kinetic energy part, which often takes the form \( -\frac{\hbar^2}{2m} \nabla^2 \).
- \( \hat{V} \) represents the potential energy part, which depends on the specific problem.

### Example: Particle in a Potential Well

For a simple one-dimensional potential well, the time-independent Schrödinger Equation might be written as:

\[ -\frac{\hbar^2}{2m} \frac{d^2 \psi(x)}{d x^2} + V(x) \psi(x) = E \psi(x) \]

Where:
- \( m \) is the mass of the particle.
- \( \frac{d^2 \psi(x)}{d x^2} \) is the second derivative of the wave function with respect to position \( x \).
- \( V(x) \) is the potential energy as a function of position.

Solving the Schrödinger Equation allows physicists to determine the allowed energy levels of the system and the corresponding wave functions. These solutions provide deep insights into the behavior and properties of quantum systems, such as atoms, molecules, and subatomic particles.

---
[Back to index](index.html)
