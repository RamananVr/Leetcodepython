"""
LeetCode Problem #906: Super Palindromes

Problem Statement:
Let's say a positive integer is a super-palindrome if it is a palindrome and it is also the square of a palindrome.

Given two positive integers left and right represented as strings where left <= right, return the number of super-palindromes integers in the inclusive range [left, right].

Constraints:
- 1 <= left <= right <= 10^18
- left and right are strings representing integers without leading zeros.

Example:
Input: left = "4", right = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are super-palindromes. Note that 676 is not a super-palindrome because it is not a palindrome.
"""

# Solution
def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def superpalindromesInRange(left: str, right: str) -> int:
    left, right = int(left), int(right)
    MAGIC = 10**5  # Limit for generating palindromes
    
    def generate_palindromes(n: int) -> list:
        """Generate all palindromes up to n digits."""
        palindromes = []
        # Odd-length palindromes
        for i in range(1, MAGIC):
            s = str(i)
            palindromes.append(int(s + s[-2::-1]))
        # Even-length palindromes
        for i in range(1, MAGIC):
            s = str(i)
            palindromes.append(int(s + s[::-1]))
        return palindromes

    count = 0
    palindromes = generate_palindromes(MAGIC)
    for p in palindromes:
        square = p * p
        if square > right:
            break
        if square >= left and is_palindrome(str(square)):
            count += 1
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    left = "4"
    right = "1000"
    print(superpalindromesInRange(left, right))  # Output: 4

    # Test Case 2
    left = "1"
    right = "2"
    print(superpalindromesInRange(left, right))  # Output: 1

    # Test Case 3
    left = "1"
    right = "1000000000000000000"
    print(superpalindromesInRange(left, right))  # Output: 70

"""
Time Complexity:
- Generating palindromes: O(MAGIC), where MAGIC is the limit for generating palindromes (10^5).
- Checking each palindrome's square: O(MAGIC).
- Total: O(MAGIC).

Space Complexity:
- Storing palindromes: O(MAGIC).
- Total: O(MAGIC).

Topic: Math, Palindromes, String Manipulation
"""