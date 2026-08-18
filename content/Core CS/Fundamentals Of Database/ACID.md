# Transaction

#### What is a Transaction?

A transaction simply is a collection of SQL queries that are performed together and are treated as a single unit of work. These queries are meant to be executed together and upon success of each one of them we say that the work is done and we commit (we'll see what commit means in a bit).

Now you might say every single query is some work in itself, so why treat a group of queries as single unit, the answer is that often single query is not enough to perform the application level logical work that we want. For example consider a simple task of debiting money from one users account to another users account (something that happens in bank's server). The logical flow for this would look like this,

1. Get the user1 account details from the database.
2. Check if the user1 has enough money to send the amount requested.
3. Subtract the amount from his balance.
4. Add the amount to user2 account.

From above steps it is clear that to complete this task will need 3 SQL queries (SELECT, UPDATE, UPDATE). In reality there will much more work that needs to be done for a single money transfer, like storing transaction in a transactions table, some other bank specific logic to monitor user transactions etc and there will much more queries to finish a single money transfer request.

The task of money transfer is a logical work, it is obvious that for the transfer to be complete each of the SQL query must execute successfully, hence we say that this is a single unit of work. Now it is possible that when performing queries something wrong happens, like a failed constraint (e.g. balance > 0), the database crashed, or application level error, and we are not able to finish the entire set of queries, well in that case we would want to revert any changes that we have done so far during this transaction, otherwise data will be inconsistent.

Consider the case of money transfer, lets say we subtracted money from first users account, but before adding money to other users account something bad happens, then it would mean that first user simply lost the money without it reaching other user and this would be bad.

Hence databases provide the functionality of Transaction, before performing a group of queries that we know are a single unit of work we say to database that whatever we are going to do from now is a transaction. After we are done with all of our queries we say to database that we are satisfied with updates, now **commit** them. This is at this point that the updates are actually persisted in the database. During a transaction we can, at any moment decide to roll back any changes that we have done during this transaction and database will automatically revert that changes done so far.

Sometimes, the transactions ends unexpectedly (e.g. db crash), well in that case when the database starts, it automatically rolls back all of the running transactions.

>[!Note]
>The internals of how transactions are implemented differ from database to database. But on a high level there are two types of implementations.
>
>First is the type of transactions that are optimized for commits i.e. commits are faster (e.g. PostgreSQL). In this implementation the updates are written to disk, as the transaction is going on, and on commit we don't have to write anything to disk. But in this implementation if we decide to rollback the transaction, then it will be slow, because of all the writes will then be have to be removed.
>
>The second type of implementation is one in which we keep all of the changes in memory, and only on commit write them to disk. In this case commits will be slow but rollback will must fast.

#### Nature Of Transaction

Usually Transactions are used to change or modify the data, however a transaction can be completely read only transaction. This is usually done to isolate the transaction to have consistent reads, i.e. consider the scenario that you want to generate a report for that you have to query the data a bunch of times and each time you would read some data to generate the report. Now lets say you read something and then before next read there was an update request and the data changes, and then you read the same data again and this time you get new value, this will lead to a bad report generated with inconsistent data. We will learn more about it in isolation section.

# ACID in Relational Databases

**ACID** stands for Atomicity, Consistency, Isolation and Durability which are 4 fundamental properties that we want in a database.

### Atomicity

Atomicity means that the transactions in a database must be atomic in nature. Which means queries in a transaction must be inseparable, i.e. either all of them execute successfully or even if one query fails, all prior queries in the transaction should be rolled back. If the database went down during a transaction, then all of the successful queries in the transaction must be rolled back.

### Isolation

Isolation means that transactions in our database must be isolated from other concurrent changes, isolation answers the question "Can my inflight transaction see changes made by other transactions?". There are multiple levels of isolation and the more isolated you want the transaction to be, the more computationally costly it would be.

If at a time we only have one connection to our database, then all transactions are automatically isolated. But consider that there are multiple applications accessing our database, this gives rise to different types of **Read Phenomena**, each of them correspond to different level of isolation.

#### Read Phenomena

##### Dirty Reads

A dirty read is a read that was never committed. Consider the following scenario,
* Transaction TX1 starts.
* Another transaction TX2 starts and makes update to some row in the table.
* TX1 reads data from the same row.
* Then for some reason TX2 rolls back.
 This means that TX1 read something that doesn't even exist, this is know as **dirty read**.

![](Pasted%20image%2020241201145442.png)

##### Non-Repeatable Reads

Non-Repeatable Reads means that in a transaction we read something, then some other transaction changed it and committed, and then we read that same thing again and this time got a different value. This is similar to dirty reads, the difference here is that in this case the change is committed to the database. 

The reason it is called Non-Repeatable is because the it decides whether repeated reads for same row will be consistent or not during a transaction.

![](Pasted%20image%2020241201161429.png)

##### Phantom Reads

These types of reads generally occur when we do a range query where our result depends on a bunch of rows. Consider the scenario shown below,

![](Pasted%20image%2020241201162335.png)

The first query in TX1 reads through the entire table SALES, then TX2 inserts new row in the table, and then TX1 again reads through the table, but this time new row is also read. This is different from Non-Repeatable reads we are reading something that was not read before.

Another reason this is different from Non-repeatable reads is because of internal implementations, for non-repeatable reads, databases do things like maintaining versions of rows, or locking certain rows, but since the new row is just inserted it has no version or locks. We learn about these things later.

##### Lost Updates

To understand Lost Updates, consider the following scenario where two transactions start at the same time, and read data from the same row, i.e. both read QNT from first rows as 10. Then TX1 updates the row to value 20, and then TX2 updates the same row to 15 and commits. Which means the update made by TX1 is simply lost.

![](Pasted%20image%2020241201163317.png)

#### Isolation Levels For Inflight Transactions

* **Read Uncommitted:** No isolation, any change from outside is visible to the transaction, whether committed or not. Most of the modern databases don't even support this type and it is very uncommon to use it. All types of read phenomena can occur in this.

* **Read Committed:** Each query in a transaction only sees committed changes from other transactions. This is the most popular level of isolation and most of the databases optimise their engines for this. In this level, dirty reads is not possible, but other phenomena's are still possible.

* **Repeatable Reads:** In this level during a transaction, the db will make sure that if a row is read, then that row will remain unchanged while the transaction is running. In this level of isolation dirty reads and non-repeatable reads and lost updates won't happen, but phantom reads are still possible.

* **Snapshot:** Each query in a transaction only sees changes that have been committed up to the start of the transaction. It is like a snapshot version of the database at that moment. This type of isolation gets rid of every type of read phenomena.

* **Serialisable:** Transactions are run as if they serialised one after the other.

>[!Note]
>Note that each database implements each of these levels differently.

#### Database Implementation Of Isolation

* **Pessimistic:** This approach uses Row level locks, page locks and table locks to avoid lost updates.
* **Optimistic:** No locks, just track if things changed and fail the transaction if so.
* **Repeatable Reads** "locks" the row that you read, but it could be expensive if you read a lot of rows, PostgreSQL implements **RR** as snapshot. That is why you don't get phantom reads with PostgreSQL in repeatable read.
* Serialisable are usually implemented with optimistic concurrency control, you can implement it pessimistically with **SELECT FOR UPDATE**.

### Consistency

There are two types of consistency, 
* Consistency in Data
* Consistency in Reads

#### Consistency In Data

This of consistency basically means that whether the data within a cluster is consistent or not, i.e. it is consistent with the data model defined by the user. Below are the factors affecting the consistency in data,
* **Referential Integrity (Foreign Keys):** If the table has foreign keys, then when a records is deleted, then all records referencing this record must also be deleted, or at least change accordingly. Otherwise, the data will simply be inconsistent, for example look at the two tables below, can you find the inconsistencies?.
![ centre](Pasted%20image%2020241212100313.png)
* **Atomicity:** The transactions must be atomic in nature i.e. either all of the queries execute, or none of them execute, if the queries executed partially and then transaction ended, then the data will simply become corrupt.
* **Isolation:** Depending on the isolation level, we may get inconsistent data i.e. phantom reads, lost updates etc.

#### Consistency In Reads

If a transaction committed a change, then a new transaction immediately should see the change. This problem only occurs when there are multiple instances of our database, it affects the system as a whole and relational and No SQL databases both suffer from this.

Eventual Consistency is what we get, that is if we update a value x in the database, and then read the same value again then it might happen that we are reading from a different partition from the one in which we updated the value, eventually all partitions get the updated value, hence eventual consistency.

### Durability

Durability means that changes made by committed transactions must be persisted in a durable non-volatile storage.

But doing this is expensive and slow, since we have to do a lot of I/O. Hence databases deploy different techniques to make sure durability is achieved, while not affecting the performance too much.

Some databases like Redis compromise durability for performance.

Durability techniques
* **WAL (Write Ahead Log):** In this technique the databases persist a compressed version of the changes known as WAL (write-ahead-log segments), this is much more light weight than, writing a lot of data to disk (indexes, data files, columns, rows, etc...). 
* **Asynchronous Snapshot:** In this technique the databases occasionally takes snapshots of the database and asynchronously writes them to disk.
* **AOF (Append Only File):** This is similar to WAL i.e. it only persists the changes, so that current state of db can be constructed in case of a crash.

#### Durability - OS Cache

The database is a process running on top of some operating system, so when database issues write to disk, then this process is carried out by the operating system. Sometimes the OS says that it has written the data to disk, but it just kept it in OS cache. Operating Systems do this to batch the writes to disk and flush them at once.

The problem is that if at this point the OS crashed, then when the system restarts, then it might not be able to recover the OS Cache and our data is simply lost, so there is a lost of durability due to OS Cache.

To fix this we use the command Fsync that force writes to always go to disk.

Fsync can be expensive and slows down commits.
