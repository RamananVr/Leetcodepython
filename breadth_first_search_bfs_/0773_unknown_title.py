"""
LeetCode Problem #773: Sliding Puzzle

Problem Statement:
On a 2x3 board, there are 5 tiles labeled from 1 to 5, and an empty square represented by 0. 
A move consists of swapping the empty square with one of its 4 neighboring tiles (if the neighbor exists).

The board is solved when the tiles are arranged in the order: [[1, 2, 3], [4, 5, 0]].

Given the puzzle board as a 2D list of integers `board`, return the minimum number of moves required to solve the puzzle. 
If it is impossible to solve the puzzle, return -1.

Example:
Input: board = [[1, 2, 3], [4, 0, 5]]
Output: 1
Explanation: Swap the 0 and 5 in one move.

Constraints:
- `board` is a 2x3 list of integers.
- Each integer is in the range [0, 5], and there are no duplicate integers.
"""

from collections import deque

def slidingPuzzle(board):
    """
    Solves the sliding puzzle problem using BFS.

    :param board: List[List[int]] - 2x3 board representing the initial state of the puzzle
    :return: int - Minimum number of moves to solve the puzzle, or -1 if impossible
    """
    # Convert the board into a string for easier manipulation
    start = ''.join(str(num) for row in board for num in row)
    target = "123450"  # Target configuration

    # Define the neighbors for each position in the 1D representation of the board
    neighbors = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4],
        4: [1, 3, 5],
        5: [2, 4]
    }

    # BFS setup
    queue = deque([(start, start.index('0'), 0)])  # (current state, index of '0', moves)
    visited = set()
    visited.add(start)

    while queue:
        current, zero_idx, moves = queue.popleft()

        # Check if the current state is the target
        if current == target:
            return moves

        # Explore all possible moves
        for neighbor in neighbors[zero_idx]:
            # Swap the '0' with the neighbor
            new_state = list(current)
            new_state[zero_idx], new_state[neighbor] = new_state[neighbor], new_state[zero_idx]
            new_state_str = ''.join(new_state)

            # If the new state hasn't been visited, add it to the queue
            if new_state_str not in visited:
                visited.add(new_state_str)
                queue.append((new_state_str, neighbor, moves + 1))

    # If we exhaust the queue without finding the target, return -1
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    board1 = [[1, 2, 3], [4, 0, 5]]
    print(slidingPuzzle(board1))  # Output: 1

    # Test Case 2
    board2 = [[1, 2, 3], [5, 4, 0]]
    print(slidingPuzzle(board2))  # Output: -1

    # Test Case 3
    board3 = [[4, 1, 2], [5, 0, 3]]
    print(slidingPuzzle(board3))  # Output: 5

    # Test Case 4
    board4 = [[1, 2, 3], [4, 5, 0]]
    print(slidingPuzzle(board4))  # Output: 0

"""
Time Complexity Analysis:
- The total number of possible states for a 2x3 board is 6! = 720.
- In the worst case, we may need to explore all states, and for each state, we perform O(1) operations (swapping and checking neighbors).
- Therefore, the time complexity is O(720) = O(1) (constant in practical terms).

Space Complexity Analysis:
- We use a queue to store the states and a set to track visited states. Both can grow up to O(720) in size.
- Therefore, the space complexity is O(720) = O(1) (constant in practical terms).

Topic: Breadth-First Search (BFS)
"""