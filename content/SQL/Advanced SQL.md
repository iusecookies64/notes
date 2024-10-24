## Combining Tables in SQL

Till now we have dealt with data in a single table. Now let's try to merge information from various tables and understand them as a whole.
In SQL, we use the concept of **JOIN** to combine tables.  
Below is the query to join two tables 'employee' and 'department' in an organisation database.

```sql
SELECT * 
FROM employee 
JOIN department 
ON employee.employee_id = department.employee_id;
```

What this does is creates a new table with columns from both the tables. Then for every record in first table it goes over every record in second table and if the `ON` condition is true then it will put both the records in the new table. Although this is not what happens (more efficient algorithms are used), but this is a very good mental model to think and the details of actual implementation is hidden from us.

If there are multiple tables, then also a good mental model to understand how join will be done is that it will first combine first two tables and create an intermediate result which will be used to join with 3rd table to give final result. But in reality this is not what happens, below we go in a little more specifics of how it might happen.

<details>
<summary>Multiple Table Joins</summary>
When SQL processes multiple table joins, the database management system (DBMS) uses a query execution plan to determine the most efficient way to perform the joins. The process doesn't necessarily follow a strict left-to-right order as described in the statement. Instead, the DBMS may optimize the joins in various ways to improve performance. This optimization can involve reordering the joins, using indexes, and choosing different join algorithms (e.g., nested loop join, hash join, merge join).

In general, the DBMS might join the first two tables and then join the result with the third table, but it can also:

- Reorder the joins if a different order is more efficient.
- Combine multiple tables at once using more advanced algorithms.
- Use parallel processing to join tables concurrently.

The join order and method are determined by the query optimizer, which analyzes the query and chooses the best execution plan based on factors like table sizes, indexes, and available system resources.
</details>

Consider two tables student and course as shown below.

```sql
┌───────┬───────────────┬──────────────────┬───────────┐
│ St_id │    St_Name    │    Department    │ Course_id │
├───────┼───────────────┼──────────────────┼───────────┤
│ 1001  │ John Smith    │ Computer Science │ CS101     │
│ 1002  │ Emily Brown   │ History          │ HIS102    │
│ 1003  │ David Lee     │ Mathematics      │ MAT202    │
│ 1004  │ Sarah Johnson │ English          │ ENG201    │
│ 1005  │ Michael Chen  │ Biology          │ BIO103    │
└───────┴───────────────┴──────────────────┴───────────┘
┌───────────┬──────────────────┬─────────┬─────────┐
│ Course_id │ Course_Name      │ Credits │ Prof_id │
├───────────┼──────────────────┼─────────┼─────────┤
│ CS101     │ Computer Science │ 3       │ 2001    │
│ HIS102    │ World History II │ 3       │ 2004    │
│ MAT202    │ Linear Algebra   │ 2       │ 2002    │
│ ENG201    │ Advanced Writing │ 4       │ 2003    │
│ BIO103    │ Biology          │ 4       │ 2005    │
└───────────┴──────────────────┴─────────┴─────────┘
```

Let's say we want to join the both the tables on `Course_id`, below is the query for this.

```sql
select 
s.St_Name, s.Department, s.Course_id, c.Course_Name
from student s 
join course c 
on s.Course_id = c.Course_id;

-- output
┌───────────────┬──────────────────┬───────────┬──────────────────────────────────┐
│    St_Name    │    Department    │ Course_id │           Course_Name            │
├───────────────┼──────────────────┼───────────┼──────────────────────────────────┤
│ John Smith    │ Computer Science │ CS101     │ Introduction to Computer Science │
│ Emily Brown   │ History          │ HIS102    │ World History II                 │
│ David Lee     │ Mathematics      │ MAT202    │ Linear Algebra                   │
│ Sarah Johnson │ English          │ ENG201    │ Advanced Writing                 │
│ Michael Chen  │ Biology          │ BIO103    │ Principles of Biology            │
└───────────────┴──────────────────┴───────────┴──────────────────────────────────┘
```

