"""
LeetCode Question #351: Android Unlock Patterns

Problem Statement:
Android devices have a lock screen with a 3x3 grid of dots. Users can set an unlock pattern by connecting the dots with a swipe gesture. The pattern must adhere to the following rules:
1. Each pattern must connect at least `m` dots and at most `n` dots.
2. All dots in the pattern must be distinct.
3. A line connecting two dots can only pass through another dot if that dot has already been used in the pattern. For example, connecting 1 to 3 requires that 2 has already been used.

Given two integers `m` and `n`, return the total number of valid unlock patterns of length between `m` and `n`.

Constraints:
- 1 <= m <= n <= 9

Example:
Input: m = 1, n = 1
Output: 9
"""

def numberOfPatterns(m: int, n: int) -> int:
    def is_valid_move(used, skip, current, next_dot):
        # If the next dot is already used, it's valid
        if used[next_dot]:
            return True
        # If there's no dot in between or the dot in between is already used, it's valid
        if skip[current][next_dot] == 0 or used[skip[current][next_dot]]:
            return True
        return False

    def dfs(used, skip, current, remaining):
        if remaining == 0:
            return 1
        used[current] = True
        count = 0
        for next_dot in range(1, 10):
            if not used[next_dot] and is_valid_move(used, skip, current, next_dot):
                count += dfs(used, skip, next_dot, remaining - 1)
        used[current] = False
        return count

    # Precompute the "skip" array
    skip = [[0] * 10 for _ in range(10)]
    skip[1][3] = skip[3][1] = 2
    skip[1][7] = skip[7][1] = 4
    skip[3][9] = skip[9][3] = 6
    skip[7][9] = skip[9][7] = 8
    skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = 5
    skip[4][6] = skip[6][4] = 5

    used = [False] * 10
    total_count = 0

    # Iterate over all pattern lengths from m to n
    for length in range(m, n + 1):
        # Start from each of the 9 dots
        total_count += dfs(used, skip, 1, length - 1) * 4  # Symmetry: 1, 3, 7, 9
        total_count += dfs(used, skip, 2, length - 1) * 4  # Symmetry: 2, 4, 6, 8
        total_count += dfs(used, skip, 5, length - 1)      # Center: 5

    return total_count

# Example Test Cases
if __name__ == "__main__":
    print(numberOfPatterns(1, 1))  # Output: 9
    print(numberOfPatterns(1, 2))  # Output: 65
    print(numberOfPatterns(2, 2))  # Output: 56
    print(numberOfPatterns(3, 3))  # Output: 320

"""
Time Complexity:
- The time complexity is O(9!) because in the worst case, we explore all permutations of the 9 dots.
- However, due to the constraints (e.g., skipping rules), the actual number of explored states is much smaller.

Space Complexity:
- The space complexity is O(9) for the `used` array and the recursion stack.

Topic: Backtracking
"""