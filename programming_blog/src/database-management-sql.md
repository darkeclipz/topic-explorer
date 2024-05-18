---
title: SQL
---

[Back to index](index.html)

---
# Database Management
## SQL

Certainly! SQL (Structured Query Language) is a powerful language used for managing and manipulating relational databases. It is the standard language for relational database management systems (RDBMS), like MySQL, PostgreSQL, SQL Server, and Oracle Database.

### Key Concepts in SQL:

1. **Database**:
   - A collection of organized data. In the context of SQL, a database stores data in tables.

2. **Table**:
   - A structured set of data elements (values) organized in rows and columns. Each table has a unique name in the database.

3. **Schema**:
   - Defines the structure and organization of the database, including tables, columns, and their data types.

4. **SQL Commands**:
   SQL commands can be categorized into five main groups:

   - **DDL (Data Definition Language)**:
     - **CREATE**: Creates a new table, view, index, or database.
     - **ALTER**: Modifies an existing database object, such as adding or removing a column.
     - **DROP**: Deletes an existing database object like a table or a database.
     - **TRUNCATE**: Removes all records from a table but maintains the table structure.

   - **DML (Data Manipulation Language)**:
     - **SELECT**: Retrieves data from one or more tables.
     - **INSERT**: Adds new rows of data to a table.
     - **UPDATE**: Modifies existing data within a table.
     - **DELETE**: Removes data from a table.

   - **DCL (Data Control Language)**:
     - **GRANT**: Gives a user permission to perform specific tasks.
     - **REVOKE**: Removes previously granted permissions.

   - **TCL (Transaction Control Language)**:
     - **COMMIT**: Saves all changes made in the transaction.
     - **ROLLBACK**: Reverts changes made in the current transaction.
     - **SAVEPOINT**: Sets a savepoint within a transaction to which you can later roll back.

### Basic SQL Statements:

1. **CREATE TABLE**:
```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    hire_date DATE,
    salary DECIMAL(10, 2)
);
```

2. **INSERT INTO**:
```sql
INSERT INTO employees (employee_id, first_name, last_name, hire_date, salary)
VALUES (1, 'John', 'Doe', '2021-01-15', 60000.00);
```

3. **SELECT**:
```sql
SELECT first_name, last_name, salary
FROM employees
WHERE salary > 50000;
```

4. **UPDATE**:
```sql
UPDATE employees
SET salary = 65000.00
WHERE employee_id = 1;
```

5. **DELETE**:
```sql
DELETE FROM employees
WHERE employee_id = 1;
```

### Advanced Concepts:

1. **Joins**:
   - **INNER JOIN**: Returns rows that have matching values in both tables.
   - **LEFT JOIN**: Returns all rows from the left table, and the matched rows from the right table.
   - **RIGHT JOIN**: Returns all rows from the right table, and the matched rows from the left table.
   - **FULL OUTER JOIN**: Returns rows when there is a match in one of the tables.

   Example of an INNER JOIN:
   ```sql
   SELECT employees.first_name, employees.last_name, departments.department_name
   FROM employees
   INNER JOIN departments ON employees.department_id = departments.department_id;
   ```

2. **Indexes**:
   - Improve the speed of data retrieval operations but can slow down data modification operations.

   Example of creating an index:
   ```sql
   CREATE INDEX idx_last_name 
   ON employees(last_name);
   ```

3. **Views**:
   - A virtual table based on the result set of an SQL query.

   Example of creating a view:
   ```sql
   CREATE VIEW high_salary_employees AS
   SELECT first_name, last_name, salary
   FROM employees
   WHERE salary > 70000;
   ```

4. **Stored Procedures and Functions**:
   - Stored procedures: Reusable SQL code that you can call to perform operations.
   - Functions: Similar to stored procedures but return a value and can be used in SQL statements.

   Example of a stored procedure:
   ```sql
   CREATE PROCEDURE raise_salary(IN employee_id INT, IN increase_amount DECIMAL(10, 2))
   BEGIN
       UPDATE employees
       SET salary = salary + increase_amount
       WHERE employee_id = employee_id;
   END;
   ```

SQL is fundamental to working with relational databases, and mastering it is essential for database management and data analysis.

---
[Back to index](index.html)
