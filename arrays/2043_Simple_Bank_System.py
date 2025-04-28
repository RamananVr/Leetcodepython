"""
LeetCode Problem #2043: Simple Bank System

Problem Statement:
Design a simple bank system that supports the following operations:
1. Transfer: Transfer money from one account to another.
2. Deposit: Deposit money into an account.
3. Withdraw: Withdraw money from an account.

Implement the `Bank` class:
- `Bank(balance: List[int])`: Initializes the object with the balance of each account.
- `transfer(account1: int, account2: int, money: int) -> bool`: Transfers `money` from `account1` to `account2`. Returns `true` if the operation is successful, otherwise returns `false`.
- `deposit(account: int, money: int) -> bool`: Deposits `money` into the specified `account`. Returns `true` if the operation is successful, otherwise returns `false`.
- `withdraw(account: int, money: int) -> bool`: Withdraws `money` from the specified `account`. Returns `true` if the operation is successful, otherwise returns `false`.

Constraints:
- The number of accounts is between 1 and 10^5.
- The balance of each account is between 0 and 10^9.
- The amount of money involved in any operation is between 1 and 10^6.

Operations are guaranteed to be called one at a time.

"""

# Solution
class Bank:
    def __init__(self, balance: list[int]):
        self.balance = balance
        self.n = len(balance)  # Number of accounts

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # Check if both accounts are valid
        if not (1 <= account1 <= self.n and 1 <= account2 <= self.n):
            return False
        # Check if account1 has enough balance
        if self.balance[account1 - 1] < money:
            return False
        # Perform the transfer
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        # Check if the account is valid
        if not (1 <= account <= self.n):
            return False
        # Perform the deposit
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        # Check if the account is valid
        if not (1 <= account <= self.n):
            return False
        # Check if the account has enough balance
        if self.balance[account - 1] < money:
            return False
        # Perform the withdrawal
        self.balance[account - 1] -= money
        return True


# Example Test Cases
if __name__ == "__main__":
    # Initialize the bank with balances
    bank = Bank([100, 200, 300, 400, 500])

    # Test transfer
    assert bank.transfer(1, 2, 50) == True  # Transfer 50 from account 1 to account 2
    assert bank.transfer(1, 6, 50) == False  # Invalid account 6
    assert bank.transfer(1, 2, 200) == False  # Insufficient balance in account 1

    # Test deposit
    assert bank.deposit(3, 100) == True  # Deposit 100 into account 3
    assert bank.deposit(6, 100) == False  # Invalid account 6

    # Test withdraw
    assert bank.withdraw(4, 200) == True  # Withdraw 200 from account 4
    assert bank.withdraw(4, 300) == False  # Insufficient balance in account 4
    assert bank.withdraw(6, 100) == False  # Invalid account 6

    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

1. Transfer:
   - Time Complexity: O(1) (constant time for balance checks and updates)
   - Space Complexity: O(1) (no additional space used)

2. Deposit:
   - Time Complexity: O(1) (constant time for balance update)
   - Space Complexity: O(1) (no additional space used)

3. Withdraw:
   - Time Complexity: O(1) (constant time for balance checks and updates)
   - Space Complexity: O(1) (no additional space used)

Overall:
- Time Complexity: O(1) for each operation
- Space Complexity: O(n), where n is the number of accounts (to store balances)

Topic: Arrays
"""