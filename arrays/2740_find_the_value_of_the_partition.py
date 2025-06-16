"""
2740. Find the Value of the Partition

You are given a positive integer array nums.

Partition nums into two arrays, nums1 and nums2, such that:
- Each element of nums belongs to either nums1 or nums2.
- Both nums1 and nums2 are non-empty.
- The value of the partition is minimized.

The value of the partition is |max(nums1) - min(nums2)|.

Return the minimum possible value of the partition.

Example 1:
Input: nums = [1,3,2,4]
Output: 1
Explanation: We can partition the array nums into nums1 = [1,2] and nums2 = [3,4].
- max(nums1) = 2
- min(nums2) = 3
- The value of the partition is |max(nums1) - min(nums2)| = |2 - 3| = 1.
It can be shown that 1 is the minimum value out of all partitions.

Example 2:
Input: nums = [100,1,10]
Output: 9
Explanation: We can partition the array nums into nums1 = [10] and nums2 = [100,1].
- max(nums1) = 10
- min(nums2) = 1
- The value of the partition is |max(nums1) - min(nums2)| = |10 - 1| = 9.
It can be shown that 9 is the minimum value out of all partitions.

Constraints:
- 2 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

def find_value_of_partition(nums: list[int]) -> int:
    """
    Find minimum partition value by sorting and checking adjacent differences.
    
    Args:
        nums: Array of positive integers
        
    Returns:
        int: Minimum possible partition value
        
    Time Complexity: O(n log n) - due to sorting
    Space Complexity: O(1) - sorting in place or O(n) if creating new array
    """
    # Sort the array
    nums.sort()
    
    # The minimum partition value will be the minimum difference
    # between adjacent elements in the sorted array
    min_value = float('inf')
    
    for i in range(len(nums) - 1):
        # Consider partition where nums1 contains nums[0:i+1] and nums2 contains nums[i+1:]
        # max(nums1) = nums[i], min(nums2) = nums[i+1]
        partition_value = abs(nums[i] - nums[i + 1])
        min_value = min(min_value, partition_value)
    
    return min_value

def find_value_of_partition_optimized(nums: list[int]) -> int:
    """
    Optimized approach recognizing that we only need adjacent differences in sorted array.
    
    Args:
        nums: Array of positive integers
        
    Returns:
        int: Minimum possible partition value
        
    Time Complexity: O(n log n) - sorting dominates
    Space Complexity: O(1) - minimal extra space
    """
    # Sort the array
    sorted_nums = sorted(nums)
    
    # Find minimum adjacent difference
    min_diff = float('inf')
    for i in range(len(sorted_nums) - 1):
        diff = sorted_nums[i + 1] - sorted_nums[i]
        min_diff = min(min_diff, diff)
    
    return min_diff

def find_value_of_partition_brute_force(nums: list[int]) -> int:
    """
    Brute force approach checking all possible partitions (for verification).
    
    Args:
        nums: Array of positive integers
        
    Returns:
        int: Minimum possible partition value
        
    Time Complexity: O(2^n * n) - exponential, checking all 2^n partitions
    Space Complexity: O(n) - for storing partition subsets
    """
    n = len(nums)
    min_value = float('inf')
    
    # Try all possible non-empty partitions (2^n - 2 total, excluding empty sets)
    for mask in range(1, (1 << n) - 1):
        nums1 = []
        nums2 = []
        
        for i in range(n):
            if mask & (1 << i):
                nums1.append(nums[i])
            else:
                nums2.append(nums[i])
        
        if nums1 and nums2:  # Both partitions must be non-empty
            max_nums1 = max(nums1)
            min_nums2 = min(nums2)
            partition_value = abs(max_nums1 - min_nums2)
            min_value = min(min_value, partition_value)
    
    return min_value

def find_value_of_partition_mathematical(nums: list[int]) -> int:
    """
    Mathematical insight: optimal partition has max(nums1) and min(nums2) as adjacent in sorted array.
    
    Args:
        nums: Array of positive integers
        
    Returns:
        int: Minimum possible partition value
        
    Time Complexity: O(n log n) - sorting step
    Space Complexity: O(1) - constant extra space
    """
    # Key insight: In the optimal partition, max(nums1) and min(nums2) 
    # should be consecutive elements in the sorted array
    
    nums.sort()
    
    # The answer is the minimum difference between consecutive elements
    return min(nums[i + 1] - nums[i] for i in range(len(nums) - 1))

# Test cases
def test_find_value_of_partition():
    test_cases = [
        # Basic test cases
        ([1, 3, 2, 4], 1),      # Example 1: [1,2] and [3,4] gives |2-3| = 1
        ([100, 1, 10], 9),      # Example 2: [10] and [100,1] gives |10-1| = 9
        
        # Edge cases
        ([1, 2], 1),            # Minimum size array
        ([5, 5], 0),            # Identical elements
        ([1, 1000], 999),       # Large difference
        
        # Sorted arrays
        ([1, 2, 3, 4, 5], 1),   # Already sorted, min diff = 1
        ([10, 20, 30], 10),     # Evenly spaced
        
        # Reverse sorted
        ([5, 4, 3, 2, 1], 1),   # Reverse sorted
        
        # Random order
        ([7, 2, 9, 1, 5], 1),   # Mixed order
        ([15, 3, 8, 12], 3),    # Another mixed case
        
        # Duplicates
        ([3, 1, 3, 1], 0),      # Multiple duplicates
        ([5, 2, 5, 2, 5], 0),   # More duplicates
        
        # Large gaps
        ([1, 100, 1000], 99),   # Large gaps between elements
        ([2, 4, 100, 200], 2),  # Mix of small and large gaps
        
        # Special patterns
        ([1, 3, 5, 7, 9], 2),   # Arithmetic progression
        ([1, 2, 4, 8, 16], 1),  # Powers progression
    ]
    
    print("Testing find_value_of_partition function:")
    for i, (nums, expected) in enumerate(test_cases):
        # Make copies since sorting modifies the array
        nums_copy1 = nums[:]
        nums_copy2 = nums[:]
        nums_copy3 = nums[:]
        nums_copy4 = nums[:]
        
        result1 = find_value_of_partition(nums_copy1)
        result2 = find_value_of_partition_optimized(nums_copy2)
        result3 = find_value_of_partition_mathematical(nums_copy4)
        
        # Only run brute force for small arrays to avoid timeout
        if len(nums) <= 10:
            result4 = find_value_of_partition_brute_force(nums_copy3)
        else:
            result4 = result1  # Skip brute force for large arrays
        
        print(f"Test {i+1}: nums={nums}")
        print(f"  Expected: {expected}")
        print(f"  Basic: {result1}")
        print(f"  Optimized: {result2}")
        print(f"  Mathematical: {result3}")
        if len(nums) <= 10:
            print(f"  Brute Force: {result4}")
        
        assert result1 == expected, f"Basic failed for test case {i+1}"
        assert result2 == expected, f"Optimized failed for test case {i+1}"
        assert result3 == expected, f"Mathematical failed for test case {i+1}"
        if len(nums) <= 10:
            assert result4 == expected, f"Brute Force failed for test case {i+1}"
        print(f"  ✓ All passed\n")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_find_value_of_partition()

"""
Time Complexity Analysis:
- Basic/Optimized/Mathematical: O(n log n) - dominated by sorting step
- Brute Force: O(2^n * n) - exponential, checking all partitions

Space Complexity Analysis:
- Basic/Optimized/Mathematical: O(1) or O(n) depending on sorting implementation
- Brute Force: O(n) - for storing partition subsets

Key Insights:
1. The optimal partition has max(nums1) and min(nums2) as consecutive elements in sorted order
2. This reduces the problem to finding minimum adjacent difference in sorted array
3. Sorting allows us to consider all possible optimal partitions efficiently
4. The mathematical insight eliminates the need to explicitly construct partitions

Mathematical Proof:
- For any partition, let a = max(nums1) and b = min(nums2)
- If a and b are not consecutive in sorted order, we can improve the partition
- Moving elements between a and b to the opposite partition reduces |a - b|
- Therefore, optimal partitions have consecutive elements as boundary points

Topics: Arrays, Sorting, Greedy, Math
"""
