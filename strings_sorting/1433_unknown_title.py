"""
LeetCode Problem #1433: Check If a String Can Break Another String

Problem Statement:
Given two strings `s1` and `s2` of the same length, determine if one string can break the other string. 
A string `x` can break string `y` (both of the same length) if `x[i] >= y[i]` (in lexicographical order) 
for all `i` in the range `[0, len(x) - 1]`.

Return `True` if `s1` can break `s2` or `s2` can break `s1`, otherwise return `False`.

Constraints:
- `s1.length == s2.length`
- `1 <= s1.length <= 10^5`
- `s1` and `s2` consist of only lowercase English letters.
"""

def checkIfCanBreak(s1: str, s2: str) -> bool:
    """
    Determines if one string can break the other string.

    Args:
    s1 (str): First string.
    s2 (str): Second string.

    Returns:
    bool: True if one string can break the other, False otherwise.
    """
    # Sort both strings lexicographically
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    
    # Check if s1 can break s2
    can_s1_break_s2 = all(c1 >= c2 for c1, c2 in zip(sorted_s1, sorted_s2))
    
    # Check if s2 can break s1
    can_s2_break_s1 = all(c2 >= c1 for c1, c2 in zip(sorted_s1, sorted_s2))
    
    # Return True if either condition is satisfied
    return can_s1_break_s2 or can_s2_break_s1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: s1 can break s2
    s1 = "abc"
    s2 = "xya"
    print(checkIfCanBreak(s1, s2))  # Expected output: True

    # Test Case 2: s2 can break s1
    s1 = "abe"
    s2 = "acd"
    print(checkIfCanBreak(s1, s2))  # Expected output: True

    # Test Case 3: Neither string can break the other
    s1 = "leetcode"
    s2 = "interview"
    print(checkIfCanBreak(s1, s2))  # Expected output: False

    # Test Case 4: Edge case with single character strings
    s1 = "a"
    s2 = "b"
    print(checkIfCanBreak(s1, s2))  # Expected output: True

    # Test Case 5: Edge case with identical strings
    s1 = "abc"
    s2 = "abc"
    print(checkIfCanBreak(s1, s2))  # Expected output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting both strings takes O(n log n), where n is the length of the strings.
- The comparison using `zip` and `all` takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- Sorting creates temporary lists, which take O(n) space.
- Overall space complexity: O(n).

Topic: Strings, Sorting
"""