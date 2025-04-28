"""
LeetCode Problem #1553: Minimum Number of Days to Eat N Oranges

Problem Statement:
There are n oranges in a kitchen. You decide to eat them over some number of days. 
In a single day, you can decide to eat one orange or half of the oranges (if the number of oranges is even) 
or one-third of the oranges (if the number of oranges is divisible by 3).

You want to eat all the oranges in the kitchen as quickly as possible. Return the minimum number of days.

Example 1:
Input: n = 10
Output: 4
Explanation: You have 10 oranges.
- Day 1: Eat 1/2 of the oranges, 10 -> 5.
- Day 2: Eat 1/2 of the oranges, 5 -> 2.
- Day 3: Eat 1 orange, 2 -> 1.
- Day 4: Eat the last orange, 1 -> 0.

Example 2:
Input: n = 6
Output: 3
Explanation: You have 6 oranges.
- Day 1: Eat 1/2 of the oranges, 6 -> 3.
- Day 2: Eat 1/3 of the oranges, 3 -> 1.
- Day 3: Eat the last orange, 1 -> 0.

Example 3:
Input: n = 1
Output: 1

Constraints:
- 1 <= n <= 2 * 10^9
"""

# Solution
from functools import lru_cache

def minDays(n: int) -> int:
    @lru_cache(None)
    def dfs(oranges):
        if oranges == 0:
            return 0
        if oranges == 1:
            return 1
        # Option 1: Eat 1 orange and recurse on the remaining oranges
        eat_one = 1 + dfs(oranges - 1)
        # Option 2: Eat half the oranges (if divisible by 2) and recurse
        eat_half = 1 + dfs(oranges // 2) + (oranges % 2)
        # Option 3: Eat one-third of the oranges (if divisible by 3) and recurse
        eat_third = 1 + dfs(oranges // 3) + (oranges % 3)
        # Return the minimum of all options
        return min(eat_one, eat_half, eat_third)
    
    return dfs(n)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 10
    print(f"Input: {n1}, Output: {minDays(n1)}")  # Expected Output: 4

    # Test Case 2
    n2 = 6
    print(f"Input: {n2}, Output: {minDays(n2)}")  # Expected Output: 3

    # Test Case 3
    n3 = 1
    print(f"Input: {n3}, Output: {minDays(n3)}")  # Expected Output: 1

    # Test Case 4
    n4 = 56
    print(f"Input: {n4}, Output: {minDays(n4)}")  # Expected Output: 6

    # Test Case 5
    n5 = 100
    print(f"Input: {n5}, Output: {minDays(n5)}")  # Expected Output: 9

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function uses memoization to store results for subproblems. 
- The number of unique states is proportional to the number of integers from 1 to n. 
- Each state is computed in constant time due to memoization.
- Therefore, the time complexity is O(n).

Space Complexity:
- The space complexity is determined by the recursion stack and the memoization table.
- The recursion stack can go as deep as O(log(n)) due to the division operations.
- The memoization table stores results for up to n states, so it uses O(n) space.
- Overall space complexity: O(n).
"""

# Topic: Dynamic Programming