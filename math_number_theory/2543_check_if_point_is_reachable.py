"""
LeetCode Question #2543: Check if Point Is Reachable

Problem Statement:
You are given two integers `x` and `y` representing the coordinates of a point on an infinite 2D grid. 
Initially, you are at the origin `(0, 0)`. You can move according to the following rules:

1. You can move to a point `(x + y, y)` or `(x, x + y)` from a point `(x, y)`.

Return `true` if you can reach the point `(x, y)` starting from the origin `(0, 0)`, and `false` otherwise.

Constraints:
- 1 <= x, y <= 10^9
"""

# Solution
def isReachable(x: int, y: int) -> bool:
    """
    Determines if the point (x, y) is reachable from the origin (0, 0) using the given movement rules.
    """
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    # The point is reachable if the greatest common divisor (GCD) of x and y is a power of 2.
    return (gcd(x, y) & (gcd(x, y) - 1)) == 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Reachable point
    x1, y1 = 6, 10
    print(isReachable(x1, y1))  # Expected output: True

    # Test Case 2: Unreachable point
    x2, y2 = 5, 7
    print(isReachable(x2, y2))  # Expected output: False

    # Test Case 3: Reachable point
    x3, y3 = 8, 16
    print(isReachable(x3, y3))  # Expected output: True

    # Test Case 4: Edge case with small values
    x4, y4 = 1, 1
    print(isReachable(x4, y4))  # Expected output: True

    # Test Case 5: Large values
    x5, y5 = 1024, 2048
    print(isReachable(x5, y5))  # Expected output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function uses the Euclidean algorithm to compute the GCD of x and y. The time complexity of the GCD algorithm is O(log(min(x, y))).
- Checking if the GCD is a power of 2 is a constant-time operation, O(1).
- Overall time complexity: O(log(min(x, y))).

Space Complexity:
- The function uses a constant amount of space for variables and does not use any additional data structures.
- Overall space complexity: O(1).

Topic: Math, Number Theory
"""