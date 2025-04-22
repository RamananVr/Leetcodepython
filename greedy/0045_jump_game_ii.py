"""
LeetCode Question #45: Jump Game II

Problem Statement:
You are given an integer array `nums`. You are initially positioned at the first index, and each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 1000
"""

def jump(nums):
    """
    Function to calculate the minimum number of jumps to reach the last index.

    :param nums: List[int] - Array representing maximum jump lengths at each position.
    :return: int - Minimum number of jumps to reach the last index.
    """
    n = len(nums)
    if n == 1:
        return 0

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= n - 1:
                break

    return jumps

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 1, 1, 4]
    print(jump(nums1))  # Output: 2

    # Test Case 2
    nums2 = [2, 3, 0, 1, 4]
    print(jump(nums2))  # Output: 2

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    print(jump(nums3))  # Output: 3

    # Test Case 4
    nums4 = [1]
    print(jump(nums4))  # Output: 0

    # Test Case 5
    nums5 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]
    print(jump(nums5))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
The algorithm iterates through the array once, making it O(n), where n is the length of the array.

Space Complexity:
The algorithm uses a constant amount of extra space, making it O(1).

Topic: Greedy
"""