>[!Note]
>In the above query we have given alias to tables so that we can easily the alias which makes easy to reference the table, especially when the tables names are huge.

### Inner Joins

In the previous query we joined the table 'student' and 'course'.  

There could be cases where none of the students has opted for a particular course.

- In such cases, when the tables are joined, the rows which does not match are excluded by default.
- The row which has the name of the course which **IS NOT** opted by any of the student **WILL BE EXCLUDED** when both the tables are joined.

When the tables are joined in this manner its called **Inner Joins**. This is the default behaviour of the joins.

### Left Joins

We've learned that by default SQL removes the rows which doesn't match while joining tables.

However, if we wish to join two tables whose rows doesn't match, we can do that using **LEFT JOIN**.  
When two tables are joined using 'LEFT JOIN', and if the rows don't match,

- All the rows in the first table(left) will be kept as such and
- Whenever a row doesn't a corresponding row in the second table (right), those columns will be kept blank.

Below is the query to join the table 'customer' and 'order' using LEFT JOIN

```sql
 SELECT *
 FROM customer
 LEFT JOIN order
 ON customer.cust_id = order.cust_id;
```

### Primary Key vs Foreign Key

Primary Key in a table is used to uniquely identify a row in a table. It also has a certain criteria

- The value should not be NULL
- Each value should be unique
- A table should not have more than one Primary key

You might have already observed that primary keys are used to join tables.  
Joining the table is only possible if there is a matching column in the tables which are to be joined.  
Which means that a table's primary key can be found in a different table.

A primary key of a table when present in a different table is referred to as a **Foreign Key**.  
In the tables student and course we have common column `Course_id` which is primary key for the course table, while is a foreign key for the student table.

Below is a query to create a student table with `Course_id` foreign key.

```sql
CREATE TABLE student (
	id INT PRIMARY KEY,
	St_Name TEXT,
	Department TEXT,
	Course_id TEXT,
	FOREIGN KEY (Course_id) REFERENCES course(Course_id)
);
```

If you create a column in a database table that is intended to be a foreign key but do not explicitly define it as such, the database will treat it as a regular column. Here are the implications of this approach:

##### 1. **No Referential Integrity:**

- The database will not enforce referential integrity. This means that there will be no automatic checks to ensure that the values in the foreign key column exist in the referenced primary key column of another table. You could insert a value that does not exist in the parent table, leading to potential data inconsistency.

##### 2. **No Automatic Index Creation:**

- When you define a foreign key, many databases automatically create an index on the foreign key column to optimize join operations and lookups. Without explicitly defining the foreign key, this index will not be created automatically, which can impact query performance.

##### 3. **No Cascade Operations:**

- Foreign key constraints often come with options for cascade operations (`ON DELETE CASCADE`, `ON UPDATE CASCADE`). Without defining the foreign key, these automatic cascade operations will not be available, so you would need to handle such logic manually in your application code.

##### 4. **Potential for Orphaned Records:**

- Without foreign key constraints, there is a higher risk of creating orphaned records. For example, if a row in the parent table is deleted, rows in the child table that reference it will remain, leading to data inconsistency.

### Cross join

In the past few problems we've learned how to join the tables which were inter related.  
Now, lets try to join tables which are not at all related.  

We use the concept of **CROSS JOIN** to join such tables. In this each row from left table is simply mapped to every row in the other table and result is returned.

Let's say we want to know for every student what all course they can take, then we can cross join student and course table as shown below.

```sql
 SELECT s.St_Name, c.Course_Name 
 FROM student s 
 CROSS JOIN course c;
```

### Union

Till now, we have joined tables by columns. Now let’s join the data by rows.  
We use the concept of **UNION** to do that.  
UNION helps us to place a table right on top of another table.  
There are set of criteria to be followed while appending the tables:

