"""
LeetCode Problem 2774: Array Upper Bound

Write a function that accepts a sorted array of integers and a target integer. The function should use binary search to find the index of the first element that is greater than the target. If no such element exists, return the length of the array.

This is equivalent to finding the "upper bound" of the target in the array.

Constraints:
- 0 <= arr.length <= 10^4
- -10^4 <= arr[i], target <= 10^4
- arr is sorted in non-decreasing order.

Example 1:
Input: arr = [3,4,5], target = 4
Output: 2
Explanation: The first element greater than 4 is 5 at index 2.

Example 2:
Input: arr = [1,3,5,6], target = 2
Output: 1
Explanation: The first element greater than 2 is 3 at index 1.

Example 3:
Input: arr = [1,3,5,6], target = 6
Output: 4
Explanation: No element is greater than 6, so return the array length.

Topics: Array, Binary Search
"""

class Solution:
    def upperBound(self, arr: list[int], target: int) -> int:
        """
        Approach 1: Classic Binary Search for Upper Bound
        
        Find the first element greater than target using binary search.
        This is the standard upper_bound implementation.
        
        Time: O(log n)
        Space: O(1)
        """
        left, right = 0, len(arr)
        
        while left < right:
            mid = (left + right) // 2
            
            if arr[mid] <= target:
                # Current element is <= target, search right
                left = mid + 1
            else:
                # Current element is > target, could be answer
                right = mid
        
        return left
    
    def upperBound_alternative(self, arr: list[int], target: int) -> int:
        """
        Approach 2: Alternative binary search implementation
        
        Slightly different implementation but same logic.
        
        Time: O(log n)
        Space: O(1)
        """
        left, right = 0, len(arr) - 1
        result = len(arr)
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] > target:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result
    
    def upperBound_linear(self, arr: list[int], target: int) -> int:
        """
        Approach 3: Linear search (for comparison)
        
        Simple linear scan to find first element > target.
        
        Time: O(n)
        Space: O(1)
        """
        for i in range(len(arr)):
            if arr[i] > target:
                return i
        return len(arr)
    
    def upperBound_builtin(self, arr: list[int], target: int) -> int:
        """
        Approach 4: Using Python's bisect module
        
        Use built-in binary search implementation.
        
        Time: O(log n)
        Space: O(1)
        """
        import bisect
        return bisect.bisect_right(arr, target)
    
    def upperBound_recursive(self, arr: list[int], target: int) -> int:
        """
        Approach 5: Recursive binary search
        
        Recursive implementation of binary search for upper bound.
        
        Time: O(log n)
        Space: O(log n) - recursion stack
        """
        def binary_search(left, right):
            if left >= right:
                return left
            
            mid = (left + right) // 2
            
            if arr[mid] <= target:
                return binary_search(mid + 1, right)
            else:
                return binary_search(left, mid)
        
        return binary_search(0, len(arr))

def test_upper_bound():
    """Test the upper bound solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Basic case
    assert solution.upperBound([3, 4, 5], 4) == 2
    
    # Test case 2: Target not in array, middle value
    assert solution.upperBound([1, 3, 5, 6], 2) == 1
    
    # Test case 3: Target larger than all elements
    assert solution.upperBound([1, 3, 5, 6], 6) == 4
    
    # Test case 4: Target smaller than all elements
    assert solution.upperBound([3, 4, 5], 2) == 0
    
    # Test case 5: Empty array
    assert solution.upperBound([], 5) == 0
    
    # Test case 6: Single element array
    assert solution.upperBound([5], 3) == 0
    assert solution.upperBound([5], 5) == 1
    assert solution.upperBound([5], 7) == 1
    
    # Test case 7: Duplicate elements
    assert solution.upperBound([1, 2, 2, 2, 3], 2) == 4
    
    # Test case 8: All same elements
    assert solution.upperBound([5, 5, 5, 5], 5) == 4
    assert solution.upperBound([5, 5, 5, 5], 4) == 0
    
    # Test case 9: Negative numbers
    assert solution.upperBound([-3, -1, 0, 2, 4], -1) == 2
    assert solution.upperBound([-5, -3, -1], -2) == 2
    
    # Test case 10: Large array
    large_arr = list(range(0, 1000, 2))  # [0, 2, 4, 6, ..., 998]
    assert solution.upperBound(large_arr, 100) == 51  # First element > 100 is 102
    
    # Compare all approaches
    test_cases = [
        ([3, 4, 5], 4),
        ([1, 3, 5, 6], 2),
        ([1, 3, 5, 6], 6),
        ([3, 4, 5], 2),
        ([], 5),
        ([5], 3),
        ([5], 5),
        ([5], 7),
        ([1, 2, 2, 2, 3], 2),
        ([5, 5, 5, 5], 5),
        ([5, 5, 5, 5], 4),
        ([-3, -1, 0, 2, 4], -1),
        ([-5, -3, -1], -2)
    ]
    
    for arr, target in test_cases:
        result1 = solution.upperBound(arr, target)
        result2 = solution.upperBound_alternative(arr, target)
        result3 = solution.upperBound_linear(arr, target)
        result4 = solution.upperBound_builtin(arr, target)
        result5 = solution.upperBound_recursive(arr, target)
        
        assert result1 == result2 == result3 == result4 == result5, \
            f"Mismatch for arr={arr}, target={target}: {result1}, {result2}, {result3}, {result4}, {result5}"
    
    print("All upper bound tests passed!")

if __name__ == "__main__":
    test_upper_bound()
