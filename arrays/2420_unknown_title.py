"""
LeetCode Problem #2420: Find All Good Indices

Problem Statement:
You are given a 0-indexed integer array nums of size n and a positive integer k.

We call an index i in the range k <= i < n - k a good index if the following conditions are satisfied:
1. The k elements that are just before the index i are in non-increasing order.
2. The k elements that are just after the index i are in non-decreasing order.

Return a list of all good indices sorted in increasing order.

Example 1:
Input: nums = [2,1,1,1,3,4,1], k = 2
Output: [2,3]
Explanation:
For index 2, the subarray [2,1] is non-increasing and [1,3] is non-decreasing.
For index 3, the subarray [1,1] is non-increasing and [3,4] is non-decreasing.
No other index satisfies the conditions.

Example 2:
Input: nums = [2,1,1,2], k = 2
Output: []
Explanation:
For index 2, the subarray [2,1] is not non-increasing.
Therefore, there are no good indices.

Constraints:
- n == nums.length
- 3 <= n <= 10^5
- 1 <= nums[i] <= 10^6
- 1 <= k <= n / 2
"""

def goodIndices(nums, k):
    """
    Finds all good indices in the array nums based on the given conditions.

    :param nums: List[int] - The input array of integers.
    :param k: int - The size of the subarrays to check.
    :return: List[int] - A list of all good indices.
    """
    n = len(nums)
    non_increasing = [0] * n
    non_decreasing = [0] * n

    # Calculate non-increasing prefix
    for i in range(1, n):
        if nums[i] <= nums[i - 1]:
            non_increasing[i] = non_increasing[i - 1] + 1

    # Calculate non-decreasing suffix
    for i in range(n - 2, -1, -1):
        if nums[i] <= nums[i + 1]:
            non_decreasing[i] = non_decreasing[i + 1] + 1

    # Find all good indices
    result = []
    for i in range(k, n - k):
        if non_increasing[i - 1] >= k - 1 and non_decreasing[i + 1] >= k - 1:
            result.append(i)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 1, 1, 1, 3, 4, 1]
    k1 = 2
    print(goodIndices(nums1, k1))  # Output: [2, 3]

    # Test Case 2
    nums2 = [2, 1, 1, 2]
    k2 = 2
    print(goodIndices(nums2, k2))  # Output: []

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5, 6]
    k3 = 1
    print(goodIndices(nums3, k3))  # Output: [1, 2, 3, 4]

    # Test Case 4
    nums4 = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
    k4 = 3
    print(goodIndices(nums4, k4))  # Output: [4]

"""
Time Complexity:
- Calculating the non-increasing prefix and non-decreasing suffix takes O(n) time.
- Iterating through the array to find good indices takes O(n) time.
- Overall time complexity: O(n).

Space Complexity:
- We use two auxiliary arrays, non_increasing and non_decreasing, each of size n.
- Overall space complexity: O(n).

Topic: Arrays
"""