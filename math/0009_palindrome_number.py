"""
LeetCode Question #9: Palindrome Number

Problem Statement:
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

An integer is a palindrome when it reads the same backward as forward. For example, `121` is a palindrome while `123` is not.

Constraints:
- -2^31 <= x <= 2^31 - 1
- You are not allowed to convert the integer into a string.

Follow-up:
Could you solve it without converting the integer to a string?
"""

def isPalindrome(x: int) -> bool:
    """
    Determines if an integer is a palindrome without converting it to a string.

    Args:
    x (int): The input integer.

    Returns:
    bool: True if the integer is a palindrome, False otherwise.
    """
    # Negative numbers are not palindromes
    if x < 0:
        return False

    # Numbers ending in 0 (except 0 itself) are not palindromes
    if x != 0 and x % 10 == 0:
        return False

    reversed_half = 0
    while x > reversed_half:
        # Extract the last digit and build the reversed half
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    # Check if the number is a palindrome
    # For even-length numbers, x == reversed_half
    # For odd-length numbers, x == reversed_half // 10
    return x == reversed_half or x == reversed_half // 10

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Positive palindrome number
    print(isPalindrome(121))  # Expected output: True

    # Test Case 2: Negative number (not a palindrome)
    print(isPalindrome(-121))  # Expected output: False

    # Test Case 3: Positive non-palindrome number
    print(isPalindrome(123))  # Expected output: False

    # Test Case 4: Single-digit number (always a palindrome)
    print(isPalindrome(7))  # Expected output: True

    # Test Case 5: Number ending in 0 (not a palindrome unless it's 0)
    print(isPalindrome(10))  # Expected output: False

    # Test Case 6: Large palindrome number
    print(isPalindrome(12321))  # Expected output: True

"""
Time Complexity Analysis:
- The while loop runs until `x` becomes less than or equal to `reversed_half`.
- In each iteration, we divide `x` by 10, so the number of iterations is proportional to the number of digits in `x`.
- If `d` is the number of digits in `x`, the time complexity is O(d).
- Since the number of digits in `x` is proportional to log10(x), the time complexity is O(log10(x)).

Space Complexity Analysis:
- We use a constant amount of extra space (for variables like `reversed_half`).
- Therefore, the space complexity is O(1).

Topic: Math
"""