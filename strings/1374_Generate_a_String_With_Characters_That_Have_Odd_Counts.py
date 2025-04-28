"""
LeetCode Problem #1374: Generate a String With Characters That Have Odd Counts

Problem Statement:
Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.

The returned string must contain only lowercase English letters. If there are multiple valid strings, return any of them.

Example 1:
Input: n = 4
Output: "pppz"
Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. 
Note that there are many other valid strings such as "ohhh" and "love".

Example 2:
Input: n = 2
Output: "xy"
Explanation: "xy" is a valid string since 'x' occurs once and 'y' occurs once. 
Note that there are many other valid strings such as "ab" and "cd".

Example 3:
Input: n = 7
Output: "holaaaa"
Explanation: "holaaaa" is a valid string since 'h' occurs once and 'o' occurs once and 'l' occurs once and 'a' occurs four times.

Constraints:
- 1 <= n <= 500
"""

# Python Solution
def generateTheString(n: int) -> str:
    """
    Generate a string with n characters such that each character occurs an odd number of times.
    """
    # If n is odd, we can simply return a string of 'a' repeated n times.
    if n % 2 == 1:
        return 'a' * n
    # If n is even, we can return a string of 'a' repeated (n-1) times and one 'b'.
    else:
        return 'a' * (n - 1) + 'b'

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 4
    print(f"Input: {n1}, Output: {generateTheString(n1)}")  # Expected: "aaab" or similar

    # Test Case 2
    n2 = 2
    print(f"Input: {n2}, Output: {generateTheString(n2)}")  # Expected: "ab" or similar

    # Test Case 3
    n3 = 7
    print(f"Input: {n3}, Output: {generateTheString(n3)}")  # Expected: "aaaaaaa" or similar

    # Test Case 4
    n4 = 1
    print(f"Input: {n4}, Output: {generateTheString(n4)}")  # Expected: "a"

    # Test Case 5
    n5 = 10
    print(f"Input: {n5}, Output: {generateTheString(n5)}")  # Expected: "aaaaaaaaab" or similar

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution runs in O(n) time because we are constructing a string of length n.

Space Complexity:
- The space complexity is O(n) because the output string requires space proportional to its length.
"""

# Topic: Strings