"""
LeetCode Question #1486: XOR Operation in an Array

Problem Statement:
You are given an integer `n` and an integer `start`.

Define an array `nums` where `nums[i] = start + 2 * i` (0-indexed) and `n == nums.length`.

Return the bitwise XOR of all elements of `nums`.

Example 1:
Input: n = 5, start = 0
Output: 8
Explanation: nums = [0, 2, 4, 6, 8], and 0 ^ 2 ^ 4 ^ 6 ^ 8 = 8.

Example 2:
Input: n = 4, start = 3
Output: 8
Explanation: nums = [3, 5, 7, 9], and 3 ^ 5 ^ 7 ^ 9 = 8.

Constraints:
- 1 <= n <= 1000
- 0 <= start <= 1000
"""

# Clean, Correct Python Solution
def xorOperation(n: int, start: int) -> int:
    result = 0
    for i in range(n):
        result ^= start + 2 * i
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, start1 = 5, 0
    print(xorOperation(n1, start1))  # Output: 8

    # Test Case 2
    n2, start2 = 4, 3
    print(xorOperation(n2, start2))  # Output: 8

    # Test Case 3
    n3, start3 = 1, 7
    print(xorOperation(n3, start3))  # Output: 7

    # Test Case 4
    n4, start4 = 10, 5
    print(xorOperation(n4, start4))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
The function iterates through the range of `n` once, performing a constant-time XOR operation for each element.
Thus, the time complexity is O(n).

Space Complexity:
The function uses a constant amount of extra space (the `result` variable).
Thus, the space complexity is O(1).

Topic: Bit Manipulation
"""