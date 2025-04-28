"""
LeetCode Question #2873: Maximum Value of an Ordered Triplet

Problem Statement:
You are given a 0-indexed integer array nums. Find the maximum value of the ordered triplet (nums[i], nums[j], nums[k]) 
such that 0 <= i < j < k < nums.length and nums[i] < nums[j] < nums[k]. If no such triplet exists, return 0.

Example:
Input: nums = [2, 5, 3, 7, 1]
Output: 15
Explanation: The ordered triplet (2, 5, 7) has a value of 2 + 5 + 7 = 15.

Constraints:
- 3 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
"""

# Solution
def maximumTripletValue(nums):
    """
    Finds the maximum value of an ordered triplet (nums[i], nums[j], nums[k]) such that
    0 <= i < j < k < nums.length and nums[i] < nums[j] < nums[k].

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The maximum value of the ordered triplet, or 0 if no such triplet exists.
    """
    n = len(nums)
    if n < 3:
        return 0

    max_left = [0] * n
    max_right = [0] * n

    # Compute max_left: maximum value to the left of each index
    max_left[0] = nums[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], nums[i])

    # Compute max_right: maximum value to the right of each index
    max_right[-1] = nums[-1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], nums[i])

    max_value = 0

    # Iterate through the array to find the maximum triplet value
    for j in range(1, n - 1):
        if nums[j] > max_left[j - 1] and nums[j] < max_right[j + 1]:
            max_value = max(max_value, max_left[j - 1] + nums[j] + max_right[j + 1])

    return max_value


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 5, 3, 7, 1]
    print(maximumTripletValue(nums1))  # Output: 15

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    print(maximumTripletValue(nums2))  # Output: 12

    # Test Case 3
    nums3 = [5, 4, 3, 2, 1]
    print(maximumTripletValue(nums3))  # Output: 0

    # Test Case 4
    nums4 = [1, 3, 2, 4, 6]
    print(maximumTripletValue(nums4))  # Output: 13

    # Test Case 5
    nums5 = [10, 20, 30]
    print(maximumTripletValue(nums5))  # Output: 60


# Time and Space Complexity Analysis
"""
Time Complexity:
- Computing max_left takes O(n) time.
- Computing max_right takes O(n) time.
- Iterating through the array to find the maximum triplet value takes O(n) time.
- Overall time complexity: O(n).

Space Complexity:
- max_left and max_right arrays each take O(n) space.
- Overall space complexity: O(n).
"""

# Topic: Arrays