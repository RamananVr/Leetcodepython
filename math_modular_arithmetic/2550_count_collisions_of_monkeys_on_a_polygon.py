"""
LeetCode Question #2550: Count Collisions of Monkeys on a Polygon

Problem Statement:
There is a regular convex polygon with `n` sides. The vertices of the polygon are labeled as `1, 2, ..., n` in a clockwise direction. Initially, each vertex is occupied by a monkey. Each monkey can either move to the adjacent vertex in a clockwise direction or in a counterclockwise direction. Each monkey randomly chooses its direction of movement.

The movement of the monkeys happens simultaneously. A collision occurs if two or more monkeys arrive at the same vertex after moving.

Given an integer `n`, return the number of ways the monkeys can move such that at least one collision occurs. Since the answer may be very large, return it modulo `10^9 + 7`.

Constraints:
- `3 <= n <= 10^9`

Example:
Input: n = 4
Output: 14

Explanation:
There are 2^4 = 16 total ways the monkeys can move. Among these, only 2 ways result in no collisions:
1. All monkeys move clockwise.
2. All monkeys move counterclockwise.
Thus, the number of ways with at least one collision is 16 - 2 = 14.
"""

# Python Solution
def monkeyMove(n: int) -> int:
    MOD = 10**9 + 7
    # Total ways monkeys can move: 2^n
    total_ways = pow(2, n, MOD)
    # Subtract the 2 collision-free cases (all clockwise or all counterclockwise)
    collision_ways = (total_ways - 2) % MOD
    return collision_ways

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 4
    print(monkeyMove(n))  # Output: 14

    # Test Case 2
    n = 3
    print(monkeyMove(n))  # Output: 6

    # Test Case 3
    n = 5
    print(monkeyMove(n))  # Output: 30

    # Test Case 4
    n = 10
    print(monkeyMove(n))  # Output: 1022

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution uses Python's `pow` function with three arguments, which computes modular exponentiation efficiently in O(log n) time.
- Thus, the time complexity is O(log n).

Space Complexity:
- The solution uses a constant amount of extra space, so the space complexity is O(1).

Topic: Math, Modular Arithmetic
"""