- The number of columns of the tables should be same.
- The data type of the table should be of the same order of that of the first table.

Consider Following two tables namely Arts and Science.

```sql
-- TO PRINT THE TABLES
SELECT * FROM Arts;
SELECT * FROM Science;
-- GET THE UNION TABLE
SELECT * FROM Arts UNION SELECT * FROM Science;
┌─────┬───────────┐
│ id  │   name    │
├─────┼───────────┤
│ 111 │ Economics │
│ 112 │ History   │
│ 113 │ Sociology │
└─────┴───────────┘
┌────────┬───────────┐
│ Sub_id │ Sub_Name  │
├────────┼───────────┤
│ 108    │ Physic    │
│ 109    │ Chemistry │
│ 110    │ Biology   │
└────────┴───────────┘
-- UNION TABLE
┌─────┬───────────┐
│ id  │   name    │
├─────┼───────────┤
│ 108 │ Physic    │
│ 109 │ Chemistry │
│ 110 │ Biology   │
│ 111 │ Economics │
│ 112 │ History   │
│ 113 │ Sociology │
└─────┴───────────┘
```

The columns labels are determined by the result of the first query, for the rest of the queries the returned table must have same number of columns and compatible data types.

### WITH

**WITH** is used to create temporary tables when we need to define a named subquery that can be referenced later in the SQL statement.

- The same task could have been done by a **WHERE** clause inside a JOIN statement - however, using a **WITH** allows us to reduce the complexity of the query

Let us consider the data base of an organisation, where we have a table 'employee' and a table 'department'.  
Lets find out the department of the top 3 highly paid employees.  
Note that the department details are not mentioned in the table 'employee'.

Below is query to find out the department of the top 3 highly paid employees

```sql
 WITH top_employee AS(     -- This table has only 2 columns - 'name' and 'emp_id'
 SELECT name,emp_id
 FROM employee
 ORDER BY salary DESC
 LIMIT 3                   -- This table has only 3 rows - highest paid employees
 )
 SELECT top_employee.name,department.dept_name
 FROM top_employee
 JOIN department
 ON top_employee.emp_id=department.emp_id;
```

Using the with clause is also known as CTE (Common Table Expression).
### Data Transformation

In this module we'll learn the concept of data transformation using 'Subqueries'. Subqueries (also known as nested queries or inner queries) are used to transform data in a table by creating a new table that is based on the results of a subquery.  
This new table can be used as a source for further analysis or used to create a new table. This is referred to as data transformation or table transformation.

Here are some examples of table transformation using subqueries:

- Filtering based on subquery: A subquery can be used to filter rows from a table based on a condition.
- Creating a new table using subquery: A subquery can be used to create a new table based on the results of a query.
- Updating a table using subquery: A subquery can be used to update a table by setting the values of one or more columns based on a condition.

We'll use restaurant database to learn about subqueries.

### Non-Correlated Subqueries

A subquery is a query nested inside another query.

A **non-correlated** subquery is a subquery that can be executed independently of the outer query.

- The subquery does not depend on the outer query for its results.
- Non-correlated subqueries are typically used to retrieve a single value or a set of values that are used in the WHERE clause or the HAVING clause of the outer query.

Let us take an example for a **non-correlated** subquery

- Suppose you have customer information in the table 'customers' and their restaurant order information in the table 'orders'
- Below is the query to get the customer information of those who have placed an order with order value >1000.

Query:

```sql
SELECT * 
FROM customers
WHERE customer_id IN ( 
     SELECT customer_id 
     FROM orders
     WHERE order_value >1000);
```

Below is a query to find the customers whose order value is more than average order value.

```sql
SELECT *
FROM customers
WHERE customer_id IN (
	SELECT customer_id
	FROM orders
	WHERE order_value > (
		SELECT AVG(order_value)
		FROM orders
	)
);
```

