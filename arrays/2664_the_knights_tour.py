"""
LeetCode Question #2664: The Knight's Tour

Problem Statement:
Given two positive integers m and n, and two non-negative integers startRow and startCol, return a matrix representing a valid knight's tour on an m x n chessboard starting from position (startRow, startCol).

A knight's tour is a sequence of moves where a knight visits every square on the chessboard exactly once.

The knight moves in an L-shape: 2 squares in one direction and 1 square in the perpendicular direction, or 1 square in one direction and 2 squares in the perpendicular direction.

Return the tour as a matrix where tour[i][j] represents the step number when the knight first visits square (i, j). The starting square should be marked as 0.

Examples:
Example 1:
Input: m = 3, n = 4, startRow = 0, startCol = 0
Output: [[0,3,6,9],[11,8,1,4],[2,5,10,7]]
Explanation: One possible knight's tour starting from (0,0).

Example 2:
Input: m = 1, n = 1, startRow = 0, startCol = 0
Output: [[0]]
Explanation: The knight starts and ends at the only square.

Constraints:
- 1 <= m, n <= 5
- 0 <= startRow < m
- 0 <= startCol < n
"""

from typing import List

def tourOfKnight(m: int, n: int, startRow: int, startCol: int) -> List[List[int]]:
    """
    Find a valid knight's tour using backtracking.
    
    Strategy: Use backtracking with Warnsdorff's heuristic for efficiency.
    Warnsdorff's rule: Always move to the square from which the knight 
    will have the fewest onward moves.
    """
    # Knight move directions
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), 
             (1, -2), (1, 2), (2, -1), (2, 1)]
    
    # Initialize board
    board = [[-1] * n for _ in range(m)]
    board[startRow][startCol] = 0
    
    def is_valid(x, y):
        """Check if position (x, y) is valid and unvisited."""
        return 0 <= x < m and 0 <= y < n and board[x][y] == -1
    
    def get_degree(x, y):
        """Get the number of valid moves from position (x, y)."""
        count = 0
        for dx, dy in moves:
            if is_valid(x + dx, y + dy):
                count += 1
        return count
    
    def backtrack(x, y, step):
        """Backtracking function to find knight's tour."""
        if step == m * n:
            return True
        
        # Get all valid next moves
        next_moves = []
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                degree = get_degree(nx, ny)
                next_moves.append((degree, nx, ny))
        
        # Sort by Warnsdorff's rule (fewest onward moves first)
        next_moves.sort()
        
        # Try each move
        for _, nx, ny in next_moves:
            board[nx][ny] = step
            if backtrack(nx, ny, step + 1):
                return True
            board[nx][ny] = -1  # backtrack
        
        return False
    
    # Start the tour
    if backtrack(startRow, startCol, 1):
        return board
    else:
        # Should not happen with given constraints
        return [[-1] * n for _ in range(m)]

def tourOfKnightSimple(m: int, n: int, startRow: int, startCol: int) -> List[List[int]]:
    """
    Simple backtracking without Warnsdorff's heuristic.
    """
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), 
             (1, -2), (1, 2), (2, -1), (2, 1)]
    
    board = [[-1] * n for _ in range(m)]
    board[startRow][startCol] = 0
    
    def is_safe(x, y):
        return 0 <= x < m and 0 <= y < n and board[x][y] == -1
    
    def solve(x, y, step):
        if step == m * n:
            return True
        
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_safe(nx, ny):
                board[nx][ny] = step
                if solve(nx, ny, step + 1):
                    return True
                board[nx][ny] = -1
        
        return False
    
    solve(startRow, startCol, 1)
    return board

def tourOfKnightIterative(m: int, n: int, startRow: int, startCol: int) -> List[List[int]]:
    """
    Iterative approach using stack.
    """
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), 
             (1, -2), (1, 2), (2, -1), (2, 1)]
    
    board = [[-1] * n for _ in range(m)]
    board[startRow][startCol] = 0
    
    def is_valid(x, y):
        return 0 <= x < m and 0 <= y < n and board[x][y] == -1
    
    stack = [(startRow, startCol, 1)]
    
    while stack:
        x, y, step = stack.pop()
        
        if step == m * n:
            return board
        
        # Find next valid moves
        found_move = False
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                board[nx][ny] = step
                stack.append((nx, ny, step + 1))
                found_move = True
                break
        
        if not found_move and step < m * n:
            # Backtrack: find the cell with current step-1 and reset cells with step >= current step
            for i in range(m):
                for j in range(n):
                    if board[i][j] >= step:
                        board[i][j] = -1
    
    return board

