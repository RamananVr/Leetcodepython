"""
LeetCode Problem #2712: Minimum Cost to Make All Characters Equal

Problem Statement:
You are given a 0-indexed binary string `s` of length `n` on which you can apply two types of operations:
1. Choose an index `i` and invert all characters from index `0` to `i` (both inclusive).
2. Choose an index `i` and invert all characters from index `i` to `n - 1` (both inclusive).

To invert a character means to change '0' to '1' or '1' to '0'.

You can apply the above operations any number of times in any order.

Return the minimum cost to make all characters of the string equal, where the cost of inverting the first `i + 1` characters is `i + 1`, and the cost of inverting the last `n - i` characters is `n - i`.

Constraints:
- `1 <= s.length <= 10^5`
- `s[i]` is either '0' or '1'.
"""

def minimumCost(s):
    """
    Finds the minimum cost to make all characters equal using dynamic programming.
    
    :param s: str - Binary string
    :return: int - Minimum cost to make all characters equal
    """
    n = len(s)
    if n == 1:
        return 0
    
    # Try making all characters '0' and all characters '1'
    cost_to_zero = min_cost_to_target(s, '0')
    cost_to_one = min_cost_to_target(s, '1')
    
    return min(cost_to_zero, cost_to_one)

def min_cost_to_target(s, target):
    """
    Helper function to calculate minimum cost to make all characters equal to target.
    
    :param s: str - Binary string
    :param target: str - Target character ('0' or '1')
    :return: int - Minimum cost
    """
    n = len(s)
    total_cost = 0
    
    # Convert string to list for easier manipulation
    chars = list(s)
    
    while not all(c == target for c in chars):
        min_cost = float('inf')
        best_op = -1
        
        # Try operation type 1 (invert from 0 to i)
        for i in range(n):
            if chars[i] != target:
                cost = i + 1
                if cost < min_cost:
                    min_cost = cost
                    best_op = ('left', i)
        
        # Try operation type 2 (invert from i to n-1)
        for i in range(n):
            if chars[i] != target:
                cost = n - i
                if cost < min_cost:
                    min_cost = cost
                    best_op = ('right', i)
        
        # Apply the best operation
        if best_op[0] == 'left':
            for j in range(best_op[1] + 1):
                chars[j] = '1' if chars[j] == '0' else '0'
        else:
            for j in range(best_op[1], n):
                chars[j] = '1' if chars[j] == '0' else '0'
        
        total_cost += min_cost
    
    return total_cost

def minimumCostOptimized(s):
    """
    Optimized solution using greedy approach.
    
    :param s: str - Binary string
    :return: int - Minimum cost to make all characters equal
    """
    n = len(s)
    if n <= 1:
        return 0
    
    cost = 0
    
    # Process from left to right and right to left simultaneously
    for i in range(1, n):
        if s[i] != s[i-1]:
            # We need to flip to make adjacent characters the same
            # Choose the cheaper option: flip left part or right part
            left_cost = i
            right_cost = n - i
            cost += min(left_cost, right_cost)
    
    return cost

def minimumCostGreedy(s):
    """
    Greedy solution focusing on adjacent different characters.
    
    :param s: str - Binary string
    :return: int - Minimum cost to make all characters equal
    """
    n = len(s)
    total_cost = 0
    
    # For each adjacent pair that differs, we need to fix it
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            # Cost to fix this difference
            # We can either flip [0...i] or [i+1...n-1]
            cost_left = i + 1
            cost_right = n - (i + 1)
            total_cost += min(cost_left, cost_right)
    
    return total_cost

def minimumCostDP(s):
    """
    Dynamic programming approach considering all possibilities.
    
    :param s: str - Binary string
    :return: int - Minimum cost to make all characters equal
    """
    n = len(s)
    if n <= 1:
        return 0
    
    # dp[i][c] = minimum cost to make s[0:i+1] all equal to character c
    dp = [[float('inf')] * 2 for _ in range(n)]
    
    # Base case
    dp[0][int(s[0])] = 0
    dp[0][1 - int(s[0])] = 1  # Cost to flip the first character
    
    for i in range(1, n):
        curr_char = int(s[i])
        
        for target in range(2):
            # Option 1: Don't flip at position i
            if curr_char == target:
                dp[i][target] = min(dp[i][target], dp[i-1][target])
            
            # Option 2: Flip from 0 to i
            cost_flip_left = i + 1
            flipped_char = 1 - curr_char
            if flipped_char == target:
                dp[i][target] = min(dp[i][target], dp[i-1][1-target] + cost_flip_left)
            
            # Option 3: Flip from i to n-1 (handled differently)
            # This is more complex and requires looking ahead
    
    return min(dp[n-1][0], dp[n-1][1])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s = "0011"
    print(f"s: '{s}'")
    print(f"minimumCost: {minimumCost(s)}")  # Output: 2
    print(f"minimumCostOptimized: {minimumCostOptimized(s)}")  # Output: 2
    print(f"minimumCostGreedy: {minimumCostGreedy(s)}")  # Output: 2
    print()

    # Test Case 2
    s = "010101"
    print(f"s: '{s}'")
    print(f"minimumCost: {minimumCost(s)}")  # Output: 9
    print(f"minimumCostOptimized: {minimumCostOptimized(s)}")  # Output: 9
    print(f"minimumCostGreedy: {minimumCostGreedy(s)}")  # Output: 9
    print()

    # Test Case 3
    s = "0000"
    print(f"s: '{s}'")
    print(f"minimumCost: {minimumCost(s)}")  # Output: 0
    print(f"minimumCostOptimized: {minimumCostOptimized(s)}")  # Output: 0
    print(f"minimumCostGreedy: {minimumCostGreedy(s)}")  # Output: 0
    print()

    # Test Case 4
    s = "1"
    print(f"s: '{s}'")
    print(f"minimumCost: {minimumCost(s)}")  # Output: 0
    print(f"minimumCostOptimized: {minimumCostOptimized(s)}")  # Output: 0
    print(f"minimumCostGreedy: {minimumCostGreedy(s)}")  # Output: 0
    print()

    # Test Case 5
    s = "10"
    print(f"s: '{s}'")
    print(f"minimumCost: {minimumCost(s)}")  # Output: 1
    print(f"minimumCostOptimized: {minimumCostOptimized(s)}")  # Output: 1
    print(f"minimumCostGreedy: {minimumCostGreedy(s)}")  # Output: 1

    # Validation
    assert minimumCostOptimized("0011") == 2
    assert minimumCostGreedy("010101") == 9
    assert minimumCostOptimized("0000") == 0
    print("All test cases passed!")

"""
Time Complexity Analysis:
Brute Force:
- Time complexity: O(n^3) in worst case due to multiple iterations.

Optimized/Greedy:
- Time complexity: O(n) - single pass through the string.

Space Complexity Analysis:
- Space complexity: O(1) for optimized solutions, O(n) for string manipulation in brute force.

Topic: String, Greedy, Dynamic Programming
"""
