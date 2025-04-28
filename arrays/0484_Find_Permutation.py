"""
LeetCode Problem #484: Find Permutation

Problem Statement:
Given a string `s` that only contains the characters 'D' (decreasing) and 'I' (increasing), 
let `n` be the length of the string plus 1. Return any permutation of the first `n` positive 
integers that satisfy the given input string `s`.

- 'D' means the next number is smaller than the previous number.
- 'I' means the next number is greater than the previous number.

You can assume that `s` is a valid string containing only 'I' and 'D' characters.

Example 1:
Input: s = "IDID"
Output: [1, 3, 2, 4, 5]

Example 2:
Input: s = "III"
Output: [1, 2, 3, 4]

Example 3:
Input: s = "DDI"
Output: [3, 2, 1, 4]

Constraints:
- 1 <= s.length <= 10^5
- s contains only characters 'I' or 'D'.
"""

def findPermutation(s: str) -> list[int]:
    """
    Returns a permutation of the first n positive integers that satisfies the given string s.
    """
    n = len(s) + 1
    low, high = 1, n
    result = []

    for char in s:
        if char == 'I':
            result.append(low)
            low += 1
        elif char == 'D':
            result.append(high)
            high -= 1

    # Append the last remaining number
    result.append(low)  # At this point, low == high
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "IDID"
    print(f"Input: {s1} -> Output: {findPermutation(s1)}")  # Expected: [1, 3, 2, 4, 5]

    # Test Case 2
    s2 = "III"
    print(f"Input: {s2} -> Output: {findPermutation(s2)}")  # Expected: [1, 2, 3, 4]

    # Test Case 3
    s3 = "DDI"
    print(f"Input: {s3} -> Output: {findPermutation(s3)}")  # Expected: [3, 2, 1, 4]

    # Test Case 4 (Edge Case: Single 'I')
    s4 = "I"
    print(f"Input: {s4} -> Output: {findPermutation(s4)}")  # Expected: [1, 2]

    # Test Case 5 (Edge Case: Single 'D')
    s5 = "D"
    print(f"Input: {s5} -> Output: {findPermutation(s5)}")  # Expected: [2, 1]

"""
Time Complexity:
- The algorithm iterates through the string `s` once, performing O(1) operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string `s`.

Space Complexity:
- The algorithm uses a result list of size n (length of `s` + 1).
- Therefore, the space complexity is O(n).

Topic: Arrays
"""