"""
LeetCode Question #52: N-Queens II

Problem Statement:
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below:
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

Constraints:
- 1 <= n <= 9
"""

def totalNQueens(n: int) -> int:
    def backtrack(row: int, cols: set, diagonals1: set, diagonals2: set) -> int:
        # If all rows are filled, we found a valid solution
        if row == n:
            return 1
        
        solutions = 0
        for col in range(n):
            diag1 = row - col
            diag2 = row + col
            # Check if the current position is under attack
            if col in cols or diag1 in diagonals1 or diag2 in diagonals2:
                continue
            
            # Place the queen and mark the attack zones
            cols.add(col)
            diagonals1.add(diag1)
            diagonals2.add(diag2)
            
            # Recurse to the next row
            solutions += backtrack(row + 1, cols, diagonals1, diagonals2)
            
            # Backtrack: remove the queen and unmark the attack zones
            cols.remove(col)
            diagonals1.remove(diag1)
            diagonals2.remove(diag2)
        
        return solutions
    
    return backtrack(0, set(), set(), set())

# Example Test Cases
if __name__ == "__main__":
    print(totalNQueens(4))  # Output: 2
    print(totalNQueens(1))  # Output: 1
    print(totalNQueens(8))  # Output: 92

"""
Time Complexity:
- The time complexity is O(N!), where N is the size of the board. This is because for the first row, we have N choices, for the second row, we have N-1 choices, and so on.

Space Complexity:
- The space complexity is O(N) due to the recursion stack and the sets used to track columns and diagonals.

Topic: Backtracking
"""