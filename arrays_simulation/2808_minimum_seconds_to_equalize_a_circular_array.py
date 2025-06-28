"""
LeetCode Problem 2808: Minimum Seconds to Equalize a Circular Array

You are given a 0-indexed array nums of n integers.

At every second, you perform the following operation:
- For every index i, replace nums[i] with either nums[i], nums[(i - 1 + n) % n], or nums[(i + 1) % n].

Return the minimum number of seconds needed to make all values in the array equal.

Constraints:
- 1 <= n <= 10^5
- 1 <= nums[i] <= 10^9

Example 1:
Input: nums = [1,2,1,2]
Output: 1
Explanation: We can equalize the array in 1 second:
- At the 1st second, replace nums[0] and nums[2] with nums[1] and nums[3] respectively. After the 1st second, nums = [2,2,2,2].

Example 2:
Input: nums = [2,1,3,3,2]
Output: 2
Explanation: We can equalize the array in 2 seconds:
- At the 1st second, replace nums[0] with nums[1], and nums[4] with nums[3]. After the 1st second, nums = [1,1,3,3,3].
- At the 2nd second, replace nums[0] and nums[1] with nums[2]. After the 2nd second, nums = [3,3,3,3,3].
It can be proven that 2 seconds is the minimum time to equalize the array.

Example 3:
Input: nums = [5,5,5,5]
Output: 0
Explanation: We don't need to perform any operations as all elements in the initial array are the same.
"""

def minimum_seconds_to_equalize(nums):
    """
    Approach 1: BFS Simulation for Each Unique Value
    
    For each unique value, simulate how many seconds it takes to spread to entire array.
    
    Time Complexity: O(n * k) where k is number of unique values
    Space Complexity: O(n)
    """
    from collections import deque, defaultdict
    
    n = len(nums)
    if n == 1:
        return 0
    
    # Get all unique values and their positions
    value_positions = defaultdict(list)
    for i, val in enumerate(nums):
        value_positions[val].append(i)
    
    min_seconds = float('inf')
    
    # Try each unique value as the target
    for target_val, positions in value_positions.items():
        # BFS to find minimum seconds for this target value
        seconds = bfs_spread_time(nums, positions, n)
        min_seconds = min(min_seconds, seconds)
    
    return min_seconds

def bfs_spread_time(nums, initial_positions, n):
    """
    BFS to calculate spread time for a given target value
    """
    from collections import deque
    
    # Mark initial positions as reached at time 0
    reached = [-1] * n
    queue = deque()
    
    for pos in initial_positions:
        reached[pos] = 0
        queue.append((pos, 0))
    
    max_time = 0
    
    while queue:
        pos, time = queue.popleft()
        
        # Check adjacent positions (circular array)
        for next_pos in [(pos - 1) % n, (pos + 1) % n]:
            if reached[next_pos] == -1:
                reached[next_pos] = time + 1
                max_time = max(max_time, time + 1)
                queue.append((next_pos, time + 1))
    
    return max_time

