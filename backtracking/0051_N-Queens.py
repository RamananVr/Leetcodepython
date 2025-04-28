"""
LeetCode Problem #51: N-Queens

Problem Statement:
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example:
Input: n = 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

Constraints:
- 1 <= n <= 9
"""

def solveNQueens(n: int):
    def backtrack(row, diagonals, anti_diagonals, cols, board):
        # If we've placed queens in all rows, add the solution
        if row == n:
            result.append(["".join(r) for r in board])
            return
        
        for col in range(n):
            curr_diag = row - col
            curr_anti_diag = row + col
            
            # Check if the current position is under attack
            if col in cols or curr_diag in diagonals or curr_anti_diag in anti_diagonals:
                continue
            
            # Place the queen
            board[row][col] = 'Q'
            cols.add(col)
            diagonals.add(curr_diag)
            anti_diagonals.add(curr_anti_diag)
            
            # Recurse to the next row
            backtrack(row + 1, diagonals, anti_diagonals, cols, board)
            
            # Backtrack: remove the queen
            board[row][col] = '.'
            cols.remove(col)
            diagonals.remove(curr_diag)
            anti_diagonals.remove(curr_anti_diag)
    
    result = []
    empty_board = [["."] * n for _ in range(n)]
    backtrack(0, set(), set(), set(), empty_board)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 4
    print("Solutions for n = 4:")
    solutions = solveNQueens(n)
    for solution in solutions:
        for row in solution:
            print(row)
        print()
    
    # Test Case 2
    n = 1
    print("Solutions for n = 1:")
    solutions = solveNQueens(n)
    for solution in solutions:
        for row in solution:
            print(row)
        print()

"""
Time Complexity Analysis:
- The time complexity of the N-Queens problem is O(N!), where N is the size of the board. This is because there are N choices for the first row, N-1 choices for the second row, N-2 for the third, and so on, leading to N! permutations in the worst case.

Space Complexity Analysis:
- The space complexity is O(N^2) for the board representation and O(N) for the sets used to track columns, diagonals, and anti-diagonals. Thus, the overall space complexity is O(N^2).

Topic: Backtracking
"""