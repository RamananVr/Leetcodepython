"""
2735. Collecting Chocolates

You are given a 0-indexed integer array nums of size n and a non-negative integer x.

You are initially at position 0 in the array and can move to either the left or the right.

The array is circular, so when you are at position i:
- Moving to the right takes you to position (i + 1) % n
- Moving to the left takes you to position (i - 1 + n) % n

You want to collect all chocolates in the array. The cost of collecting the chocolate at position i is nums[i].

You can also perform a rotation operation any number of times. Each rotation operation costs x and shifts all elements in the array to the left by one position:
- nums becomes [nums[1], nums[2], ..., nums[n-1], nums[0]]

Return the minimum cost to collect all chocolates.

Example 1:
Input: nums = [20,1,15], x = 5
Output: 13
Explanation: Initially, the array is [20,1,15].
We can do the following operations:
- Collect the chocolate at index 1, which costs nums[1] = 1.
- Do a rotation operation, which costs x = 5. Now the array is [1,15,20].
- Collect the chocolate at index 1, which costs nums[1] = 15.
- Do a rotation operation, which costs x = 5. Now the array is [15,20,1].
- Collect the chocolate at index 1, which costs nums[1] = 20.
The total cost is 1 + 5 + 15 + 5 + 20 = 46.

Alternatively:
- Collect all chocolates at their original positions: 20 + 1 + 15 = 36.
But we can be smarter:
- Collect chocolate at index 1 (cost 1)
- Rotate once (cost 5), now [1,15,20], collect at index 1 (cost 15)  
- Rotate once (cost 5), now [15,20,1], collect at index 1 (cost 20)
Total: 1 + 5 + 15 + 5 + 20 = 46. But this is not optimal.

Actually optimal:
- Collect at index 1: cost 1
- Rotate twice (cost 10): [15,20,1] -> [20,1,15], collect at index 1: cost 1
Wait, that's not right either.

Let me recalculate: collect chocolate at position 1 (cost 1), then we need the other chocolates.
We can collect at their original positions (20 + 15 = 35) for total 36.
Or we can rotate to bring them to position 1: 
- After 1 rotation: [1,15,20], collect at pos 1 costs 15, total rotations = 1
- After 2 rotations: [15,20,1], collect at pos 1 costs 20, total rotations = 2
So strategy is: 1 + (5*1 + 15) + (5*2 + 20) = 1 + 20 + 30 = 51, which is worse.

Actually, let's collect all at once: 20 + 1 + 15 = 36.
Or collect at position with minimum after rotations:
- Position 0: 20 (0 rotations), 1 (2 rotations), 15 (1 rotation) -> min(20, 1+2*5, 15+1*5) = min(20, 11, 20) = 11
- Position 1: 1 (0 rotations), 15 (1 rotation), 20 (2 rotations) -> min(1, 15+5, 20+10) = min(1, 20, 30) = 1  
- Position 2: 15 (0 rotations), 20 (1 rotation), 1 (2 rotations) -> min(15, 20+5, 1+10) = min(15, 25, 11) = 11
Total minimum: 11 + 1 + 11 = 23.

Wait, that's not how it works. We collect ALL chocolates, so we need the sum.
Let me reconsider...

Example 2:
Input: nums = [1,2,3], x = 4
Output: 6
Explanation: The optimal strategy is to collect all chocolates at their initial positions: 1 + 2 + 3 = 6.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 10^9
- 0 <= x <= 10^9
"""

def min_cost_to_collect_chocolates(nums: list[int], x: int) -> int:
    """
    Find minimum cost to collect all chocolates considering rotation operations.
    
    Args:
        nums: Array of chocolate costs at each position
        x: Cost of each rotation operation
        
    Returns:
        int: Minimum total cost to collect all chocolates
        
    Time Complexity: O(n^2) - trying all rotation strategies
    Space Complexity: O(n) - storing minimum costs for each position
    """
    n = len(nums)
    
    # For each chocolate, compute minimum cost to collect it at any position
    min_costs = [float('inf')] * n
    
    # Try all possible numbers of rotations (0 to n-1)
    for rotations in range(n):
        rotation_cost = rotations * x
        
        for i in range(n):
            # After 'rotations' rotations, chocolate originally at position i
            # will be at position (i - rotations) % n
            new_position = (i - rotations) % n
            
            # Cost to collect this chocolate = rotation cost + chocolate value
            cost = rotation_cost + nums[i]
            min_costs[new_position] = min(min_costs[new_position], cost)
    
    return sum(min_costs)

