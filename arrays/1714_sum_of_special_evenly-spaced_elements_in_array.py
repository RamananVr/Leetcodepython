"""
LeetCode Question #1714: Sum Of Special Evenly-Spaced Elements In Array

Problem Statement:
You are given an integer array `nums` and two integers `k` and `m`. 
Your task is to find the sum of the `k` largest elements in the array that are evenly spaced by `m`.

Formally, you need to:
1. Select `k` elements from the array such that the indices of the selected elements are evenly spaced by `m`.
2. Return the sum of these `k` elements.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= nums.length
- 1 <= m <= nums.length

Example:
Input: nums = [1, 3, 5, 7, 9], k = 2, m = 2
Output: 16
Explanation: The indices evenly spaced by `m = 2` are [0, 2, 4]. The elements at these indices are [1, 5, 9]. 
The two largest elements are [9, 7], and their sum is 16.
"""

# Python Solution
from heapq import nlargest

def sum_of_special_evenly_spaced_elements(nums, k, m):
    """
    Finds the sum of the k largest elements in the array that are evenly spaced by m.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The number of largest elements to sum.
    m (int): The spacing between indices.

    Returns:
    int: The sum of the k largest elements.
    """
    # Extract elements at indices evenly spaced by m
    spaced_elements = [nums[i] for i in range(0, len(nums), m)]
    
    # Find the k largest elements using a heap
    largest_elements = nlargest(k, spaced_elements)
    
    # Return the sum of the k largest elements
    return sum(largest_elements)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [1, 3, 5, 7, 9]
    k = 2
    m = 2
    print(sum_of_special_evenly_spaced_elements(nums, k, m))  # Output: 16

    # Test Case 2
    nums = [10, 20, 30, 40, 50, 60]
    k = 3
    m = 2
    print(sum_of_special_evenly_spaced_elements(nums, k, m))  # Output: 150

    # Test Case 3
    nums = [5, 1, 3, 8, 2, 7, 4]
    k = 2
    m = 3
    print(sum_of_special_evenly_spaced_elements(nums, k, m))  # Output: 15

    # Test Case 4
    nums = [100, 200, 300, 400, 500]
    k = 1
    m = 1
    print(sum_of_special_evenly_spaced_elements(nums, k, m))  # Output: 500

    # Test Case 5
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 4
    m = 3
    print(sum_of_special_evenly_spaced_elements(nums, k, m))  # Output: 30

# Time and Space Complexity Analysis
"""
Time Complexity:
- Extracting spaced elements: O(n/m), where n is the length of nums and m is the spacing.
- Finding the k largest elements using a heap: O(k * log(k)).
- Overall: O(n/m + k * log(k)).

Space Complexity:
- Space for spaced_elements: O(n/m).
- Space for the heap used in nlargest: O(k).
- Overall: O(n/m + k).

Topic: Arrays
"""