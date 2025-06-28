"""
LeetCode Problem 2811: Check if it is Possible to Split Array

You are given an array nums of length n and an integer m.

You need to determine if it is possible to split the array into n non-empty arrays such that:
- Each element belongs to exactly one array.
- Each array has a sum greater than or equal to m.

Return true if such a split is possible, or false otherwise.

Constraints:
- 1 <= n <= 100
- 1 <= nums[i] <= 100
- 1 <= m <= 200

Example 1:
Input: nums = [2, 2, 1], m = 4
Output: true
Explanation: We can split the array into [2, 2] and [1]. However, spliting into [2] and [2, 1] is not valid because the array [2] has a sum 2 which is less than m = 4.

Example 2:
Input: nums = [2, 1, 3], m = 5 
Output: false
Explanation: There is no way to split the array such that each array has a sum >= 5.

Example 3:
Input: nums = [2, 3, 3, 2, 3], m = 6
Output: true
Explanation: We can split the array into [2, 3, 3] and [2, 3] where both arrays have a sum >= 6.
"""

def can_split_array(nums, m):
    """
    Approach 1: Recursive Backtracking
    
    Try all possible ways to split the array.
    
    Time Complexity: O(2^n)
    Space Complexity: O(n)
    """
    n = len(nums)
    
    def backtrack(index, current_sum, subarrays_count):
        if index == n:
            return subarrays_count > 0 and current_sum >= m
        
        # Option 1: Add current element to current subarray
        can_continue = backtrack(index + 1, current_sum + nums[index], subarrays_count)
        if can_continue:
            return True
        
        # Option 2: Start new subarray with current element (if current subarray is valid)
        if current_sum >= m:
            can_start_new = backtrack(index + 1, nums[index], 1)
            if can_start_new:
                return True
        
        return False
    
    # Start with first element
    return backtrack(1, nums[0], 1)

def can_split_array_dp(nums, m):
    """
    Approach 2: Dynamic Programming
    
    Use DP to check if we can split array ending at each position.
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    n = len(nums)
    if n == 0:
        return True
    
    # dp[i] = True if we can split nums[0:i+1] into valid subarrays
    dp = [False] * n
    
    # Check all possible first subarrays
    current_sum = 0
    for i in range(n):
        current_sum += nums[i]
        if current_sum >= m:
            dp[i] = True
    
    # Fill the DP table
    for i in range(1, n):
        if dp[i]:  # Already true from first subarray
            continue
            
        # Try all possible last subarrays ending at i
        current_sum = 0
        for j in range(i, -1, -1):
            current_sum += nums[j]
            if current_sum >= m and (j == 0 or dp[j-1]):
                dp[i] = True
                break
    
    return dp[n-1]

def can_split_array_greedy(nums, m):
    """
    Approach 3: Greedy Approach
    
    Greedily form subarrays as soon as sum >= m.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(nums)
    current_sum = 0
    subarrays_formed = 0
    
    for i in range(n):
        current_sum += nums[i]
        
        # If current sum is >= m, we can form a subarray
        if current_sum >= m:
            subarrays_formed += 1
            current_sum = 0
    
    # Check if we have remaining elements that don't form a valid subarray
    if current_sum > 0 and current_sum < m:
        return False
    
    return subarrays_formed > 0

