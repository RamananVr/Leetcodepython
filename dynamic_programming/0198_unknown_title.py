"""
LeetCode Problem #198: House Robber

Problem Statement:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected, 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you 
can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9), and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400
"""

# Clean, Correct Python Solution
def rob(nums):
    """
    Function to calculate the maximum amount of money that can be robbed without alerting the police.

    :param nums: List[int] - List of integers representing the money in each house.
    :return: int - Maximum amount of money that can be robbed.
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    # Initialize variables to store the maximum money robbed up to the previous two houses
    prev1, prev2 = 0, 0

    for num in nums:
        # Calculate the maximum money robbed up to the current house
        current = max(prev1, prev2 + num)
        # Update the previous two houses
        prev2 = prev1
        prev1 = current

    return prev1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 1]
    print(rob(nums1))  # Output: 4

    # Test Case 2
    nums2 = [2, 7, 9, 3, 1]
    print(rob(nums2))  # Output: 12

    # Test Case 3
    nums3 = [2, 1, 1, 2]
    print(rob(nums3))  # Output: 4

    # Test Case 4
    nums4 = [5]
    print(rob(nums4))  # Output: 5

    # Test Case 5
    nums5 = []
    print(rob(nums5))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
The solution iterates through the list of houses once, performing constant-time operations for each house.
Thus, the time complexity is O(n), where n is the number of houses.

Space Complexity:
The solution uses only a constant amount of extra space to store the variables `prev1` and `prev2`.
Thus, the space complexity is O(1).
"""

# Topic: Dynamic Programming