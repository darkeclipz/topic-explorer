---
title: Backtracking
---

[Back to index](index.html)

---
# Algorithms
## Backtracking

Backtracking is a general algorithmic technique that is used to solve problems incrementally, by building up candidates to the solutions piece by piece, and abandoning a candidate ("backtracking") as soon as it determines that the candidate cannot possibly be completed to form a valid solution.

Here are the key concepts and steps involved in backtracking:

### Key Concepts:

1. **Candidate Solution**: An incremental solution to the problem that can be built piece by piece. The candidate solution is tested at each step to see if it should be completed or abandoned.

2. **Partial Solution**: A candidate solution that has been built up to a certain point but is not yet complete.

3. **Feasibility**: A function that checks whether a given partial solution is still valid and can possibly lead to a complete and correct solution.

4. **Solution Completion**: A function or condition that checks whether a given partial solution is complete and satisfies all the problem’s requirements.

5. **Backtracking**: The process of abandoning a partial solution and returning (backtracking) to the previous state to try out a different path of the solution space.

### Typical Steps in Backtracking:

1. **Start with an empty candidate solution.**
2. **Extend the candidate solution by adding a new piece:**
   - If the candidate solution is now complete and valid, report it as a solution (or perform the desired action).
   - If the candidate solution is not yet complete but is still valid, recursively attempt to extend it further.
   - If the candidate solution is invalid, abandon it (backtrack) and remove the last added piece.
3. **Repeat the above steps until all possible candidates are generated and tested.**

### Example Problems:

1. **N-Queens Problem**: Place N queens on an N×N chessboard so that no two queens threaten each other. The algorithm tries to place a queen in each row, one by one, and backtracks if placing the queen leads to a conflict.

2. **Maze Solving**: Find a path from the start to the end of a maze. The algorithm tries moving in all possible directions (up, down, left, right) from the current position and backtracks if it hits a wall or a previously visited cell.

3. **Sudoku Solver**: Fill a 9×9 grid so that each row, each column, and each of the nine 3×3 boxes contain the numbers 1 to 9. The algorithm tries placing each number in a cell and backtracks if it leads to an invalid Sudoku state.

### Pseudocode Example:

Here’s a general pseudocode for a backtracking algorithm:

```pseudocode
function backtrack(candidate):
    if candidate is a complete solution:
        report candidate as a solution
        return

    for next in all possible choices for the next step:
        if candidate is still valid after adding next:
            choose next
            backtrack(candidate + next)
            unchoose next  // remove the last added step to try another one
```

### Tips for Implementing Backtracking:

1. **Pruning Early**: Implement feasibility checks early to prune invalid partial solutions as soon as possible.
2. **Memoization**: Cache results of expensive feasibility checks to avoid redundant computations.
3. **Efficient Data Structures**: Use data structures that allow quick modifications and checks, such as sets or bitmasks.

Backtracking is a brute-force approach but can be optimized significantly with smart pruning and efficient feasibility checks. It is a powerful technique used in various combinatorial and constraint satisfaction problems.

---
[Back to index](index.html)
