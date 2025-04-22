"""
LeetCode Problem #357: Count Numbers with Unique Digits

Problem Statement:
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.

Example 1:
Input: n = 2
Output: 91
Explanation: The answer should be the total numbers in the range [0, 100), excluding those with repeated digits.
For example, 11, 22, 33, etc., are excluded.

Example 2:
Input: n = 0
Output: 1
Explanation: The only number in the range [0, 1) is 0.

Constraints:
- 0 <= n <= 8
"""

def countNumbersWithUniqueDigits(n: int) -> int:
    """
    Function to count numbers with unique digits for a given n.
    """
    if n == 0:
        return 1
    if n == 1:
        return 10

    # Start with the count for n = 1
    count = 10
    unique_digits = 9  # Choices for the first digit (1-9)
    available_digits = 9  # Remaining digits to choose from (0-9 excluding the first digit)

    for i in range(2, n + 1):
        unique_digits *= available_digits
        count += unique_digits
        available_digits -= 1  # Reduce the number of available digits

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 2
    print(f"Input: n = {n1}, Output: {countNumbersWithUniqueDigits(n1)}")  # Expected: 91

    # Test Case 2
    n2 = 0
    print(f"Input: n = {n2}, Output: {countNumbersWithUniqueDigits(n2)}")  # Expected: 1

    # Test Case 3
    n3 = 3
    print(f"Input: n = {n3}, Output: {countNumbersWithUniqueDigits(n3)}")  # Expected: 739

    # Test Case 4
    n4 = 1
    print(f"Input: n = {n4}, Output: {countNumbersWithUniqueDigits(n4)}")  # Expected: 10

    # Test Case 5
    n5 = 8
    print(f"Input: n = {n5}, Output: {countNumbersWithUniqueDigits(n5)}")  # Expected: 2345851

"""
Time Complexity:
- The loop runs at most n times (where n <= 8), so the time complexity is O(n).
- Each iteration involves simple arithmetic operations, which are O(1).
- Overall time complexity: O(n).

Space Complexity:
- The space complexity is O(1) since we use a constant amount of extra space.

Topic: Math, Combinatorics
"""