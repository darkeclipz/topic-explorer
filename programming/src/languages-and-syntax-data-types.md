---
title: Data Types
---

[Back to index](index.html)

---
# Languages and Syntax
## Data Types

### Data Types

Data types are fundamental to any programming language. They define the kind of data that can be stored and manipulated within a program. Understanding data types is crucial because they help allocate the correct amount of memory and determine what operations can be performed on the data. Below are some of the most common data types you'll encounter:

1. **Primitive Data Types**
    - **Integer** (int): Represents whole numbers. Example: `int age = 25;`
    - **Floating-point** (float, double): Represents numbers with a fractional part. Example: `float price = 19.99;`
    - **Character** (char): Represents single characters. Example: `char initial = 'A';`
    - **Boolean** (bool): Represents true or false values. Example: `bool isAvailable = true;`

2. **Composite Data Types**
    - **Array**: A collection of elements of the same type. Example in C: `int numbers[5] = {1, 2, 3, 4, 5};`
    - **String**: Typically a sequence of characters. Strings can be implemented as arrays of characters or objects depending on the language. Example: `string name = "Alice";`
    - **Enumerations** (enum): A user-defined data type consisting of a set of named values. Example in C++: `enum Color { RED, GREEN, BLUE };`

3. **Abstract Data Types**
    - **Class**: Used in object-oriented programming to define a blueprint for objects. Example in C++:
    ```cpp
    class Car {
        public:
            string brand;
            string model;
            int year;
    };
    ```
    - **Structure** (struct): Used to group different types of data under a single name in languages like C and C++. Example:
    ```cpp
    struct Person {
        string name;
        int age;
        float height;
    };
    ```

4. **Reference Data Types**
    - **Pointers**: Variables that store memory addresses. Example in C++: `int* ptr;`
    - **Reference**: An alias for another variable. Example in C++: `int& ref = someVariable;`

5. **Collection Data Types**
    - **List**: An ordered collection of elements. Example in Python: `my_list = [1, 2, 3, 4, 5]`
    - **Dictionary**: A collection of key-value pairs. Example in Python: `my_dict = {"name": "Alice", "age": 25}`
    - **Set**: A collection of unique elements. Example in Python: `my_set = {1, 2, 3, 4, 5}`

### Key Concepts

1. **Type Inference**: Some languages like Python use type inference to automatically deduce the data type of a variable.
    Example:
    ```python
    num = 10  # num is inferred to be of type int
    ```

2. **Type Casting**: Converting one data type to another. This can be explicit or implicit.
    - **Explicit Casting**: Manually casting types. Example in Python: `num = float(9)`
    - **Implicit Casting**: Automatically casting types when needed. Example: 
    ```python
    num = 9
    result = num + 5.5 # num is implicitly converted to float
    ```

3. **Immutability**: Some data types like strings in Python are immutable, meaning their values cannot be changed after they are created. Instead, any operation that changes the string results in a new string.
  
4. **Memory Management**: Different data types require different amounts of memory. Understanding this is crucial for efficient coding, especially in languages like C and C++ where manual memory management is common.
  
### Examples in Different Languages

- **Python**:
  ```python
  x = 5          # int
  y = 3.14       # float
  name = "Alice" # string
  flag = True    # bool
  ```

- **Java**:
  ```java
  int age = 25;
  double price = 19.99;
  char initial = 'A';
  boolean isAvailable = true;
  ```

- **C++**:
  ```cpp
  int age = 25;
  float price = 19.99f;
  char initial = 'A';
  bool isAvailable = true;
  ```

Understanding data types in depth helps you write efficient and error-free code, making it easier to manage memory and design better data structures and algorithms.

---
[Back to index](index.html)
