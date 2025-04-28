"""
LeetCode Problem #2563: Count the Number of Fair Pairs

Problem Statement:
You are given a 0-indexed integer array `nums` of size `n` and two integers `lower` and `upper`.

A pair `(i, j)` is called fair if:
- `0 <= i < j < n`, and
- `lower <= nums[i] + nums[j] <= upper`.

Return the number of fair pairs.

Example:
Input: nums = [1, 4, 2, 3], lower = 3, upper = 6
Output: 4
Explanation: There are 4 fair pairs:
- (0, 1): nums[0] + nums[1] = 1 + 4 = 5 (within range [3, 6])
- (0, 2): nums[0] + nums[2] = 1 + 2 = 3 (within range [3, 6])
- (1, 3): nums[1] + nums[3] = 4 + 3 = 7 (not within range [3, 6])
- (2, 3): nums[2] + nums[3] = 2 + 3 = 5 (within range [3, 6])

Constraints:
- `1 <= nums.length <= 10^5`
- `nums.length == n`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= lower <= upper <= 10^9`
"""

# Solution
from bisect import bisect_left, bisect_right

def countFairPairs(nums, lower, upper):
    """
    Counts the number of fair pairs in the array `nums` such that
    the sum of the pair lies within the range [lower, upper].

    Args:
    nums (List[int]): The input array of integers.
    lower (int): The lower bound of the sum range.
    upper (int): The upper bound of the sum range.

    Returns:
    int: The number of fair pairs.
    """
    nums.sort()
    count = 0

    for i in range(len(nums)):
        # Find the range of valid indices for nums[j] such that
        # lower <= nums[i] + nums[j] <= upper
        left = bisect_left(nums, lower - nums[i], i + 1)
        right = bisect_right(nums, upper - nums[i], i + 1)
        count += (right - left)

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [1, 4, 2, 3]
    lower = 3
    upper = 6
    print(countFairPairs(nums, lower, upper))  # Output: 4

    # Test Case 2
    nums = [0, 0, 0, 0]
    lower = 0
    upper = 0
    print(countFairPairs(nums, lower, upper))  # Output: 6

    # Test Case 3
    nums = [1, 1, 1, 1]
    lower = 2
    upper = 3
    print(countFairPairs(nums, lower, upper))  # Output: 6

    # Test Case 4
    nums = [-1, 0, 1, 2]
    lower = 0
    upper = 2
    print(countFairPairs(nums, lower, upper))  # Output: 4

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array takes O(n log n).
- For each element in the array, we perform two binary searches, each taking O(log n).
- Thus, the overall time complexity is O(n log n).

Space Complexity:
- The sorting operation is in-place, so the space complexity is O(1) (ignoring input storage).

Overall: Time Complexity = O(n log n), Space Complexity = O(1)
"""

# Topic: Arrays, Binary Search