---
title: Searching
---

[Back to index](index.html)

---
# Algorithms
## Searching

Searching algorithms are a fundamental concept in computer science that deal with finding an element within a data structure. These algorithms can be categorized into two main types: sequential (or linear) searches and interval (or binary) searches. Here's an overview of various searching algorithms:

### 1. Linear Search
**Description:** Checks each element in the list sequentially until the target element is found or the end of the list is reached.
**Time Complexity:** O(n), where n is the number of elements in the list.
**Usage:** Suitable for small or unsorted datasets.

#### Example:
```python
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
```

### 2. Binary Search
**Description:** Efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing the list in half and comparing the target value to the middle element.
**Time Complexity:** O(log n), where n is the number of elements in the list.
**Usage:** Requires the list to be sorted beforehand.

#### Example:
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### 3. Depth-First Search (DFS)
**Description:** An algorithm for traversing or searching tree or graph data structures. Starts at the root and explores as far as possible along each branch before backtracking.
**Usage:** Useful for scenarios like solving puzzles or searching in tree/graph structures.

#### Example:
```python
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(set(graph[vertex]) - visited)
    return visited
```

### 4. Breadth-First Search (BFS)
**Description:** Another algorithm for traversing or searching tree or graph data structures. It starts at the root and explores all neighbor nodes at the present depth before moving on to nodes at the next depth level.
**Usage:** Useful for finding the shortest path in unweighted graphs.

#### Example:
```python
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return visited
```

### 5. Exponential Search
**Description:** A combination of binary search and iterative doubling. It works by finding the range where the target element must exist and then performing a binary search within that range.
**Time Complexity:** O(log n), but with an additional cost of O(log n) for finding the range.
**Usage:** Optimal for unbounded or infinite lists.

#### Example:
```python
def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    
    index = 1
    while index < len(arr) and arr[index] <= target:
        index *= 2
    
    return binary_search(arr[0:min(index, len(arr))], target)
```

### 6. Jump Search
**Description:** Works on sorted arrays. It checks elements by jumping ahead by fixed steps and when it finds a high enough value, it performs a linear search backward.
**Time Complexity:** O(√n)
**Usage:** Offers a balance between linear search and binary search.

#### Example:
```python
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1
```

### Conclusion
Each searching algorithm has its strengths and is suitable for different types of datasets and use cases. Understanding the underlying principles of these algorithms helps in selecting the most efficient algorithm for a given problem.

---
[Back to index](index.html)
