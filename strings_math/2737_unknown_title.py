"""
LeetCode Problem #2737: Find the Closest Palindrome

Problem Statement:
Given a string `s` representing a positive integer, return the closest integer (not including itself), 
which is a palindrome. If there is a tie, return the smaller one.

The input string `s` is guaranteed to represent a positive integer without leading zeros.

Constraints:
- 1 <= s.length <= 18
- `s` consists of only digits.
- The input number does not have leading zeros.

Example:
Input: s = "123"
Output: "121"

Input: s = "1"
Output: "0"

Note:
- A palindrome is a number that reads the same backward as forward, e.g., "121" or "9".
"""

def closestPalindrome(s: str) -> str:
    def is_palindrome(x: str) -> bool:
        return x == x[::-1]

    def create_palindrome(prefix: str, odd_length: bool) -> int:
        if odd_length:
            return int(prefix + prefix[-2::-1])  # Mirror excluding the last digit
        else:
            return int(prefix + prefix[::-1])  # Mirror the entire prefix

    n = len(s)
    num = int(s)

    # Generate candidates
    candidates = set()
    candidates.add(10**n + 1)  # Smallest palindrome with one more digit
    candidates.add(10**(n-1) - 1)  # Largest palindrome with one less digit

    prefix = s[:(n + 1) // 2]  # First half of the number
    prefix_num = int(prefix)

    # Generate palindromes by modifying the prefix
    for diff in [-1, 0, 1]:
        new_prefix = str(prefix_num + diff)
        candidates.add(create_palindrome(new_prefix, n % 2 == 1))

    # Remove the original number itself
    candidates.discard(num)

    # Find the closest palindrome
    closest = None
    for candidate in candidates:
        if closest is None or abs(candidate - num) < abs(closest - num) or \
           (abs(candidate - num) == abs(closest - num) and candidate < closest):
            closest = candidate

    return str(closest)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "123"
    print(closestPalindrome(s1))  # Output: "121"

    # Test Case 2
    s2 = "1"
    print(closestPalindrome(s2))  # Output: "0"

    # Test Case 3
    s3 = "99"
    print(closestPalindrome(s3))  # Output: "101"

    # Test Case 4
    s4 = "808"
    print(closestPalindrome(s4))  # Output: "797"

    # Test Case 5
    s5 = "1000"
    print(closestPalindrome(s5))  # Output: "999"

"""
Time Complexity:
- Let n = len(s).
- Generating candidates involves creating a few palindromes (constant number of operations).
- Comparing candidates involves iterating over a small set of numbers (constant size).
- Thus, the time complexity is O(n), dominated by string manipulations.

Space Complexity:
- The space complexity is O(n) due to the storage of intermediate strings and candidates.

Topic: Strings, Math
"""