def can_split_array_optimized(nums, m):
    """
    Approach 4: Optimized Check
    
    Check if total sum allows for valid split.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    total_sum = sum(nums)
    n = len(nums)
    
    # If we need n subarrays each with sum >= m, total sum must be >= n * m
    # But this is too restrictive since we can have fewer subarrays
    
    # More practical: check if we can greedily form valid subarrays
    current_sum = 0
    min_subarrays_needed = 0
    
    for num in nums:
        current_sum += num
        if current_sum >= m:
            min_subarrays_needed += 1
            current_sum = 0
    
    # If there are leftover elements, they must be absorbed by previous subarrays
    # or form their own subarray if sum >= m
    if current_sum > 0:
        if current_sum < m:
            # These elements need to be merged with previous subarray
            # Only possible if we have at least one previous subarray
            return min_subarrays_needed > 0
        else:
            min_subarrays_needed += 1
    
    return min_subarrays_needed > 0

def can_split_array_memoization(nums, m):
    """
    Approach 5: Recursion with Memoization
    
    Use memoization to optimize recursive solution.
    
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    """
    n = len(nums)
    memo = {}
    
    def can_split(start, must_start_new):
        if start == n:
            return not must_start_new
        
        if (start, must_start_new) in memo:
            return memo[(start, must_start_new)]
        
        result = False
        current_sum = 0
        
        # Try all possible endings for current subarray
        for end in range(start, n):
            current_sum += nums[end]
            
            if current_sum >= m:
                # Can end current subarray here
                remaining_possible = can_split(end + 1, False)
                if remaining_possible:
                    result = True
                    break
        
        memo[(start, must_start_new)] = result
        return result
    
    return can_split(0, True)

def can_split_array_sliding_window(nums, m):
    """
    Approach 6: Sliding Window Approach
    
    Use sliding window to find valid subarrays.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(nums)
    
    def has_valid_subarray_starting_at(start):
        """Check if there's a valid subarray starting at given position"""
        current_sum = 0
        for i in range(start, n):
            current_sum += nums[i]
            if current_sum >= m:
                return i + 1  # Return ending position + 1
        return -1
    
    position = 0
    while position < n:
        next_position = has_valid_subarray_starting_at(position)
        if next_position == -1:
            return False
        position = next_position
    
    return True

# Test cases
def test_can_split_array():
    test_cases = [
        ([2, 2, 1], 4, True),
        ([2, 1, 3], 5, False),
        ([2, 3, 3, 2, 3], 6, True),
        ([1, 1, 1, 1], 2, True),
        ([5], 5, True),
        ([3], 5, False),
        ([1, 2, 3, 4, 5], 3, True),
        ([1, 1, 1], 5, False),
        ([10, 5, 2, 3], 7, True),
        ([1, 2, 2, 1, 2], 3, True)
    ]
    
    approaches = [
        ("Recursive Backtracking", can_split_array),
        ("Dynamic Programming", can_split_array_dp),
        ("Greedy", can_split_array_greedy),
        ("Optimized", can_split_array_optimized),
        ("Memoization", can_split_array_memoization),
        ("Sliding Window", can_split_array_sliding_window)
    ]
    
    for approach_name, func in approaches:
        print(f"Testing {approach_name} approach:")
        all_passed = True
        
        for nums, m, expected in test_cases:
            try:
                result = func(nums[:], m)
                passed = result == expected
                if not passed:
                    all_passed = False
                
                print(f"  Input: nums={nums}, m={m}")
                print(f"  Expected: {expected}, Got: {result}")
                print(f"  {'✓' if passed else '✗'}")
            except Exception as e:
                print(f"  Input: nums={nums}, m={m}")
                print(f"  Error: {e}")
                print(f"  ✗")
                all_passed = False
        
        print(f"  Overall: {'✓ All Passed' if all_passed else '✗ Some Failed'}\n")

def test_edge_cases():
    """Test edge cases specifically"""
    edge_cases = [
        ([], 1, True),      # Empty array
        ([100], 50, True),  # Single element >= m
        ([25], 50, False),  # Single element < m
        ([1] * 100, 1, True),  # All elements = 1, m = 1
        ([1] * 100, 101, False),  # Impossible case
    ]
    
    print("Testing Edge Cases:")
    for nums, m, expected in edge_cases:
        try:
            result = can_split_array_greedy(nums, m)
            passed = result == expected
            print(f"  nums={nums if len(nums) <= 10 else f'[1]*{len(nums)}'}, m={m}")
            print(f"  Expected: {expected}, Got: {result}, {'✓' if passed else '✗'}")
        except Exception as e:
            print(f"  Error: {e}")

if __name__ == "__main__":
    test_can_split_array()
    print("\n" + "="*50)
    test_edge_cases()

"""
Topics: Arrays, Dynamic Programming, Greedy, Backtracking
Difficulty: Medium

Key Insights:
1. Greedy approach: form subarrays as soon as sum >= m
2. DP tracks whether valid split exists up to each position
3. Backtracking explores all possible splits
4. Must ensure no leftover elements with sum < m
5. Total sum constraint provides early termination

Companies: Google, Microsoft, Amazon, Apple
"""
