"""
LeetCode Question #16: 3Sum Closest

Problem Statement:
Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1, 2, 1, -4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0, 0, 0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

Constraints:
- 3 <= nums.length <= 500
- -10^3 <= nums[i] <= 10^3
- -10^4 <= target <= 10^4
"""

def threeSumClosest(nums, target):
    """
    Finds the sum of three integers in nums that is closest to the target.

    :param nums: List[int] - The input array of integers.
    :param target: int - The target integer.
    :return: int - The sum of the three integers closest to the target.
    """
    nums.sort()  # Sort the array to use the two-pointer approach
    closest_sum = float('inf')  # Initialize closest_sum to infinity

    for i in range(len(nums) - 2):
        # Use two pointers to find the closest sum for the current element
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            # Update closest_sum if the current sum is closer to the target
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            # Move pointers based on the comparison with the target
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                # If the current sum equals the target, return it immediately
                return current_sum

    return closest_sum


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [-1, 2, 1, -4]
    target1 = 1
    print(threeSumClosest(nums1, target1))  # Output: 2

    # Test Case 2
    nums2 = [0, 0, 0]
    target2 = 1
    print(threeSumClosest(nums2, target2))  # Output: 0

    # Test Case 3
    nums3 = [1, 1, 1, 0]
    target3 = 100
    print(threeSumClosest(nums3, target3))  # Output: 3

    # Test Case 4
    nums4 = [-3, -2, -5, 3, -4]
    target4 = -1
    print(threeSumClosest(nums4, target4))  # Output: -2

# Topic: Arrays