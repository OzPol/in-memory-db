import sys
import os

# Add the root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from in_memory_db import InMemoryDB

class TestInMemoryDB(unittest.TestCase):
    def test_put_without_transaction(self):
        db = InMemoryDB()
        with self.assertRaises(Exception) as context:
            db.put('A', 5)
        self.assertTrue('No active transaction' in str(context.exception))
    
    def test_transactional_operations(self):
        db = InMemoryDB()

        # 1. Should return "A does not exist.", because 'A' doesn't exist in the DB yet
        self.assertEqual(db.get("A"), "A does not exist")

        # 2. Should throw an error because a transaction is not in progress
        with self.assertRaises(Exception) as context:
            db.put("A", 5)
        self.assertTrue("No active transaction" in str(context.exception))

        # 3. Starts a new transaction
        db.begin_transaction()

        # 4. Set value of 'A' to 5, but it's not committed yet
        db.put("A", 5)

        # 5. Should return "A does not exist.", because updates to 'A' are not committed yet
        self.assertEqual(db.get("A"), "A does not exist")

        # 6. Update 'A's value to 6 within the transaction
        db.put("A", 6)

        # 7. Commit the open transaction
        db.commit()

        # 8. Should return "A = 6.", that was the last value of 'A' to be committed
        self.assertEqual(db.get("A"), "A = 6")

        # 9. Throws an error, because there is no open transaction
        with self.assertRaises(Exception) as context:
            db.commit()
        self.assertTrue("No active transaction" in str(context.exception))

        # 10. Throws an error because there is no ongoing transaction
        with self.assertRaises(Exception) as context:
            db.rollback()
        self.assertTrue("No active transaction" in str(context.exception))

        # 11. Should return "B does not exist.", because 'B' does not exist in the database
        self.assertEqual(db.get("B"), "B does not exist")

        # 12. Starts a new transaction
        db.begin_transaction()

        # 13. Set key 'B's value to 10 within the transaction
        db.put("B", 10)

        # 14. Rollback the transaction - revert any changes made to 'B'
        db.rollback()

        # 15. Should return "B does not exist.", because changes to 'B' were rolled back
        self.assertEqual(db.get("B"), "B does not exist")


if __name__ == '__main__':
    unittest.main()
