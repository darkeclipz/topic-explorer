---
title: Model Theory
---

[Back to index](index.html)

---
# Mathematical Logic
## Model Theory

Model Theory is a branch of mathematical logic that deals with the relationship between formal languages (such as those used in logic and algebra) and their interpretations or models. Here are the key components and concepts of Model Theory:

### Key Concepts

1. **Language and Syntax**: 
   - **Formal Language**: A set of symbols and rules for forming expressions (sentences, formulas) in a given logical system.
   - **Syntax**: The formal rules that govern the structure of these expressions.

2. **Structures and Semantics**:
   - **Structure (Model)**: An interpretation of a formal language that assigns meanings to its symbols and formulas. A structure consists of a domain (a set of objects) and interpretations of functions, relations, and constants defined in the language.
   - **Semantic Truth**: A formula is considered true in a structure if it holds true when the symbols in the formula are interpreted according to the structure.

3. **Satisfaction**:
   - A structure **M** satisfies a formula **φ** (denoted as **M ⊨ φ**) if φ is true in M given the interpretation of its symbols.
   - A set of sentences is satisfiable if there is some model in which all the sentences are true.

4. **Elementary Equivalence and Elementary Embeddings**:
   - **Elementary Equivalence**: Two structures are elementarily equivalent if they satisfy exactly the same first-order sentences.
   - **Elementary Embedding**: A map between structures that preserves the truth of all sentences (formulas) in the language.

5. **Theories**:
   - A **theory** is a set of sentences in a formal language.
   - A theory is **complete** if, for every sentence in the language, the sentence or its negation is provable from the theory.
   - A theory is **consistent** if it does not lead to a contradiction (i.e., it does not prove both a sentence and its negation).

### Fundamental Theorems

1. **Completeness Theorem**: 
   - States that if a formula is true in every model of a given theory, then there is a proof of that formula from the axioms of the theory.

2. **Compactness Theorem**:
   - If every finite subset of a set of sentences is satisfiable, then the entire set is satisfiable.

3. **Löwenheim-Skolem Theorems**:
   - **Downward Löwenheim-Skolem Theorem**: If a countable first-order theory has an infinite model, it has a countable model.
   - **Upward Löwenheim-Skolem Theorem**: If a first-order theory has an infinite model, it has models of every infinite cardinality.

## Applications

1. **Mathematical Structures**: Analysis of algebraic structures such as groups, rings, and fields.
2. **Computer Science**: Development of formal verification methods, model checking, and specification languages.
3. **Philosophy**: Investigation of the nature of mathematical truth and the foundations of mathematics.

### Example

If you have a language with a single binary relation symbol **R**, a model (structure) could be a set with a specific interpretation of **R**. For instance, if the domain is the set of natural numbers, **R** could be interpreted as the "less than" relation.

Understanding how different models satisfy the same or different sets of sentences can reveal much about the models themselves and the logical systems they inhabit.

In summary, Model Theory provides the tools to study the connections between syntactic expressions and their semantic interpretations, revealing deep insights into the nature of mathematical and logical structures.

---
[Back to index](index.html)
