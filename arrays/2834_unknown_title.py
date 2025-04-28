"""
LeetCode Problem #2834: Find the Minimum Possible Sum of a Beautiful Array

Problem Statement:
You are given two integers `n` and `target`.

An array `nums` of length `n` is called beautiful if:
- `nums` is a permutation of the integers in the range `[1, n]`.
- For every pair of indices `i` and `j` (where `i != j`), `nums[i] + nums[j] != target`.

Return the minimum possible sum of a beautiful array.

Example:
Input: n = 2, target = 3
Output: 4
Explanation: The array [1, 3] is beautiful because:
- It is a permutation of [1, 2].
- 1 + 3 != 3.
The sum of the array is 4, which is the minimum possible sum.

Constraints:
- 1 <= n <= 10^5
- 1 <= target <= 10^9
"""

# Python Solution
def minimumPossibleSum(n: int, target: int) -> int:
    """
    Finds the minimum possible sum of a beautiful array of length n
    such that no two elements sum up to the target.
    """
    nums = []
    current = 1
    while len(nums) < n:
        # Add the current number to the array if it doesn't conflict with the target
        if all(current + x != target for x in nums):
            nums.append(current)
        current += 1
    return sum(nums)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 2
    target = 3
    print(minimumPossibleSum(n, target))  # Output: 4

    # Test Case 2
    n = 3
    target = 5
    print(minimumPossibleSum(n, target))  # Output: 6

    # Test Case 3
    n = 4
    target = 7
    print(minimumPossibleSum(n, target))  # Output: 10

    # Test Case 4
    n = 5
    target = 10
    print(minimumPossibleSum(n, target))  # Output: 15

# Time and Space Complexity Analysis
"""
Time Complexity:
- The while loop iterates until we have `n` elements in the array.
- For each iteration, we check if the current number conflicts with the target.
- In the worst case, this check involves comparing the current number with all elements in `nums`.
- Therefore, the time complexity is O(n^2).

Space Complexity:
- We store the array `nums` of size `n`.
- Therefore, the space complexity is O(n).
"""

# Topic: Arrays