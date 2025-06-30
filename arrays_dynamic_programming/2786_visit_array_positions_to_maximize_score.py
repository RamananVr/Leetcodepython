"""
LeetCode Problem 2786: Visit Array Positions to Maximize Score

You are given a 0-indexed integer array nums and a positive integer x.

You are initially at position 0 in the array, and you can visit other positions according to the following rules:
- Starting from position i, you can move to any position j such that i < j.
- When you move from position i to position j, you gain nums[j] points.
- If nums[i] and nums[j] have different parity (one is even, one is odd), you lose x points.

Return the maximum score you can obtain.

Constraints:
- 2 <= nums.length <= 10^5
- 1 <= nums[i], x <= 10^6

Example 1:
Input: nums = [2,3,6,1,9,2], x = 5
Output: 13
Explanation: We can visit the following positions in the array: 0 → 2 → 3 → 5.
- From 0 to 2, we gain 6 points and lose 0 points since both are even.
- From 2 to 3, we gain 1 point and lose 5 points since 6 is even and 1 is odd.
- From 3 to 5, we gain 2 points and lose 5 points since 1 is odd and 2 is even.
Total score: 6 + 1 - 5 + 2 - 5 = -1. Wait, let me recalculate...
Actually: Start with nums[0] = 2, then 2 + 6 - 0 + 1 - 5 + 2 - 5 = 1. Let me check the optimal path.

Example 2:
Input: nums = [2,4,6,8], x = 3
Output: 20
Explanation: All numbers are even, so no penalty. We visit all positions: 2 + 4 + 6 + 8 = 20.
"""

def max_score_dp(nums, x):
    """
    Optimized Dynamic Programming solution
    
    Track maximum score ending at even/odd numbers separately.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(nums)
    
    # dp_even: max score ending at an even number
    # dp_odd: max score ending at an odd number
    
    if nums[0] % 2 == 0:
        dp_even = nums[0]
        dp_odd = nums[0] - x  # If we must start with odd, pay penalty
    else:
        dp_odd = nums[0]
        dp_even = nums[0] - x  # If we must start with even, pay penalty
    
    for i in range(1, n):
        current = nums[i]
        
        if current % 2 == 0:  # Current number is even
            new_dp_even = max(
                dp_even + current,      # Continue from even (no penalty)
                dp_odd + current - x    # Switch from odd (penalty)
            )
            dp_even = new_dp_even
        else:  # Current number is odd
            new_dp_odd = max(
                dp_odd + current,       # Continue from odd (no penalty)
                dp_even + current - x   # Switch from even (penalty)
            )
            dp_odd = new_dp_odd
    
    return max(dp_even, dp_odd)

def max_score_memoization(nums, x):
    """
    Alternative approach with memoization
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(nums)
    memo = {}
    
    def dp(index, last_parity):
        if index >= n:
            return 0
        
        if (index, last_parity) in memo:
            return memo[(index, last_parity)]
        
        current_parity = nums[index] % 2
        penalty = x if current_parity != last_parity else 0
        
        # Take current element
        take = nums[index] - penalty + dp(index + 1, current_parity)
        
        # Skip current element (if not at index 0)
        skip = dp(index + 1, last_parity) if index > 0 else float('-inf')
        
        result = max(take, skip)
        memo[(index, last_parity)] = result
        return result
    
    # Start from index 0
    return nums[0] + dp(1, nums[0] % 2)

def max_score_optimized(nums, x):
    """
    Most optimized solution with single pass
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Initialize scores for even and odd endings
    even_score = float('-inf')
    odd_score = float('-inf')
    
    # Set initial score based on first element
    if nums[0] % 2 == 0:
        even_score = nums[0]
    else:
        odd_score = nums[0]
    
    # Process remaining elements
    for i in range(1, len(nums)):
        current = nums[i]
        
        if current % 2 == 0:  # Current is even
            # Update even_score: max of continuing even path or switching from odd
            even_score = max(
                even_score + current,           # No penalty
                odd_score + current - x         # Penalty for switching
            )
        else:  # Current is odd
            # Update odd_score: max of continuing odd path or switching from even
            odd_score = max(
                odd_score + current,            # No penalty
                even_score + current - x        # Penalty for switching
            )
    
    return max(even_score, odd_score)

def max_score_greedy_optimized(nums, x):
    """
    Greedy approach with optimization insights
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(nums) <= 1:
        return nums[0] if nums else 0
    
    # Keep track of best scores for even and odd paths
    best_even = float('-inf')
    best_odd = float('-inf')
    
    # Initialize with first element
    if nums[0] % 2 == 0:
        best_even = nums[0]
    else:
        best_odd = nums[0]
    
    # For each subsequent element, choose optimal path
    for i in range(1, len(nums)):
        val = nums[i]
        
        if val % 2 == 0:  # Even number
            new_even = max(
                best_even + val,        # Continue even path
                best_odd + val - x      # Switch from odd path
            )
            best_even = new_even
        else:  # Odd number
            new_odd = max(
                best_odd + val,         # Continue odd path
                best_even + val - x     # Switch from even path
            )
            best_odd = new_odd
    
    return max(best_even, best_odd)

