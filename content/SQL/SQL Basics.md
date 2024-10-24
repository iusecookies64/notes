Structured Query Language (SQL) is a programming language specifically created to access, organise and manipulate data within relational databases. In a relational database, information is arranged into one or more tables, each containing columns and rows of interconnected data entries that relate to each other in some way.

### Introduction to data types

All data stored in a relational database is of a certain data type. Some of the most common data types are:

- INTEGER, a positive or negative whole number
- TEXT, a text string
- DATE, the date formatted as YYYY-MM-DD
- REAL, a decimal value

### Introduction to statement

The following code is an example of a SQL statement.  
A statement refers to a piece of text that the database system can interpret as a valid command.  
It is important to note that SQL statements are terminated by a semicolon **`;`** which indicates the end of the statement.

```sql
CREATE TABLE table_name (
   column_1 data_type,
   column_2 data_type,
   column_3 data_type 
);
```

**CREATE TABLE** is a clause.
- In SQL, clauses are utilised to execute specific functions or operations.
- It is customary to write clauses in SQL statements using capital letters.
- In SQL, clauses can also be referred to as commands as they are used to perform specific actions or operations on the data stored within a database..

**table_name** refers to the name of the specific table on which a particular command or operation is being performed.

**(column_1 data_type, column_2 data_type, column_3 data_type)** are parameters.

- A parameter is a set of values, columns, or data types that are provided to a clause as an input argument.

### Create table

Using a **CREATE TABLE** statement in SQL enables the creation of a new table in the database.  
This statement can be used whenever a new table needs to be created, starting with a blank slate.  
The example statement below demonstrates the creation of a new table called **student**.

```sql
CREATE TABLE student (
   Student_id INT,
   Student_Name  TEXT,
   Contact_Number INT
);

-- after this query the table changes as follows

┌─────────────┬────────────────┬────────────────┐
│ Student_id  │ Student_Name   │ Contact_Number │
├─────────────┼────────────────┼────────────────┤
│             │                │                │
└─────────────┴────────────────┴────────────────┘
```

The above query will create an empty table 'student' as mentioned below:

### Insert table

Rows are added into a table using the **INSERT INTO** statement.  
Below is the query to add the details of 'Abel George' to the existing table student.

```sql
 INSERT INTO student(Student_id,Student_Name,Contact_Number)
 VALUES (34,'Abel George',910023432), (23, 'Derail Gupta', 999999999);
```

```sql
┌─────────────┬────────────────┬────────────────┐
│ Student_id  │ Student_Name   │ Contact_Number │
├─────────────┼────────────────┼────────────────┤
│ 34          │ Abel George    │ 910023432      │
├─────────────┼────────────────┼────────────────┤
│ 23          │ Derail Gupta   │ 999999999      │
└─────────────┴────────────────┴────────────────┘
```

- The clause INSERT INTO is used to append the specified row or multiple rows to a table.
- student is the table the row is added to.
- (Student_id, Student_Name, Contact_Number) are the parameters used to specify the columns into which data will be inserted.
- VALUES is used to specify the data that is being inserted.
- (34,'Abel George',910023432) is a parameter identifying the values being inserted.
- 34: an integer that will be added to Student_id column
- 'Abel George': text that will be added to student Name column. It should always be in single quotes.
- 910023432: Number that will be added to Contact_Number column.

**Multiple rows can be added to a table in a single query by separating the parameters(used to insert data to a single row) by a comma `','`**

### Alter table

The **ALTER** statement is used to append a new column to an existing table.  
Below is the query to add a new column 'Department' and set a default value, to the existing table student.

```sql
ALTER TABLE student
ADD COLUMN Department TEXT default NULL;

-- after this query the table changes as follows

┌─────────────┬────────────────┬────────────────┬───────────────┐
│ Student_id  │ Student_Name   │ Contact_Number │ Department    │
├─────────────┼────────────────┼────────────────┼───────────────┤
│ 34          │ Abel George    │ 910023432      │ NULL          │
├─────────────┼────────────────┼────────────────┼───────────────┤
│ 23          │ Derail Gupta   │ 999999999      │ NULL          │
└─────────────┴────────────────┴────────────────┴───────────────┘
```

