"""
LeetCode Problem #276: Paint Fence

Problem Statement:
You are painting a fence with `n` posts. There are `k` different colors available, and you must paint the fence 
such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Constraints:
- 1 <= n <= 50
- 1 <= k <= 50
"""

def numWays(n: int, k: int) -> int:
    """
    Calculate the number of ways to paint the fence such that no more than two adjacent posts have the same color.

    :param n: Number of fence posts
    :param k: Number of available colors
    :return: Total number of ways to paint the fence
    """
    if n == 0:
        return 0
    if n == 1:
        return k
    
    # Initialize the number of ways to paint the first two posts
    same = k  # Ways to paint the first two posts with the same color
    diff = k * (k - 1)  # Ways to paint the first two posts with different colors
    
    for i in range(3, n + 1):
        # Calculate the number of ways to paint the current post
        new_same = diff  # Current post can only be the same as the previous one if the previous two are different
        new_diff = (same + diff) * (k - 1)  # Current post can be different from the previous one
        
        # Update same and diff for the next iteration
        same = new_same
        diff = new_diff
    
    # Total ways to paint the fence
    return same + diff

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Small number of posts and colors
    n1, k1 = 3, 2
    print(f"numWays({n1}, {k1}) = {numWays(n1, k1)}")  # Expected output: 6

    # Test Case 2: Single post
    n2, k2 = 1, 3
    print(f"numWays({n2}, {k2}) = {numWays(n2, k2)}")  # Expected output: 3

    # Test Case 3: Two posts
    n3, k3 = 2, 4
    print(f"numWays({n3}, {k3}) = {numWays(n3, k3)}")  # Expected output: 16

    # Test Case 4: Larger number of posts and colors
    n4, k4 = 5, 3
    print(f"numWays({n4}, {k4}) = {numWays(n4, k4)}")  # Expected output: 180

    # Test Case 5: Edge case with no posts
    n5, k5 = 0, 5
    print(f"numWays({n5}, {k5}) = {numWays(n5, k5)}")  # Expected output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the range from 3 to n, performing constant-time calculations for each iteration.
- Therefore, the time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of space to store variables (`same`, `diff`, `new_same`, `new_diff`).
- Therefore, the space complexity is O(1).

Topic: Dynamic Programming (DP)
"""