"""
LeetCode Problem #2849: Determine if a Cell is Reachable at a Given Time

Problem Statement:
You are given four integers `sx`, `sy`, `fx`, `fy`, and an integer `t`. 
- `(sx, sy)` represents the starting position of a cell in a 2D grid.
- `(fx, fy)` represents the final position of a cell in the same grid.
- `t` represents the maximum time you are allowed to move.

You can move one cell in one of the four cardinal directions (up, down, left, right) in one unit of time.

Return `True` if you can reach the final position `(fx, fy)` from the starting position `(sx, sy)` within `t` units of time. Otherwise, return `False`.

Constraints:
- `0 <= sx, sy, fx, fy <= 10^9`
- `1 <= t <= 10^9`
"""

def is_reachable_at_time(sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
    """
    Determines if the final position (fx, fy) is reachable from the starting position (sx, sy)
    within t units of time.

    Args:
    - sx (int): Starting x-coordinate.
    - sy (int): Starting y-coordinate.
    - fx (int): Final x-coordinate.
    - fy (int): Final y-coordinate.
    - t (int): Maximum time allowed.

    Returns:
    - bool: True if reachable within t time, False otherwise.
    """
    # Calculate the Manhattan distance between the start and final positions
    manhattan_distance = abs(fx - sx) + abs(fy - sy)
    
    # Check if the Manhattan distance is less than or equal to t
    # and if the difference between t and the distance is even (to ensure parity)
    return manhattan_distance <= t and (t - manhattan_distance) % 2 == 0


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Reachable within time
    sx, sy, fx, fy, t = 0, 0, 2, 2, 4
    print(is_reachable_at_time(sx, sy, fx, fy, t))  # Expected: True

    # Test Case 2: Not enough time to reach
    sx, sy, fx, fy, t = 0, 0, 3, 3, 4
    print(is_reachable_at_time(sx, sy, fx, fy, t))  # Expected: False

    # Test Case 3: Exact time to reach
    sx, sy, fx, fy, t = 1, 1, 3, 3, 4
    print(is_reachable_at_time(sx, sy, fx, fy, t))  # Expected: True

    # Test Case 4: Parity mismatch
    sx, sy, fx, fy, t = 0, 0, 1, 1, 2
    print(is_reachable_at_time(sx, sy, fx, fy, t))  # Expected: False

    # Test Case 5: Same start and end position
    sx, sy, fx, fy, t = 5, 5, 5, 5, 1
    print(is_reachable_at_time(sx, sy, fx, fy, t))  # Expected: True


"""
Time Complexity:
- Calculating the Manhattan distance takes O(1) time.
- The final condition check is also O(1).
- Overall, the time complexity is O(1).

Space Complexity:
- The solution uses a constant amount of space, so the space complexity is O(1).

Topic: Math, Grid, Simulation
"""