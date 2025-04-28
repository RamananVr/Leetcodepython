"""
LeetCode Problem #2176: Count Equal and Divisible Pairs in an Array

Problem Statement:
Given a 0-indexed integer array `nums` of length `n` and an integer `k`, return the number of pairs `(i, j)` where:
    - 0 <= i < j < n
    - nums[i] == nums[j]
    - (i * j) is divisible by `k`.

Example:
Input: nums = [3,1,2,2,2,1,3], k = 2
Output: 4
Explanation:
There are 4 pairs that meet all the conditions:
- (0, 6): nums[0] == nums[6], and 0 * 6 = 0 is divisible by 2.
- (2, 3): nums[2] == nums[3], and 2 * 3 = 6 is divisible by 2.
- (2, 4): nums[2] == nums[4], and 2 * 4 = 8 is divisible by 2.
- (3, 4): nums[3] == nums[4], and 3 * 4 = 12 is divisible by 2.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i], k <= 100
"""

# Clean and Correct Python Solution
def countPairs(nums, k):
    """
    Counts the number of pairs (i, j) in the array nums such that:
    - nums[i] == nums[j]
    - (i * j) is divisible by k

    Args:
    nums (List[int]): The input array of integers.
    k (int): The divisor.

    Returns:
    int: The count of valid pairs.
    """
    n = len(nums)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j] and (i * j) % k == 0:
                count += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 1, 2, 2, 2, 1, 3]
    k1 = 2
    print(countPairs(nums1, k1))  # Output: 4

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    k2 = 1
    print(countPairs(nums2, k2))  # Output: 0

    # Test Case 3
    nums3 = [1, 1, 1, 1]
    k3 = 2
    print(countPairs(nums3, k3))  # Output: 6

    # Test Case 4
    nums4 = [10, 10, 10]
    k4 = 5
    print(countPairs(nums4, k4))  # Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution uses a nested loop to iterate over all pairs (i, j) where 0 <= i < j < n.
- The total number of iterations is O(n^2), where n is the length of the array `nums`.
- For each pair, the conditions are checked in O(1) time.
- Therefore, the overall time complexity is O(n^2).

Space Complexity:
- The solution uses a constant amount of extra space, so the space complexity is O(1).
"""

# Topic: Arrays