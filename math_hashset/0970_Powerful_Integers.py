"""
LeetCode Problem #970: Powerful Integers

Problem Statement:
Given three integers `x`, `y`, and `bound`, return a list of all the powerful integers that have a value less than or equal to `bound`.

An integer is powerful if it can be represented as `x^i + y^j` for integers `i >= 0` and `j >= 0`.

You may return the answer in any order. The answer should not contain duplicate values.

Constraints:
- 1 <= x, y <= 100
- 0 <= bound <= 10^6
"""

def powerfulIntegers(x: int, y: int, bound: int) -> list:
    """
    Returns a list of all powerful integers less than or equal to the given bound.
    """
    result = set()
    i = 0

    # Iterate over powers of x
    while x**i <= bound:
        j = 0
        # Iterate over powers of y
        while x**i + y**j <= bound:
            result.add(x**i + y**j)
            if y == 1:  # If y == 1, y^j will always be 1 for j >= 0
                break
            j += 1
        if x == 1:  # If x == 1, x^i will always be 1 for i >= 0
            break
        i += 1

    return list(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    x1, y1, bound1 = 2, 3, 10
    print("Test Case 1:", powerfulIntegers(x1, y1, bound1))  # Expected Output: [2, 3, 4, 5, 7, 9, 10]

    # Test Case 2
    x2, y2, bound2 = 3, 5, 15
    print("Test Case 2:", powerfulIntegers(x2, y2, bound2))  # Expected Output: [2, 4, 6, 8, 10, 14]

    # Test Case 3
    x3, y3, bound3 = 2, 1, 10
    print("Test Case 3:", powerfulIntegers(x3, y3, bound3))  # Expected Output: [2, 3, 5, 9]

    # Test Case 4
    x4, y4, bound4 = 1, 1, 0
    print("Test Case 4:", powerfulIntegers(x4, y4, bound4))  # Expected Output: []

"""
Time Complexity:
- Let `m` be the maximum power of `x` such that `x^m <= bound`.
- Let `n` be the maximum power of `y` such that `y^n <= bound`.
- The algorithm iterates over all combinations of `i` and `j` where `0 <= i <= m` and `0 <= j <= n`.
- In the worst case, the time complexity is O(m * n), where m = log(bound) / log(x) and n = log(bound) / log(y).

Space Complexity:
- The space complexity is O(k), where `k` is the number of unique powerful integers added to the result set.

Topic: Math, HashSet
"""