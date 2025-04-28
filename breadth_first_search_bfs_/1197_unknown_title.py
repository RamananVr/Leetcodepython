"""
LeetCode Problem #1197: Minimum Knight Moves

Problem Statement:
In an infinite chessboard with coordinates from (-infinity, -infinity) to (infinity, infinity), 
you have a knight at the coordinate (0, 0). A knight has 8 possible moves it can make, as follows:
    - (2, 1), (2, -1), (-2, 1), (-2, -1)
    - (1, 2), (1, -2), (-1, 2), (-1, -2)

Return the minimum number of steps needed to move the knight to the coordinate (x, y). 
It is guaranteed that the answer exists.

Constraints:
- |x| + |y| <= 300
"""

from collections import deque

def minKnightMoves(x: int, y: int) -> int:
    """
    Returns the minimum number of steps required for a knight to move from (0, 0) to (x, y).
    """
    # Normalize the target coordinates to the first quadrant
    x, y = abs(x), abs(y)
    
    # Possible moves for a knight
    directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    # BFS initialization
    queue = deque([(0, 0, 0)])  # (current_x, current_y, steps)
    visited = set()
    visited.add((0, 0))
    
    while queue:
        curr_x, curr_y, steps = queue.popleft()
        
        # If we reach the target, return the number of steps
        if curr_x == x and curr_y == y:
            return steps
        
        # Explore all possible moves
        for dx, dy in directions:
            next_x, next_y = curr_x + dx, curr_y + dy
            
            # Only consider positions in the first quadrant and avoid revisiting
            if (next_x, next_y) not in visited and next_x >= -2 and next_y >= -2:
                visited.add((next_x, next_y))
                queue.append((next_x, next_y, steps + 1))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Target is (2, 1)
    print(minKnightMoves(2, 1))  # Expected Output: 1
    
    # Test Case 2: Target is (5, 5)
    print(minKnightMoves(5, 5))  # Expected Output: 4
    
    # Test Case 3: Target is (0, 0)
    print(minKnightMoves(0, 0))  # Expected Output: 0
    
    # Test Case 4: Target is (-1, -1)
    print(minKnightMoves(-1, -1))  # Expected Output: 2
    
    # Test Case 5: Target is (300, 300)
    print(minKnightMoves(300, 300))  # Expected Output: 212

"""
Time and Space Complexity Analysis:

Time Complexity:
- The BFS explores all reachable positions until it finds the target. 
- Since the problem guarantees that |x| + |y| <= 300, the search space is limited to a bounded region.
- Each position has at most 8 neighbors, so the complexity is approximately O(|x| * |y|).

Space Complexity:
- The space complexity is determined by the size of the `visited` set and the `queue`.
- Both are proportional to the number of reachable positions, which is O(|x| * |y|).

Topic: Breadth-First Search (BFS)
"""