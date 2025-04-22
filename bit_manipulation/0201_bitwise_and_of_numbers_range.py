"""
LeetCode Question #201: Bitwise AND of Numbers Range

Problem Statement:
Given two integers `left` and `right` that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Example 1:
Input: left = 5, right = 7
Output: 4

Example 2:
Input: left = 0, right = 0
Output: 0

Example 3:
Input: left = 1, right = 2147483647
Output: 0

Constraints:
- 0 <= left <= right <= 2^31 - 1
"""

def rangeBitwiseAnd(left: int, right: int) -> int:
    """
    Compute the bitwise AND of all numbers in the range [left, right].
    """
    shift = 0
    # Find the common prefix of left and right by shifting both numbers right
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    
    # Shift the common prefix back to its original position
    return left << shift

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    left = 5
    right = 7
    print(rangeBitwiseAnd(left, right))  # Output: 4

    # Test Case 2
    left = 0
    right = 0
    print(rangeBitwiseAnd(left, right))  # Output: 0

    # Test Case 3
    left = 1
    right = 2147483647
    print(rangeBitwiseAnd(left, right))  # Output: 0

    # Additional Test Case
    left = 12
    right = 15
    print(rangeBitwiseAnd(left, right))  # Output: 12

"""
Time and Space Complexity Analysis:

Time Complexity:
- The while loop runs until `left` equals `right`. In the worst case, the loop runs for the number of bits in the integers, which is O(log(max(left, right))). 
- Therefore, the time complexity is O(log(max(left, right))).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Bit Manipulation
"""