"""
LeetCode Problem 2760: Longest Even Odd Subarray With Threshold

You are given a 0-indexed integer array nums and an integer threshold.

Find the length of the longest subarray of nums starting at an even index, where:
- The first element of the subarray is even
- All elements in the subarray are <= threshold
- Adjacent elements have different parity (even/odd alternating)

Return the length of such a subarray, or 0 if no such subarray exists.

Example 1:
Input: nums = [3,2,5,4], threshold = 5
Output: 3
Explanation: The subarray [2,5,4] starting at index 1 (even index) has length 3.
- First element 2 is even
- All elements (2,5,4) are <= 5
- Elements alternate: 2(even), 5(odd), 4(even)

Example 2:
Input: nums = [1,2], threshold = 2
Output: 1
Explanation: The subarray [2] starting at index 1 (even index) has length 1.
- First element 2 is even
- 2 <= 2
- Single element trivially alternates

Example 3:
Input: nums = [2,3,4,5], threshold = 4
Output: 3
Explanation: The subarray [2,3,4] starting at index 0 (even index) has length 3.
- First element 2 is even
- All elements (2,3,4) are <= 4
- Elements alternate: 2(even), 3(odd), 4(even)

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
- 1 <= threshold <= 100
"""

from typing import List


def longestAlternatingSubarray(nums: List[int], threshold: int) -> int:
    """
    Find the longest alternating even-odd subarray starting at even index.
    
    Strategy:
    1. Try starting at each even index
    2. Check if first element is even and <= threshold
    3. Extend while elements alternate parity and stay <= threshold
    4. Track maximum length found
    
    Args:
        nums: Array of integers
        threshold: Maximum allowed value
        
    Returns:
        Length of longest valid subarray
        
    Time Complexity: O(n^2) worst case
    Space Complexity: O(1)
    """
    n = len(nums)
    max_length = 0
    
    # Try starting at each even index
    for start in range(0, n, 2):  # Even indices: 0, 2, 4, ...
        # Check if first element meets requirements
        if nums[start] % 2 != 0 or nums[start] > threshold:
            continue
        
        # Extend the subarray while conditions are met
        length = 1
        for i in range(start + 1, n):
            # Check threshold condition
            if nums[i] > threshold:
                break
            
            # Check alternating parity condition
            if nums[i] % 2 == nums[i-1] % 2:
                break
            
            length += 1
        
        max_length = max(max_length, length)
    
    return max_length


def longestAlternatingSubarrayOptimized(nums: List[int], threshold: int) -> int:
    """
    Optimized approach using single pass with state tracking.
    
    Args:
        nums: Array of integers
        threshold: Maximum allowed value
        
    Returns:
        Length of longest valid subarray
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(nums)
    max_length = 0
    current_length = 0
    
    for i in range(n):
        # Check if we can start a new subarray at this position
        if (i % 2 == 0 and  # Even index
            nums[i] % 2 == 0 and  # Even value
            nums[i] <= threshold):  # Within threshold
            current_length = 1
        # Check if we can extend current subarray
        elif (current_length > 0 and
              nums[i] <= threshold and
              nums[i] % 2 != nums[i-1] % 2):  # Different parity from previous
            current_length += 1
        else:
            # Reset if conditions not met
            current_length = 0
        
        max_length = max(max_length, current_length)
    
    return max_length


def longestAlternatingSubarrayBruteForce(nums: List[int], threshold: int) -> int:
    """
    Brute force approach checking all possible subarrays.
    
    Args:
        nums: Array of integers
        threshold: Maximum allowed value
        
    Returns:
        Length of longest valid subarray
        
    Time Complexity: O(n^3)
    Space Complexity: O(1)
    """
    n = len(nums)
    max_length = 0
    
    # Try all possible starting positions (even indices only)
    for start in range(0, n, 2):
        # Try all possible ending positions
        for end in range(start, n):
            if is_valid_subarray(nums, start, end, threshold):
                max_length = max(max_length, end - start + 1)
    
    return max_length


def is_valid_subarray(nums: List[int], start: int, end: int, threshold: int) -> bool:
    """
    Check if subarray from start to end meets all conditions.
    
    Args:
        nums: Array of integers
        start: Start index (must be even)
        end: End index (inclusive)
        threshold: Maximum allowed value
        
    Returns:
        True if subarray is valid, False otherwise
    """
    # Check if start index is even
    if start % 2 != 0:
        return False
    
    # Check if first element is even
    if nums[start] % 2 != 0:
        return False
    
    # Check all elements
    for i in range(start, end + 1):
        # Check threshold condition
        if nums[i] > threshold:
            return False
        
        # Check alternating parity (except for first element)
        if i > start and nums[i] % 2 == nums[i-1] % 2:
            return False
    
    return True


def longestAlternatingSubarrayDP(nums: List[int], threshold: int) -> int:
    """
    Dynamic programming approach.
    
    dp[i] = length of longest valid subarray ending at position i
    
    Args:
        nums: Array of integers
        threshold: Maximum allowed value
        
    Returns:
        Length of longest valid subarray
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(nums)
    if n == 0:
        return 0
    
    dp = [0] * n
    max_length = 0
    
    for i in range(n):
        # Case 1: Start new subarray at even index
        if (i % 2 == 0 and 
            nums[i] % 2 == 0 and 
            nums[i] <= threshold):
            dp[i] = 1
        
        # Case 2: Extend previous subarray
        if (i > 0 and 
            dp[i-1] > 0 and
            nums[i] <= threshold and
            nums[i] % 2 != nums[i-1] % 2):
            dp[i] = max(dp[i], dp[i-1] + 1)
        
        max_length = max(max_length, dp[i])
    
    return max_length


