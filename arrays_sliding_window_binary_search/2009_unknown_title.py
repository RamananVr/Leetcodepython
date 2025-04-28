"""
LeetCode Problem #2009: Minimum Number of Operations to Make Array Continuous

Problem Statement:
You are given an integer array nums. In one operation, you can replace any element in nums with any integer.

nums is considered continuous if all elements in nums are unique and the difference between the maximum and minimum 
element in nums is equal to nums.length - 1.

Return the minimum number of operations required to make nums continuous.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

# Solution
from bisect import bisect_left

def min_operations(nums):
    """
    Function to calculate the minimum number of operations to make the array continuous.
    
    Args:
    nums (List[int]): The input array of integers.
    
    Returns:
    int: The minimum number of operations required.
    """
    # Step 1: Remove duplicates and sort the array
    sorted_unique_nums = sorted(set(nums))
    n = len(nums)
    
    # Step 2: Use a sliding window to find the maximum number of elements that can be part of a continuous array
    max_continuous = 0
    for i, num in enumerate(sorted_unique_nums):
        # Find the largest number that can be part of the continuous range starting from num
        upper_bound = num + n - 1
        j = bisect_left(sorted_unique_nums, upper_bound + 1)
        max_continuous = max(max_continuous, j - i)
    
    # Step 3: Calculate the minimum operations required
    return n - max_continuous

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 2, 5, 3]
    print(min_operations(nums1))  # Expected Output: 0

    # Test Case 2
    nums2 = [1, 2, 3, 5, 6]
    print(min_operations(nums2))  # Expected Output: 1

    # Test Case 3
    nums3 = [1, 10, 100, 1000]
    print(min_operations(nums3))  # Expected Output: 3

    # Test Case 4
    nums4 = [8, 5, 6, 7, 9]
    print(min_operations(nums4))  # Expected Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array and removing duplicates takes O(n log n), where n is the length of nums.
- The sliding window approach iterates over the sorted unique array, which has at most n elements, and uses binary search (O(log n)) for each element. 
  Thus, this step takes O(n log n).
- Overall time complexity: O(n log n).

Space Complexity:
- The space complexity is O(n) due to the storage of the sorted unique array.
- Overall space complexity: O(n).

Topic: Arrays, Sliding Window, Binary Search
"""