"""
LeetCode Question #628: Maximum Product of Three Numbers

Problem Statement:
Given an integer array `nums`, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6

Example 2:
Input: nums = [1,2,3,4]
Output: 24

Example 3:
Input: nums = [-1,-2,-3]
Output: -6

Constraints:
- 3 <= nums.length <= 10^4
- -10^3 <= nums[i] <= 10^3
"""

def maximumProduct(nums):
    """
    Finds the maximum product of three numbers in the array.

    :param nums: List[int] - The input array of integers.
    :return: int - The maximum product of three numbers.
    """
    # Sort the array
    nums.sort()
    
    # The maximum product can be achieved in two ways:
    # 1. Product of the three largest numbers.
    # 2. Product of the two smallest numbers (negative numbers) and the largest number.
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    print(maximumProduct(nums1))  # Output: 6

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    print(maximumProduct(nums2))  # Output: 24

    # Test Case 3
    nums3 = [-1, -2, -3]
    print(maximumProduct(nums3))  # Output: -6

    # Test Case 4
    nums4 = [-10, -10, 5, 2]
    print(maximumProduct(nums4))  # Output: 500

    # Test Case 5
    nums5 = [0, 0, 0]
    print(maximumProduct(nums5))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- Accessing the required elements after sorting is O(1).
- Therefore, the overall time complexity is O(n log n).

Space Complexity:
- The sorting operation is performed in-place, so no additional space is used apart from the input array.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""