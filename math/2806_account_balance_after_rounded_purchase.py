"""
LeetCode Problem 2806: Account Balance After Rounded Purchase

Initially, you have a bank account balance of 100 dollars.

You are given an integer purchaseAmount representing the amount of a purchase in dollars.

When making a purchase, the amount spent is rounded to the nearest multiple of 10 dollars. In other words:
- If the last digit of purchaseAmount is less than 5, round down to the nearest multiple of 10.
- If the last digit of purchaseAmount is greater than or equal to 5, round up to the nearest multiple of 10.

Return the account balance after making the purchase.

Constraints:
- 0 <= purchaseAmount <= 100

Example 1:
Input: purchaseAmount = 9
Output: 90
Explanation: In this case, the nearest multiple of 10 to 9 is 10. Hence, your account balance becomes 100 - 10 = 90.

Example 2:
Input: purchaseAmount = 15
Output: 80
Explanation: In this case, the nearest multiple of 10 to 15 is 20. Hence, your account balance becomes 100 - 20 = 80.

Example 3:
Input: purchaseAmount = 10
Output: 90
Explanation: In this case, 10 is already a multiple of 10. Hence, your account balance becomes 100 - 10 = 90.
"""

def account_balance_after_purchase(purchase_amount):
    """
    Approach 1: Mathematical Rounding
    
    Use mathematical rounding rules to round to nearest 10.
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # Round to nearest multiple of 10
    last_digit = purchase_amount % 10
    
    if last_digit < 5:
        # Round down
        rounded_amount = purchase_amount - last_digit
    else:
        # Round up
        rounded_amount = purchase_amount + (10 - last_digit)
    
    return 100 - rounded_amount

def account_balance_after_purchase_builtin(purchase_amount):
    """
    Approach 2: Using Built-in Round Function
    
    Use Python's built-in round function with custom logic.
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # Round to nearest 10
    rounded_amount = round(purchase_amount / 10) * 10
    return 100 - rounded_amount

def account_balance_after_purchase_floor_ceil(purchase_amount):
    """
    Approach 3: Using Floor and Ceil
    
    Compare distances to floor and ceil multiples of 10.
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    import math
    
    # Get floor and ceil multiples of 10
    floor_multiple = (purchase_amount // 10) * 10
    ceil_multiple = floor_multiple + 10
    
    # Choose the nearest one
    if purchase_amount - floor_multiple < ceil_multiple - purchase_amount:
        rounded_amount = floor_multiple
    else:
        rounded_amount = ceil_multiple
    
    return 100 - rounded_amount

def account_balance_after_purchase_conditional(purchase_amount):
    """
    Approach 4: Direct Conditional Logic
    
    Use if-else conditions for clarity.
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    last_digit = purchase_amount % 10
    
    if last_digit == 0:
        rounded_amount = purchase_amount
    elif last_digit <= 5:
        rounded_amount = purchase_amount - last_digit
    else:
        rounded_amount = purchase_amount + (10 - last_digit)
    
    return 100 - rounded_amount

