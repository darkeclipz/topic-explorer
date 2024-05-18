---
title: Linked Lists
---

[Back to index](index.html)

---
# Data Structures
## Linked Lists

### Linked Lists

A Linked List is a linear data structure where elements, called nodes, are not stored in contiguous memory locations. Instead, each node contains a reference (or link) to the next node in the sequence. This allows for efficient insertion and deletion of elements, as it eliminates the need for shifting elements (which is necessary in arrays).

#### Key Components
1. **Node**: The basic unit of a linked list, comprising:
   - `Data`: The value or data stored in the node.
   - `Next`: A reference (or pointer) to the next node in the list.

2. **Head**: A reference to the first node in the linked list. It is used to traverse and access other nodes in the list.

#### Types of Linked Lists
1. **Singly Linked List**: Each node contains one reference to the next node.
2. **Doubly Linked List**: Each node contains two references - one to the next node and one to the previous node.
3. **Circular Linked List**: Similar to a singly or doubly linked list, except the last node points back to the first node, forming a circle.

#### Basic Operations
- **Traversal**: Visiting each node in the linked list.
- **Insertion**:
  - At the beginning
  - At the end
  - After a given node
- **Deletion**:
  - At the beginning
  - At the end
  - A specific node (by value or position)
- **Search**: Finding an element in the list.
- **Update**: Modifying the value of an existing node.

#### Example of Singly Linked List

Here's a simple representation and some basic operations on a singly linked list in Python:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
linked_list = SinglyLinkedList()
linked_list.insert_at_end(1)
linked_list.insert_at_end(2)
linked_list.insert_at_end(3)
linked_list.insert_at_beginning(0)
linked_list.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> None
```

### Advantages
- **Dynamic Size**: A linked list can grow and shrink in size dynamically as elements are added or removed.
- **Ease of Insertions/Deletions**: Elements can be easily inserted or deleted without reorganizing the entire structure.

### Disadvantages
- **Memory Usage**: Linked lists use extra memory for storing pointers (references) in addition to the data.
- **Traversal Time**: Accessing elements in a linked list requires traversing from the head node, making it slower compared to direct array indexing.

### Applications
- Implementing dynamic memory management
- Constructing other data structures like stacks, queues, graphs, etc.
- Managing ordered data in databases and file systems

Linked lists are fundamental structures in computer science and are the foundation for more complex data structures. Understanding their properties and operations is crucial for effective programming and optimization.

---
[Back to index](index.html)
