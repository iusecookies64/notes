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
│ 34          │ Abel George    │ 910023432      │ 'CSE'         │
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
│ 34          │ Abel George    │ 910023432      │ 'CSE'         │
├─────────────┼────────────────┼────────────────┼───────────────┤
│ 23          │ Derail Gupta   │ 999999999      │ NULL          │
└─────────────┴────────────────┴────────────────┴───────────────┘
```