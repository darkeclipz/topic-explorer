---
title: Propositional Logic
---

[Back to index](index.html)

---
# Mathematical Logic
## Propositional Logic

Propositional logic, also known as propositional calculus or statement logic, is a branch of mathematical logic that deals with the manipulation and analysis of propositions—statements that can be either true or false. Here are the key aspects and concepts of propositional logic:

### 1. **Propositions**
- A proposition is a declarative statement that is either true (T) or false (F). For example:
  - "The sky is blue." (can be true or false depending on context)
  - "2 + 2 = 4." (true)
  - "5 is less than 3." (false)

### 2. **Logical Connectives**
- **AND (∧)**: The conjunction of two propositions \(P\) and \(Q\) (written as \(P ∧ Q\)) is true if and only if both \(P\) and \(Q\) are true.
- **OR (∨)**: The disjunction of two propositions \(P\) and \(Q\) (written as \(P ∨ Q\)) is true if at least one of \(P\) or \(Q\) is true.
- **NOT (¬)**: The negation of a proposition \(P\) (written as ¬\(P\)) is true if \(P\) is false.
- **IMPLICATION (→)**: The implication \(P → Q\) is true if \(P\) is false or \(Q\) is true (i.e., it is only false when \(P\) is true and \(Q\) is false).
- **BICONDITIONAL (↔)**: The biconditional \(P ↔ Q\) is true if \(P\) and \(Q\) are both true or both false.

### 3. **Truth Tables**
- Truth tables list the possible truth values of propositions and their combinations:
  - **AND (∧) Truth Table:**
    | P | Q | P ∧ Q |
    |---|---|-------|
    | T | T |   T   |
    | T | F |   F   |
    | F | T |   F   |
    | F | F |   F   |

  - **OR (∨) Truth Table:**
    | P | Q | P ∨ Q |
    |---|---|-------|
    | T | T |   T   |
    | T | F |   T   |
    | F | T |   T   |
    | F | F |   F   |

  - **IMPLICATION (→) Truth Table:**
    | P | Q | P → Q |
    |---|---|-------|
    | T | T |   T   |
    | T | F |   F   |
    | F | T |   T   |
    | F | F |   T   |

  - **NOT (¬) Truth Table:**
    | P | ¬P |
    |---|----|
    | T |  F |
    | F |  T |

### 4. **Logical Equivalences**
- Equivalent propositions have the same truth value in all possible scenarios. Common logical equivalences include:
  - **De Morgan's Laws:**
    - ¬(P ∧ Q) ≡ ¬P ∨ ¬Q
    - ¬(P ∨ Q) ≡ ¬P ∧ ¬Q
  - **Double Negation:**
    - ¬(¬P) ≡ P
  - **Distributive Laws:**
    - P ∧ (Q ∨ R) ≡ (P ∧ Q) ∨ (P ∧ R)
    - P ∨ (Q ∧ R) ≡ (P ∨ Q) ∧ (P ∨ R)

### 5. **Tautologies and Contradictions**
- **Tautology**: A proposition that is true in every possible scenario (e.g., \(P ∨ ¬P\)).
- **Contradiction**: A proposition that is false in every possible scenario (e.g., \(P ∧ ¬P\)).

### 6. **Proof Techniques**
- **Truth Table Method**: Enumerating all possible truth values to show the truth value of complex propositions.
- **Algebraic Method**: Using logical equivalences to transform propositions and prove statements.
- **Direct Proof**: Showing that a proposition leads logically to a conclusion.
- **Indirect Proof** (Contradiction): Assuming the opposite of what you want to prove and showing that this assumption leads to a contradiction.

In summary, propositional logic is fundamental to mathematical logic, computer science, and many areas of philosophy. It provides the basic framework for reasoning about truth and constructs more complex logical systems.

---
[Back to index](index.html)
