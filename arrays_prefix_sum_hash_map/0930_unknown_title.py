"""
LeetCode Problem #930: Binary Subarrays With Sum

Problem Statement:
Given a binary array `nums` and an integer `goal`, return the number of non-empty subarrays with a sum equal to `goal`.

A subarray is a contiguous part of the array.

Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are [1,0,1], [0,1,0,1], [1,0,1,0], and [1,0,1].

Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15

Constraints:
- 1 <= nums.length <= 3 * 10^4
- nums[i] is either 0 or 1.
- 0 <= goal <= nums.length
"""

# Solution
def numSubarraysWithSum(nums, goal):
    """
    Function to calculate the number of subarrays with sum equal to the given goal.

    Args:
    nums (List[int]): Binary array (contains only 0s and 1s).
    goal (int): Target sum for subarrays.

    Returns:
    int: Number of subarrays with sum equal to goal.
    """
    from collections import defaultdict

    prefix_sum_count = defaultdict(int)
    prefix_sum_count[0] = 1  # Base case: one way to have a prefix sum of 0
    prefix_sum = 0
    result = 0

    for num in nums:
        prefix_sum += num
        # Check if there exists a prefix sum that would make the current subarray sum equal to the goal
        result += prefix_sum_count[prefix_sum - goal]
        # Update the count of the current prefix sum
        prefix_sum_count[prefix_sum] += 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 0, 1, 0, 1]
    goal1 = 2
    print(numSubarraysWithSum(nums1, goal1))  # Expected Output: 4

    # Test Case 2
    nums2 = [0, 0, 0, 0, 0]
    goal2 = 0
    print(numSubarraysWithSum(nums2, goal2))  # Expected Output: 15

    # Test Case 3
    nums3 = [1, 1, 1, 1, 1]
    goal3 = 3
    print(numSubarraysWithSum(nums3, goal3))  # Expected Output: 3

    # Test Case 4
    nums4 = [0, 1, 0, 1, 0, 1]
    goal4 = 1
    print(numSubarraysWithSum(nums4, goal4))  # Expected Output: 9

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array `nums`.

Space Complexity:
- The algorithm uses a dictionary to store prefix sums and their counts. In the worst case, the dictionary could store up to n unique prefix sums.
- Therefore, the space complexity is O(n).
"""

# Topic: Arrays, Prefix Sum, Hash Map