---
title: Dynamic Programming
---

[Back to index](index.html)

---
# Algorithms
## Dynamic Programming

Dynamic programming (DP) is a method for solving complex problems by breaking them down into simpler subproblems. It is particularly useful for optimization problems, where the goal is to find the best solution among many possible options. The main concept behind dynamic programming is to store the solutions to subproblems so that they do not need to be recomputed when needed later. This helps to reduce the overall computation time.

Here are the key concepts and steps involved in dynamic programming:

### Key Concepts:

1. **Overlapping Subproblems**: DP is effective when the problem can be broken down into subproblems that overlap, meaning that the same subproblems are solved multiple times.

2. **Optimal Substructure**: The optimal solution to the problem can be constructed from the optimal solutions of its subproblems.

3. **Memoization**: This technique involves storing the results of expensive function calls and reusing them when the same inputs occur again. This is typically implemented using a hash table or an array.

4. **Tabulation**: This is a bottom-up approach where solutions to all subproblems are computed iteratively and stored in a table (array) before the overall solution is computed.

### Steps to Solve a Problem Using Dynamic Programming:

1. **Define the Structure of the Optimal Solution**: Break down the original problem into smaller subproblems. Define how the optimal solution of the original problem can be composed from the solutions of these subproblems.

2. **Recursively Define the Optimal Solution**: Develop a recursive formulation for the problem, expressing the solution of the original problem in terms of the solutions of its subproblems.

3. **Compute the Values of Subproblems**: Use memoization (top-down approach) or tabulation (bottom-up approach) to compute the value of each subproblem.

4. **Construct the Optimal Solution**: If needed, reconstruct the solution to the original problem from the computed values of subproblems.

### Example: Fibonacci Number Calculation

One classic example to illustrate dynamic programming is computing the nth Fibonacci number.

#### Recursive Approach (Without DP):

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

This approach has an exponential time complexity because it solves the same subproblems multiple times.

#### Dynamic Programming Approach:

**Memoization (Top-Down Approach):**

```python
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
```

**Tabulation (Bottom-Up Approach):**

```python
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

Both the memoization and tabulation approaches greatly reduce the time complexity to O(n) by storing the results of subproblems.

### Applications of Dynamic Programming:

1. **Knapsack Problem**: Select items to maximize the total value without exceeding the weight limit.
2. **Longest Common Subsequence**: Find the longest subsequence common to two sequences.
3. **Edit Distance**: Measure the similarity between two strings by counting the minimum number of operations needed to transform one string into another.
4. **Matrix Chain Multiplication**: Determine the most efficient way to multiply matrices.
5. **Shortest Path Problems**: Such as the Floyd-Warshall algorithm used in finding shortest paths in a weighted graph.

Dynamic programming is a powerful tool that can be applied to a wide range of problems, making it an essential part of the toolkit for any software developer or computer scientist.

---
[Back to index](index.html)
