class BankAccount:
    def __init__(self, acc_number, owner, balance, limit=None):
        # TODO: Add your attributes here
        pass

    def deposit(self, amount):
        # TODO: Implement deposit logic
        # 1. Check if amount is positive
        # 2. Add to private balance
        # 3. Print a success or error message
        pass

    def withdraw(self, amount):
        # TODO: Implement withdraw logic
        # 1. Check if amount is valid (positive and <= balance)
        # 2. Deduct from private balance
        # 3. Print success or error message
        pass

    def get_balance(self):
        # TODO: Return the private balance
        pass


class StudentAccount(BankAccount):
    def __init__(self, acc_number, owner, balance, limit=2000):
        # TODO: Initialize the parent class (don't forget 'limit' attribute)
        pass
        
    def withdraw(self, amount):
        # TODO: Override withdraw method
        # 1. Check if amount is greater than self.limit
        # 2. If yes, print Error "Limit Exceeded"
        # 3. If no, call the parent's withdraw method using super()
        pass

    def __str__(self): 
        # Optional: Returns a pretty string representation
        return f"[Student] {self.acc_number} | {self.owner}"


class BusinessAccount(BankAccount):
    # Class Attribute for service fee
    __service_fee = 10

    def __init__(self, acc_number, owner, balance):
        super().__init__(acc_number, owner, balance)

    def withdraw(self, amount):
        # TODO: Override withdraw method
        # 1. Calculate total = amount + service_fee
        # 2. Call parent's withdraw with the TOTAL amount
        # 3. Print a message saying a fee was applied
        pass

    def set_service_fee(new_fee):
        # TODO: Static method to set a new service fee
        pass

    def __str__(self): 
        # Optional: Returns a pretty string representation
        return f"[Business] {self.acc_number} | {self.owner}"

    
    





