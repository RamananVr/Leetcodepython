"""
LeetCode Question #1931: Painting a Grid With Three Different Colors

Problem Statement:
You are given two integers m and n. Consider an m x n grid where each cell is initially white. 
You want to paint the grid using three different colors such that no two adjacent cells have the same color.

Return the number of ways to paint the grid. Since the answer may be very large, return it modulo 10^9 + 7.

Constraints:
- 1 <= m, n <= 5

Example:
Input: m = 1, n = 1
Output: 3

Input: m = 1, n = 2
Output: 6

Input: m = 5, n = 5
Output: 580986
"""

# Solution
def numOfWays(m: int, n: int) -> int:
    MOD = 10**9 + 7

    # Generate all valid rows for the grid
    def generate_valid_rows(m):
        def is_valid(row):
            for i in range(1, len(row)):
                if row[i] == row[i - 1]:
                    return False
            return True

        def dfs(index, current_row):
            if index == m:
                valid_rows.append(tuple(current_row))
                return
            for color in range(3):
                current_row.append(color)
                if is_valid(current_row):
                    dfs(index + 1, current_row)
                current_row.pop()

        valid_rows = []
        dfs(0, [])
        return valid_rows

    valid_rows = generate_valid_rows(m)

    # Precompute compatibility between rows
    def are_compatible(row1, row2):
        for i in range(m):
            if row1[i] == row2[i]:
                return False
        return True

    compatibility = {}
    for row1 in valid_rows:
        for row2 in valid_rows:
            if are_compatible(row1, row2):
                compatibility.setdefault(row1, []).append(row2)

    # Dynamic programming to count ways to paint the grid
    dp = {row: 1 for row in valid_rows}

    for _ in range(n - 1):
        new_dp = {row: 0 for row in valid_rows}
        for row in valid_rows:
            for compatible_row in compatibility[row]:
                new_dp[compatible_row] = (new_dp[compatible_row] + dp[row]) % MOD
        dp = new_dp

    return sum(dp.values()) % MOD


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    m, n = 1, 1
    print(numOfWays(m, n))  # Output: 3

    # Test Case 2
    m, n = 1, 2
    print(numOfWays(m, n))  # Output: 6

    # Test Case 3
    m, n = 5, 5
    print(numOfWays(m, n))  # Output: 580986


"""
Time and Space Complexity Analysis:

Time Complexity:
- Generating valid rows: O(3^m), where m is the number of rows in the grid.
- Compatibility check: O((3^m)^2 * m), as we compare all pairs of valid rows.
- Dynamic programming: O(n * (3^m)^2), where n is the number of columns in the grid.

Overall time complexity: O(n * (3^m)^2).

Space Complexity:
- Valid rows storage: O(3^m).
- Compatibility dictionary: O((3^m)^2).
- DP table: O(3^m).

Overall space complexity: O((3^m)^2).

Topic: Dynamic Programming
"""