"""
LeetCode Problem #1281: Subtract the Product and Sum of Digits of an Integer

Problem Statement:
Given an integer number `n`, return the difference between the product of its digits and the sum of its digits.

Example 1:
Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15

Example 2:
Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21

Constraints:
- 1 <= n <= 10^5
"""

# Python Solution
def subtractProductAndSum(n: int) -> int:
    product = 1
    summation = 0
    
    while n > 0:
        digit = n % 10
        product *= digit
        summation += digit
        n //= 10
    
    return product - summation

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 234
    print(f"Input: {n1}, Output: {subtractProductAndSum(n1)}")  # Expected Output: 15

    # Test Case 2
    n2 = 4421
    print(f"Input: {n2}, Output: {subtractProductAndSum(n2)}")  # Expected Output: 21

    # Test Case 3
    n3 = 1
    print(f"Input: {n3}, Output: {subtractProductAndSum(n3)}")  # Expected Output: 0

    # Test Case 4
    n4 = 99999
    print(f"Input: {n4}, Output: {subtractProductAndSum(n4)}")  # Expected Output: 59031

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through each digit of the number `n`. The number of digits in `n` is proportional to log10(n).
- Therefore, the time complexity is O(log n).

Space Complexity:
- The function uses a constant amount of space for variables `product`, `summation`, and `digit`.
- Therefore, the space complexity is O(1).
"""

# Topic: Math