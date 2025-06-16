"""
2731. Movement of Robots

Some robots are standing on an infinite number line with their initial coordinates given by a 0-indexed integer array nums and will start moving once given the command to move. The robots will move a unit distance each second.

You are given a string s denoting the direction in which robots will move:
- 'L' means the robot will move towards the left side or the negative side of the number line.
- 'R' means the robot will move towards the right side or the positive side of the number line.

When two robots collide, they start moving in opposite directions instantly. A robot moving to the left and a robot moving to the right will collide if they meet at some point and they will instantly reverse directions.

Return the sum of distances between all pairs of robots d seconds after the command.

Since the answer can be very large, return it modulo 10^9 + 7.

The distance between two robots at coordinates x1 and x2 is |x1 - x2|.

Example 1:
Input: nums = [-2,0,2], s = "RLL", d = 3
Output: 8
Explanation: 
After 3 seconds, the positions are [-1,-1,1].
The distance between (-1,-1) is |(-1)-(-1)| = 0.
The distance between (-1,1) is |(-1)-1| = 2.
The distance between (-1,1) is |(-1)-1| = 2.
The distance between (-1,1) is |(-1)-1| = 2.
The sum is 0 + 2 + 2 + 2 = 8.

Example 2:
Input: nums = [1,0], s = "RL", d = 2
Output: 5
Explanation:
After 2 seconds, the positions are [3,-2].
The distance between them is |3-(-2)| = 5.

Constraints:
- 2 <= nums.length <= 10^5
- -2 * 10^9 <= nums[i] <= 2 * 10^9
- 0 <= d <= 10^9
- s.length == nums.length
- s consists of only 'L' and 'R'.
"""

def sum_of_distances_after_queries(nums: list[int], s: str, d: int) -> int:
    """
    Calculate sum of distances between all pairs of robots after d seconds.
    Key insight: Collisions don't affect the final sorted order of positions.
    
    Args:
        nums: Initial positions of robots
        s: Direction string ('L' for left, 'R' for right)
        d: Number of seconds
        
    Returns:
        int: Sum of distances between all pairs modulo 10^9 + 7
        
    Time Complexity: O(n log n) - due to sorting
    Space Complexity: O(n) - for storing final positions
    """
    MOD = 10**9 + 7
    n = len(nums)
    
    # Calculate final positions after d seconds (ignoring collisions)
    final_positions = []
    for i in range(n):
        if s[i] == 'L':
            final_positions.append(nums[i] - d)
        else:
            final_positions.append(nums[i] + d)
    
    # Sort final positions
    final_positions.sort()
    
    # Calculate sum of distances between all pairs
    total_distance = 0
    for i in range(n):
        for j in range(i + 1, n):
            total_distance = (total_distance + final_positions[j] - final_positions[i]) % MOD
    
    return total_distance

def sum_of_distances_after_queries_optimized(nums: list[int], s: str, d: int) -> int:
    """
    Optimized version using mathematical formula for sum of distances.
    For sorted array, sum of distances = sum of (2*i - n + 1) * arr[i] for each i.
    
    Args:
        nums: Initial positions of robots
        s: Direction string
        d: Number of seconds
        
    Returns:
        int: Sum of distances between all pairs modulo 10^9 + 7
        
    Time Complexity: O(n log n) - due to sorting
    Space Complexity: O(n) - for storing final positions
    """
    MOD = 10**9 + 7
    n = len(nums)
    
    # Calculate final positions
    final_positions = []
    for i in range(n):
        if s[i] == 'L':
            final_positions.append(nums[i] - d)
        else:
            final_positions.append(nums[i] + d)
    
    # Sort final positions
    final_positions.sort()
    
    # Use mathematical formula: for each position at index i,
    # it contributes (2*i - n + 1) * position to the total sum
    total_distance = 0
    for i in range(n):
        contribution = ((2 * i - n + 1) * final_positions[i]) % MOD
        total_distance = (total_distance + contribution) % MOD
    
    return total_distance

