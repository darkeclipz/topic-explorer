---
title: Stacks
---

[Back to index](index.html)

---
# Data Structures
## Stacks

A stack is a fundamental data structure used in programming and computer science, which follows the Last In, First Out (LIFO) principle. Here is a detailed explanation of stacks:

### Core Concepts

1. **LIFO Principle**:
   - The last element added to the stack is the first one to be removed. This is similar to stacking plates; the last plate placed on top is the first to be removed.

2. **Basic Operations**:
   - **Push**: Adds an element to the top of the stack.
   - **Pop**: Removes and returns the top element from the stack.
   - **Peek/Top**: Returns the top element without removing it.
   - **isEmpty**: Checks if the stack is empty.
   - **isFull**: Checks if the stack is full (relevant for stacks with a maximum capacity).

### Implementation Details

Stacks can be implemented using arrays or linked lists. Here’s a brief overview of both:

- **Array-Based Implementation**:
  - An array is used to store stack elements.
  - An integer variable (`top`) is used to keep track of the index of the top element.
  - Efficient for push and pop operations with O(1) time complexity.
  - Limitation: Fixed size; if not dynamic, the maximum size of the stack needs to be defined.

- **Linked List-Based Implementation**:
  - A linked list is used, where each node points to the next node.
  - The top of the stack is typically the head of the linked list.
  - Dynamic size; can grow and shrink as needed.
  - Push and pop operations have O(1) time complexity, but there may be a slight overhead due to pointer manipulation.

### Applications

Stacks are used in various scenarios and algorithms:

- **Function Call Management**: The call stack in programming languages.
- **Expression Evaluation**: For converting infix expressions to postfix or prefix using stacks, and for evaluating postfix expressions.
- **Backtracking Algorithms**: Such as those used in solving puzzles (e.g., Mazes, Sudoku).
- **Undo Mechanisms**: Found in text editors, where the last action can be reverted.
- **Syntax Parsing**: For parsing expressions, particularly in compilers and interpreters.

### Example in Code (Array-Based Implementation in Python)

Here’s a simple implementation of a stack using an array in Python:

```python
class Stack:
    def __init__(self, size):
        self.stack = [None] * size  # Fixed-size stack
        self.top = -1
        self.size = size

    def push(self, item):
        if self.isFull():
            raise Exception("Stack Overflow")
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack Underflow")
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.stack[self.top]

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.size - 1

# Usage
s = Stack(5)
s.push(1)
s.push(2)
print(s.pop())  # Output: 2
print(s.peek()) # Output: 1
```

### Considerations

- **Size Constraints**: When using an array-based stack, be conscious of the stack size limit.
- **Overflow and Underflow**: Proper error handling for when the stack is full (overflow) or empty (underflow) is essential.

Understanding how stacks operate and their implementations helps in solving various computational problems efficiently.

---
[Back to index](index.html)