def minimum_seconds_to_equalize_optimized(nums):
    """
    Approach 2: Mathematical Analysis - Maximum Gap Between Same Values
    
    For each value, find the maximum gap between consecutive occurrences.
    The answer is ceil(max_gap / 2).
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    from collections import defaultdict
    
    n = len(nums)
    if n == 1:
        return 0
    
    # Group positions by value
    value_positions = defaultdict(list)
    for i, val in enumerate(nums):
        value_positions[val].append(i)
    
    min_seconds = float('inf')
    
    for val, positions in value_positions.items():
        max_gap = calculate_max_gap(positions, n)
        seconds_needed = (max_gap + 1) // 2
        min_seconds = min(min_seconds, seconds_needed)
    
    return min_seconds

def calculate_max_gap(positions, n):
    """
    Calculate maximum gap between consecutive positions (considering circular array)
    """
    if len(positions) == 1:
        return n - 1  # Gap to reach all other positions
    
    positions.sort()
    max_gap = 0
    
    # Check gaps between consecutive positions
    for i in range(len(positions)):
        next_i = (i + 1) % len(positions)
        if next_i == 0:
            # Circular gap: from last position to first position
            gap = n - positions[i] + positions[0] - 1
        else:
            gap = positions[next_i] - positions[i] - 1
        max_gap = max(max_gap, gap)
    
    return max_gap

def minimum_seconds_to_equalize_dp(nums):
    """
    Approach 3: Dynamic Programming Approach
    
    Use DP to track spread of each value over time.
    
    Time Complexity: O(n * log n)
    Space Complexity: O(n)
    """
    from collections import defaultdict
    
    n = len(nums)
    if n == 1:
        return 0
    
    # Find positions of each unique value
    positions_map = defaultdict(list)
    for i, val in enumerate(nums):
        positions_map[val].append(i)
    
    min_time = float('inf')
    
    for val, positions in positions_map.items():
        time_needed = calculate_spread_time_dp(positions, n)
        min_time = min(min_time, time_needed)
    
    return min_time

def calculate_spread_time_dp(positions, n):
    """
    Calculate time needed for positions to spread to entire array
    """
    if len(positions) >= n:
        return 0
    
    positions.sort()
    
    # For each position, calculate time to reach farthest point
    max_time = 0
    
    for i in range(len(positions)):
        # Distance to next occurrence (circular)
        next_i = (i + 1) % len(positions)
        
        if next_i == 0:
            # Distance from current to first (wrapping around)
            distance = n - positions[i] + positions[0]
        else:
            distance = positions[next_i] - positions[i]
        
        # Time to cover half the distance (meeting in middle)
        time = (distance - 1) // 2
        max_time = max(max_time, time)
    
    return max_time

def minimum_seconds_to_equalize_greedy(nums):
    """
    Approach 4: Greedy Solution with Interval Analysis
    
    Analyze intervals between same values and find optimal spreading.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    from collections import defaultdict
    
    n = len(nums)
    
    # Special case: already equal
    if len(set(nums)) == 1:
        return 0
    
    # Map each value to its positions
    value_positions = defaultdict(list)
    for i, val in enumerate(nums):
        value_positions[val].append(i)
    
    result = float('inf')
    
    for val, positions in value_positions.items():
        # Calculate maximum time needed for this value to dominate
        max_spread_time = 0
        
        positions.sort()
        m = len(positions)
        
        for i in range(m):
            # Calculate distance to next occurrence
            next_idx = (i + 1) % m
            if next_idx == 0:
                # Wrap around distance
                dist = n - positions[i] + positions[0] - 1
            else:
                dist = positions[next_idx] - positions[i] - 1
            
            # Time needed to fill this gap
            spread_time = (dist + 1) // 2
            max_spread_time = max(max_spread_time, spread_time)
        
        result = min(result, max_spread_time)
    
    return result

def minimum_seconds_simulation(nums):
    """
    Approach 5: Direct Simulation (Brute Force)
    
    Simulate the actual process step by step.
    
    Time Complexity: O(n * seconds) - can be slow for large inputs
    Space Complexity: O(n)
    """
    n = len(nums)
    if len(set(nums)) == 1:
        return 0
    
    seconds = 0
    current = nums[:]
    
    while len(set(current)) > 1:
        seconds += 1
        new_array = current[:]
        
        for i in range(n):
            # Choose the most frequent value among current and neighbors
            candidates = [
                current[i],
                current[(i - 1) % n],
                current[(i + 1) % n]
            ]
            
            # Use the value that appears most in the neighborhood
            # For simplicity, use any neighbor value that's different
            for candidate in candidates:
                if candidate != current[i]:
                    new_array[i] = candidate
                    break
        
        current = new_array
        
        # Prevent infinite loop
        if seconds > n:
            break
    
    return seconds

# Test cases
def test_minimum_seconds_to_equalize():
    test_cases = [
        ([1, 2, 1, 2], 1),
        ([2, 1, 3, 3, 2], 2),
        ([5, 5, 5, 5], 0),
        ([1, 2, 3], 1),
        ([1], 0),
        ([1, 1, 2, 2], 1),
        ([1, 2, 3, 4, 5], 2),
        ([3, 1, 3, 1], 1)
    ]
    
    approaches = [
        ("BFS Simulation", minimum_seconds_to_equalize),
        ("Optimized Gap Analysis", minimum_seconds_to_equalize_optimized),
        ("DP Approach", minimum_seconds_to_equalize_dp),
        ("Greedy Interval", minimum_seconds_to_equalize_greedy)
    ]
    
    for approach_name, func in approaches:
        print(f"Testing {approach_name} approach:")
        all_passed = True
        
        for nums, expected in test_cases:
            try:
                result = func(nums[:])  # Pass copy to avoid modification
                passed = result == expected
                if not passed:
                    all_passed = False
                
                print(f"  Input: {nums}")
                print(f"  Expected: {expected}, Got: {result}")
                print(f"  {'✓' if passed else '✗'}")
            except Exception as e:
                print(f"  Input: {nums}")
                print(f"  Error: {e}")
                print(f"  ✗")
                all_passed = False
        
        print(f"  Overall: {'✓ All Passed' if all_passed else '✗ Some Failed'}\n")

if __name__ == "__main__":
    test_minimum_seconds_to_equalize()

"""
Topics: Arrays, BFS, Greedy, Mathematical Analysis
Difficulty: Medium

Key Insights:
1. Each unique value can potentially become the final value
2. The key is finding maximum gap between consecutive occurrences
3. Time needed = ceil(max_gap / 2) for each value
4. BFS simulation provides exact but slower solution
5. Mathematical analysis gives O(n) solution

Companies: Google, Microsoft, Amazon, Meta
"""
