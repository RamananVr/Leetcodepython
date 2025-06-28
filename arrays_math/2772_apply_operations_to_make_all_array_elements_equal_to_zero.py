"""
LeetCode Problem 2772: Apply Operations to Make All Array Elements Equal to Zero

You are given a 0-indexed integer array nums and a positive integer k.

You can apply the following operation on the array any number of times:
- Choose any index i where 0 <= i < n, and decrease nums[i] by k.

Return true if you can make all the elements of the array equal to 0, or false otherwise.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
- 1 <= k <= 100

Example 1:
Input: nums = [2,4,6], k = 2
Output: true
Explanation: We can apply the operation 3 times:
- Apply the operation on index 0, and nums becomes [0,4,6].
- Apply the operation on index 1 twice, and nums becomes [0,0,6].
- Apply the operation on index 2 three times, and nums becomes [0,0,0].

Example 2:
Input: nums = [1,3,5], k = 3
Output: false
Explanation: It is not possible to make all the elements equal to 0.

Topics: Array, Math
"""

class Solution:
    def canMakeEqual(self, nums: list[int], k: int) -> bool:
        """
        Approach 1: Mathematical Analysis
        
        For each element nums[i], we can only decrease it by multiples of k.
        To make nums[i] equal to 0, we need nums[i] to be divisible by k.
        
        Mathematical insight:
        - We can decrease nums[i] by k any number of times
        - To reach 0, we need nums[i] = m * k for some non-negative integer m
        - This means nums[i] % k must equal 0
        
        Time: O(n) - check each element once
        Space: O(1) - only using constant extra space
        """
        for num in nums:
            if num % k != 0:
                return False
        return True
    
    def canMakeEqual_simulation(self, nums: list[int], k: int) -> bool:
        """
        Approach 2: Simulation approach
        
        Actually simulate the process of decreasing each element to 0.
        
        Time: O(n * max(nums) / k) - for each element, divide by k until 0
        Space: O(1)
        """
        for num in nums:
            temp = num
            while temp > 0:
                if temp < k:
                    return False  # Cannot decrease further
                temp -= k
        return True
    
    def canMakeEqual_gcd_approach(self, nums: list[int], k: int) -> bool:
        """
        Approach 3: GCD-based approach (alternative mathematical view)
        
        For each number to reach 0 by subtracting k repeatedly,
        the number must be a multiple of k.
        
        Time: O(n)
        Space: O(1)
        """
        import math
        
        for num in nums:
            gcd = math.gcd(num, k)
            if num // gcd * gcd != num or gcd != k:
                return False
        return True
    
    def canMakeEqual_iterative_reduction(self, nums: list[int], k: int) -> bool:
        """
        Approach 4: Iterative reduction
        
        Keep reducing each element until it's either 0 or becomes less than k.
        
        Time: O(n * max(nums) / k)
        Space: O(n) - copy of array
        """
        nums_copy = nums[:]
        
        while any(x > 0 for x in nums_copy):
            progress_made = False
            
            for i in range(len(nums_copy)):
                if nums_copy[i] >= k:
                    nums_copy[i] -= k
                    progress_made = True
            
            if not progress_made:
                # Some elements are positive but less than k
                return False
        
        return True

def test_can_make_equal():
    """Test the can make equal solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Basic case - all divisible by k
    assert solution.canMakeEqual([2, 4, 6], 2) == True
    
    # Test case 2: Not all divisible by k
    assert solution.canMakeEqual([1, 3, 5], 3) == False
    
    # Test case 3: Single element divisible
    assert solution.canMakeEqual([10], 5) == True
    
    # Test case 4: Single element not divisible
    assert solution.canMakeEqual([7], 3) == False
    
    # Test case 5: All zeros already
    assert solution.canMakeEqual([0, 0, 0], 5) == True
    
    # Test case 6: k equals 1 (always possible)
    assert solution.canMakeEqual([1, 2, 3, 4, 5], 1) == True
    
    # Test case 7: Large k, small numbers
    assert solution.canMakeEqual([3, 6, 9], 10) == False
    
    # Test case 8: k equals max element
    assert solution.canMakeEqual([5, 10, 15], 5) == True
    
    # Test case 9: Mixed case
    assert solution.canMakeEqual([4, 8, 12, 7], 4) == False
    
    # Test case 10: All same values
    assert solution.canMakeEqual([6, 6, 6], 2) == True
    
    # Compare different approaches
    test_cases = [
        ([2, 4, 6], 2),
        ([1, 3, 5], 3),
        ([10], 5),
        ([7], 3),
        ([0, 0, 0], 5),
        ([1, 2, 3, 4, 5], 1),
        ([3, 6, 9], 10),
        ([5, 10, 15], 5),
        ([4, 8, 12, 7], 4),
        ([6, 6, 6], 2)
    ]
    
    for nums, k in test_cases:
        result1 = solution.canMakeEqual(nums, k)
        result2 = solution.canMakeEqual_simulation(nums, k)
        result3 = solution.canMakeEqual_iterative_reduction(nums, k)
        assert result1 == result2 == result3, f"Mismatch for nums={nums}, k={k}: {result1}, {result2}, {result3}"
    
    # Test edge cases
    assert solution.canMakeEqual([100], 1) == True
    assert solution.canMakeEqual([99], 100) == False
    assert solution.canMakeEqual([0], 50) == True
    
    print("All can make equal tests passed!")

if __name__ == "__main__":
    test_can_make_equal()
