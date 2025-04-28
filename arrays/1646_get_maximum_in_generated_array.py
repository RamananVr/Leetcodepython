"""
LeetCode Question #1646: Get Maximum in Generated Array

Problem Statement:
You are given an integer `n`. A 0-indexed integer array `nums` of length `n + 1` is generated as follows:
- `nums[0] = 0`
- `nums[1] = 1` (if `n >= 1`)
- `nums[2 * i] = nums[i]` (for `2 <= 2 * i <= n`)
- `nums[2 * i + 1] = nums[i] + nums[i + 1]` (for `2 <= 2 * i + 1 <= n`)

Return the maximum integer in the array `nums`.

Example:
Input: n = 7
Output: 3
Explanation: According to the rules:
nums = [0, 1, 1, 2, 1, 3, 2, 3], and the maximum is 3.

Constraints:
- `0 <= n <= 100`
"""

# Python Solution
def getMaximumGenerated(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    nums = [0] * (n + 1)
    nums[0], nums[1] = 0, 1
    
    for i in range(1, n // 2 + 1):
        if 2 * i <= n:
            nums[2 * i] = nums[i]
        if 2 * i + 1 <= n:
            nums[2 * i + 1] = nums[i] + nums[i + 1]
    
    return max(nums)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 7
    print(getMaximumGenerated(n))  # Output: 3

    # Test Case 2
    n = 2
    print(getMaximumGenerated(n))  # Output: 1

    # Test Case 3
    n = 3
    print(getMaximumGenerated(n))  # Output: 2

    # Test Case 4
    n = 0
    print(getMaximumGenerated(n))  # Output: 0

    # Test Case 5
    n = 1
    print(getMaximumGenerated(n))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The loop runs for `n // 2 + 1` iterations, and each iteration performs constant-time operations.
- Therefore, the time complexity is O(n).

Space Complexity:
- We use an array `nums` of size `n + 1` to store the generated values.
- Therefore, the space complexity is O(n).

Topic: Arrays
"""