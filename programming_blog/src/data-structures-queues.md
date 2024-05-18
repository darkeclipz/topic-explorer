---
title: Queues
---

[Back to index](index.html)

---
# Data Structures
## Queues

A queue is a linear data structure that follows a particular order for operations. The order is commonly referred to as First In, First Out (FIFO). This means the first element added to the queue will be the first one to be removed, similar to people standing in a line waiting for service.

### Key Concepts of Queues

1. **Enqueue**: The operation of adding an element to the back of the queue.
2. **Dequeue**: The operation of removing an element from the front of the queue.
3. **Front**: The first element of the queue.
4. **Rear**: The last element of the queue.
5. **IsEmpty**: A method to check if the queue is empty.
6. **IsFull**: A method to check if the queue is full (relevant in static queues).

### Types of Queues

1. **Simple Queue (Linear Queue)**:
   - Follows the FIFO principle strictly.
   - Elements are added to the rear and removed from the front.
   - When the queue is full (in a fixed-size implementation), no other elements can be enqueued until space is freed.

2. **Circular Queue**:
   - The rear end connects back to the front end, making the queue circular.
   - Helps in efficiently utilizing space as it can reuse the empty spaces left after dequeuing in the beginning.

3. **Priority Queue**:
   - Each element in the queue has a certain priority level.
   - Elements with higher priority are dequeued before elements with lower priority, regardless of their position in the queue.

4. **Double-Ended Queue (Deque)**:
   - Allows insertion and deletion at both the front and the rear ends.
   - Can be used both as a queue (FIFO) or as a stack (LIFO: Last In, First Out).

### Operations

- **Enqueue()**: Adds an element to the end of the queue.
    ```python
    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.queue.append(item)
    ```

- **Dequeue()**: Removes and returns the front element of the queue.
    ```python
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue.pop(0)
    ```

- **Peek()**: Returns the front element without removing it.
    ```python
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[0]
    ```

### Implementation in Python

Using a list to implement a simple queue:
```python
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self, size):
        return len(self.queue) == size

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[0]

    def size(self):
        return len(self.queue)
```

### Applications of Queues

- **Resource scheduling**: Queues are widely used in operating systems for scheduling processes.
- **Breadth-First Search (BFS)**: BFS algorithm uses a queue to explore nodes level by level.
- **Print Spooling**: Printer spooling services use queues to hold print jobs.
- **Handling requests**: Web servers use a queue to manage requests in the order they are received.

Queues are fundamental data structures useful in various fields including operating systems, networking, and real-time systems for managing tasks in a controlled and structured way.

---
[Back to index](index.html)
