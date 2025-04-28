"""
LeetCode Problem #2571: Minimum Operations to Reduce X to Zero

Problem Statement:
You are given an integer array `nums` and an integer `x`. In one operation, you can remove the leftmost or rightmost element from the array `nums` and subtract its value from `x`. Note that this operation reduces the size of the array.

Return the minimum number of operations required to reduce `x` to exactly 0. If it is not possible to reduce `x` to 0, return -1.

Example 1:
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements [2,3] (2 operations).

Example 2:
Input: nums = [5,6,7,8,9], x = 4
Output: -1
Explanation: It is not possible to reduce x to 0.

Example 3:
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the first three elements [3,2,20] and the last two elements [1,3] (5 operations).

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
- 1 <= x <= 10^9
"""

# Python Solution
def minOperations(nums, x):
    """
    Finds the minimum number of operations to reduce x to 0 by removing elements
    from the left or right of the array.

    :param nums: List[int] - The input array of integers.
    :param x: int - The target value to reduce to 0.
    :return: int - The minimum number of operations, or -1 if not possible.
    """
    target = sum(nums) - x
    if target < 0:
        return -1

    max_len = -1
    current_sum = 0
    left = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum > target and left <= right:
            current_sum -= nums[left]
            left += 1

        if current_sum == target:
            max_len = max(max_len, right - left + 1)

    return len(nums) - max_len if max_len != -1 else -1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 1, 4, 2, 3]
    x1 = 5
    print(minOperations(nums1, x1))  # Output: 2

    # Test Case 2
    nums2 = [5, 6, 7, 8, 9]
    x2 = 4
    print(minOperations(nums2, x2))  # Output: -1

    # Test Case 3
    nums3 = [3, 2, 20, 1, 1, 3]
    x3 = 10
    print(minOperations(nums3, x3))  # Output: 5

    # Test Case 4
    nums4 = [1, 1]
    x4 = 3
    print(minOperations(nums4, x4))  # Output: -1

    # Test Case 5
    nums5 = [1, 1, 1, 1, 1]
    x5 = 5
    print(minOperations(nums5, x5))  # Output: 5


# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm uses a sliding window approach, where each element is processed at most twice (once when expanding the window and once when contracting it).
- Therefore, the time complexity is O(n), where n is the length of the input array `nums`.

Space Complexity:
- The algorithm uses a constant amount of extra space for variables like `current_sum`, `left`, and `right`.
- Hence, the space complexity is O(1).
"""

# Topic: Sliding Window, Two Pointers