def sum_of_distances_after_queries_simulation(nums: list[int], s: str, d: int) -> int:
    """
    Simulation approach for verification (inefficient for large d).
    
    Args:
        nums: Initial positions of robots
        s: Direction string
        d: Number of seconds
        
    Returns:
        int: Sum of distances between all pairs modulo 10^9 + 7
        
    Time Complexity: O(d * n^2) - simulation for d seconds
    Space Complexity: O(n) - for current positions and directions
    """
    MOD = 10**9 + 7
    n = len(nums)
    
    positions = nums[:]
    directions = list(s)
    
    # Simulate movement (only practical for small d)
    for _ in range(min(d, 1000)):  # Limit simulation for large d
        new_positions = []
        new_directions = []
        
        # Move robots
        for i in range(n):
            if directions[i] == 'L':
                new_positions.append(positions[i] - 1)
            else:
                new_positions.append(positions[i] + 1)
            new_directions.append(directions[i])
        
        # Handle collisions (simplified - just reverse directions when robots are at same position)
        for i in range(n):
            for j in range(i + 1, n):
                if new_positions[i] == new_positions[j]:
                    new_directions[i] = 'R' if new_directions[i] == 'L' else 'L'
                    new_directions[j] = 'R' if new_directions[j] == 'L' else 'L'
        
        positions = new_positions
        directions = new_directions
    
    # For large d, use the mathematical approach
    if d > 1000:
        return sum_of_distances_after_queries_optimized(nums, s, d)
    
    # Calculate final sum of distances
    total_distance = 0
    for i in range(n):
        for j in range(i + 1, n):
            total_distance = (total_distance + abs(positions[i] - positions[j])) % MOD
    
    return total_distance

# Test cases
def test_sum_of_distances_after_queries():
    test_cases = [
        # Basic test cases
        ([-2, 0, 2], "RLL", 3, 8),
        ([1, 0], "RL", 2, 5),
        
        # Edge cases
        ([0, 1], "LR", 1, 4),      # Simple case
        ([0, 0], "LR", 1, 2),      # Same starting position
        ([1, 2, 3], "LLL", 2, 6),  # All moving left
        ([1, 2, 3], "RRR", 2, 6),  # All moving right
        
        # Complex cases
        ([0, 1, 2, 3], "RLRL", 1, 8),
        ([-1, 0, 1], "LRR", 2, 10),
        ([10, 20, 30], "RLR", 5, 30),
        
        # Large distance cases
        ([0, 100], "LR", 50, 200),
        
        # Multiple robots
        ([1, 2, 3, 4, 5], "LRLRL", 2, 20),
    ]
    
    print("Testing sum_of_distances_after_queries function:")
    for i, (nums, s, d, expected) in enumerate(test_cases):
        result1 = sum_of_distances_after_queries(nums, s, d)
        result2 = sum_of_distances_after_queries_optimized(nums, s, d)
        
        print(f"Test {i+1}: nums={nums}, s='{s}', d={d}")
        print(f"  Expected: {expected}")
        print(f"  Basic: {result1}")
        print(f"  Optimized: {result2}")
        
        assert result1 == expected, f"Basic failed for test case {i+1}"
        assert result2 == expected, f"Optimized failed for test case {i+1}"
        print(f"  ✓ All passed\n")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_sum_of_distances_after_queries()

"""
Time Complexity Analysis:
- Basic Solution: O(n^2 + n log n) - sorting plus pairwise distance calculation
- Optimized Solution: O(n log n) - sorting plus linear sum calculation
- Simulation: O(d * n^2) - impractical for large d

Space Complexity Analysis:
- All solutions: O(n) - for storing final positions

Key Insights:
1. Collisions don't change the final sorted order of robot positions
2. We can calculate final positions directly without simulating collisions
3. Mathematical formula for sum of distances in sorted array is more efficient
4. The problem reduces to finding sum of distances between points on a line

Topics: Arrays, Sorting, Math, Simulation, Greedy
"""