While altering the table we can either keep the newly added column blank or we could set a **default** value (as mentioned above) to it. Lets run the query by adding a default value to the newly added column.

### Update table

The **UPDATE** statement is used to edit a row or multiple rows in a table.  
Below is the query to Set the Age as 6, for the student with student_id - 34 to the existing table student.

```sql
UPDATE student
SET Department = 'CSE'
WHERE student_id = 34;

-- after this query the table changes as follows

┌─────────────┬────────────────┬────────────────┬───────────────┐
│ Student_id  │ Student_Name   │ Contact_Number │ Department    │
├─────────────┼────────────────┼────────────────┼───────────────┤
│ 34          │ Abel George    │ 910023432      │ CSE           │
├─────────────┼────────────────┼────────────────┼───────────────┤
│ 23          │ Derail Gupta   │ 999999999      │ NULL          │
└─────────────┴────────────────┴────────────────┴───────────────┘
```

The 'WHERE' condition can be applied for any column. We will learn more about 'WHERE' later.

### Delete From

The **DELETE FROM** statement is used to remove one or multiple rows from a table.  
You can use the statement when you want to delete existing records.

Below is the query to delete all rows in the student table with student_id - 08 (table added below for reference).

```sql
DELETE FROM  student
WHERE student_id = 08;

-- after this query the table changes as follows
-- no change since there is not row with student_id=8

┌─────────────┬────────────────┬────────────────┬───────────────┐
│ Student_id  │ Student_Name   │ Contact Number │ Department    │
├─────────────┼────────────────┼────────────────┼───────────────┤
│ 34          │ Abel George    │ 910023432      │ CSE           │
├─────────────┼────────────────┼────────────────┼───────────────┤
│ 23          │ Derail Gupta   │ 999999999      │ NULL          │
└─────────────┴────────────────┴────────────────┴───────────────┘
```

### Constraints

**Constraints** provide details about the usage of a column and are applied after specifying the column's data type.  
They enable the database to reject any inserted data that violates a particular constraint.  
The following statement is used to impose constraints on the "student" table.

Below is the query to create a table student with a set of constraints.

```sql
 CREATE TABLE  student (
	 student_id INT PRIMARY KEY,
	 student_Name TEXT UNIQUE,
	 Department TEXT NOT NULL
 ); 
```

- **PRIMARY KEY** can be utilized to uniquely identify a row in a table.  When attempting to insert a row with the same value as an existing row in the table, a constraint violation will occur, preventing the insertion of the new row.
- **UNIQUE** columns contain distinct values for each row, similar to **"PRIMARY KEY"** columns, but unlike primary key columns, a table can have multiple unique columns.
- **NOT NULL** columns must have a value assigned to them.  When attempting to insert a row without providing a value for a **"NOT NULL"** column, a constraint violation will occur, preventing the insertion of the new row.

>[!Note]
>**Difference Between UNIQUE and PRIMARY KEY**
>
>**UNIQUE** constrains simple makes sure that every value in a column is unique, this column can have **NULL** value, but only one such value is allowed. A table can have multiple columns that have unique constraint. Values in a unique column can be updated as long as the new updated value is unique. A unique key can be referenced by **FOREIGN KEY** of another table.
>
>**PRIMARY KEY** constraint on the other hand is used to uniquely identify records in the table, it cannot be null and is usually a key that is rarely changed. Primary key can be just a column or a combination of columns, but there can only be one primary key in a table unlike UNIQUE keys. A Primary key of one table can be referenced by **FOREIGN KEY** of another table.
>
>**Indexing Difference**
>
>The entire table is indexed according to the primary key, which means that primary key physically decides where the data is stored. This is also known as clustered indexing. For each unique key another index is created where only the pointer to the stored is stored. This is known as non-clustered indexing.

