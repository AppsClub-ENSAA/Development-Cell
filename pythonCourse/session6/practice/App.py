"""
==================================================================================
CHALLENGE: THE 'SMART BANK' SYSTEM
==================================================================================
TASK: 
You are hired to build the backend logic for a new banking system. 
The database connection is already built for you (DatabaseRepository).

YOUR MISSION:
1. Implement the 'BankAccount' parent class with Encapsulation (Private balance).
2. Implement 'StudentAccount' which enforces a withdrawal limit (2000 DH).
3. Implement 'BusinessAccount' which adds a service fee (10 DH) to withdrawals.
4. Implement a repository respecting the pattern to save/load accounts from RAM.
5. Complete the 'App' class to run the simulation.

Order of Implementation:
1. BankAccount class, StudentAccount, BusinessAccount (in BankAccount.py)
2. MemoryRepository class (in Repository.py)
3. App class to simulate the operations (in App.py)

CONCEPTS:
- OOP Pillars: Inheritance, Polymorphism, Encapsulation, Abstraction.
==================================================================================
"""

from Repository import DatabaseRepository, MemoryRepository
from BankAccount import StudentAccount, BusinessAccount


class App:
    def __init__(self):
        self.repo = DatabaseRepository()
        print("=== Welcome to SmartBank System ===\n")

    def run(self):
        # TODO 1: Create a StudentAccount (e.g., Ali, 1500 DH)
        
        # TODO 2: Create a BusinessAccount (e.g., TechCorp, 10000 DH)

        # TODO 3: Try to withdraw 500 from Student (Should succeed)
        
        # TODO 4: Try to withdraw 5000 from Student (Should fail because of Limit)

        # TODO 5: Withdraw 2000 from Business (Should deduct 2010 DH)

        # TODO 6: Save both accounts using self.repo.save()
        
        # TODO 7: Try to load them back to verify

        pass

    def close(self):
        self.repo.close()


app = App()
app.run()
app.close()