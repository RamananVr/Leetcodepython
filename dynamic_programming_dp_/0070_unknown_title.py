"""
LeetCode Problem #70: Climbing Stairs

Problem Statement:
You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Constraints:
- 1 <= n <= 45
"""

# Solution
def climbStairs(n: int) -> int:
    """
    This function calculates the number of distinct ways to climb a staircase with `n` steps,
    where you can take either 1 or 2 steps at a time.
    """
    if n <= 2:
        return n

    # Initialize variables to store the number of ways to reach the last two steps
    prev1, prev2 = 2, 1

    # Iterate from step 3 to n
    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Small input
    n = 2
    print(f"Number of ways to climb {n} steps: {climbStairs(n)}")  # Expected: 2

    # Test Case 2: Small input
    n = 3
    print(f"Number of ways to climb {n} steps: {climbStairs(n)}")  # Expected: 3

    # Test Case 3: Medium input
    n = 5
    print(f"Number of ways to climb {n} steps: {climbStairs(n)}")  # Expected: 8

    # Test Case 4: Large input
    n = 10
    print(f"Number of ways to climb {n} steps: {climbStairs(n)}")  # Expected: 89

    # Test Case 5: Edge case
    n = 1
    print(f"Number of ways to climb {n} steps: {climbStairs(n)}")  # Expected: 1

"""
Time Complexity:
- The solution iterates from 3 to n, so the time complexity is O(n).

Space Complexity:
- The solution uses only two variables (`prev1` and `prev2`) to store intermediate results, so the space complexity is O(1).

Topic: Dynamic Programming (DP)
"""