## Introduction to Queries

In this module, let us learn the different commands to **QUERY** a single table database. Queries are used to **talk** to the database and carry out specific actions. Throughout this module, let us use the **Flights** table to understand how passengers have booked their flight tickets.

Let us check the data currently stored in the **Flights** table.

```sql
┌──────────────┬────────────────┬────────┬──────────┬─────────────┐
│ Passenger_id │ Passenger_name │ Gender │  Origin  │ Destination │
├──────────────┼────────────────┼────────┼──────────┼─────────────┤
│ 10001        │ Jackson        │ Male   │ Mumbai   │ New York    │
│ 10002        │ Riya           │ Female │ Mumbai   │ Delhi       │
│ 10003        │ Roy            │ Male   │ London   │ Delhi       │
│ 10004        │ Anthony        │ Male   │ Mumbai   │ Cairo       │
│ 10005        │ Salim          │ Male   │ Ohio     │ New York    │
│ 10006        │ Dia            │ Female │ New York │ Cairo       │
│ 10007        │ Jackson        │ Male   │ New York │ London      │
│ 10008        │ Dia            │ Female │ Beijing  │ Mumbai      │
│ 10009        │ Riya           │ Female │ Damascus │ Mumbai      │
│ 10010        │ Betty          │ Female │ Beijing  │ Cairo       │
└──────────────┴────────────────┴────────┴──────────┴─────────────┘
```

### SELECT Query

As you saw in the problem earlier, the **Flights** table had the following information in columns

- Passenger_id with datatype INT
- Passenger_name with datatype VARCHAR
- Gender with datatype VARCHAR
- Origin with datatype VARCHAR
- Destination with datatype VARCHAR

To view data entries in specific columns of a table, the following syntax is used

```sql
	select column_1, column_2
	from Flights;
```

To view **ALL** rows of a table, the following syntax is used

```sql
    select *
    from Flights;
```

For example consider the following query.

```sql
select Passenger_name, Gender from flights;

-- the result would be
┌────────────────┬────────┐
│ Passenger_name │ Gender │
├────────────────┼────────┤
│ Jackson        │ Male   │
│ Riya           │ Female │
│ Roy            │ Male   │
│ Anthony        │ Male   │
│ Salim          │ Male   │
│ Dia            │ Female │
│ Jackson        │ Male   │
│ Dia            │ Female │
│ Riya           │ Female │
│ Betty          │ Female │
└────────────────┴────────┘
```

### DISTINCT

In the **Flights** table, what all 'Origins' exist? The following query should give us the result.

```sql
     Select Origin 
     from Flights;
```

However, if we want to find the **unique** origin locations, we will use the **DISTINCT** syntax in the following format.

```sql
     Select Distinct Origin 
     from Flights;
```

The output for the above query will be.

```sql
┌──────────┐
│  Origin  │
├──────────┤
│ Mumbai   │
│ London   │
│ Ohio     │
│ New York │
│ Beijing  │
│ Damascus │
└──────────┘
```

But if we have **DISTINCT** with multiple columns, well then unique tuples will be returned. For example consider the below example.

```sql
select Origin, Gender from Flights;
select distinct Origin, Gender from Flights;

-- result of first query
┌──────────┬────────┐
│  Origin  │ Gender │
├──────────┼────────┤
│ Mumbai   │ Male   │
│ Mumbai   │ Female │
│ London   │ Male   │
│ Mumbai   │ Male   │
│ Ohio     │ Male   │
│ New York │ Female │
│ New York │ Male   │
│ Beijing  │ Female │
│ Damascus │ Female │
│ Beijing  │ Female │
└──────────┴────────┘

-- result of second query
┌──────────┬────────┐
│  Origin  │ Gender │
├──────────┼────────┤
│ Mumbai   │ Male   │
│ Mumbai   │ Female │
│ London   │ Male   │
│ Ohio     │ Male   │
│ New York │ Female │
│ New York │ Male   │
│ Beijing  │ Female │
│ Damascus │ Female │
└──────────┴────────┘
```

