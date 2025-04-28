"""
LeetCode Question #1459: Maximum Product of Two Elements in an Array

Problem Statement:
Given the array nums, obtain the maximum product of two elements in the array. 
You must choose two different indices i and j such that:
- nums[i] and nums[j] are the two elements chosen.
- The product is calculated as (nums[i] - 1) * (nums[j] - 1).

Return the maximum product you can get.

Constraints:
- 2 <= nums.length <= 500
- 1 <= nums[i] <= 10^3
"""

# Solution
def maxProduct(nums):
    """
    Finds the maximum product of two elements in the array as per the problem statement.

    Args:
    nums (List[int]): List of integers.

    Returns:
    int: Maximum product of two elements in the array.
    """
    # Sort the array in descending order
    nums.sort(reverse=True)
    
    # The two largest elements are nums[0] and nums[1]
    return (nums[0] - 1) * (nums[1] - 1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 4, 5, 2]
    print(maxProduct(nums1))  # Expected Output: 12

    # Test Case 2
    nums2 = [1, 5, 4, 5]
    print(maxProduct(nums2))  # Expected Output: 16

    # Test Case 3
    nums3 = [10, 2, 5, 2]
    print(maxProduct(nums3))  # Expected Output: 36

    # Test Case 4
    nums4 = [1, 1, 1, 1]
    print(maxProduct(nums4))  # Expected Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- Accessing the first two elements after sorting is O(1).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation is performed in-place, so no additional space is used.
- Overall space complexity: O(1).

Topic: Arrays
"""