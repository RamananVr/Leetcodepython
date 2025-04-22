"""
LeetCode Question #479: Largest Palindrome Product

Problem Statement:
Given an integer n, return the largest palindrome that can be made as the product of two n-digit numbers. 
Since the answer can be very large, return it modulo 1337.

Example 1:
Input: n = 2
Output: 987
Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Example 2:
Input: n = 1
Output: 9

Constraints:
- 1 <= n <= 8
"""

def largestPalindrome(n: int) -> int:
    if n == 1:
        return 9  # Special case for single-digit numbers

    upper_limit = 10**n - 1  # Largest n-digit number
    lower_limit = 10**(n - 1)  # Smallest n-digit number
    max_palindrome = 0

    for i in range(upper_limit, lower_limit - 1, -1):
        for j in range(i, lower_limit - 1, -1):
            product = i * j
            if product <= max_palindrome:
                break  # No need to check smaller products
            if str(product) == str(product)[::-1]:  # Check if the product is a palindrome
                max_palindrome = product

    return max_palindrome % 1337

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 2
    print(f"Input: n = {n}")
    print(f"Output: {largestPalindrome(n)}")  # Expected Output: 987

    # Test Case 2
    n = 1
    print(f"Input: n = {n}")
    print(f"Output: {largestPalindrome(n)}")  # Expected Output: 9

    # Test Case 3
    n = 3
    print(f"Input: n = {n}")
    print(f"Output: {largestPalindrome(n)}")  # Expected Output: 123 (Example for larger n)

"""
Time Complexity:
- The outer loop runs from the largest n-digit number down to the smallest, so it iterates approximately 10^n times.
- The inner loop also runs approximately 10^n times in the worst case.
- Checking if a number is a palindrome takes O(d), where d is the number of digits in the product. For n-digit numbers, d is at most 2n.
- Overall time complexity: O((10^n)^2 * 2n) = O(n * 10^(2n)).

Space Complexity:
- The space complexity is O(1) since we are only using a few variables to store intermediate results.

Topic: Math, Brute Force
"""