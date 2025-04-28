"""
LeetCode Problem #1925: Count Square Sum Triples

Problem Statement:
A square triple (a, b, c) is a triple where:
    - a, b, and c are integers.
    - 1 <= a, b, c <= n.
    - a^2 + b^2 = c^2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

Example:
Input: n = 5
Output: 2
Explanation: The square triples are (3, 4, 5) and (4, 3, 5).

Constraints:
- 1 <= n <= 250
"""

def countTriples(n: int) -> int:
    """
    Function to count the number of square sum triples (a, b, c) such that:
    1 <= a, b, c <= n and a^2 + b^2 = c^2.
    """
    count = 0
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            c_squared = a * a + b * b
            c = int(c_squared ** 0.5)
            if c <= n and c * c == c_squared:
                count += 1
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 5
    print(f"Input: n = {n}")
    print(f"Output: {countTriples(n)}")  # Expected Output: 2

    # Test Case 2
    n = 10
    print(f"Input: n = {n}")
    print(f"Output: {countTriples(n)}")  # Expected Output: 4

    # Test Case 3
    n = 1
    print(f"Input: n = {n}")
    print(f"Output: {countTriples(n)}")  # Expected Output: 0

    # Test Case 4
    n = 15
    print(f"Input: n = {n}")
    print(f"Output: {countTriples(n)}")  # Expected Output: 8

"""
Time Complexity:
- The outer loop runs for `n` iterations (1 <= a <= n).
- The inner loop also runs for `n` iterations (1 <= b <= n).
- For each pair (a, b), we perform a constant-time operation to calculate c and check if it satisfies the conditions.
- Therefore, the overall time complexity is O(n^2).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Math, Brute Force
"""