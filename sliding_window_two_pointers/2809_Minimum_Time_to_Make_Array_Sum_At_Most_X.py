"""
LeetCode Problem #2809: Minimum Time to Make Array Sum At Most X

Problem Statement:
You are given an integer array `nums` and an integer `x`. In one operation, you can remove the leftmost or the rightmost element from the array `nums` and subtract its value from `x`. Your goal is to find the minimum number of operations required to make `x` less than or equal to 0. If it is not possible, return -1.

Example:
Input: nums = [1, 1, 4, 2, 3], x = 5
Output: 2
Explanation: Remove the last two elements (3 and 2) to make x = 0.

Constraints:
1. 1 <= nums.length <= 10^5
2. 1 <= nums[i] <= 10^4
3. 1 <= x <= 10^9
"""

# Solution
def minOperations(nums, x):
    """
    Finds the minimum number of operations to make x <= 0 by removing elements
    from either the left or the right of the array.

    :param nums: List[int] - The input array of integers.
    :param x: int - The target value to reduce to 0 or less.
    :return: int - The minimum number of operations, or -1 if not possible.
    """
    total_sum = sum(nums)
    target = total_sum - x
    if target < 0:
        return -1  # Not possible to reduce x to 0 or less

    max_len = -1
    current_sum = 0
    left = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        # Shrink the window if the current sum exceeds the target
        while current_sum > target and left <= right:
            current_sum -= nums[left]
            left += 1

        # Check if the current window matches the target
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
- Calculating the total sum of the array takes O(n).
- The sliding window approach iterates through the array once, which is O(n).
- Overall time complexity: O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space for variables (current_sum, left, etc.).
- Overall space complexity: O(1).
"""

# Topic: Sliding Window, Two Pointers