From the above we can see that in the first result there were duplicate tuples, in the first one there are 2 tuples `('Mumbai', 'Male')` and 2 tuples with `('Beijing', 'Female')`.

### WHERE

The **WHERE** clause helps us obtain information which meets specific conditions.

In the previous problem, we saw the 'Origins' of flights.  
Let us try and identify flights that originate out of 'Mumbai' using the following syntax.

```sql
Select *
from Flights
WHERE Origin = 'Mumbai';

-- output for above query is
┌──────────────┬────────────────┬────────┬────────┬─────────────┐
│ Passenger_id │ Passenger_name │ Gender │ Origin │ Destination │
├──────────────┼────────────────┼────────┼────────┼─────────────┤
│ 10001        │ Jackson        │ Male   │ Mumbai │ New York    │
│ 10002        │ Riya           │ Female │ Mumbai │ Delhi       │
│ 10004        │ Anthony        │ Male   │ Mumbai │ Cairo       │
└──────────────┴────────────────┴────────┴────────┴─────────────┘
```

### BETWEEN

The **BETWEEN** clause is used along with **WHERE** to filter the table based on 2 values.

- The values can be text

```sql
select * from Flights
where passenger_name BETWEEN 'A' AND 'D';
```

- The values can be integers

```sql
select * from Flights
where passenger_id BETWEEN 10001 AND 10007;
```

This is similar to doing `passenger_id >= 10001 AND passenger_id <= 10007`. For strings this is a lexicographic comparison. For example look at the queries below.

```sql
-- query 1
select * from Flights
where passenger_name BETWEEN 'Az' AND 'DD';

-- query 2
select * from Flights
where passenger_name BETWEEN 'AZ' AND 'DD';

-- result for query 1
┌──────────────┬────────────────┬────────┬─────────┬─────────────┐
│ Passenger_id │ Passenger_name │ Gender │ Origin  │ Destination │
├──────────────┼────────────────┼────────┼─────────┼─────────────┤
│ 10010        │ Betty          │ Female │ Beijing │ Cairo       │
└──────────────┴────────────────┴────────┴─────────┴─────────────┘

-- result for query 2
┌──────────────┬────────────────┬────────┬─────────┬─────────────┐
│ Passenger_id │ Passenger_name │ Gender │ Origin  │ Destination │
├──────────────┼────────────────┼────────┼─────────┼─────────────┤
│ 10004        │ Anthony        │ Male   │ Mumbai  │ Cairo       │
│ 10010        │ Betty          │ Female │ Beijing │ Cairo       │
└──────────────┴────────────────┴────────┴─────────┴─────────────┘
```

The reason is so because `Anthony > AZ` but `Anthony < Az`.

### AND

The **AND** clause is used along with **WHERE** to filter the table based on 2 separate conditions.

Check the following example - **AND** combines the two conditions.

```sql
select * from Flights
where origin = 'Mumbai'
and passenger_id BETWEEN 10001 AND 10007;
```

Any query containing **AND** will return a result **ONLY** if all conditions are **TRUE**.

### OR

The **OR** clause is used along with **WHERE** to filter the table which meets any one of the given multiple conditions.

Check the following syntax - **OR** combines the two conditions.

```sql
select * from Flights
where origin = 'Mumbai'
or origin = 'New York';
```

Any query containing **OR** will return a result if **ANY** of the conditions is **TRUE**.

### Like

The **LIKE** operator is used along with **WHERE** to filter the similar values. Remember that '=' was used for exact match.

- `%` is used with **LIKE** as a replacement for multiple letters.  The query below will give us the table.

