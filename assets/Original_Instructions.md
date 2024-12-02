
# Data Processing and Storage Assignment

## Table of Contents
- [Overview](#overview)
- [Instructions](#instructions)

## Overview

- Transactions are an important part of relational databases. Transactions allow "all or nothing" updates to databases to prevent dirty writes.This is especially important while dealing with things like money. For example: Let’s say you are building a money transfer app like Venmo. When A initiates a transfer of X dollars to B, two things need to happen:
  - X dollars should be deducted from A’s account
  - X dollars should be added to B’s account
- If either of these things fail, it will leave the overall accounting in a bad state.
- In the real world these two updates are made as part of a single transaction.

In this assignment you will build an in-memory database with transaction support.

## Instructions

1. In the language of your choice you have to build an in-memory key-value database that supports the following functions (See Fig 1 for a sample interface definition):
   - `begin_transaction()`
   - `put(key, value)`
   - `get(key)`
   - `commit()`
   - `rollback()`
2. Keys should be strings and values should be integers.
3. `put(key, val)` will create a new key with the provided value if a key doesn’t exist. Otherwise it will update the value of an existing key.
4. `get(key)` will return the value associated with the key or `null` if the key doesn’t exist.
5. If `put(key, val)` is called when a transaction is not in progress, throw an exception.
6. `get(key)` can be called anytime even when a transaction is not in progress.
7. `begin_transaction()` starts a new transaction.
8. At a time only a single transaction may exist.
9. Within a transaction you can make as many changes to as many keys as you like. However, they should not be "visible" to `get()` until the transaction is committed.
10. A transaction ends when either `commit()` or `rollback()` is called.
11. `commit()` applies changes made within the transaction to the main state. Allowing any future `get()` calls to "see" the changes made within the transaction.
12. `rollback()` should abort all the changes made within the transaction and everything should go back to the way it was before.
13. See Fig 2 for some examples.

### Fig 1

```java
interface InMemoryDB {
  int get(String key);

  void put(String key, int val);

  void begin_transaction();

  void commit();

  void rollback();
}
```

### Fig 2

```java
InMemoryDB inmemoryDB;

// should return null, because A doesn’t exist in the DB yet
inmemoryDB.get("A");

// should throw an error because a transaction is not in progress
inmemoryDB.put("A", 5);

// starts a new transaction
inmemoryDB.begin_transaction();

// sets value of A to 5, but it’s not committed yet
inmemoryDB.put("A", 5);

// should return null, because updates to A are not committed yet
inmemoryDB.get("A");

// update A’s value to 6 within the transaction
inmemoryDB.put("A", 6);

// commits the open transaction
inmemoryDB.commit();

// should return 6, that was the last value of A to be committed
inmemoryDB.get("A");

// throws an error, because there is no open transaction
inmemoryDB.commit();

// throws an error because there is no ongoing transaction
inmemoryDB.rollback();

// should return null because B does not exist in the database
inmemoryDB.get("B");

// starts a new transaction
inmemoryDB.begin_transaction();

// Set key B’s value to 10 within the transaction
inmemoryDB.put("B", 10);

// Rollback the transaction - revert any changes made to B
inmemoryDB.rollback();

// Should return null because changes to B were rolled back
inmemoryDB.get("B");
```
