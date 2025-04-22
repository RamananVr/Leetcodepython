"""
LeetCode Question #55: Jump Game

Problem Statement:
You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return `true` if you can reach the last index, or `false` otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5
"""

def canJump(nums):
    """
    Determines if you can reach the last index of the array.

    :param nums: List[int] - The input array where each element represents the maximum jump length.
    :return: bool - True if you can reach the last index, False otherwise.
    """
    max_reachable = 0
    for i, jump in enumerate(nums):
        if i > max_reachable:
            return False
        max_reachable = max(max_reachable, i + jump)
        if max_reachable >= len(nums) - 1:
            return True
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 1, 1, 4]
    print(canJump(nums1))  # Output: True

    # Test Case 2
    nums2 = [3, 2, 1, 0, 4]
    print(canJump(nums2))  # Output: False

    # Test Case 3
    nums3 = [0]
    print(canJump(nums3))  # Output: True (Already at the last index)

    # Test Case 4
    nums4 = [2, 0, 0]
    print(canJump(nums4))  # Output: True

    # Test Case 5
    nums5 = [1, 1, 1, 0, 0]
    print(canJump(nums5))  # Output: False

"""
Time Complexity:
- O(n): We iterate through the array once, where `n` is the length of the array.

Space Complexity:
- O(1): We use a constant amount of extra space.

Topic: Arrays, Greedy
"""