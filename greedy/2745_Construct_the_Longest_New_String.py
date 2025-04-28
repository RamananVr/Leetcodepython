"""
LeetCode Problem #2745: Construct the Longest New String

Problem Statement:
You are given three integers `x`, `y`, and `z`.

You have `x` number of "AA" strings, `y` number of "BB" strings, and `z` number of "AB" strings. 
You want to construct the longest possible string by concatenating these strings together under the following rules:
1. You can only use each string once.
2. The resulting string must not contain two consecutive "AA" substrings or two consecutive "BB" substrings.

Return the length of the longest string you can construct.

Constraints:
- 0 <= x, y, z <= 10^5
"""

def longestString(x: int, y: int, z: int) -> int:
    """
    Calculate the length of the longest string that can be constructed
    using the given number of "AA", "BB", and "AB" strings.

    Args:
    x (int): Number of "AA" strings.
    y (int): Number of "BB" strings.
    z (int): Number of "AB" strings.

    Returns:
    int: The length of the longest string.
    """
    # The maximum number of "AB" pairs we can use is determined by the smaller of x and y.
    ab_pairs = min(x, y)
    
    # Each "AB" pair contributes 4 characters ("AB" + "BA").
    result = ab_pairs * 4
    
    # After using the "AB" pairs, we can add one more "AA" or "BB" if available.
    if x > ab_pairs:
        result += 2  # Add one "AA" (2 characters).
    elif y > ab_pairs:
        result += 2  # Add one "BB" (2 characters).
    
    # Finally, add the "AB" strings (each contributes 2 characters).
    result += z * 2
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    x1, y1, z1 = 2, 3, 1
    print(longestString(x1, y1, z1))  # Expected Output: 10

    # Test Case 2
    x2, y2, z2 = 5, 5, 2
    print(longestString(x2, y2, z2))  # Expected Output: 24

    # Test Case 3
    x3, y3, z3 = 0, 0, 0
    print(longestString(x3, y3, z3))  # Expected Output: 0

    # Test Case 4
    x4, y4, z4 = 1, 0, 1
    print(longestString(x4, y4, z4))  # Expected Output: 4

    # Test Case 5
    x5, y5, z5 = 10, 15, 5
    print(longestString(x5, y5, z5))  # Expected Output: 48

"""
Time Complexity Analysis:
- Calculating the minimum of x and y takes O(1).
- All other operations (arithmetic and comparisons) are O(1).
- Therefore, the overall time complexity is O(1).

Space Complexity Analysis:
- The solution uses a constant amount of extra space for variables.
- Therefore, the overall space complexity is O(1).

Topic: Greedy
"""