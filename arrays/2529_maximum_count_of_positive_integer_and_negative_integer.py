"""
LeetCode Question #2529: Maximum Count of Positive Integer and Negative Integer

Problem Statement:
Given an integer array `nums` sorted in non-decreasing order, return the maximum count of either positive integers or negative integers in the array.

- An integer `x` is positive if `x > 0`.
- An integer `x` is negative if `x < 0`.
- The array is sorted in non-decreasing order, meaning that negative numbers will appear first, followed by zeros (if any), and then positive numbers.

Example:
Input: nums = [-2, -1, -1, 0, 0, 1, 2, 3]
Output: 3
Explanation: There are 3 negative numbers (-2, -1, -1) and 3 positive numbers (1, 2, 3). Since the maximum count is 3, return 3.

Constraints:
- 1 <= nums.length <= 100
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order.
"""

# Solution
def maximumCount(nums):
    """
    Function to find the maximum count of positive or negative integers in a sorted array.

    Args:
    nums (List[int]): A sorted list of integers.

    Returns:
    int: The maximum count of positive or negative integers.
    """
    # Count negative numbers
    negative_count = 0
    for num in nums:
        if num < 0:
            negative_count += 1
        else:
            break  # Stop counting once we reach zero or positive numbers

    # Count positive numbers
    positive_count = 0
    for num in nums[::-1]:  # Iterate from the end of the array
        if num > 0:
            positive_count += 1
        else:
            break  # Stop counting once we reach zero or negative numbers

    # Return the maximum count
    return max(negative_count, positive_count)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [-2, -1, -1, 0, 0, 1, 2, 3]
    print(maximumCount(nums1))  # Output: 3

    # Test Case 2
    nums2 = [-3, -2, -1, 0, 0, 0, 4, 5]
    print(maximumCount(nums2))  # Output: 3

    # Test Case 3
    nums3 = [0, 0, 0, 0]
    print(maximumCount(nums3))  # Output: 0

    # Test Case 4
    nums4 = [-5, -4, -3, -2, -1]
    print(maximumCount(nums4))  # Output: 5

    # Test Case 5
    nums5 = [1, 2, 3, 4, 5]
    print(maximumCount(nums5))  # Output: 5


# Time and Space Complexity Analysis
"""
Time Complexity:
- Counting negative numbers involves iterating through the array until the first non-negative number is encountered. This takes O(n) in the worst case.
- Counting positive numbers involves iterating through the array in reverse until the first non-positive number is encountered. This also takes O(n) in the worst case.
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The solution uses a constant amount of extra space (two integer variables for counting). Hence, the space complexity is O(1).
"""

# Topic: Arrays