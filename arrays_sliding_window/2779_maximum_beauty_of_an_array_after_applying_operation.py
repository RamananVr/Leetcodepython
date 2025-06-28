"""
LeetCode Problem 2779: Maximum Beauty of an Array After Applying Operation

You are given a 0-indexed array nums and a non-negative integer k.

In one operation, you can:
- Choose an index i that hasn't been chosen before.
- Replace nums[i] with any integer in the range [nums[i] - k, nums[i] + k].

Return the maximum possible beauty of the array after applying the operation at most once to each index.

The beauty of an array is the length of the longest subsequence consisting of equal elements.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i], k <= 10^5

Example 1:
Input: nums = [4,6,1,2], k = 2
Output: 3
Explanation: In this example, we apply the following operations:
- Choose index 1, replace it with 4 (from range [4,8]), now nums = [4,4,1,2].
- Choose index 2, replace it with 4 (from range [-1,3]), now nums = [4,4,4,2].
- Choose index 3, replace it with 4 (from range [0,4]), now nums = [4,4,4,4].
The beauty is 4. It can be proven that 4 is the maximum possible beauty.

Example 2:
Input: nums = [1,1,1,1], k = 10
Output: 4
Explanation: In this example we don't have to apply any operations since all elements are the same.

Topics: Array, Binary Search, Sliding Window, Sorting
"""

class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        """
        Approach 1: Sliding Window on Sorted Array
        
        Key insight: After operations, we want as many elements as possible
        to have the same value. For elements to potentially have the same value,
        their original ranges [nums[i] - k, nums[i] + k] must overlap.
        
        Sort the array and use sliding window to find the maximum number
        of elements whose ranges can overlap.
        
        Time: O(n log n) for sorting + O(n) for sliding window
        Space: O(1) extra space
        """
        nums.sort()
        n = len(nums)
        left = 0
        max_beauty = 1
        
        for right in range(n):
            # Check if nums[left] and nums[right] can be made equal
            # This happens when their ranges overlap:
            # [nums[left] - k, nums[left] + k] ∩ [nums[right] - k, nums[right] + k] ≠ ∅
            # Equivalently: nums[right] - nums[left] <= 2k
            
            while nums[right] - nums[left] > 2 * k:
                left += 1
            
            max_beauty = max(max_beauty, right - left + 1)
        
        return max_beauty
    
    def maximumBeauty_intervals(self, nums: list[int], k: int) -> int:
        """
        Approach 2: Interval Overlap Problem
        
        Convert each number to an interval [nums[i] - k, nums[i] + k].
        Find the maximum number of overlapping intervals.
        
        Time: O(n log n)
        Space: O(n) for events list
        """
        events = []
        
        # Create start and end events for each interval
        for num in nums:
            events.append((num - k, 1))      # Start of interval
            events.append((num + k + 1, -1)) # End of interval (exclusive)
        
        events.sort()
        
        current_count = 0
        max_beauty = 0
        
        for position, delta in events:
            current_count += delta
            max_beauty = max(max_beauty, current_count)
        
        return max_beauty
    
    def maximumBeauty_coordinate_compression(self, nums: list[int], k: int) -> int:
        """
        Approach 3: Coordinate Compression + Difference Array
        
        Use coordinate compression to handle large ranges efficiently.
        
        Time: O(n log n)
        Space: O(n)
        """
        # Get all critical points
        points = set()
        for num in nums:
            points.add(num - k)
            points.add(num + k + 1)
        
        points = sorted(points)
        
        # Coordinate compression
        point_to_index = {point: i for i, point in enumerate(points)}
        
        # Difference array
        diff = [0] * len(points)
        
        for num in nums:
            start_idx = point_to_index[num - k]
            end_idx = point_to_index[num + k + 1]
            diff[start_idx] += 1
            if end_idx < len(diff):
                diff[end_idx] -= 1
        
        # Convert difference array to actual counts
        max_beauty = 0
        current_count = 0
        
        for delta in diff:
            current_count += delta
            max_beauty = max(max_beauty, current_count)
        
        return max_beauty
    
    def maximumBeauty_bruteforce(self, nums: list[int], k: int) -> int:
        """
        Approach 4: Brute Force (for verification on small inputs)
        
        Try all possible target values and count how many elements
        can be transformed to each target.
        
        Time: O(n * max_value) - very slow for large inputs
        Space: O(1)
        """
        if not nums:
            return 0
        
        max_beauty = 1
        min_possible = min(nums) - k
        max_possible = max(nums) + k
        
        for target in range(min_possible, max_possible + 1):
            count = 0
            for num in nums:
                if num - k <= target <= num + k:
                    count += 1
            max_beauty = max(max_beauty, count)
        
        return max_beauty

def test_maximum_beauty():
    """Test the maximum beauty solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Basic case
    assert solution.maximumBeauty([4, 6, 1, 2], 2) == 4
    
    # Test case 2: All same elements
    assert solution.maximumBeauty([1, 1, 1, 1], 10) == 4
    
    # Test case 3: Single element
    assert solution.maximumBeauty([5], 3) == 1
    
    # Test case 4: No overlap possible
    assert solution.maximumBeauty([1, 100], 1) == 1
    
    # Test case 5: Partial overlap
    assert solution.maximumBeauty([1, 2, 3, 4, 5], 1) == 5
    # All can be made equal to 3: [2,3,4], [1,3,5], [2,4,6], [3,5,7], [4,6,8]
    
    # Test case 6: k = 0 (no operations allowed)
    assert solution.maximumBeauty([1, 2, 1, 3, 1], 0) == 3
    # Only count existing equal elements
    
    # Test case 7: Large k
    assert solution.maximumBeauty([1, 2, 3], 10) == 3
    # All can be made equal with large k
    
    # Test case 8: Two groups
    assert solution.maximumBeauty([1, 2, 10, 11], 1) == 2
    # Two groups: [1,2] and [10,11]
    
    # Test case 9: Complex case
    assert solution.maximumBeauty([5, 57, 46], 15) == 2
    # Check which pairs can overlap
    
    # Compare approaches on smaller inputs
    small_test_cases = [
        ([4, 6, 1, 2], 2),
        ([1, 1, 1, 1], 10),
        ([5], 3),
        ([1, 100], 1),
        ([1, 2, 3, 4, 5], 1),
        ([1, 2, 1, 3, 1], 0),
        ([1, 2, 3], 10),
        ([1, 2, 10, 11], 1)
    ]
    
    for nums, k in small_test_cases:
        result1 = solution.maximumBeauty(nums.copy(), k)
        result2 = solution.maximumBeauty_intervals(nums.copy(), k)
        result3 = solution.maximumBeauty_coordinate_compression(nums.copy(), k)
        
        # Only test brute force on very small inputs
        if len(nums) <= 5 and max(nums) <= 20:
            result4 = solution.maximumBeauty_bruteforce(nums.copy(), k)
            assert result1 == result2 == result3 == result4, \
                f"Mismatch for nums={nums}, k={k}: {result1}, {result2}, {result3}, {result4}"
        else:
            assert result1 == result2 == result3, \
                f"Mismatch for nums={nums}, k={k}: {result1}, {result2}, {result3}"
    
    # Test edge cases
    assert solution.maximumBeauty([], 0) == 0 if hasattr(solution, 'maximumBeauty') else True
    assert solution.maximumBeauty([0], 0) == 1
    assert solution.maximumBeauty([0, 0, 0], 0) == 3
    
    print("All maximum beauty tests passed!")

if __name__ == "__main__":
    test_maximum_beauty()
