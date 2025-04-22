"""
LeetCode Question #9: Palindrome Number

Problem Statement:
Given an integer x, return true if x is a palindrome, and false otherwise.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is a palindrome while 123 is not.

Constraints:
- -2^31 <= x <= 2^31 - 1

Follow up:
Could you solve it without converting the integer to a string?
"""

def isPalindrome(x: int) -> bool:
    """
    Determines whether the given integer x is a palindrome.

    Args:
    x (int): The integer to check.

    Returns:
    bool: True if x is a palindrome, False otherwise.
    """
    # Negative numbers are not palindromes
    if x < 0:
        return False
    
    # Initialize variables for reversing the number
    original = x
    reversed_num = 0
    
    while x > 0:
        # Extract the last digit and add it to the reversed number
        reversed_num = reversed_num * 10 + x % 10
        # Remove the last digit from x
        x //= 10
    
    # Check if the reversed number matches the original number
    return original == reversed_num

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
    
    # Test Case 5: Large palindrome number
    print(isPalindrome(12321))  # Expected output: True
    
    # Test Case 6: Large non-palindrome number
    print(isPalindrome(12345))  # Expected output: False

# Topic: Math