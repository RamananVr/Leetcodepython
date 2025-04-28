"""
LeetCode Problem #1066: Campus Bikes II

Problem Statement:
On a campus represented as a 2D grid, there are `n` workers and `m` bikes, with `n <= m`. You are given an array `workers` of length `n`, where `workers[i] = [xi, yi]` is the position of the i-th worker. You are also given an array `bikes` of length `m`, where `bikes[j] = [xj, yj]` is the position of the j-th bike.

We assign one unique bike to each worker so that the sum of the Manhattan distances between each worker and their assigned bike is minimized.

The Manhattan distance between two points `(p1, q1)` and `(p2, q2)` is `|p1 - p2| + |q1 - q2|`.

Return the minimum possible sum of Manhattan distances between workers and bikes.

Constraints:
- `n == workers.length`
- `m == bikes.length`
- `1 <= n <= 10`
- `n <= m <= 40`
- `workers[i].length == 2`
- `bikes[j].length == 2`
- `0 <= workers[i][0], workers[i][1], bikes[j][0], bikes[j][1] < 1000`
- All worker positions are distinct.
- All bike positions are distinct.

"""

from functools import lru_cache

def assignBikes(workers, bikes):
    """
    Function to find the minimum sum of Manhattan distances between workers and bikes.
    Uses bitmasking and dynamic programming to solve the problem efficiently.
    """
    @lru_cache(None)
    def dfs(worker_idx, bike_mask):
        # Base case: If all workers are assigned, return 0
        if worker_idx == len(workers):
            return 0
        
        min_distance = float('inf')
        for bike_idx in range(len(bikes)):
            # If the bike is not yet assigned
            if not (bike_mask & (1 << bike_idx)):
                # Calculate Manhattan distance
                distance = abs(workers[worker_idx][0] - bikes[bike_idx][0]) + abs(workers[worker_idx][1] - bikes[bike_idx][1])
                # Recur for the next worker with the current bike assigned
                min_distance = min(min_distance, distance + dfs(worker_idx + 1, bike_mask | (1 << bike_idx)))
        
        return min_distance
    
    # Start DFS with the first worker and no bikes assigned
    return dfs(0, 0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    workers1 = [[0, 0], [2, 1]]
    bikes1 = [[1, 2], [3, 3]]
    print(assignBikes(workers1, bikes1))  # Expected Output: 6

    # Test Case 2
    workers2 = [[0, 0], [1, 1], [2, 0]]
    bikes2 = [[1, 0], [2, 2], [2, 1]]
    print(assignBikes(workers2, bikes2))  # Expected Output: 4

    # Test Case 3
    workers3 = [[0, 0]]
    bikes3 = [[1, 1], [2, 2]]
    print(assignBikes(workers3, bikes3))  # Expected Output: 2

"""
Time Complexity:
- There are `n` workers and `m` bikes. For each worker, we try all unassigned bikes.
- The number of states in the DP is `O(n * 2^m)` because there are `n` workers and `2^m` possible bike assignments.
- For each state, we iterate over `m` bikes, leading to a total complexity of `O(n * m * 2^m)`.

Space Complexity:
- The space complexity is determined by the size of the memoization cache, which is `O(n * 2^m)`.
- Additionally, the recursion stack can go up to `O(n)` depth.

Primary Topic: Dynamic Programming (DP) with Bitmasking
"""