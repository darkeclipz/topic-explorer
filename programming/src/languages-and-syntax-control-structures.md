---
title: Control Structures
---

[Back to index](index.html)

---
# Languages and Syntax
## Control Structures

Control structures are fundamental components of programming languages that dictate the flow of execution and control the sequence in which statements and instructions are executed. They enable programmers to specify logic paths based on conditions and loops. Here are the primary types of control structures:

### 1. **Conditional Statements:**
   These structures perform operations based on whether a condition is true or false.

   - **`if` Statement:**
     Executes a block of code if a specified condition is true.
     ```python
     if condition:
         # Code to execute if condition is true
     ```

   - **`else` Statement:**
     Executes a block of code if the `if` condition is false.
     ```python
     if condition:
         # Code to execute if condition is true
     else:
         # Code to execute if condition is false
     ```

   - **`elif` / `else if` Statement:**
     Provides an additional condition to check if the initial `if` condition is false.
     ```python
     if condition1:
         # Code to execute if condition1 is true
     elif condition2:
         # Code to execute if condition2 is true
     else:
         # Code to execute if none of the above conditions is true
     ```

### 2. **Looping Structures:**
   These structures allow repeated execution of a block of code while a condition is true or for a specific number of iterations.

   - **`for` Loop:**
     Iterates over a sequence (such as a list, tuple, dictionary, set, or range).
     ```python
     for item in sequence:
         # Code to execute for each item in sequence
     ```

   - **`while` Loop:**
     Repeats a block of code as long as a condition is true.
     ```python
     while condition:
         # Code to execute as long as condition is true
     ```

   - **`do-while` Loop:**
     Executes a block of code at least once and then repeats the execution as long as the condition is true (not present in certain languages like Python but widely used in C/C++ and Java).
     ```java
     do {
         // Code to execute
     } while (condition);
     ```

### 3. **Jump Statements:**
   These statements transfer control to another part of the program.

   - **`break` Statement:**
     Exits the nearest enclosing loop or switch statement.
     ```python
     for item in sequence:
         if condition:
             break  # Exits the loop
     ```

   - **`continue` Statement:**
     Skips the current iteration of the loop and moves to the next iteration.
     ```python
     for item in sequence:
         if condition:
             continue  # Skips the rest of the code in this iteration
         # More code to execute
     ```

   - **`return` Statement:**
     Exits a function and optionally returns a value to the function caller.
     ```python
     def function_name():
         return value  # Exits the function and returns value
     ```

   - **`goto` Statement:**
     Transfers control to the labeled statement (not recommended and considered harmful as it leads to unmanageable code).
     ```c
     goto label;
     // More code
     label:
     // Code to execute after the jump
     ```

### 4. **Switch Case Statements:**
   Allows a variable to be tested for equality against a list of values (cases).
   ```java
   switch (expression) {
       case value1:
           // Code to execute if expression == value1
           break;
       case value2:
           // Code to execute if expression == value2
           break;
       default:
           // Code to execute if expression doesn't match any case
   }
   ```

These control structures, when combined, provide a robust framework for defining the logical flow and operations in a program. Understanding and effectively utilizing control structures is foundational in writing efficient, readable, and maintainable code.

---
[Back to index](index.html)