def longestAlternatingSubarraySimple(nums: List[int], threshold: int) -> int:
    """
    Simple implementation focusing on clarity.
    
    Args:
        nums: Array of integers
        threshold: Maximum allowed value
        
    Returns:
        Length of longest valid subarray
        
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    max_length = 0
    
    for start in range(0, len(nums), 2):  # Only even indices
        if nums[start] % 2 == 0 and nums[start] <= threshold:
            length = 1
            
            for i in range(start + 1, len(nums)):
                if (nums[i] <= threshold and 
                    nums[i] % 2 != nums[i-1] % 2):
                    length += 1
                else:
                    break
            
            max_length = max(max_length, length)
    
    return max_length


# Test cases
def test_longestAlternatingSubarray():
    """Test the longestAlternatingSubarray function with various inputs."""
    
    test_cases = [
        {
            "nums": [3, 2, 5, 4],
            "threshold": 5,
            "expected": 3,
            "description": "Example 1: [2,5,4] starting at index 1"
        },
        {
            "nums": [1, 2],
            "threshold": 2,
            "expected": 1,
            "description": "Example 2: [2] starting at index 1"
        },
        {
            "nums": [2, 3, 4, 5],
            "threshold": 4,
            "expected": 3,
            "description": "Example 3: [2,3,4] starting at index 0"
        },
        {
            "nums": [1, 1, 1],
            "threshold": 2,
            "expected": 0,
            "description": "No valid subarray (all odd, no even start)"
        },
        {
            "nums": [2],
            "threshold": 1,
            "expected": 0,
            "description": "Single element exceeds threshold"
        },
        {
            "nums": [2],
            "threshold": 3,
            "expected": 1,
            "description": "Single valid element"
        },
        {
            "nums": [2, 2, 2],
            "threshold": 3,
            "expected": 1,
            "description": "No alternating (all even)"
        },
        {
            "nums": [2, 3, 6, 5],
            "threshold": 5,
            "expected": 2,
            "description": "Threshold violation breaks sequence"
        },
        {
            "nums": [4, 1, 2, 3],
            "threshold": 5,
            "expected": 4,
            "description": "Full array is valid"
        }
    ]
    
    for i, test in enumerate(test_cases):
        nums = test["nums"]
        threshold = test["threshold"]
        expected = test["expected"]
        
        print(f"Test {i+1}: {test['description']}")
        print(f"  Input: nums = {nums}, threshold = {threshold}")
        print(f"  Expected: {expected}")
        
        # Test main solution
        result1 = longestAlternatingSubarray(nums, threshold)
        print(f"  Two-loop approach: {result1}")
        
        # Test optimized solution
        result2 = longestAlternatingSubarrayOptimized(nums, threshold)
        print(f"  Single-pass optimized: {result2}")
        
        # Test simple solution
        result3 = longestAlternatingSubarraySimple(nums, threshold)
        print(f"  Simple approach: {result3}")
        
        # Test DP solution
        result4 = longestAlternatingSubarrayDP(nums, threshold)
        print(f"  DP approach: {result4}")
        
        # Verify results
        assert result1 == expected, f"Two-loop approach failed for test {i+1}"
        assert result2 == expected, f"Optimized approach failed for test {i+1}"
        assert result3 == expected, f"Simple approach failed for test {i+1}"
        assert result4 == expected, f"DP approach failed for test {i+1}"
        
        # Show detailed analysis for smaller inputs
        if len(nums) <= 6:
            print("  Detailed analysis:")
            for start in range(0, len(nums), 2):
                if nums[start] % 2 == 0 and nums[start] <= threshold:
                    length = 1
                    subarray = [nums[start]]
                    for j in range(start + 1, len(nums)):
                        if (nums[j] <= threshold and 
                            nums[j] % 2 != nums[j-1] % 2):
                            length += 1
                            subarray.append(nums[j])
                        else:
                            break
                    print(f"    Start at index {start}: {subarray} (length {length})")
        
        print(f"  ✓ All solutions passed!")
        print()


if __name__ == "__main__":
    test_longestAlternatingSubarray()

"""
Complexity Analysis:

1. Two-loop Approach (longestAlternatingSubarray):
   - Time Complexity: O(n^2) - try each even starting position, extend optimally
   - Space Complexity: O(1) - only using constant extra space

2. Optimized Single-pass (longestAlternatingSubarrayOptimized):
   - Time Complexity: O(n) - single pass with state tracking
   - Space Complexity: O(1) - constant space

3. Brute Force (longestAlternatingSubarrayBruteForce):
   - Time Complexity: O(n^3) - all start/end pairs plus validation
   - Space Complexity: O(1) - constant space

4. Dynamic Programming (longestAlternatingSubarrayDP):
   - Time Complexity: O(n) - single pass
   - Space Complexity: O(n) - DP array

Key Insights:
- Must start at even index (0, 2, 4, ...)
- First element must be even and <= threshold
- Adjacent elements must have different parity (even/odd alternating)
- All elements must be <= threshold

Algorithm Strategy:
1. Try each even starting position
2. Check if first element is even and within threshold
3. Extend while maintaining alternating parity and threshold constraint
4. Track maximum length achieved

Optimization Techniques:
- Single pass with state tracking
- Early termination when constraints violated
- Dynamic programming for overlapping subproblems

Edge Cases:
- Empty array
- Single element arrays
- All elements exceed threshold
- No even elements at even indices
- No alternating pattern possible

Constraint Handling:
- Even index requirement: start ∈ {0, 2, 4, ...}
- Even first element: nums[start] % 2 == 0
- Threshold: nums[i] <= threshold for all i in subarray
- Alternating parity: nums[i] % 2 != nums[i-1] % 2

Topics: Arrays, Two Pointers, Dynamic Programming, Sliding Window
"""
