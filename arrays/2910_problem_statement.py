"""
LeetCode Question #2910: Problem Statement

Given a 0-indexed integer array `nums` of length `n`, find the maximum value of the following expression:

    nums[i] + nums[j] + i - j

where `0 <= i, j < n` and `i != j`.

Return the maximum value of the expression.

Constraints:
- `2 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

"""

def maxExpressionValue(nums):
    """
    This function calculates the maximum value of the expression nums[i] + nums[j] + i - j
    for all valid pairs (i, j) in the array nums.
    """
    # Initialize variables to track the maximum values of nums[i] + i and nums[j] - j
    max_i = float('-inf')
    max_value = float('-inf')

    # Iterate through the array
    for j in range(len(nums)):
        # Update the maximum value of the expression using the current nums[j] - j
        max_value = max(max_value, max_i + nums[j] - j)
        # Update the maximum value of nums[i] + i
        max_i = max(max_i, nums[j] + j)

    return max_value

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, -1]
    print(maxExpressionValue(nums1))  # Expected Output: 5

    # Test Case 2
    nums2 = [2, 4, 6, 2, 5]
    print(maxExpressionValue(nums2))  # Expected Output: 11

    # Test Case 3
    nums3 = [-1, -2, -3, -4]
    print(maxExpressionValue(nums3))  # Expected Output: -2

    # Test Case 4
    nums4 = [10, -5, 3, 4, 7]
    print(maxExpressionValue(nums4))  # Expected Output: 16

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses a constant amount of extra space for variables (max_i and max_value).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""