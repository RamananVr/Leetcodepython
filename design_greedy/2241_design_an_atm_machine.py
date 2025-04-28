"""
LeetCode Question #2241: Design an ATM Machine

Problem Statement:
An ATM machine stores banknotes of 5 denominations: 20, 50, 100, 200, and 500 dollars. Initially, the ATM is empty. 
You can use the ATM machine in two ways:

1. `deposit(banknotesCount)`: Deposits banknotes into the ATM. 
   - `banknotesCount` is a list of 5 integers representing the number of banknotes of each denomination to deposit.
   - For example, `banknotesCount[0]` is the number of $20 banknotes, `banknotesCount[1]` is the number of $50 banknotes, and so on.

2. `withdraw(amount)`: Withdraws the requested amount of money from the ATM.
   - Returns a list of 5 integers representing the number of banknotes of each denomination to withdraw, in the order `[20, 50, 100, 200, 500]`.
   - If it is not possible to withdraw the requested amount, returns `[-1]`.

Constraints:
- The sum of the banknotes in the ATM will not exceed 10^9.
- The requested amount will not exceed 10^9.
- The denominations are sorted in ascending order: `[20, 50, 100, 200, 500]`.

"""

class ATM:
    def __init__(self):
        # Initialize the ATM with zero banknotes for each denomination
        self.denominations = [20, 50, 100, 200, 500]
        self.banknotes = [0] * 5

    def deposit(self, banknotesCount):
        # Add the deposited banknotes to the ATM
        for i in range(5):
            self.banknotes[i] += banknotesCount[i]

    def withdraw(self, amount):
        # Attempt to withdraw the requested amount
        result = [0] * 5
        for i in range(4, -1, -1):  # Start from the largest denomination
            if amount >= self.denominations[i]:
                # Determine the maximum number of banknotes of this denomination to use
                num_banknotes = min(amount // self.denominations[i], self.banknotes[i])
                result[i] = num_banknotes
                amount -= num_banknotes * self.denominations[i]

        if amount == 0:
            # If the amount is successfully withdrawn, update the ATM's banknotes
            for i in range(5):
                self.banknotes[i] -= result[i]
            return result
        else:
            # If the amount cannot be withdrawn, return [-1]
            return [-1]


# Example Test Cases
if __name__ == "__main__":
    atm = ATM()

    # Test Case 1: Deposit banknotes
    atm.deposit([0, 1, 2, 1, 0])  # Deposit 0x$20, 1x$50, 2x$100, 1x$200, 0x$500
    print(atm.withdraw(600))  # Expected output: [0, 1, 2, 1, 0] (1x$50, 2x$100, 1x$200)

    # Test Case 2: Withdraw an amount that cannot be fulfilled
    print(atm.withdraw(800))  # Expected output: [-1] (Not enough banknotes)

    # Test Case 3: Withdraw an exact amount
    atm.deposit([10, 0, 0, 0, 1])  # Deposit 10x$20, 0x$50, 0x$100, 0x$200, 1x$500
    print(atm.withdraw(520))  # Expected output: [10, 0, 0, 0, 1] (10x$20, 1x$500)

    # Test Case 4: Withdraw an amount that leaves the ATM empty
    print(atm.withdraw(520))  # Expected output: [-1] (Not enough banknotes)

"""
Time and Space Complexity Analysis:

1. `deposit(banknotesCount)`:
   - Time Complexity: O(1) (constant time to update the banknotes array).
   - Space Complexity: O(1) (no additional space used).

2. `withdraw(amount)`:
   - Time Complexity: O(1) (constant time to iterate over the 5 denominations).
   - Space Complexity: O(1) (no additional space used).

Overall:
- Time Complexity: O(1) for both operations.
- Space Complexity: O(1).

Topic: Design, Greedy
"""