The above query works fine, but in some databases it might happen that the query optimizer re-calculates the inner subquery for every row in the outer subquery. This will really affect the query performance. To guarantee that the query to calculate the average only once we can change the query using `WITH` clause.

```sql
WITH AVGOrderValue AS (
	SELECT AVG(order_value) as avg_order FROM orders
)

SELECT * 
FROM customers
WHERE customer_id IN (
	SELECT customer_id
	FROM orders, AVGOrderValue
	WHERE order_value > AVGOrderValue.avg_order
)
```

>[!Note]
>Notice in the above query, in order to compare order value from `AVGOrderValue.avg_order` we need to set the context first, otherwise referencing the column value without proper context can be problematic (especially when there are more than 1 value in that column). To set the context we join the tables, the above syntax i.e. `FROM orders, AVGOrderValue` creates a `CROSS JOIN`  of the tables.


### When Subqueries are Executed More Than Once 

To understand which subqueries run repeatedly for each row and which are executed only once, it's essential to look at the context in which the subquery is used. Here are some key points and strategies to help determine the behavior:

### Subqueries Executed Only Once

1. **Scalar Subqueries in the `SELECT` Clause**:
   Scalar subqueries that return a single value and are used in the `SELECT` clause or as a constant value in the `WHERE` clause are typically executed once. For example:
   
```sql
SELECT customer_id,
	(SELECT AVG(order_value) FROM orders) AS avg_order_value
FROM customers;
```

Here, the subquery `(SELECT AVG(order_value) FROM orders)` is executed once because it is a scalar subquery used to calculate a constant value.

2. **Subqueries in the `WITH` Clause (CTE)**:
   Common Table Expressions (CTEs) defined using the `WITH` clause are executed once. For example:
```sql
WITH AvgOrderValue AS (
   SELECT AVG(order_value) AS avg_value
   FROM orders
)
SELECT *
FROM customers
WHERE customer_id IN (
   SELECT customer_id
   FROM orders
   WHERE order_value > (SELECT avg_value FROM AvgOrderValue)
);
```

Here, the `AvgOrderValue` CTE is computed once, and the result is reused in the main query.

### Subqueries Executed Repeatedly

1. **Correlated Subqueries**:
   A correlated subquery depends on values from the outer query. It is evaluated once for each row processed by the outer query. For example:
   
   ```sql
SELECT c.customer_id, c.name
FROM customers c
WHERE c.customer_id IN (
   SELECT o.customer_id
   FROM orders o
   WHERE o.order_value > (SELECT AVG(order_value) FROM orders WHERE orders.customer_id = c.customer_id)
);
   ```

In this example, the subquery `(SELECT AVG(order_value) FROM orders WHERE orders.customer_id = c.customer_id)` is correlated with the outer query because it depends on `c.customer_id`. This subquery is executed once for each row in the `customers` table.

2. **Subqueries in the `WHERE` Clause with Non-Scalar Results**:
   When a subquery in the `WHERE` clause returns a non-scalar result and is not optimized by the query planner, it may be executed repeatedly. For example:
   
```sql
SELECT *
FROM customers
WHERE customer_id IN (
   SELECT customer_id
   FROM orders
   WHERE order_value > 1000
);
```

In this case, the subquery is typically executed once, but depending on the query optimizer and the complexity of the conditions, there could be scenarios where it's reevaluated more frequently, especially if the database engine is not optimizing it effectively.

### How to Confirm the Execution Plan

To confirm how often a subquery is executed, you can use the `EXPLAIN` or `EXPLAIN ANALYZE` statement provided by most SQL databases. This statement shows the execution plan for the query, detailing how the database engine will execute it. Here's an example using PostgreSQL:

```sql
EXPLAIN ANALYZE
SELECT *
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM orders
    WHERE order_value > 1000
);
```

The output will show you if the subquery is executed once or multiple times. Analyzing the execution plan can provide insights into the performance and optimization of your query.

### Correlated Subqueries

