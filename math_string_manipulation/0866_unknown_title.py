"""
LeetCode Problem #866: Prime Palindrome

Problem Statement:
Given an integer n, return the smallest prime palindrome greater than or equal to n.

An integer is a palindrome if it reads the same backward as forward. For example, 12321 is a palindrome.

- A prime number is a number greater than 1 with no divisors other than 1 and itself.
- For example, 2, 3, 5, 7, 11, and 13 are prime numbers.

Note:
1. 1 <= n <= 10^8
2. The answer is guaranteed to exist and be less than 2 * 10^8.
"""

# Solution
import math

def is_prime(num):
    """Helper function to check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    """Helper function to check if a number is a palindrome."""
    s = str(num)
    return s == s[::-1]

def prime_palindrome(n):
    """
    Function to find the smallest prime palindrome greater than or equal to n.
    """
    # Special case: All even-length palindromes are divisible by 11 (except 11 itself),
    # so we can skip checking even-length palindromes.
    if 8 <= n <= 11:
        return 11

    while True:
        if is_palindrome(n) and is_prime(n):
            return n
        n += 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 6
    print(prime_palindrome(n))  # Output: 7

    # Test Case 2
    n = 8
    print(prime_palindrome(n))  # Output: 11

    # Test Case 3
    n = 13
    print(prime_palindrome(n))  # Output: 101

    # Test Case 4
    n = 100
    print(prime_palindrome(n))  # Output: 101

    # Test Case 5
    n = 9989900
    print(prime_palindrome(n))  # Output: 100030001

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Checking if a number is a palindrome: O(d), where d is the number of digits in the number.
   - Checking if a number is prime: O(sqrt(n)).
   - In the worst case, we increment n repeatedly until we find a prime palindrome. This depends on the density of prime palindromes.
   - Overall, the time complexity is approximately O(n * sqrt(n)) in the worst case.

2. Space Complexity:
   - The space complexity is O(1), as we are using a constant amount of extra space.

Topic: Math, String Manipulation
"""