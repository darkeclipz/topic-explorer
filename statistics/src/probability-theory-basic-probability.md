---
title: Basic Probability
---

[Back to index](index.html)

---
# Probability Theory
## Basic Probability

Sure, basic probability is a fundamental concept in statistics and mathematics that deals with the likelihood or chance of different outcomes. Here are some key aspects of basic probability:

### 1. **Definition of Probability:**
   - **Probability (P):** A measure of how likely an event is to occur, ranging from 0 (impossible event) to 1 (certain event).

### 2. **Sample Space (S):**
   - The set of all possible outcomes of a random experiment. 
     - Example: For a coin toss, the sample space is \( S = \{ \text{Heads}, \text{Tails} \} \).

### 3. **Event (E):**
   - A subset of the sample space. It represents one or more outcomes.
     - Example: In rolling a die, the event of rolling an even number is \( E = \{2, 4, 6\} \).

### 4. **Types of Events:**
   - **Independent Events:** Two events are independent if the occurrence of one does not affect the occurrence of the other.
     - Example: Tossing a coin and rolling a die.
   - **Mutually Exclusive Events:** Two events are mutually exclusive if they cannot occur at the same time.
     - Example: Drawing an Ace and drawing a King from a standard deck of cards.

### 5. **Basic Probability Formulas:**
   - **Probability of an event \( E \):** 
     \[
     P(E) = \frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}}
     \]

   - **Complementary Events:**
     \[
     P(E') = 1 - P(E)
     \]
     where \( E' \) is the complement of event \( E \), which means \( E' \) is the event that \( E \) does not occur.

   - **Addition Rule for Mutually Exclusive Events:**
     \[
     P(A \cup B) = P(A) + P(B)
     \]
     where \( A \cup B \) is the event that either \( A \) or \( B \) or both occur.

   - **General Addition Rule:**
     \[
     P(A \cup B) = P(A) + P(B) - P(A \cap B)
     \]
     where \( A \cap B \) is the event that both \( A \) and \( B \) occur.

   - **Multiplication Rule for Independent Events:**
     \[
     P(A \cap B) = P(A) \times P(B)
     \]

### 6. **Conditional Probability:**
   - The probability of an event occurring given that another event has occurred is called conditional probability.
     \[
     P(A | B) = \frac{P(A \cap B)}{P(B)}
     \]
     where \( P(A | B) \) is the probability of event \( A \) occurring given that \( B \) has occurred.

### 7. **Bayes’ Theorem:**
   - A powerful formula for finding probabilities that incorporates conditional probabilities.
     \[
     P(A | B) = \frac{P(B | A) \times P(A)}{P(B)}
     \]

### 8. **Law of Total Probability:**
   - If \( B_1, B_2, \dots, B_n \) are mutually exclusive events that cover the entire sample space, i.e., \( P(B_1 \cup B_2 \cup \dots \cup B_n) = 1 \), then for any event \( A \),
     \[
     P(A) = P(A \cap B_1) + P(A \cap B_2) + \cdots + P(A \cap B_n)
     \]
   - In a simpler form:
     \[
     P(A) = \sum_{i=1}^{n} P(A | B_i) P(B_i)
     \]

By understanding these fundamental principles, you can analyze random experiments and make informed predictions about the likelihood of various outcomes.

---
[Back to index](index.html)
