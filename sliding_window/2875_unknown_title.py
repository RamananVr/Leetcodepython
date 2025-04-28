"""
LeetCode Problem #2875: Minimum Size Subarray Sum

Problem Statement:
Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a contiguous subarray [nums[l], nums[l+1], ..., nums[r]] of which the sum is greater than or equal to `target`. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4

Follow-up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""

def minSubArrayLen(target: int, nums: list[int]) -> int:
    """
    Finds the minimal length of a contiguous subarray of which the sum is greater than or equal to target.
    If no such subarray exists, returns 0.
    """
    n = len(nums)
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(n):
        current_sum += nums[right]

        # Shrink the window as much as possible while the condition is met
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(minSubArrayLen(target, nums))  # Output: 2

    # Test Case 2
    target = 4
    nums = [1, 4, 4]
    print(minSubArrayLen(target, nums))  # Output: 1

    # Test Case 3
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    print(minSubArrayLen(target, nums))  # Output: 0

    # Test Case 4
    target = 15
    nums = [1, 2, 3, 4, 5]
    print(minSubArrayLen(target, nums))  # Output: 5

    # Test Case 5
    target = 100
    nums = [1, 2, 3, 4, 5]
    print(minSubArrayLen(target, nums))  # Output: 0

"""
Time Complexity:
- The algorithm uses a sliding window approach, where each element is visited at most twice (once when expanding the window and once when contracting it).
- Therefore, the time complexity is O(n), where n is the length of the input array `nums`.

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Sliding Window
"""