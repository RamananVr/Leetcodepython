"""
LeetCode Problem #1654: Minimum Jumps to Reach Home

Problem Statement:
A certain bug's home is on the x-axis at position `x`. The bug starts at position `0` and wants to get to position `x`. 
The bug can jump either forward or backward:
- A forward jump consists of moving from position `pos` to `pos + a`.
- A backward jump consists of moving from position `pos` to `pos - b`.

However, the bug cannot jump backward twice in a row. Additionally, there are some forbidden positions on the x-axis 
that the bug cannot land on.

Given an integer array `forbidden`, integers `a`, `b`, and `x`, return the minimum number of jumps needed for the bug 
to reach its home. If there is no possible way to reach the home, return `-1`.

Constraints:
- `1 <= forbidden.length <= 1000`
- `1 <= a, b, x <= 2000`
- `0 <= forbidden[i] <= 2000`
- All the elements in `forbidden` are distinct.
- Position `x` is not forbidden.

Example:
Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
Output: 3
Explanation: 3 jumps are needed (0 -> 3 -> 6 -> 9).

Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
Output: -1

Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
Output: 2
Explanation: 2 jumps are needed (0 -> 16 -> 7).
"""

from collections import deque

def minimumJumps(forbidden, a, b, x):
    # Define the maximum boundary to avoid infinite loops
    max_limit = max(x + b, max(forbidden) + a + b)
    forbidden_set = set(forbidden)
    
    # BFS queue: (current_position, jumps, can_jump_back)
    queue = deque([(0, 0, True)])
    visited = set([(0, True)])  # (position, can_jump_back)

    while queue:
        position, jumps, can_jump_back = queue.popleft()

        # If we reach the target position, return the number of jumps
        if position == x:
            return jumps

        # Forward jump
        forward = position + a
        if forward <= max_limit and forward not in forbidden_set and (forward, True) not in visited:
            visited.add((forward, True))
            queue.append((forward, jumps + 1, True))

        # Backward jump (only if allowed)
        backward = position - b
        if can_jump_back and backward >= 0 and backward not in forbidden_set and (backward, False) not in visited:
            visited.add((backward, False))
            queue.append((backward, jumps + 1, False))

    # If we exhaust the queue without finding the target, return -1
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    forbidden = [14, 4, 18, 1, 15]
    a = 3
    b = 15
    x = 9
    print(minimumJumps(forbidden, a, b, x))  # Output: 3

    # Test Case 2
    forbidden = [8, 3, 16, 6, 12, 20]
    a = 15
    b = 13
    x = 11
    print(minimumJumps(forbidden, a, b, x))  # Output: -1

    # Test Case 3
    forbidden = [1, 6, 2, 14, 5, 17, 4]
    a = 16
    b = 9
    x = 7
    print(minimumJumps(forbidden, a, b, x))  # Output: 2

"""
Time Complexity:
- Let `F` be the size of the `forbidden` array, and `L` be the maximum position we consider (`max_limit`).
- In the worst case, we explore all positions up to `max_limit` with both forward and backward jumps.
- Each position is visited at most twice (once with `can_jump_back=True` and once with `can_jump_back=False`).
- Thus, the time complexity is O(L + F).

Space Complexity:
- The space complexity is O(L + F) due to the `visited` set, `forbidden_set`, and the BFS queue.

Topic: Breadth-First Search (BFS)
"""