def min_cost_to_collect_chocolates_optimized(nums: list[int], x: int) -> int:
    """
    Optimized approach using dynamic programming concept.
    
    Args:
        nums: Array of chocolate costs
        x: Rotation cost
        
    Returns:
        int: Minimum total cost
        
    Time Complexity: O(n^2) - but with better constant factors
    Space Complexity: O(n) - for tracking minimum costs
    """
    n = len(nums)
    
    # min_cost[i] = minimum cost to collect chocolate that's currently at position i
    min_cost = nums[:]  # Initially, each chocolate is at its original position
    total_cost = sum(nums)  # Cost without any rotations
    
    # Try performing 1, 2, ..., n-1 rotations
    for rotation in range(1, n):
        rotation_cost = rotation * x
        current_total = rotation_cost
        
        # After 'rotation' rotations, update positions
        for i in range(n):
            # Original chocolate at position (i + rotation) % n is now at position i
            original_pos = (i + rotation) % n
            min_cost[i] = min(min_cost[i], nums[original_pos])
            current_total += min_cost[i]
        
        total_cost = min(total_cost, current_total)
    
    return total_cost

def min_cost_to_collect_chocolates_brute_force(nums: list[int], x: int) -> int:
    """
    Brute force approach considering all rotation strategies.
    
    Args:
        nums: Array of chocolate costs
        x: Rotation cost
        
    Returns:
        int: Minimum total cost
        
    Time Complexity: O(n^2) - trying all rotation counts
    Space Complexity: O(1) - constant extra space
    """
    n = len(nums)
    min_total_cost = float('inf')
    
    # Try 0 to n-1 rotations
    for rotations in range(n):
        total_cost = rotations * x
        
        # For each position, find minimum cost chocolate that can be placed there
        for pos in range(n):
            min_cost_at_pos = float('inf')
            
            # Check all possible chocolates that can be at this position
            for r in range(rotations + 1):
                # After r rotations, chocolate originally at (pos + r) % n will be at pos
                original_pos = (pos + r) % n
                min_cost_at_pos = min(min_cost_at_pos, nums[original_pos])
            
            total_cost += min_cost_at_pos
        
        min_total_cost = min(min_total_cost, total_cost)
    
    return min_total_cost

# Test cases
def test_min_cost_to_collect_chocolates():
    test_cases = [
        # Basic test cases
        ([20, 1, 15], 5, 13),
        ([1, 2, 3], 4, 6),
        
        # Edge cases
        ([5], 1, 5),              # Single chocolate
        ([1, 1], 1, 2),           # Two identical chocolates
        ([10, 1], 2, 3),          # Better to rotate
        ([1, 10], 2, 3),          # Better to rotate
        
        # No rotation beneficial
        ([1, 2, 3, 4], 10, 10),   # High rotation cost
        ([5, 5, 5], 1, 15),       # All same values
        
        # Rotation beneficial
        ([100, 1, 1], 1, 4),      # Much cheaper to rotate
        ([1, 100, 1], 1, 3),      # Middle element expensive
        
        # Complex cases
        ([3, 1, 2], 1, 4),        
        ([4, 3, 2, 1], 2, 6),     
        ([10, 1, 1, 10], 3, 7),   
    ]
    
    print("Testing min_cost_to_collect_chocolates function:")
    for i, (nums, x, expected) in enumerate(test_cases):
        result1 = min_cost_to_collect_chocolates(nums, x)
        result2 = min_cost_to_collect_chocolates_optimized(nums, x)
        
        print(f"Test {i+1}: nums={nums}, x={x}")
        print(f"  Expected: {expected}")
        print(f"  Basic: {result1}")
        print(f"  Optimized: {result2}")
        
        assert result1 == expected, f"Basic failed for test case {i+1}"
        assert result2 == expected, f"Optimized failed for test case {i+1}"
        print(f"  ✓ All passed\n")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_min_cost_to_collect_chocolates()

"""
Time Complexity Analysis:
- Basic Solution: O(n^2) - for each position, try all rotation counts
- Optimized Solution: O(n^2) - but with better tracking of minimum costs
- Brute Force: O(n^3) - trying all rotations and all positions

Space Complexity Analysis:
- Basic/Optimized: O(n) - storing minimum costs array
- Brute Force: O(1) - constant extra space

Key Insights:
1. We can perform any number of rotations, each costing x
2. The goal is to minimize total cost: rotation_cost + sum_of_chocolate_costs
3. For each final position, we want the cheapest chocolate that can reach it
4. A chocolate at original position i can reach position j with (i-j)%n rotations
5. We need to balance rotation costs with chocolate savings

Topics: Arrays, Dynamic Programming, Greedy, Circular Array
"""
