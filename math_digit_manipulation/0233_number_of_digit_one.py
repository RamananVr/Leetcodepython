"""
LeetCode Question #233: Number of Digit One

Problem Statement:
Given an integer `n`, count the total number of digit `1` appearing in all non-negative integers less than or equal to `n`.

Example 1:
Input: n = 13
Output: 6
Explanation: The digit 1 appears in the numbers 1, 10, 11, 12, and 13.

Example 2:
Input: n = 0
Output: 0

Constraints:
- 0 <= n <= 10^9
"""

def countDigitOne(n: int) -> int:
    """
    Function to count the total number of digit '1' appearing in all non-negative integers <= n.
    """
    if n <= 0:
        return 0

    count = 0
    factor = 1  # Represents the current digit's place value (1, 10, 100, etc.)
    
    while n // factor > 0:
        lower_digits = n % factor
        current_digit = (n // factor) % 10
        higher_digits = n // (factor * 10)
        
        if current_digit == 0:
            count += higher_digits * factor
        elif current_digit == 1:
            count += higher_digits * factor + lower_digits + 1
        else:
            count += (higher_digits + 1) * factor
        
        factor *= 10
    
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 13
    print(f"Input: {n1}, Output: {countDigitOne(n1)}")  # Expected Output: 6

    # Test Case 2
    n2 = 0
    print(f"Input: {n2}, Output: {countDigitOne(n2)}")  # Expected Output: 0

    # Test Case 3
    n3 = 100
    print(f"Input: {n3}, Output: {countDigitOne(n3)}")  # Expected Output: 21

    # Test Case 4
    n4 = 99
    print(f"Input: {n4}, Output: {countDigitOne(n4)}")  # Expected Output: 20

    # Test Case 5
    n5 = 1234
    print(f"Input: {n5}, Output: {countDigitOne(n5)}")  # Expected Output: 689

"""
Time Complexity:
The time complexity of the solution is O(log10(n)), where n is the input number. This is because we process each digit of the number, and the number of digits in n is proportional to log10(n).

Space Complexity:
The space complexity is O(1) since we are using a constant amount of extra space.

Topic: Math, Digit Manipulation
"""