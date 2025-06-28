"""
LeetCode Problem 2763: Sum of Imbalance Numbers of All Subarrays

You are given a 0-indexed integer array nums. The imbalance number of a 0-indexed integer array arr of length n is defined as the number of indices i (0 <= i < n - 1) such that:
- arr[i+1] - arr[i] > 1, and
- arr is a sorted array in non-decreasing order.

Return the sum of imbalance numbers of all subarrays of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= nums.length

Example 1:
Input: nums = [2,3,1,4]
Output: 3
Explanation: There are 3 imbalance numbers:
- Subarray [2,3]: sorted = [2,3], imbalance = 0
- Subarray [3,1]: sorted = [1,3], imbalance = 1 (3-1 > 1)
- Subarray [1,4]: sorted = [1,4], imbalance = 1 (4-1 > 1)

Example 2:
Input: nums = [1,3,3,3,5]
Output: 8

Topics: Arrays, Sorting
"""

class Solution:
    def sumImbalanceNumbers(self, nums: list[int]) -> int:
        """
        Approach 1: Brute Force - Check all subarrays
        
        For each subarray:
        1. Sort the subarray
        2. Count imbalance numbers (differences > 1)
        3. Add to total sum
        
        Time: O(n^3 log n) - O(n^2) subarrays, O(n log n) sort each
        Space: O(n) - for sorting
        """
        n = len(nums)
        total_imbalance = 0
        
        # Check all possible subarrays
        for i in range(n):
            for j in range(i, n):
                # Get subarray and sort it
                subarray = nums[i:j+1]
                subarray.sort()
                
                # Count imbalance numbers
                imbalance = 0
                for k in range(len(subarray) - 1):
                    if subarray[k+1] - subarray[k] > 1:
                        imbalance += 1
                
                total_imbalance += imbalance
        
        return total_imbalance
    
    def sumImbalanceNumbers_optimized(self, nums: list[int]) -> int:
        """
        Approach 2: Optimized with incremental sorting
        
        For each starting position, maintain sorted list as we extend.
        Use binary search for insertion.
        
        Time: O(n^3) - O(n^2) subarrays, O(n) for each insertion/imbalance calc
        Space: O(n)
        """
        n = len(nums)
        total_imbalance = 0
        
        for i in range(n):
            sorted_subarray = []
            
            for j in range(i, n):
                # Insert nums[j] into sorted position
                self._insert_sorted(sorted_subarray, nums[j])
                
                # Count imbalance numbers
                imbalance = 0
                for k in range(len(sorted_subarray) - 1):
                    if sorted_subarray[k+1] - sorted_subarray[k] > 1:
                        imbalance += 1
                
                total_imbalance += imbalance
        
        return total_imbalance
    
    def _insert_sorted(self, arr: list[int], val: int) -> None:
        """Insert val into sorted array arr maintaining order."""
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < val:
                left = mid + 1
            else:
                right = mid
        arr.insert(left, val)
    
    def sumImbalanceNumbers_mathematical(self, nums: list[int]) -> int:
        """
        Approach 3: Mathematical approach using contribution counting
        
        For each pair of positions, count how many subarrays they contribute
        an imbalance to.
        
        Time: O(n^3) - still need to check all subarrays for this problem
        Space: O(1)
        """
        n = len(nums)
        total_imbalance = 0
        
        # For each subarray, we need to sort and count imbalances
        # This approach doesn't offer significant optimization for this problem
        # due to the nature of imbalance calculation
        
        for i in range(n):
            for j in range(i, n):
                subarray = sorted(nums[i:j+1])
                
                # Count imbalance numbers efficiently
                imbalance = 0
                for k in range(len(subarray) - 1):
                    if subarray[k+1] - subarray[k] > 1:
                        imbalance += 1
                
                total_imbalance += imbalance
        
        return total_imbalance

def test_sum_imbalance_numbers():
    """Test the sum of imbalance numbers solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Basic case
    assert solution.sumImbalanceNumbers([2, 3, 1, 4]) == 3
    
    # Test case 2: Another case
    assert solution.sumImbalanceNumbers([1, 3, 3, 3, 5]) == 8
    
    # Test case 3: Single element
    assert solution.sumImbalanceNumbers([1]) == 0
    
    # Test case 4: Two elements - consecutive
    assert solution.sumImbalanceNumbers([1, 2]) == 0
    
    # Test case 5: Two elements - gap
    assert solution.sumImbalanceNumbers([1, 3]) == 1
    
    # Test case 6: All same elements
    assert solution.sumImbalanceNumbers([2, 2, 2]) == 0
    
    # Test case 7: Sorted ascending
    assert solution.sumImbalanceNumbers([1, 2, 3, 4]) == 0
    
    # Test case 8: With gaps
    assert solution.sumImbalanceNumbers([1, 4, 7]) == 3  # [1,4], [4,7], [1,4,7]
    
    # Compare optimized version
    test_cases = [
        [2, 3, 1, 4],
        [1, 3, 3, 3, 5],
        [1],
        [1, 2],
        [1, 3],
        [2, 2, 2],
        [1, 2, 3, 4]
    ]
    
    for nums in test_cases:
        result1 = solution.sumImbalanceNumbers(nums)
        result2 = solution.sumImbalanceNumbers_optimized(nums)
        result3 = solution.sumImbalanceNumbers_mathematical(nums)
        assert result1 == result2 == result3, f"Mismatch for {nums}: {result1}, {result2}, {result3}"
    
    print("All sum of imbalance numbers tests passed!")

if __name__ == "__main__":
    test_sum_imbalance_numbers()
