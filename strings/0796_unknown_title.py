"""
LeetCode Problem #796: Rotate String

Problem Statement:
Given two strings `s` and `goal`, return `True` if and only if `s` can become `goal` after some number of shifts on `s`.

A shift on `s` consists of moving the leftmost character of `s` to the rightmost position. 
For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.

Constraints:
- `s` and `goal` consist of lowercase English letters.
- `1 <= s.length, goal.length <= 100`.
"""

def rotateString(s: str, goal: str) -> bool:
    """
    Determines if string `s` can be rotated to become string `goal`.

    Args:
    s (str): The original string.
    goal (str): The target string.

    Returns:
    bool: True if `s` can be rotated to become `goal`, False otherwise.
    """
    # Check if lengths are different; if so, return False immediately
    if len(s) != len(goal):
        return False
    
    # Concatenate `s` with itself and check if `goal` is a substring
    return goal in (s + s)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic rotation
    s1 = "abcde"
    goal1 = "cdeab"
    print(rotateString(s1, goal1))  # Expected: True

    # Test Case 2: No rotation possible
    s2 = "abcde"
    goal2 = "abced"
    print(rotateString(s2, goal2))  # Expected: False

    # Test Case 3: Identical strings
    s3 = "aaaaa"
    goal3 = "aaaaa"
    print(rotateString(s3, goal3))  # Expected: True

    # Test Case 4: Different lengths
    s4 = "abc"
    goal4 = "abcd"
    print(rotateString(s4, goal4))  # Expected: False

    # Test Case 5: Empty strings
    s5 = ""
    goal5 = ""
    print(rotateString(s5, goal5))  # Expected: True

"""
Time Complexity Analysis:
- Concatenating `s` with itself takes O(n), where n is the length of `s`.
- Checking if `goal` is a substring of `s + s` takes O(n) in the average case.
- Overall time complexity: O(n).

Space Complexity Analysis:
- The concatenated string `s + s` takes O(n) additional space.
- Overall space complexity: O(n).

Topic: Strings
"""