```sql
select * from Flights
where origin like '%York%';

┌──────────────┬────────────────┬────────┬──────────┬─────────────┐
│ Passenger_id │ Passenger_name │ Gender │  Origin  │ Destination │
├──────────────┼────────────────┼────────┼──────────┼─────────────┤
│ 10006        │ Dia            │ Female │ New York │ Cairo       │
│ 10007        │ Jackson        │ Male   │ New York │ London      │
└──────────────┴────────────────┴────────┴──────────┴─────────────┘
```

- `_` is used with **LIKE** as a replacement for single letters / characters.  The query below will give us the table.

```sql
select * from Flights
where passenger_id like '1000_';

┌──────────────┬────────────────┬────────┬──────────┬─────────────┐
│ Passenger_id │ Passenger_name │ Gender │  Origin  │ Destination │
├──────────────┼────────────────┼────────┼──────────┼─────────────┤
│ 10001        │ Jackson        │ Male   │ Mumbai   │ New York    │
│ 10002        │ Riya           │ Female │ Mumbai   │ Delhi       │
│ 10003        │ Roy            │ Male   │ London   │ Delhi       │
│ 10004        │ Anthony        │ Male   │ Mumbai   │ Cairo       │
│ 10005        │ Salim          │ Male   │ Ohio     │ New York    │
│ 10006        │ Dia            │ Female │ New York │ Cairo       │
│ 10007        │ Jackson        │ Male   │ New York │ London      │
│ 10008        │ Dia            │ Female │ Beijing  │ Mumbai      │
│ 10009        │ Riya           │ Female │ Damascus │ Mumbai      │
└──────────────┴────────────────┴────────┴──────────┴─────────────┘
```

We can also combine multiple **LIKE** conditions.

```sql
-- query for destination ends with o and origin starts with M
select * from flights where Destination like '%o' and Origin like 'M%';
-- result
┌──────────────┬────────────────┬────────┬────────┬─────────────┐
│ Passenger_id │ Passenger_name │ Gender │ Origin │ Destination │
├──────────────┼────────────────┼────────┼────────┼─────────────┤
│ 10004        │ Anthony        │ Male   │ Mumbai │ Cairo       │
└──────────────┴────────────────┴────────┴────────┴─────────────┘
```

### Order by

**ORDER BY** is used to sort the results of the query in an ascending or descending order.

- By default, the following syntax returns the result sorted in an ascending order
- The **ORDER BY** clause should be written after the SELECT, FROM, WHERE, GROUP BY, and HAVING clauses, but before the LIMIT clause (if one is used).

```sql
select * from Flights
ORDER BY passenger_name;

Output
┌──────────────┬────────────────┬────────┬──────────┬─────────────┐
│ Passenger_id │ Passenger_name │ Gender │  Origin  │ Destination │
├──────────────┼────────────────┼────────┼──────────┼─────────────┤
│ 10004        │ Anthony        │ Male   │ Mumbai   │ Cairo       │
│ 10010        │ Betty          │ Female │ Beijing  │ Cairo       │
│ 10006        │ Dia            │ Female │ New York │ Cairo       │
│ 10008        │ Dia            │ Female │ Beijing  │ Mumbai      │
│ 10001        │ Jackson        │ Male   │ Mumbai   │ New York    │
│ 10007        │ Jackson        │ Male   │ New York │ London      │
│ 10002        │ Riya           │ Female │ Mumbai   │ Delhi       │
│ 10009        │ Riya           │ Female │ Damascus │ Mumbai      │
│ 10003        │ Roy            │ Male   │ London   │ Delhi       │
│ 10005        │ Salim          │ Male   │ Ohio     │ New York    │
└──────────────┴────────────────┴────────┴──────────┴─────────────┘
```

- To sort the results in a descending order, use the following syntax

```sql
select * from Flights
ORDER BY passenger_name DESC;
```

### LIMIT

