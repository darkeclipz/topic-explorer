---
title: Hash Tables
---

[Back to index](index.html)

---
# Data Structures
## Hash Tables

Certainly! Hash tables, also known as hash maps, are a fundamental data structure used in many programming languages because of their efficiency in storing and retrieving data. Here is an explanation of what hash tables are and how they work:

### What is a Hash Table?

A hash table is a collection of key-value pairs, where each key is mapped to a value. The main advantage of using a hash table over other data structures is that it provides very efficient average-case time complexity for lookups, insertions, and deletions, typically O(1).

### Key Concepts

1. **Hash Function**: 
   - A hash function transforms a key into an index in an array (also called a hash table).
   - It takes an input (or key) and returns an integer (hash code), which represents the index in the array where the value associated with the key should be stored.
   - A good hash function evenly distributes the keys across the array to minimize collisions.

2. **Buckets**:
   - Each slot in the array of a hash table is called a bucket.
   - A bucket can store one or more key-value pairs.

3. **Collisions**:
   - A collision occurs when two different keys hash to the same index.
   - Collisions are managed through various techniques like chaining and open addressing.

### Collision Resolution Techniques

1. **Chaining**:
   - Each bucket contains a linked list or another data structure that holds all elements hashed to the same index.
   - When a collision occurs, the new key-value pair is appended to the list existing at that bucket.
   
   ```plaintext
   Hash Table with Chaining
   
   Index 0: [ (key1, value1) ] -> [ (key5, value5) ]
   Index 1: [ (key2, value2) ]
   Index 2: [ (key3, value3) ] -> [ (key4, value4) ]
   ```

2. **Open Addressing**:
   - Instead of maintaining separate chains, open addressing tries to keep all elements within the hash table array.
   - When a collision occurs, the algorithm probes or searches for the next available slot in the array.
   
   - Common probing methods include:
     - **Linear Probing**: Check the next subsequent cells sequentially.
     - **Quadratic Probing**: Check cells at intervals of quadratic values (1, 4, 9, etc.).
     - **Double Hashing**: Use a second hash function to determine the step size for probing.

   ```plaintext
   Hash Table with Linear Probing
   
   Index 0: (key1, value1)
   Index 1: (key2, value2)
   Index 2: (key5, value5)   // This spot was found after checking index 0 and 1
   ```

### Advantages of Using Hash Tables

- **Fast Lookups**: Average-case O(1) time complexity.
- **Efficient Insertions and Deletions**: Average-case O(1) operations.
- **Flexible Keys**: Keys can be of various types, as long as they can be hashed.

### Disadvantages of Using Hash Tables

- **Worse-Case Performance**: In the worst case, operations can degrade to O(n), typically due to poor hash function or excessive collisions.
- **Memory Usage**: May use more memory compared to other data structures due to the extra space required for the array and linked lists in chaining.
- **Complexity**: Implementation can be more complex compared to simpler data structures like arrays or linked lists.

### Example Usage

In Python, hash tables are implemented as dictionaries (`dict`):

```python
# Example of a hash table in Python using a dictionary
hash_table = {}

# Insert key-value pairs
hash_table["name"] = "Alice"
hash_table["age"] = 30

# Retrieve values
print(hash_table["name"])  # Output: Alice
print(hash_table["age"])   # Output: 30

# Update value
hash_table["age"] = 31

# Delete a key-value pair
del hash_table["name"]
```

In summary, hash tables are a powerful and efficient way to manage key-value pairs, making them a crucial topic in data structures. Understanding their workings, advantages, disadvantages, and how to handle collisions will greatly enhance your programming and problem-solving skills.

---
[Back to index](index.html)
