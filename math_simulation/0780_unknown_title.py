"""
LeetCode Problem #780: Reaching Points

Problem Statement:
A point (x, y) can move to (x + y, y) or (x, x + y) in one step. Initially, you start at the point (sx, sy). 
Given a target point (tx, ty), return True if you can reach the target point (tx, ty) starting from (sx, sy), 
otherwise return False.

Constraints:
- 1 <= sx, sy, tx, ty <= 10^9
"""

def reachingPoints(sx: int, sy: int, tx: int, ty: int) -> bool:
    """
    Determines if the point (sx, sy) can reach (tx, ty) using the allowed moves.
    """
    while tx > sx and ty > sy:
        if tx > ty:
            tx %= ty
        else:
            ty %= tx

    if tx == sx and ty >= sy and (ty - sy) % sx == 0:
        return True
    if ty == sy and tx >= sx and (tx - sx) % sy == 0:
        return True

    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    sx, sy, tx, ty = 1, 1, 3, 5
    print(reachingPoints(sx, sy, tx, ty))  # Expected: True

    # Test Case 2
    sx, sy, tx, ty = 1, 1, 2, 2
    print(reachingPoints(sx, sy, tx, ty))  # Expected: False

    # Test Case 3
    sx, sy, tx, ty = 1, 1, 1, 1
    print(reachingPoints(sx, sy, tx, ty))  # Expected: True

    # Test Case 4
    sx, sy, tx, ty = 1, 1, 9, 5
    print(reachingPoints(sx, sy, tx, ty))  # Expected: True

    # Test Case 5
    sx, sy, tx, ty = 35, 13, 455, 118
    print(reachingPoints(sx, sy, tx, ty))  # Expected: True

"""
Time Complexity:
- The algorithm works by reducing the larger of tx or ty modulo the smaller value until one of them matches sx or sy.
- In the worst case, the number of modulo operations is proportional to log(max(tx, ty)).
- Therefore, the time complexity is O(log(max(tx, ty))).

Space Complexity:
- The algorithm uses a constant amount of space, so the space complexity is O(1).

Topic: Math, Simulation
"""