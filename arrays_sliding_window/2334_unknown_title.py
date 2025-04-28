"""
LeetCode Problem #2334: "Subarray With Elements Greater Than or Equal to Target"

Problem Statement:
You are given an integer array `nums` and an integer `target`. Find the length of the smallest contiguous subarray such that all elements in the subarray are greater than or equal to `target`. If no such subarray exists, return `-1`.

Example:
Input: nums = [1, 2, 3, 4, 5], target = 3
Output: 2
Explanation: The subarray [3, 4] is the smallest subarray where all elements are >= 3.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i], target <= 10^9
"""

# Solution
def smallest_subarray_with_target(nums, target):
    """
    Finds the length of the smallest contiguous subarray where all elements are greater than or equal to the target.

    :param nums: List[int] - The input array of integers.
    :param target: int - The target value.
    :return: int - The length of the smallest subarray, or -1 if no such subarray exists.
    """
    n = len(nums)
    min_length = float('inf')
    left = 0

    for right in range(n):
        if nums[right] >= target:
            while left <= right and all(nums[i] >= target for i in range(left, right + 1)):
                min_length = min(min_length, right - left + 1)
                left += 1

    return min_length if min_length != float('inf') else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5]
    target1 = 3
    print(smallest_subarray_with_target(nums1, target1))  # Expected Output: 2

    # Test Case 2
    nums2 = [1, 1, 1, 1, 1]
    target2 = 2
    print(smallest_subarray_with_target(nums2, target2))  # Expected Output: -1

    # Test Case 3
    nums3 = [5, 6, 7, 8, 9]
    target3 = 6
    print(smallest_subarray_with_target(nums3, target3))  # Expected Output: 1

    # Test Case 4
    nums4 = [3, 3, 3, 3, 3]
    target4 = 3
    print(smallest_subarray_with_target(nums4, target4))  # Expected Output: 1

    # Test Case 5
    nums5 = [10, 20, 30, 40, 50]
    target5 = 25
    print(smallest_subarray_with_target(nums5, target5))  # Expected Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution iterates through the array using a sliding window approach.
- For each element, it checks the subarray condition, which can take O(n) in the worst case.
- Overall complexity: O(n^2).

Space Complexity:
- The solution uses a constant amount of extra space.
- Overall complexity: O(1).
"""

# Topic: Arrays, Sliding Window