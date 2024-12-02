# In-memory database class with support for transactions.
class InMemoryDB:
    def __init__(self):
        self.main_db = {}                           # Main database to store committed key-value pairs
        self.transaction_active = False             # Transaction log to store uncommitted changes
        self.transaction_log = {}                   # Flag to indicate if a transaction is active

    def begin_transaction(self):
        """
        Starts a new transaction.
        Raises an exception if a transaction is already in progress.
        """
        if self.transaction_active:
            raise Exception("Transaction already in progress")
        # Initialize a new transaction
        self.transaction_active = True
        self.transaction_log = {}
        return "Transaction started."

    def put(self, key, value):
        """
        Inserts or updates a key-value pair within a transaction.
        Raises an exception if no transaction is active.
        """
        if not self.transaction_active:
            raise Exception("No active transaction")
        if not key or not key.strip():
            raise Exception("Key cannot be empty or whitespace")
        if not isinstance(value, int):
            raise Exception("Value must be an integer")
        # Store the change in the transaction log
        self.transaction_log[key] = value
        return f"Set {key} = {value}"
    
    def get(self, key):
        """
        Retrieves the value associated with the key from the main database.
        Returns None if the key does not exist.
        Note: Uncommitted changes are not visible to this method until after commit() is called,
        regardless of whether we are within a transaction or not.
        """
        value = self.main_db.get(key)   # The built in dictionary's get() method
        if value is None:
            return f"{key} does not exist"
        return f"{key} = {value}"
    
    def commit(self):
        """
        Commits the current transaction, applying all changes to the main database.
        Raises an exception if no transaction is active.
        """
        if not self.transaction_active:
            raise Exception("No active transaction to commit")
        if not self.transaction_log:  # Check if there are no changes
            self.transaction_active = False
            self.transaction_log = {}
            return "Transaction committed: No changes made!"  # Message when no changes are made   
        # Apply the changes from the transaction log to the main database
        self.main_db.update(self.transaction_log)
        # Reset the transaction
        self.transaction_active = False
        self.transaction_log = {}
        return "Transaction committed: Changes applied!"  # Message when changes are applied

    def rollback(self):
        """
        Aborts the current transaction, discarding all uncommitted changes.
        Raises an exception if no transaction is active.
        """
        if not self.transaction_active:
            raise Exception("No active transaction")
        
        self.transaction_log = {}               # Discard the changes in the transaction log
        self.transaction_active = False         # End the transaction
        return "Transaction rolled back."       # Return a message indicating the transaction was rolled back


"""
Main Database (main_db): Stores all committed key-value pairs.
Transaction Log (transaction_log): Temporarily holds changes made during a transaction.
Transaction Active Flag (transaction_active): Indicates whether a transaction is currently active.
"""