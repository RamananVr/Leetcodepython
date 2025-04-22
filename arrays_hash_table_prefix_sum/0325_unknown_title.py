"""
LeetCode Problem #325: Maximum Size Subarray Sum Equals k

Problem Statement:
Given an integer array `nums` and an integer `k`, return the maximum length of a subarray that sums to `k`. 
If there isn't one, return 0 instead.

Example 1:
Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.

Example 2:
Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.

Constraints:
- 1 <= nums.length <= 2 * 10^5
- -10^4 <= nums[i] <= 10^4
- -10^9 <= k <= 10^9
"""

def maxSubArrayLen(nums, k):
    """
    Finds the maximum length of a subarray that sums to k.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The target sum.

    Returns:
    int: The maximum length of a subarray that sums to k, or 0 if no such subarray exists.
    """
    prefix_sum = 0
    prefix_map = {0: -1}  # Maps prefix_sum to its earliest index
    max_length = 0

    for i, num in enumerate(nums):
        prefix_sum += num

        # Check if there's a subarray that sums to k
        if prefix_sum - k in prefix_map:
            max_length = max(max_length, i - prefix_map[prefix_sum - k])

        # Store the first occurrence of this prefix_sum
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, -1, 5, -2, 3]
    k1 = 3
    print(maxSubArrayLen(nums1, k1))  # Output: 4

    # Test Case 2
    nums2 = [-2, -1, 2, 1]
    k2 = 1
    print(maxSubArrayLen(nums2, k2))  # Output: 2

    # Test Case 3
    nums3 = [1, 2, 3]
    k3 = 3
    print(maxSubArrayLen(nums3, k3))  # Output: 2

    # Test Case 4
    nums4 = [1, 2, 3]
    k4 = 7
    print(maxSubArrayLen(nums4, k4))  # Output: 0

    # Test Case 5
    nums5 = [1, -1, 1, -1, 1, -1]
    k5 = 0
    print(maxSubArrayLen(nums5, k5))  # Output: 6

"""
Time Complexity:
- O(n): We iterate through the array once, and each operation (checking the dictionary and updating it) is O(1).

Space Complexity:
- O(n): In the worst case, we store all prefix sums in the dictionary.

Topic: Arrays, Hash Table, Prefix Sum
"""