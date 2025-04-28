"""
LeetCode Problem #1464: Maximum Product of Two Elements in an Array

Problem Statement:
Given the array `nums`, you need to find the maximum product of two elements in the array. 
The product of two elements is defined as `(nums[i] - 1) * (nums[j] - 1)` where `i` and `j` are 
indices of the two elements (0 <= i, j < nums.length) and `i != j`.

Return the maximum product you can achieve.

Constraints:
- 2 <= nums.length <= 500
- 1 <= nums[i] <= 10^3
"""

# Python Solution
def maxProduct(nums):
    """
    Finds the maximum product of two elements in the array after subtracting 1 from each.

    :param nums: List[int] - The input array of integers.
    :return: int - The maximum product of two elements after subtracting 1 from each.
    """
    # Sort the array in descending order
    nums.sort(reverse=True)
    # The two largest numbers are now at the start of the array
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
    nums3 = [3, 7]
    print(maxProduct(nums3))  # Expected Output: 12

    # Test Case 4
    nums4 = [10, 2, 5, 2]
    print(maxProduct(nums4))  # Expected Output: 36

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- Accessing the first two elements after sorting is O(1).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation is in-place, so no additional space is used apart from a few variables.
- Overall space complexity: O(1).

Topic: Arrays
"""