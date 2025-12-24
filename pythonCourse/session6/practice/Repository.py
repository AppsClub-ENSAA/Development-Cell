from abc import ABC, abstractmethod
from BankAccount import StudentAccount, BusinessAccount 
import sqlite3

class AccountRepository(ABC):
    """
    The 'Contract'. Any storage system MUST implement these methods.
    """
    @abstractmethod
    def save(self, account):
        pass

    @abstractmethod
    def load(self, acc_number):
        pass

    @abstractmethod
    def close(self):
        pass

# Implementation A: RAM Storage (Fast, but temporary)
class MemoryRepository(AccountRepository):
    def __init__(self):
        # TODO: Initialize an empty dictionary to store accounts
        pass

    def save(self, account):
        # TODO: Save the account object in the dictionary using acc_number as key
        pass

    def load(self, acc_number):
        # TODO: Retrieve the account object from the dictionary by acc_number
        pass
    
    def close(self):
        # TODO: Clear the dictionary 
        # the clearing itself is optional but we should implement the method close() forced by the abstract class(contract)
        pass


# Implementation B: SQL Storage (Slower, but permanent)
class DatabaseRepository(AccountRepository):
    """
    Handles saving/loading accounts to a SQLite database.
    (Do not modify this class)
    """
    def __init__(self, db_name="bank.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()    
        
        self.cursor.execute( """
            CREATE TABLE IF NOT EXISTS accounts (
                acc_number TEXT PRIMARY KEY,
                owner TEXT,
                balance REAL,
                type TEXT,
                withdrawal_limit REAL)
            """)
        self.conn.commit()

    def save(self, account):
        try:
            acc_type = account.__class__.__name__

            self.cursor.execute("""
                INSERT OR REPLACE INTO accounts 
                (acc_number, owner, balance, type, withdrawal_limit)
                VALUES (?, ?, ?, ?, ?)
            """, (account.acc_number, account.owner, account.get_balance(), acc_type , account.limit))
            
            self.conn.commit()
            print(f">> [SQL] Saved {account.acc_number} <{acc_type}> to Database.")
        except Exception as e:
            print(f"Database Error: {e}")

    def load(self, acc_number):
        self.cursor.execute("SELECT * FROM accounts WHERE acc_number=?", (acc_number,))
        account = self.cursor.fetchone()
        
        if account:
            # Unpack all 5 columns
            acc_num, owner, balance, acc_type, limit_val = account
            
            # Re-create the specific object using the saved extra data
            if acc_type == "StudentAccount":
                return StudentAccount(acc_num, owner, balance, limit=limit_val)
            
            elif acc_type == "BusinessAccount":
                return BusinessAccount(acc_num, owner, balance)
 
        return None

    def close(self):
        self.conn.close()
        print("Database connection closed (data persisted).")