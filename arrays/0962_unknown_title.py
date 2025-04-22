"""
LeetCode Problem #962: Maximum Width Ramp

Problem Statement:
A "ramp" in an array `nums` is a pair `(i, j)` for which `i < j` and `nums[i] <= nums[j]`. 
The width of such a ramp is `j - i`.

Given an integer array `nums`, return the maximum width of a ramp in `nums`. If no ramp exists, return `0`.

Example 1:
Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The ramp (i=1, j=5) has width 5 - 1 = 4, and nums[1] <= nums[5].

Example 2:
Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The ramp (i=2, j=9) has width 9 - 2 = 7, and nums[2] <= nums[9].

Constraints:
- 2 <= nums.length <= 5 * 10^4
- 0 <= nums[i] <= 10^5
"""

# Solution
def maxWidthRamp(nums):
    """
    Finds the maximum width of a ramp in the array `nums`.

    :param nums: List[int] - The input array of integers.
    :return: int - The maximum width of a ramp.
    """
    # Step 1: Create a list of indices sorted by the values in nums
    sorted_indices = sorted(range(len(nums)), key=lambda i: nums[i])
    
    # Step 2: Initialize variables
    max_width = 0
    min_index = float('inf')
    
    # Step 3: Iterate through sorted indices to calculate the maximum width
    for index in sorted_indices:
        max_width = max(max_width, index - min_index)
        min_index = min(min_index, index)
    
    return max_width

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [6, 0, 8, 2, 1, 5]
    print(maxWidthRamp(nums1))  # Output: 4

    # Test Case 2
    nums2 = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]
    print(maxWidthRamp(nums2))  # Output: 7

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    print(maxWidthRamp(nums3))  # Output: 4

    # Test Case 4
    nums4 = [5, 4, 3, 2, 1]
    print(maxWidthRamp(nums4))  # Output: 0

    # Test Case 5
    nums5 = [1, 1, 1, 1, 1]
    print(maxWidthRamp(nums5))  # Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the indices based on the values in `nums` takes O(n log n), where `n` is the length of the array.
- Iterating through the sorted indices to calculate the maximum width takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The `sorted_indices` list takes O(n) space.
- Other variables use O(1) space.
- Overall space complexity: O(n).

Topic: Arrays
"""