def tourOfKnightOptimized(m: int, n: int, startRow: int, startCol: int) -> List[List[int]]:
    """
    Optimized version with better heuristics.
    """
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), 
             (1, -2), (1, 2), (2, -1), (2, 1)]
    
    board = [[-1] * n for _ in range(m)]
    
    def is_valid(x, y):
        return 0 <= x < m and 0 <= y < n and board[x][y] == -1
    
    def count_onward_moves(x, y):
        """Count valid moves from position (x, y)."""
        count = 0
        for dx, dy in moves:
            if is_valid(x + dx, y + dy):
                count += 1
        return count
    
    def solve():
        """Solve using Warnsdorff's rule."""
        path = [(startRow, startCol)]
        board[startRow][startCol] = 0
        
        for step in range(1, m * n):
            curr_x, curr_y = path[-1]
            next_moves = []
            
            # Collect all possible moves with their accessibility
            for dx, dy in moves:
                next_x, next_y = curr_x + dx, curr_y + dy
                if is_valid(next_x, next_y):
                    accessibility = count_onward_moves(next_x, next_y)
                    next_moves.append((accessibility, next_x, next_y))
            
            if not next_moves:
                # Dead end, need to backtrack
                return False
            
            # Choose move with minimum accessibility (Warnsdorff's rule)
            next_moves.sort()
            _, next_x, next_y = next_moves[0]
            
            board[next_x][next_y] = step
            path.append((next_x, next_y))
        
        return True
    
    if solve():
        return board
    else:
        # Fallback to simple backtracking
        return tourOfKnightSimple(m, n, startRow, startCol)

# Test Cases
if __name__ == "__main__":
    test_cases = [
        (3, 4, 0, 0),
        (1, 1, 0, 0),
        (2, 2, 0, 0),
        (3, 3, 0, 0),
        (4, 4, 0, 0),
        (5, 5, 2, 2)
    ]
    
    def validate_tour(board, m, n, start_row, start_col):
        """Validate if the tour is correct."""
        if board[start_row][start_col] != 0:
            return False
        
        # Check if all cells are visited exactly once
        visited = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] < 0 or board[i][j] >= m * n:
                    return False
                if board[i][j] in visited:
                    return False
                visited.add(board[i][j])
        
        if len(visited) != m * n:
            return False
        
        # Check knight moves
        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), 
                 (1, -2), (1, 2), (2, -1), (2, 1)]
        
        for step in range(m * n - 1):
            # Find current and next positions
            curr_pos = next_pos = None
            for i in range(m):
                for j in range(n):
                    if board[i][j] == step:
                        curr_pos = (i, j)
                    if board[i][j] == step + 1:
                        next_pos = (i, j)
            
            if not curr_pos or not next_pos:
                return False
            
            # Check if move is valid knight move
            dx = next_pos[0] - curr_pos[0]
            dy = next_pos[1] - curr_pos[1]
            if (dx, dy) not in moves:
                return False
        
        return True
    
    print("Testing main approach:")
    for m, n, startRow, startCol in test_cases:
        result = tourOfKnight(m, n, startRow, startCol)
        is_valid = validate_tour(result, m, n, startRow, startCol)
        print(f"tourOfKnight({m}, {n}, {startRow}, {startCol}) = Valid tour: {'✓' if is_valid else '✗'}")
        if m <= 3 and n <= 3:  # Print small boards
            for row in result:
                print(f"  {row}")
    
    print("\nTesting simple approach:")
    for m, n, startRow, startCol in test_cases[:4]:  # Test smaller cases
        result = tourOfKnightSimple(m, n, startRow, startCol)
        is_valid = validate_tour(result, m, n, startRow, startCol)
        print(f"tourOfKnightSimple({m}, {n}, {startRow}, {startCol}) = Valid tour: {'✓' if is_valid else '✗'}")

"""
Time and Space Complexity Analysis:

Main Approach (with Warnsdorff's heuristic):
Time Complexity: O(8^(m*n)) in worst case, but much better in practice
- Warnsdorff's heuristic significantly reduces the search space
- For small boards (m,n ≤ 5), runs quickly
Space Complexity: O(m*n) - for the board and recursion stack

Simple Backtracking:
Time Complexity: O(8^(m*n)) - explores all possible knight moves
Space Complexity: O(m*n) - for the board and recursion stack

Optimized Approach:
Time Complexity: O(m*n * 8^2) for Warnsdorff's rule calculation per step
Space Complexity: O(m*n) - for the board

Key Insights:
1. Knight's tour is a classic backtracking problem
2. Warnsdorff's rule greatly improves performance: always move to square with fewest onward moves
3. For small boards, simple backtracking often works
4. The problem guarantees a solution exists for given constraints

Knight Move Pattern:
- 8 possible moves in L-shape
- Move 2 squares in one direction, 1 in perpendicular
- Need to check bounds and avoid visited squares

Topic: Backtracking, Graph Traversal, Heuristic Search, Chess Problems
"""
