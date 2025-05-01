"""
LeetCode Problem #1635: "Hopper's Game"

Problem Statement:
Hopper is playing a game where he starts at the first index of an array `nums` and wants to reach the last index. 
Each element in the array represents the maximum jump length Hopper can make from that position. 
Determine if Hopper can reach the last index.

You are given an integer array `nums`. Return `True` if Hopper can reach the last index, or `False` otherwise.

Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5

Example 1:
Input: nums = [2,3,1,1,4]
Output: True
Explanation: Hopper can jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: False
Explanation: Hopper will always reach index 3, but its maximum jump length is 0, so it cannot move further.

Follow-up:
Can you come up with an O(n) solution?
"""

def canJump(nums):
    """
    Determines if Hopper can reach the last index of the array.

    :param nums: List[int] - Array of non-negative integers representing jump lengths
    :return: bool - True if Hopper can reach the last index, False otherwise
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
    print(canJump(nums3))  # Output: True

    # Test Case 4
    nums4 = [2, 0, 0]
    print(canJump(nums4))  # Output: True

    # Test Case 5
    nums5 = [1, 1, 0, 1]
    print(canJump(nums5))  # Output: False

"""
Time Complexity Analysis:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity Analysis:
- The algorithm uses a single integer variable `max_reachable` to track the farthest index that can be reached.
- Therefore, the space complexity is O(1).

Topic: Greedy Algorithm
"""