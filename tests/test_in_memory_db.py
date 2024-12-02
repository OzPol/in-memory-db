# File: test_in_memory_db.py
import sys
import os

# Add the root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from in_memory_db import InMemoryDB

def main():
    db = InMemoryDB()

    # Should return None, because 'A' doesn't exist yet
    print(db.get('A'))  # Output: None

    try:
        # Should raise an exception because there's no active transaction
        db.put('A', 5)
    except Exception as e:
        print(e)  # Output: No active transaction

    # Start a transaction
    db.begin_transaction()

    # Put 'A' within the transaction
    db.put('A', 5)

    # Should still return None, because 'A' is not committed yet
    print(db.get('A'))  # Output: 5 (since get can see uncommitted changes within the transaction)

    # Commit the transaction
    db.commit()

    # Now 'A' should return 5
    print(db.get('A'))  # Output: 5

    # Try to commit again without an active transaction
    try:
        db.commit()
    except Exception as e:
        print(e)  # Output: No active transaction

    # Start another transaction and rollback
    db.begin_transaction()
    db.put('A', 10)
    print(db.get('A'))  # Output: 10
    db.rollback()
    print(db.get('A'))  # Output: 5

if __name__ == "__main__":
    main()
