"""
LeetCode Problem #688: Knight Probability in Chessboard

Problem Statement:
On an `n x n` chessboard, a knight starts at the cell `(row, column)` and attempts to make exactly `k` moves. 
The rows and columns are 0-indexed, so the top-left cell is `(0, 0)`, and the bottom-right cell is `(n - 1, n - 1)`.

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, 
then one square in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the board) 
and moves there.

The knight continues moving until it has made exactly `k` moves or has moved off the chessboard. Return the probability that the knight 
remains on the board after it has stopped moving.

Constraints:
- `1 <= n <= 25`
- `0 <= k <= 100`
- `0 <= row, column <= n - 1`
"""

def knightProbability(n: int, k: int, row: int, column: int) -> float:
    # Directions the knight can move
    directions = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    
    # Memoization table to store probabilities
    memo = {}

    def dfs(remaining_moves, x, y):
        # If the knight is off the board, probability is 0
        if x < 0 or x >= n or y < 0 or y >= n:
            return 0
        # If no moves are left, the knight is on the board, probability is 1
        if remaining_moves == 0:
            return 1
        # If the result is already computed, return it
        if (remaining_moves, x, y) in memo:
            return memo[(remaining_moves, x, y)]
        
        # Calculate probability by exploring all 8 possible moves
        prob = 0
        for dx, dy in directions:
            prob += dfs(remaining_moves - 1, x + dx, y + dy) / 8
        
        # Store the result in memo and return
        memo[(remaining_moves, x, y)] = prob
        return prob

    # Start the DFS from the initial position
    return dfs(k, row, column)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    k = 2
    row = 0
    column = 0
    print(f"Test Case 1: {knightProbability(n, k, row, column)}")  # Expected Output: 0.0625

    # Test Case 2
    n = 8
    k = 30
    row = 6
    column = 4
    print(f"Test Case 2: {knightProbability(n, k, row, column)}")  # Expected Output: A small probability close to 0

    # Test Case 3
    n = 1
    k = 0
    row = 0
    column = 0
    print(f"Test Case 3: {knightProbability(n, k, row, column)}")  # Expected Output: 1.0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The number of states in the memoization table is O(k * n * n), where `k` is the number of moves and `n` is the size of the board.
- For each state, we iterate over 8 possible moves, so the total time complexity is O(k * n * n * 8) = O(k * n^2).

Space Complexity:
- The space complexity is determined by the size of the memoization table, which is O(k * n * n).
- Additionally, the recursion stack can go up to a depth of `k`, so the total space complexity is O(k * n^2).

Topic: Dynamic Programming (DP)
"""