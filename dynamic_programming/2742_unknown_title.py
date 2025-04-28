"""
LeetCode Problem #2742: Painting the Walls

Problem Statement:
You are given two arrays, `cost` and `time`, of size `n` where:
- `cost[i]` is the cost of painting the i-th wall.
- `time[i]` is the time it takes to paint the i-th wall.

You can hire workers to paint the walls. Each worker can paint one wall at a time. If you hire a worker to paint the i-th wall, it will take `time[i]` hours and cost `cost[i]` dollars.

You can also choose to paint the walls yourself. If you paint the i-th wall yourself, it will take `time[i]` hours, but it will cost you nothing.

Your goal is to minimize the total cost of painting all the walls, while ensuring that the total time spent painting the walls does not exceed `n` hours.

Return the minimum cost to paint all the walls.

Constraints:
- `1 <= n <= 1000`
- `1 <= cost[i], time[i] <= 1000`
"""

# Solution
def paintWalls(cost, time):
    """
    Function to calculate the minimum cost to paint all the walls.

    Args:
    cost (List[int]): The cost of hiring workers for each wall.
    time (List[int]): The time required to paint each wall.

    Returns:
    int: The minimum cost to paint all the walls.
    """
    n = len(cost)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(n):
        for j in range(n, -1, -1):
            if j + time[i] + 1 <= n:
                dp[j + time[i] + 1] = min(dp[j + time[i] + 1], dp[j] + cost[i])

    return min(dp[n:])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    cost = [1, 2, 3]
    time = [1, 2, 3]
    print(paintWalls(cost, time))  # Expected Output: 1

    # Test Case 2
    cost = [10, 15, 20]
    time = [2, 3, 1]
    print(paintWalls(cost, time))  # Expected Output: 15

    # Test Case 3
    cost = [5, 10, 15]
    time = [3, 2, 1]
    print(paintWalls(cost, time))  # Expected Output: 10

    # Test Case 4
    cost = [1, 1, 1, 1]
    time = [1, 1, 1, 1]
    print(paintWalls(cost, time))  # Expected Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
The solution uses dynamic programming with a nested loop. The outer loop iterates over the walls (n iterations), 
and the inner loop iterates over the possible time states (n iterations). Therefore, the time complexity is O(n^2).

Space Complexity:
The solution uses a DP array of size n+1 to store the minimum cost for each time state. 
Thus, the space complexity is O(n).
"""

# Topic: Dynamic Programming