def account_balance_after_purchase_lookup(purchase_amount):
    """
    Approach 5: Lookup Table for Last Digit
    
    Use precomputed lookup table for rounding rules.
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # Lookup table for rounding: last_digit -> adjustment
    rounding_adjustment = {
        0: 0,   # 0 -> 0 (no change)
        1: -1,  # 1 -> 0 (round down)
        2: -2,  # 2 -> 0 (round down)
        3: -3,  # 3 -> 0 (round down)
        4: -4,  # 4 -> 0 (round down)
        5: 5,   # 5 -> 10 (round up)
        6: 4,   # 6 -> 10 (round up)
        7: 3,   # 7 -> 10 (round up)
        8: 2,   # 8 -> 10 (round up)
        9: 1    # 9 -> 10 (round up)
    }
    
    last_digit = purchase_amount % 10
    rounded_amount = purchase_amount + rounding_adjustment[last_digit]
    
    return 100 - rounded_amount

def account_balance_after_purchase_bitwise(purchase_amount):
    """
    Approach 6: Bitwise Operations (Alternative)
    
    Use bitwise operations for rounding (less readable but interesting).
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # Add 5 and then truncate last digit for rounding
    rounded_amount = ((purchase_amount + 5) // 10) * 10
    return 100 - rounded_amount

class BankAccount:
    """
    Approach 7: Object-Oriented Solution
    
    Model as a bank account class with purchase method.
    """
    def __init__(self, initial_balance=100):
        self.balance = initial_balance
    
    def make_purchase(self, purchase_amount):
        """
        Make a purchase with rounding to nearest 10
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Round to nearest multiple of 10
        last_digit = purchase_amount % 10
        
        if last_digit < 5:
            rounded_amount = purchase_amount - last_digit
        else:
            rounded_amount = purchase_amount + (10 - last_digit)
        
        self.balance -= rounded_amount
        return self.balance
    
    def get_balance(self):
        return self.balance
    
    def reset_balance(self, amount=100):
        self.balance = amount

def account_balance_comprehensive_test():
    """
    Comprehensive test covering edge cases
    """
    # Edge cases to test
    edge_cases = [
        0,    # Minimum value
        1,    # Round down
        4,    # Round down boundary
        5,    # Round up boundary  
        9,    # Round up
        10,   # Exact multiple
        15,   # Round up
        50,   # Exact middle
        95,   # Near maximum
        100   # Maximum value
    ]
    
    print("Comprehensive Edge Case Testing:")
    print("Purchase Amount -> Rounded Amount -> Balance")
    print("-" * 45)
    
    for amount in edge_cases:
        balance = account_balance_after_purchase(amount)
        rounded = 100 - balance
        print(f"{amount:3d} -> {rounded:3d} -> {balance:3d}")

# Test cases
def test_account_balance_after_purchase():
    test_cases = [
        (9, 90),
        (15, 80),
        (10, 90),
        (0, 100),
        (1, 100),
        (4, 100),
        (5, 90),
        (6, 90),
        (25, 70),
        (50, 50),
        (55, 40),
        (100, 0)
    ]
    
    approaches = [
        ("Mathematical", account_balance_after_purchase),
        ("Built-in Round", account_balance_after_purchase_builtin),
        ("Floor/Ceil", account_balance_after_purchase_floor_ceil),
        ("Conditional", account_balance_after_purchase_conditional),
        ("Lookup Table", account_balance_after_purchase_lookup),
        ("Bitwise", account_balance_after_purchase_bitwise)
    ]
    
    for approach_name, func in approaches:
        print(f"Testing {approach_name} approach:")
        all_passed = True
        
        for purchase_amount, expected in test_cases:
            result = func(purchase_amount)
            passed = result == expected
            if not passed:
                all_passed = False
            print(f"  Purchase: {purchase_amount}, Expected: {expected}, Got: {result}, {'✓' if passed else '✗'}")
        
        print(f"  Overall: {'✓ All Passed' if all_passed else '✗ Some Failed'}\n")
    
    # Test OOP approach
    print("Testing Object-Oriented approach:")
    account = BankAccount()
    oop_results = []
    
    for purchase_amount, expected in test_cases:
        account.reset_balance(100)
        result = account.make_purchase(purchase_amount)
        oop_results.append((purchase_amount, expected, result))
        passed = result == expected
        print(f"  Purchase: {purchase_amount}, Expected: {expected}, Got: {result}, {'✓' if passed else '✗'}")
    
    # Run comprehensive test
    print("\n")
    account_balance_comprehensive_test()

if __name__ == "__main__":
    test_account_balance_after_purchase()

"""
Topics: Math, Simulation
Difficulty: Easy

Key Insights:
1. Rounding to nearest 10: check last digit
2. Last digit < 5: round down, >= 5: round up
3. Multiple approaches: mathematical, built-in functions, lookup tables
4. Can be modeled as object-oriented bank account
5. Edge cases: 0, exact multiples, boundary values (4,5)

Companies: PayPal, Square, Stripe, Financial Services
"""