**Correlated Subqueries** as the name suggests, its inner and outer queries are related.  
The subquery is dependent on the outer query.

Let us understand this via an example

- Suppose we have a table consisting the following information - 'Employee_id', 'Department' and 'Salary' - employees can belong to various departments - Marketing / Sales / HR / Ops
- Suppose we want to find the employee id of those employees whose salary is less than the average salary of the employees **ONLY** in his department.
- This is how the query will work
    - For each employee_id in the outer query, the subquery will run.
    - The subquery will check the department of the employee and then compute the average salary of his department
    - The outer query will then take this average salary - and compare if the employee's salary is less than this average
    - If yes - then the outer query will include this employee in the output. This process will run for each row in the table

Query:

```sql
SELECT employee_id
FROM employee AS e
WHERE salary < 
	(SELECT AVG(salary)
	FROM employee
	WHERE department= e.department);
```

For the above query, the inner query will have to run every time for every row, a better way to achieve the same is to use CTE and usually in most cases using CTE's is better than subqueries.

```sql
WITH avg_salaries_table AS (
	SELECT department, AVG(salary) AS avg_salary
	FROM employee
	GROUP BY department
)

SELECT e.employee_id
FROM employee e
JOIN avg_salaries_table ast
ON e.department = ast.department AND e.salary < ast.avg_salary;
```
### Union All

In the module on **Multiple Tables** we have learned that the **UNION** operations are done to stack a table or a column over the other.  But UNION operation doesn't entertain duplicates. i.e. while combining two tables using UNION, the duplicate entries will be removed and the final output will have unique data.  
The above concern can be solved using the concept of **UNION ALL**.  
When two tables/columns are combined using **UNION ALL**, all the data will be combined and added to the resulting table, including the duplicates.

Below is the format for the same:

```sql
 SELECT * FROM table_1
 UNION ALL
 SELECT * FROM table_2;
```

Note: table_1 and table_2 should necessarily have the same count of columns

### Intersect

The **INTERSECT** operator combines two SELECT statements, but only returns the rows that are common to both SELECT statements.

Below is the format for the same:

```sql
 SELECT * FROM table_1
 INTERSECT
 SELECT * FROM table_2;
```

### Except

Previously we learned the concept of **INTERSECT**, now lets see how **EXCEPT** works.  
EXCEPT is directly opposite to that of INTERSECT.  
EXCEPT retrieves unique records from the first SELECT statement that are not present in the output of the second SELECT statement.

Below is the format for the same:

```sql
     SELECT * FROM table_1
     EXCEPT
     SELECT * FROM table_2;
```

### Conditional Aggregates Introduction

We have learned the concept of **Aggregate function** in SQL Basics, that it gives a single output value based on the calculation on multiple input values.  
Now, lets learn the concept of **Conditional Aggregate function**. In this concept we add a set of condition to the existing Aggregate functions.  
Below mentioned are some of the commonly used Aggregate functions:

- COUNT() - counts the number of rows that meet the given conditions
- MAX() & MIN() - return the largest & smallest value that meet the query conditions
- SUM() & AVG() - return the sum and average of the values in the column
- GROUP BY - used to combine rows with identical values into summary rows. It is typically used with aggregate functions such as COUNT, SUM, etc

### Case - When

**CASE WHEN** are used to add conditional logic to the sql queries.  
Let's try it out with an example. Imagine we want to get a count of employees of an organisation categorised based on their pay as follows:

- Less than Rs.20000 : Level 1
- Rs.20001- Rs.40000 : Level 2
- More than Rs.40000 : Level 3

The query for the same is as mentioned below:

```sql
SELECT
CASE
	WHEN pay < 20000 THEN 'Level 1'
	WHEN pay BETWEEN 20001 AND 40000 THEN 'Level 2'
	WHEN pay >= 40000 THEN 'Level 3'
	ELSE 'NA'             -- If the no condition is met, the row entry will be NA
END AS Pay_category,    -- Renaming the column as Pay_category
COUNT(*) as emp_count
FROM employee
GROUP BY 1;
```

