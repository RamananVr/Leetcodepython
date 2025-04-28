"""
LeetCode Problem #2806: Account Balance After Rounded Purchase

Problem Statement:
You are given an integer `purchaseAmount` representing the amount you need to pay in cents. 
In a store, the system rounds the purchase amount to the nearest multiple of 10 cents. 
If the purchase amount is already a multiple of 10, no rounding is needed.

Write a function `accountBalanceAfterPurchase` that takes an integer `purchaseAmount` and returns 
the account balance after the purchase. Assume the initial account balance is 100 cents.

The rounding rules are as follows:
- If the last digit of `purchaseAmount` is less than 5, round down to the nearest multiple of 10.
- Otherwise, round up to the nearest multiple of 10.

Constraints:
- 0 <= purchaseAmount <= 100
"""

def accountBalanceAfterPurchase(purchaseAmount: int) -> int:
    """
    Calculate the account balance after a rounded purchase.

    Args:
    purchaseAmount (int): The amount to be paid in cents.

    Returns:
    int: The remaining account balance in cents.
    """
    # Round the purchase amount to the nearest multiple of 10
    roundedAmount = (purchaseAmount + 5) // 10 * 10
    # Initial balance is 100 cents, subtract the rounded amount
    return 100 - roundedAmount

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Purchase amount is already a multiple of 10
    print(accountBalanceAfterPurchase(30))  # Expected output: 70

    # Test Case 2: Purchase amount rounds down
    print(accountBalanceAfterPurchase(24))  # Expected output: 80

    # Test Case 3: Purchase amount rounds up
    print(accountBalanceAfterPurchase(26))  # Expected output: 70

    # Test Case 4: Purchase amount is 0
    print(accountBalanceAfterPurchase(0))  # Expected output: 100

    # Test Case 5: Purchase amount is 100
    print(accountBalanceAfterPurchase(100))  # Expected output: 0

"""
Time Complexity Analysis:
- The function performs a constant number of operations (addition, division, multiplication, and subtraction).
- Therefore, the time complexity is O(1).

Space Complexity Analysis:
- The function uses a constant amount of space for variables.
- Therefore, the space complexity is O(1).

Topic: Math
"""