"""
LeetCode Problem #1913: Maximum Product Difference Between Two Pairs

Problem Statement:
The **product difference** between two pairs (a, b) and (c, d) is defined as 
(a * b) - (c * d).

- Given an integer array `nums`, choose four distinct indices `i`, `j`, `k`, and `l` 
  such that the product difference between pairs `(nums[i], nums[j])` and `(nums[k], nums[l])` 
  is maximized.

Return the maximum product difference you can achieve.

Constraints:
- 4 <= nums.length <= 10^4
- 1 <= nums[i] <= 10^4
"""

# Solution
def maxProductDifference(nums):
    """
    Finds the maximum product difference between two pairs in the array.

    :param nums: List[int] - The input array of integers.
    :return: int - The maximum product difference.
    """
    # Sort the array to easily access the largest and smallest elements
    nums.sort()
    
    # The largest two numbers are at the end of the sorted array
    max1, max2 = nums[-1], nums[-2]
    
    # The smallest two numbers are at the beginning of the sorted array
    min1, min2 = nums[0], nums[1]
    
    # Calculate the product difference
    return (max1 * max2) - (min1 * min2)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [5, 6, 2, 7, 4]
    print(maxProductDifference(nums1))  # Expected Output: 34

    # Test Case 2
    nums2 = [4, 2, 5, 9, 7, 8]
    print(maxProductDifference(nums2))  # Expected Output: 64

    # Test Case 3
    nums3 = [1, 2, 3, 4]
    print(maxProductDifference(nums3))  # Expected Output: 8

    # Test Case 4
    nums4 = [10, 20, 30, 40, 50, 60]
    print(maxProductDifference(nums4))  # Expected Output: 2900

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- Accessing the largest and smallest elements after sorting is O(1).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation is performed in-place, so no additional space is used.
- Overall space complexity: O(1).

Topic: Arrays
"""