**LIMIT** is used to view a representative / sample portion of the table.  
Databases can be very large - LIMIT helps us restrict the maximum number of rows displayed in the output.  
Review the sample syntax below

```sql
select * from Flights
ORDER BY passenger_name
LIMIT 3;
```

**LIMIT** should always be placed at the end of the query.

### NULL Values

Some rows / columns in databases can be empty - these values are treated as **NULL**.  
**IS NULL** and **IS NOT NULL** are used to filter for such entries.  
Review the sample syntax below

```sql
select * from Flights
where origin IS NULL;
```

### Rename columns using As

Before we begin aggregate functions, a useful concept to know is renaming of columns during output.

In SQL, the keyword 'AS' allows you to rename a column or table using an alias.  
Sample syntax:

```sql
select 
employee_id as 'Serial',
employee_name as 'Name',
department as 'Dept'
from employee;

-- output for above query
┌────────┬────────────────┬────────────┐
│ Serial │      Name      │    Dept    │
├────────┼────────────────┼────────────┤
│ 1      │ Kayla Thompson │ Sales      │
│ 2      │ Ethan Chen     │ Operations │
│ 3      │ Julia Lee      │ Hr         │
│ 4      │ Marcus Garcia  │ Product    │
│ 5      │ Samantha Park  │ Operations │
└────────┴────────────────┴────────────┘
```


## Aggregate Functions

Aggregate functions are functions which take a table and output a single row. The most common aggregate functions are `COUNT`, `MAX` , `MIN`, `SUM` and `AVG`.
### COUNT()

Using the COUNT() function is the most efficient method for determining the number of rows in a table.  This function accepts the name of a column as a parameter and calculates the total count of non-empty values in that column i.e. rows where value is not null. However if you want to calculate total number of rows regardless of the values inside them then we use COUNT and pass it `*` i.e. `COUNT(*)`.

Below is the query to count the rows of the table 'customer', and second query is to count number of rows where `customer_name` is not null.

```sql
SELECT COUNT(*) FROM customer;
SELECT COUNT(customer_name) FROM customer;
```

### MAX() and MIN()

The MAX() and MIN() functions retrieve the maximum and minimum values from a column, correspondingly.

Below is the query to find the highest and lowest age of the customers from the table customer

```sql
SELECT MAX(Age)
FROM customer;
```

```sql
SELECT MIN(Age)
FROM customer;
```

This query basically returns the row with maximum/minimum value, If there are multiple rows with max/min value then it returns the first row with max/min value. This can be verified by adding other columns in the query.

```sql
select first_name, MAX(age) as 'max_age' from customer;

-- output is 
┌──────────────┬────────────────┐
│ first_name   │ max_age        │
├──────────────┼────────────────┤
│ John         │ 31             │
└──────────────┴────────────────┘
```

We can get the max/min for multiple columns or the same column in single query. For example to get `min_age` and `max_age` in one query we can do .

```sql
SELECT MIN(age) AS 'min_age', MAX(age) AS 'max_age' from customer;
-- output
┌──────────────┬────────────────┐
│ min_age      │ max_age        │
├──────────────┼────────────────┤
│ 22           │ 31             │
└──────────────┴────────────────┘
```
### ROUND()

Let us introduce the **ROUND()** function as it is routinely used with aggregate functions.  
Sql uses the ROUND() functions to display numeric values rounded to a specified precision.  
The precision parameter indicates the number of decimal places to which the number should be rounded.

The ROUND() function requires two parameters enclosed in parentheses: a column name and an integer value.
Below is the query to display `Total_Purchase` rounded to 1 decimal place from the table customer.

```sql
SELECT ROUND(Total_Purchase, 1)
FROM CUSTOMER; 
```

We can also merge different aggregate functions, for example if we want to get the maximum `order_value` rounded to 2 decimal places then we can do as shown below.

```sql
SELECT ROUND(MAX(order_value)) FROM CUSTOMER;
```