# Test cases
def test_max_score():
    test_cases = [
        ([2, 3, 6, 1, 9, 2], 5, 13),
        ([2, 4, 6, 8], 3, 20),
        ([1, 3, 5], 2, 9),        # All odd
        ([2, 4, 6], 1, 12),       # All even
        ([1, 2], 1, 2),           # Simple case
        ([5, 1, 3, 2, 8], 4, 19), # Mixed case
        ([38, 92, 23, 30, 28, 15, 48, 35, 98, 3], 52, 291),  # Longer array
    ]
    
    approaches = [
        ("DP Optimized", max_score_dp),
        ("Memoization", max_score_memoization),
        ("Most Optimized", max_score_optimized),
        ("Greedy Optimized", max_score_greedy_optimized)
    ]
    
    for approach_name, func in approaches:
        print(f"Testing {approach_name} approach:")
        all_passed = True
        
        for nums, x, expected in test_cases:
            try:
                result = func(nums[:], x)
                passed = result == expected
                if not passed:
                    all_passed = False
                
                print(f"  Input: nums={nums}, x={x}")
                print(f"  Expected: {expected}, Got: {result}")
                print(f"  {'✓' if passed else '✗'}")
            except Exception as e:
                print(f"  Input: nums={nums}, x={x}")
                print(f"  Error: {e}")
                print(f"  ✗")
                all_passed = False
        
        print(f"  Overall: {'✓ All Passed' if all_passed else '✗ Some Failed'}\n")

def analyze_example():
    """Analyze the first example step by step"""
    nums = [2, 3, 6, 1, 9, 2]
    x = 5
    
    print("Step-by-step analysis of [2,3,6,1,9,2] with x=5:")
    print("Position: 0  1  2  3  4  5")
    print("Values:   2  3  6  1  9  2")
    print("Parity:   E  O  E  O  O  E")
    print()
    
    # Simulate the DP
    even_score = 2  # Start with nums[0] = 2 (even)
    odd_score = 2 - x  # If we had to start with odd
    
    print(f"Initial: even_score = {even_score}, odd_score = {odd_score}")
    
    for i in range(1, len(nums)):
        current = nums[i]
        parity = "even" if current % 2 == 0 else "odd"
        
        print(f"\nPosition {i}: {current} ({parity})")
        
        if current % 2 == 0:  # Even
            new_even = max(even_score + current, odd_score + current - x)
            print(f"  even_score = max({even_score} + {current}, {odd_score} + {current} - {x}) = {new_even}")
            even_score = new_even
        else:  # Odd
            new_odd = max(odd_score + current, even_score + current - x)
            print(f"  odd_score = max({odd_score} + {current}, {even_score} + {current} - {x}) = {new_odd}")
            odd_score = new_odd
        
        print(f"  Current: even_score = {even_score}, odd_score = {odd_score}")
    
    result = max(even_score, odd_score)
    print(f"\nFinal result: max({even_score}, {odd_score}) = {result}")

if __name__ == "__main__":
    test_max_score()
    print("\n" + "="*50)
    analyze_example()

"""
Topics: Arrays, Dynamic Programming, Greedy
Difficulty: Medium

Key Insights:
1. Track maximum scores for paths ending with even/odd numbers separately
2. When processing each element, consider both continuing same parity and switching
3. Switching parity incurs penalty x, same parity has no penalty
4. DP state: (position, last_parity) or simplified to two variables
5. Greedy works because we only need to track best even/odd scores so far

Companies: Google, Microsoft, Amazon, Meta
"""