If the ELSE condition is satisfied then a new category 'NA' will be added. However, it is not necessary to add the ELSE statement. In the absence of ELSE, if none of the cases satisfies then it will return a NULL value. `Pay_category` is the alias for the CASE statement.

>[!Note]
>In the above query we are using `GROUP BY 1`, which simply means group by first column in the select query, it is same as writing `GROUP BY Pay_category`.

### Count using Case

Previously we have used **COUNT** to fetch the total number of rows in a table or a specific column.  
Using the Case statement, we can add certain conditions and those cells which satisfy condition will only be counted.

Below is a query to count the number of employees who have a salary more than 200,000 in each departments:

```sql
SELECT department, 
COUNT(CASE WHEN salary> 200000 THEN 1 ELSE NULL END) as High_Salary 
FROM employee
GROUP BY department;
```

In the above query, all the cells in the column 'salary' is checked if it is more than 200000.

- If its satisfies it will return 1
- Else return NULL.
- The count is applied to the 1's and NULL's are ignored.

>[!Note]
>We can also use the below query to get the department wise high salary count, but there is a small caveat.
>```sql
>SELECT department, COUNT(*) as High_Salary 
>FROM employee 
>WHERE  salary > 200000
> GROUP BY department;
> ```
> The caveat is that it will simply ignore the departments in which there is no employee with high salary. This is because of the `WHERE` clause which simply ignores those rows that doesn't satisfy the condition.

### Sum using Case

We've learned the concept of **SUM**, that its used to find the sum of the cells of a particular column.  
Adding **CASE** to the sum, helps us to filter out the cells which are to be considered while calculating the sum of a column

Below is a query to find the sum of salaries of the employee across department who has an experience more than 3 years , from table 'employee':

```sql
       SELECT Department,
       SUM(CASE WHEN Exp >3 THEN Salary ELSE 0 END) as Sum_High_Salary 
       FROM employee
       GROUP BY 1;
```

In the above query,

- The CASE statement is used to check if the Exp column value is greater than 3
- If the condition is true, the Salary of the employee is added to the sum; otherwise, 0 is added.
- The SUM function then calculates the sum of all the salaries that meet the condition.
- The resulting sum is given an alias of `Sum_High_Salary`.

### Combining Aggregates

In the previous problem we've used 'CASE' to add a condition to find the sum.  
Aggregates can also be used to find the ratios or percentage using a combination.

Below is a query to find what percentage of the organization's total payout is paid as a salary to the employees who has an experience more than 3 years , from table 'employee':

```sql
SELECT Department,
(100*(SUM(CASE WHEN Exp >3 THEN Salary ELSE 0 END))/(SUM(Salary))) as High_Salary_percentage 
FROM employee
GROUP BY 1;
```

- In the above query, the CASE statement is used to check if the Exp column value is greater than 3.
- If the condition is true, the Salary of the employee is added to the sum; otherwise, 0 is added.
- The first SUM function then calculates the sum of all the salaries that meet the condition.
- And, second SUM calculates the total salary across all employees.
- Once both the SUM's are calculated we divide them and multiply by 100 to get the percentage.
- The resulting percentage is given an alias of `High_Salary_percentage`.

>[!Note]
>In the above query notice the parenthesis, SQL engine first evaluates the values inside of parenthesis before doing any other operation, hence in the above query 
>
>```sql
>(SUM(CASE WHEN Exp > 3 THEN Salary ELSE 0 END))
>```
>, the conditional sum is calculated first. Same for other sum, if these parenthesis are not use then SQL engine might misinterpret the expression giving wrong result. For example if in the expression above if we use 
>
>```sql
>(SUM(CASE WHEN Exp >3 THEN Salary ELSE 0 END) / SUM(Salary))
>```
>then we get wrong result.