### SUM()

The SUM() function in SQL facilitates the process of calculating the total sum of values within a specific column.  
It takes the column name as argument and outputs the resulting sum.

Below is the query to find the sum of the Sale from the table customer.

```sql
SELECT SUM(Sale)
FROM customer;
```

### AVG()

The AVG() function is used to calculate the **Average** of values within a specific column.  
It takes the column name as argument and outputs the resulting average.

Below is the query to find the Average Age from the table customer.

```sql
SELECT AVG(Age)
FROM customer;
```

### Group By

The GROUP BY statement in SQL is used to combine rows with identical values into summary rows. This can be thought of as first we are grouping rows based on column provided and then we are applying the aggregate on each of the groups and returning and answer group wise.

- This statement is frequently paired with aggregate functions such as COUNT(), MAX(), MIN(), SUM(), and AVG() to group the output based on one or more columns.
    - We saw in the previous problems that clauses like COUNT, MIN, MAX, SUM, AVG are aggregate functions which take a table and output a single row.
    - GROUP BY will be used to find the average Payout of each Department.
- For example, we've used the AVG() function to find the average payout of the entire table employee.  
    - Now, what if we want to know the Average payout of each department?  
    - In such cases we use Group BY statement.

Below is the query to find the average Age of the students across Divisions in the table student.

```sql
SELECT Divisions,AVG(Age)
FROM student
GROUP BY Divisions;
```

### Having

In the previous problem we saw how to use GROUP BY statement.  
SQL also gives you an option to filter out which groups should be added and which are to be removed.  
For this purpose we use **Having** statement.  
Let us try to find to out the average Age across Division which has more than 50 students.

Below is the query to find out the average Age across Division which has more than 50 students from the table student.

```sql
SELECT Division,
AVG(Age)
FROM student
GROUP BY Division
HAVING COUNT(*) > 50;
```

### Difference Between `WHERE` AND `HAVING`

The `WHERE` and `HAVING` clauses in SQL are both used to filter records, but they are applied at different stages of the query processing and serve different purposes.

#### WHERE Clause

- **Purpose**: The `WHERE` clause is used to filter rows before any groupings are made.
- **Stage**: It is applied to rows before they are grouped.
- **Usage**: It is typically used to filter rows based on specific conditions.
- **Example**:

  ```sql
  SELECT *
  FROM employees
  WHERE department = 'Sales';
  ```

  This query selects all employees who belong to the Sales department.

### HAVING Clause

- **Purpose**: The `HAVING` clause is used to filter groups after the `GROUP BY` clause has been applied.
- **Stage**: It is applied to groups after they have been created.
- **Usage**: It is typically used to filter groups based on aggregate functions (e.g., `COUNT()`, `SUM()`, `AVG()`).
- **Example**:

  ```sql
  SELECT department, COUNT(*)
  FROM employees
  GROUP BY department
  HAVING COUNT(*) > 10;
  ```
  
  This query selects departments that have more than 10 employees.

### Key Differences

1. **Timing**: 
   - `WHERE` filters rows before any grouping occurs.
   - `HAVING` filters groups after the grouping has been done.

2. **Use Case**:
   - `WHERE` is used for filtering individual rows based on a condition.
   - `HAVING` is used for filtering groups based on aggregate functions.

3. **Syntax**:
   - `WHERE` is used without `GROUP BY` and before `GROUP BY` if `GROUP BY` is used.
   - `HAVING` is used after `GROUP BY`.

### Example Combining Both
Here’s an example that uses both `WHERE` and `HAVING` clauses:
```sql
SELECT department, AVG(salary)
FROM employees
WHERE hire_date >= '2020-01-01'
GROUP BY department
HAVING AVG(salary) > 60000;
```
In this query:
- The `WHERE` clause filters employees hired on or after January 1, 2020.
- The `HAVING` clause filters departments where the average salary is greater than $60,000.
