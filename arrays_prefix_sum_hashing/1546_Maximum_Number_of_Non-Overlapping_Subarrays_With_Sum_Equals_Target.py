"""
LeetCode Problem #1546: Maximum Number of Non-Overlapping Subarrays With Sum Equals Target

Problem Statement:
Given an array `nums` and an integer `target`, return the maximum number of non-overlapping subarrays such that the sum of each subarray is equal to `target`.

A subarray is a contiguous part of the array.

Example 1:
Input: nums = [1,1,1,1,1], target = 2
Output: 2
Explanation: There are 2 non-overlapping subarrays [1,1] and [1,1] with sum equals to target.

Example 2:
Input: nums = [-1,3,5,1,4,2,-9], target = 6
Output: 2
Explanation: There are 2 non-overlapping subarrays [3,5] and [1,4,2] with sum equals to target.

Example 3:
Input: nums = [-2,6,6,3,5,4,1,2,8], target = 10
Output: 3

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 0 <= target <= 10^7
"""

# Python Solution
def maxNonOverlapping(nums, target):
    """
    Finds the maximum number of non-overlapping subarrays with sum equal to target.

    :param nums: List[int] - The input array of integers.
    :param target: int - The target sum for subarrays.
    :return: int - The maximum number of non-overlapping subarrays with sum equal to target.
    """
    prefix_sum = 0
    seen = set()
    seen.add(0)  # Initialize with 0 to handle cases where prefix_sum == target
    count = 0

    for num in nums:
        prefix_sum += num
        if prefix_sum - target in seen:
            count += 1
            seen.clear()  # Clear the set to ensure non-overlapping
            seen.add(0)  # Reset for the next subarray
            prefix_sum = 0  # Reset prefix_sum for the next subarray
        else:
            seen.add(prefix_sum)

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 1, 1, 1, 1]
    target1 = 2
    print(maxNonOverlapping(nums1, target1))  # Output: 2

    # Test Case 2
    nums2 = [-1, 3, 5, 1, 4, 2, -9]
    target2 = 6
    print(maxNonOverlapping(nums2, target2))  # Output: 2

    # Test Case 3
    nums3 = [-2, 6, 6, 3, 5, 4, 1, 2, 8]
    target3 = 10
    print(maxNonOverlapping(nums3, target3))  # Output: 3

    # Test Case 4
    nums4 = [0, 0, 0, 0, 0]
    target4 = 0
    print(maxNonOverlapping(nums4, target4))  # Output: 5

    # Test Case 5
    nums5 = [1, 2, 3, 4, 5]
    target5 = 9
    print(maxNonOverlapping(nums5, target5))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array once, performing O(1) operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The algorithm uses a set to store prefix sums. In the worst case, the set can contain up to n elements.
- Therefore, the space complexity is O(n).

Overall, the algorithm is efficient and works well for large input sizes.
"""

# Topic: Arrays, Prefix Sum, Hashing