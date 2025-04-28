"""
LeetCode Problem #2078: Two Furthest Houses With Different Colors

Problem Statement:
There are `n` houses evenly lined up on the street, and each house is painted with one of `m` colors represented by an integer array `colors` of length `n`.

Return the maximum distance between two houses with different colors.

The distance between the i-th and j-th houses is `|i - j|`, where `|x|` denotes the absolute value of `x`.

Constraints:
- `n == colors.length`
- `2 <= n <= 100`
- `0 <= colors[i] <= 100`
- Test data are generated such that at least two houses have different colors.
"""

# Python Solution
def maxDistance(colors):
    """
    Finds the maximum distance between two houses with different colors.

    :param colors: List[int] - List of integers representing house colors.
    :return: int - Maximum distance between two houses with different colors.
    """
    n = len(colors)
    max_dist = 0

    # Check from the leftmost house
    for i in range(n):
        if colors[i] != colors[-1]:
            max_dist = max(max_dist, n - 1 - i)
            break

    # Check from the rightmost house
    for i in range(n - 1, -1, -1):
        if colors[i] != colors[0]:
            max_dist = max(max_dist, i)
            break

    return max_dist

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    colors1 = [1, 1, 1, 6, 1, 1, 1]
    print(maxDistance(colors1))  # Expected Output: 3

    # Test Case 2
    colors2 = [1, 8, 3, 8, 3]
    print(maxDistance(colors2))  # Expected Output: 4

    # Test Case 3
    colors3 = [0, 1]
    print(maxDistance(colors3))  # Expected Output: 1

    # Test Case 4
    colors4 = [4, 4, 4, 4, 4, 4, 4, 4, 4, 5]
    print(maxDistance(colors4))  # Expected Output: 9

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution iterates through the `colors` array twice (once from the left and once from the right).
- Each iteration is O(n), where `n` is the length of the `colors` array.
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The solution uses a constant amount of extra space, so the space complexity is O(1).
"""

# Topic: Arrays