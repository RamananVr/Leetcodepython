"""
LeetCode Question #2653: Sliding Subarray Beauty

Problem Statement:
Given an integer array nums containing n integers, find the beauty of each subarray of size k.

The beauty of a subarray is the x-th smallest integer in the subarray if it is negative, or 0 if there are fewer than x negative integers.

Return an integer array containing n - k + 1 integers, which denote the beauty of the subarrays in order from the first index in the array.

Examples:
Example 1:
Input: nums = [1,-1,-3,-2,3], k = 3, x = 2
Output: [-1,-2,-2]
Explanation: There are 3 subarrays with size k = 3. 
The first subarray is [1, -1, -3] and the 2nd smallest negative integer is -1. 
The second subarray is [-1, -3, -2] and the 2nd smallest negative integer is -2. 
The third subarray is [-3, -2, 3] and the 2nd smallest negative integer is -2.

Example 2:
Input: nums = [-1,-2,-3,-4,-5], k = 2, x = 2
Output: [-1,-2,-3,-4]
Explanation: There are 4 subarrays with size k = 2.
For [-1, -2], the 2nd smallest negative integer is -1.
For [-2, -3], the 2nd smallest negative integer is -2.
For [-3, -4], the 2nd smallest negative integer is -3.
For [-4, -5], the 2nd smallest negative integer is -4.

Example 3:
Input: nums = [-3,1,2,-3,0,-3], k = 2, x = 1
Output: [-3,0,-3,-3,-3]
Explanation: There are 5 subarrays with size k = 2.
For [-3, 1], the 1st smallest negative integer is -3.
For [1, 2], there are no negative integers, so the beauty is 0.
For [2, -3], the 1st smallest negative integer is -3.
For [-3, 0], the 1st smallest negative integer is -3.
For [0, -3], the 1st smallest negative integer is -3.

Constraints:
- n == nums.length
- 1 <= n <= 10^5
- 1 <= k <= n
- 1 <= x <= k
- -50 <= nums[i] <= 50
"""

from typing import List
from collections import defaultdict
import heapq

def getSubarrayBeauty(nums: List[int], k: int, x: int) -> List[int]:
    """
    Find the beauty of each subarray using frequency counting approach.
    
    Since values are bounded by [-50, 50], we can use array-based counting.
    """
    n = len(nums)
    result = []
    
    # Frequency array for values from -50 to 50
    # Index 0 represents -50, index 100 represents 50
    freq = [0] * 101
    
    def get_value_from_index(idx):
        return idx - 50
    
    def get_index_from_value(val):
        return val + 50
    
    def find_kth_negative(k_val):
        """Find the k-th smallest negative number."""
        count = 0
        for i in range(50):  # Only check negative indices (0 to 49)
            count += freq[i]
            if count >= k_val:
                return get_value_from_index(i)
        return 0  # If fewer than k negative numbers
    
    # Initialize first window
    for i in range(k):
        freq[get_index_from_value(nums[i])] += 1
    
    # Find beauty of first window
    result.append(find_kth_negative(x))
    
    # Slide the window
    for i in range(k, n):
        # Remove leftmost element
        freq[get_index_from_value(nums[i - k])] -= 1
        # Add rightmost element
        freq[get_index_from_value(nums[i])] += 1
        
        # Find beauty of current window
        result.append(find_kth_negative(x))
    
    return result

def getSubarrayBeautyHeap(nums: List[int], k: int, x: int) -> List[int]:
    """
    Alternative approach using heaps (less efficient for this problem).
    """
    n = len(nums)
    result = []
    
    for i in range(n - k + 1):
        # Get current subarray
        subarray = nums[i:i + k]
        
        # Filter negative numbers and sort
        negatives = sorted([num for num in subarray if num < 0])
        
        # Get x-th smallest negative or 0
        if len(negatives) >= x:
            result.append(negatives[x - 1])
        else:
            result.append(0)
    
    return result

def getSubarrayBeautyOptimized(nums: List[int], k: int, x: int) -> List[int]:
    """
    Optimized approach using sliding window with ordered data structure simulation.
    """
    from collections import deque
    
    n = len(nums)
    result = []
    
    # Keep track of negative numbers in current window
    window_negatives = deque()
    
    def find_beauty():
        """Find x-th smallest negative in current window."""
        negatives = sorted([num for num in window_negatives if num < 0])
        if len(negatives) >= x:
            return negatives[x - 1]
        return 0
    
    # Process first window
    for i in range(k):
        window_negatives.append(nums[i])
    
    result.append(find_beauty())
    
    # Slide the window
    for i in range(k, n):
        # Remove leftmost element
        window_negatives.popleft()
        # Add new element
        window_negatives.append(nums[i])
        
        result.append(find_beauty())
    
    return result

# Test Cases
if __name__ == "__main__":
    test_cases = [
        ([1, -1, -3, -2, 3], 3, 2, [-1, -2, -2]),
        ([-1, -2, -3, -4, -5], 2, 2, [-1, -2, -3, -4]),
        ([-3, 1, 2, -3, 0, -3], 2, 1, [-3, 0, -3, -3, -3]),
        ([1, 2, 3], 3, 1, [0]),
        ([-1, -2], 1, 1, [-1, -2])
    ]
    
    print("Testing frequency counting approach:")
    for nums, k, x, expected in test_cases:
        result = getSubarrayBeauty(nums, k, x)
        print(f"getSubarrayBeauty({nums}, {k}, {x}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting heap approach:")
    for nums, k, x, expected in test_cases:
        result = getSubarrayBeautyHeap(nums, k, x)
        print(f"getSubarrayBeautyHeap({nums}, {k}, {x}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")

"""
Time and Space Complexity Analysis:

Frequency Counting Approach:
Time Complexity: O(n * C) where C = 50 (constant range of negative values)
- O(n) for sliding window
- O(C) for finding k-th negative in each window
- Overall: O(n) since C is constant
Space Complexity: O(C) = O(1) - frequency array of fixed size

Heap Approach:
Time Complexity: O(n * k * log k) - for each window, sort negative numbers
Space Complexity: O(k) - store subarray elements

Optimized Approach:
Time Complexity: O(n * k) - for each window, sort negative numbers
Space Complexity: O(k) - deque to store window elements

Topic: Arrays, Sliding Window, Sorting, Frequency Counting
"""
