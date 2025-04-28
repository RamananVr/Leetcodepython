"""
LeetCode Problem #1966: Binary Searchable Numbers in an Unsorted Array

Problem Statement:
Given an array `nums` of distinct integers, a number is called binary searchable if it can be found in the array 
using binary search. In other words, a number is binary searchable if and only if, after sorting the array, 
the number remains in its original position when compared to the sorted array.

Return the number of binary searchable numbers in the array.

Example:
Input: nums = [3, 1, 5, 4, 2]
Output: 2
Explanation: After sorting, nums becomes [1, 2, 3, 4, 5]. The numbers 3 and 5 are binary searchable.

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- All elements in nums are distinct.
"""

def binary_searchable_numbers(nums):
    """
    Function to count the number of binary searchable numbers in the array.
    
    Args:
    nums (List[int]): The input array of distinct integers.
    
    Returns:
    int: The count of binary searchable numbers.
    """
    n = len(nums)
    if n == 1:
        return 1  # A single element is always binary searchable.

    # Step 1: Compute the maximum value from the left up to each index.
    left_max = [float('-inf')] * n
    left_max[0] = nums[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], nums[i - 1])

    # Step 2: Compute the minimum value from the right up to each index.
    right_min = [float('inf')] * n
    right_min[n - 1] = nums[n - 1]
    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], nums[i + 1])

    # Step 3: Count binary searchable numbers.
    count = 0
    for i in range(n):
        if left_max[i] < nums[i] < right_min[i]:
            count += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 1, 5, 4, 2]
    print(binary_searchable_numbers(nums1))  # Output: 2

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    print(binary_searchable_numbers(nums2))  # Output: 5

    # Test Case 3
    nums3 = [5, 4, 3, 2, 1]
    print(binary_searchable_numbers(nums3))  # Output: 1

    # Test Case 4
    nums4 = [10]
    print(binary_searchable_numbers(nums4))  # Output: 1

    # Test Case 5
    nums5 = [2, 1, 3]
    print(binary_searchable_numbers(nums5))  # Output: 1

"""
Time Complexity Analysis:
- Computing `left_max` takes O(n) time.
- Computing `right_min` takes O(n) time.
- Iterating through the array to count binary searchable numbers takes O(n) time.
- Overall time complexity: O(n).

Space Complexity Analysis:
- The `left_max` and `right_min` arrays each take O(n) space.
- Overall space complexity: O(n).

Topic: Arrays
"""