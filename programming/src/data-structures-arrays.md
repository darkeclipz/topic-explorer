---
title: Arrays
---

[Back to index](index.html)

---
# Data Structures
## Arrays

Sure, here's an explanation of arrays in data structures:

### Arrays

**Definition:**
An array is a data structure that holds a fixed number of elements of the same data type in a contiguous block of memory. It's one of the simplest and most commonly used data structures.

**Key Characteristics:**
1. **Fixed Size:** The size of an array is defined at the time of its declaration and cannot be changed dynamically.
2. **Indexed Access:** Each element in the array is identified by an index, typically starting from 0 up to \( n-1 \) (where \( n \) is the size of the array).
3. **Homogeneous Elements:** All elements in an array are of the same data type (e.g., all integers, all floating-point numbers, etc.).
4. **Contiguous Memory Allocation:** Elements of the array are stored in contiguous memory locations.

**Advantages:**
1. **Fast Access:** Accessing an element by its index takes constant time, \( O(1) \).
2. **Efficient Iteration:** It is easy to iterate through the array elements.
3. **Memory Efficiency:** Arrays provide a compact structure to store similar elements, with minimal memory overhead.

**Disadvantages:**
1. **Fixed Size:** Once an array is created, its size cannot be changed.
2. **Costly Insertions and Deletions:** Adding or removing elements (except at the end) requires shifting other elements, which can be time-consuming, taking \( O(n) \) time.
3. **Wasted Space:** If the array is not fully utilized, there can be wasted memory.

**Common Operations:**
1. **Accessing Elements:** Accessing an element by index is direct and takes constant time.
   ```python
   element = array[index]
   ```
2. **Modifying Elements:** You can modify an element at a specific index.
   ```python
   array[index] = new_value
   ```
3. **Iterating Over Elements:** You can loop through the array elements.
   ```python
   for element in array:
       print(element)
   ```
4. **Inserting Elements:** Inserting elements can be costly as it may require shifting elements.
   ```python
   # Pseudo-code example
   for i from n-1 to index:
       array[i+1] = array[i]
   array[index] = new_value
   ```
5. **Deleting Elements:** Similarly, deleting elements requires shifting.
   ```python
   # Pseudo-code example
   for i from index to n-1:
       array[i] = array[i+1]
   ```

**Examples:**
- **Declaring an Array in Python:**
  ```python
  array = [1, 2, 3, 4, 5]
  ```
- **Accessing Elements:**
  ```python
  first_element = array[0]  # 1
  last_element = array[4]   # 5
  ```
- **Modifying Elements:**
  ```python
  array[2] = 10  # Now array becomes [1, 2, 10, 4, 5]
  ```

**Applications:**
- Arrays are used where data elements have a fixed size and need to be stored contiguously.
- They are the basis for other data structures such as strings, heaps, and hash tables.
- Used in algorithms and various applications like sorting, searching, and dynamic programming.

By understanding arrays, you gain a foundational tool for structuring data in an organized manner, which is essential for efficient algorithm design and implementation.

---
[Back to index](index.html)
