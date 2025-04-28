"""
LeetCode Question #2344: Minimum Deletions to Make Array Divisible

Problem Statement:
You are given two arrays `nums` and `numsDivide` of positive integers. You can delete any number of elements from `nums`. 
Return the minimum number of deletions required so that the smallest element in `nums` divides all the elements of `numsDivide`. 
If this is not possible, return -1.

Note:
- The elements in `numsDivide` are guaranteed to be positive integers.
- It is not required for the smallest element in `nums` to be present in the original array after deletions.

Constraints:
- 1 <= nums.length, numsDivide.length <= 10^5
- 1 <= nums[i], numsDivide[i] <= 10^9
"""

# Solution
from math import gcd
from functools import reduce

def min_deletions(nums, numsDivide):
    """
    Finds the minimum number of deletions required to make the smallest element in nums divide all elements in numsDivide.

    :param nums: List[int] - The array from which elements can be deleted.
    :param numsDivide: List[int] - The array whose elements must be divisible by the smallest element in nums.
    :return: int - Minimum number of deletions required, or -1 if not possible.
    """
    # Step 1: Compute the GCD of all elements in numsDivide
    gcd_value = reduce(gcd, numsDivide)
    
    # Step 2: Sort nums to find the smallest valid divisor
    nums.sort()
    
    # Step 3: Iterate through nums to find the smallest element that divides gcd_value
    for i, num in enumerate(nums):
        if gcd_value % num == 0:
            return i  # The index corresponds to the number of deletions needed
    return -1  # If no valid divisor is found

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 7, 9, 12]
    numsDivide1 = [18, 36, 72]
    print(min_deletions(nums1, numsDivide1))  # Expected Output: 0

    # Test Case 2
    nums2 = [2, 3, 2, 4, 3]
    numsDivide2 = [6, 12, 18]
    print(min_deletions(nums2, numsDivide2))  # Expected Output: 1

    # Test Case 3
    nums3 = [4, 3, 6]
    numsDivide3 = [8, 2, 6]
    print(min_deletions(nums3, numsDivide3))  # Expected Output: -1

    # Test Case 4
    nums4 = [1, 2, 3]
    numsDivide4 = [4, 8, 16]
    print(min_deletions(nums4, numsDivide4))  # Expected Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- Computing the GCD of numsDivide takes O(n), where n is the length of numsDivide.
- Sorting nums takes O(m log m), where m is the length of nums.
- Iterating through nums to find the smallest valid divisor takes O(m).
Overall, the time complexity is O(n + m log m).

Space Complexity:
- The space complexity is O(1) since we are not using any additional data structures apart from a few variables.
"""

# Topic: Arrays, Math (GCD)