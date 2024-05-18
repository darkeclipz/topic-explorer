---
title: Logic Programming
---

[Back to index](index.html)

---
# Programming Paradigms
## Logic Programming

### Logic Programming (Programming Paradigms)

**Logic Programming** is a type of programming paradigm which is largely based on formal logic. Unlike procedural or object-oriented paradigms, logic programming uses logic formulas to express computation. The primary language associated with logic programming is Prolog (Programming in Logic).

#### Key Concepts:

1. **Declarative Nature**:
   - In logic programming, you describe *what* the program should accomplish rather than *how* to accomplish it.
   - You declare facts and rules about problems in the form of logical statements.

2. **Facts and Rules**:
   - **Facts**: Basic assertions about objects or relationships. For example, `sibling(jane, john).` asserts that Jane and John are siblings.
   - **Rules**: Conditional statements that define relationships between facts. For example, `parent(X, Y) :- mother(X, Y).` asserts that X is a parent of Y if X is the mother of Y.

3. **Query**:
   - The program computes by evaluating queries against the declared facts and rules.
   - For example, you can query `?- sibling(jane, Who).` and the program will return all individuals that are siblings of Jane.

4. **Resolution and Unification**:
   - **Resolution**: The process used by the logic programming engine to infer conclusions from known facts and rules.
   - **Unification**: The process of determining variable bindings which make different logical expressions identical.

5. **Backtracking**:
   - Logic programming systems often use backtracking to search for solutions by trying different possibilities and undoing choices (backtracking) when they lead to dead ends.

#### Advantages:

1. **Clarity and Expressiveness**:
   - Programs are closer to human logical reasoning and can be more intuitive for expressing certain types of problems.

2. **Automatic Inference**:
   - The system can automatically infer new facts from existing ones using the provided rules, reducing the need for explicit instructions.

3. **Flexibility**:
   - Suitable for complex problem-solving tasks like theorem proving, natural language processing, and expert systems.

#### Criticisms:

1. **Performance**:
   - Logic programming can be less efficient than procedural programming for certain tasks due to the overhead associated with logical inference and backtracking.

2. **Scalability**:
   - Programs can become difficult to manage and scale as the number of facts and rules grows.

3. **Specialized Use**:
   - It's more suited for specific areas like artificial intelligence rather than general-purpose application development.

#### Languages:

- **Prolog**: The most well-known logic programming language.
- **Datalog**: A subset of Prolog, often used for database queries.
- **Answer Set Programming (ASP)**: A form of logic programming oriented towards difficult search problems.

Example in Prolog:

```prolog
% Facts
parent(john, mary).
parent(mary, ann).

% Rules
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

% Query
% ?- grandparent(john, ann).
% The Prolog interpreter will return 'true'.
```

In this example, the fact `parent(john, mary)` states that John is Mary's parent, and the fact `parent(mary, ann)` states that Mary is Ann's parent. The rule `grandparent(X, Y)` states that X is a grandparent of Y if X is a parent of Z and Z is a parent of Y. When querying `?- grandparent(john, ann).`, the system will deduce that John is Ann's grandparent based on the given facts and rules.

Logic programming offers a unique way to handle problems that involve complex relationships and rule-based reasoning, making it a powerful tool in the realm of artificial intelligence and beyond.

---
[Back to index](index.html)
