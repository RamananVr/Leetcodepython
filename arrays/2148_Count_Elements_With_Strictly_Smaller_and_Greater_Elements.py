"""
LeetCode Problem #2148: Count Elements With Strictly Smaller and Greater Elements

Problem Statement:
Given an integer array `nums`, return the number of elements that have both a strictly smaller and a strictly greater element appear in `nums`.

In other words, an element `nums[i]` is considered "valid" if there exists at least one element smaller than `nums[i]` and at least one element greater than `nums[i]`.

Example 1:
Input: nums = [11, 7, 2, 15]
Output: 2
Explanation: The valid elements are 7 and 11.

Example 2:
Input: nums = [-3, 3, 3, 90]
Output: 2
Explanation: The valid elements are 3 and 3.

Constraints:
- 1 <= nums.length <= 100
- -10^5 <= nums[i] <= 10^5
"""

# Python Solution
def countElements(nums):
    """
    Counts the number of elements in the array that have both a strictly smaller
    and a strictly greater element.

    :param nums: List[int] - The input array of integers.
    :return: int - The count of valid elements.
    """
    if len(nums) < 3:
        return 0  # If there are fewer than 3 elements, no element can satisfy the condition.

    min_val = min(nums)
    max_val = max(nums)

    # Count elements that are strictly greater than the minimum and strictly smaller than the maximum.
    count = sum(1 for num in nums if min_val < num < max_val)
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [11, 7, 2, 15]
    print(countElements(nums1))  # Output: 2

    # Test Case 2
    nums2 = [-3, 3, 3, 90]
    print(countElements(nums2))  # Output: 2

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    print(countElements(nums3))  # Output: 3

    # Test Case 4
    nums4 = [10, 10, 10]
    print(countElements(nums4))  # Output: 0

    # Test Case 5
    nums5 = [1]
    print(countElements(nums5))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- Finding the minimum and maximum values in the array takes O(n) time.
- Iterating through the array to count valid elements also takes O(n) time.
- Overall, the time complexity is O(n).

Space Complexity:
- The solution uses a constant amount of extra space, so the space complexity is O(1).
"""

# Topic: Arrays