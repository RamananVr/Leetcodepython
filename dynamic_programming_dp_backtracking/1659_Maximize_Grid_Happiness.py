"""
LeetCode Problem #1659: Maximize Grid Happiness

Problem Statement:
You are given an integer `m` representing the number of rows in a grid, an integer `n` representing the number of columns in the grid, and two integers `introvertsCount` and `extrovertsCount` representing the number of introverted and extroverted people respectively.

You want to maximize the happiness of the grid by placing the introverts and extroverts in the grid. The following rules apply:

1. Each cell in the grid can either be empty, have an introvert, or have an extrovert.
2. Introverts prefer to be alone and their happiness decreases if they are adjacent to other people.
3. Extroverts prefer company and their happiness increases if they are adjacent to other people.
4. The happiness of introverts and extroverts is calculated as follows:
   - An introvert placed in a cell contributes `120` happiness points initially, but loses `30` happiness points for each adjacent person (up, down, left, right).
   - An extrovert placed in a cell contributes `40` happiness points initially, and gains `20` happiness points for each adjacent person (up, down, left, right).

Return the maximum possible happiness that can be achieved by placing the introverts and extroverts in the grid.

Constraints:
- `1 <= m, n <= 5`
- `0 <= introvertsCount, extrovertsCount <= min(6, m * n)`
"""

from functools import lru_cache

def getMaxGridHappiness(m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
    # Constants for happiness values
    INTROVERT_BASE = 120
    EXTROVERT_BASE = 40
    INTROVERT_ADJ_PENALTY = 30
    EXTROVERT_ADJ_BONUS = 20

    # Total number of cells in the grid
    total_cells = m * n

    @lru_cache(None)
    def dfs(pos, introverts_left, extroverts_left, prev_row):
        if pos == total_cells or (introverts_left == 0 and extroverts_left == 0):
            return 0

        row, col = divmod(pos, n)
        next_row = prev_row[1:] + (0,)
        max_happiness = dfs(pos + 1, introverts_left, extroverts_left, next_row)

        def calculate_happiness(person_type):
            happiness = INTROVERT_BASE if person_type == 1 else EXTROVERT_BASE
            adj_effect = 0

            if col > 0 and prev_row[col - 1] != 0:
                adj_effect += -INTROVERT_ADJ_PENALTY if prev_row[col - 1] == 1 else EXTROVERT_ADJ_BONUS
                happiness += -INTROVERT_ADJ_PENALTY if person_type == 1 else EXTROVERT_ADJ_BONUS

            if row > 0 and prev_row[col] != 0:
                adj_effect += -INTROVERT_ADJ_PENALTY if prev_row[col] == 1 else EXTROVERT_ADJ_BONUS
                happiness += -INTROVERT_ADJ_PENALTY if person_type == 1 else EXTROVERT_ADJ_BONUS

            return happiness, adj_effect

        if introverts_left > 0:
            happiness, adj_effect = calculate_happiness(1)
            max_happiness = max(max_happiness, happiness + dfs(pos + 1, introverts_left - 1, extroverts_left, next_row[:col] + (1,) + next_row[col + 1:]))

        if extroverts_left > 0:
            happiness, adj_effect = calculate_happiness(2)
            max_happiness = max(max_happiness, happiness + dfs(pos + 1, introverts_left, extroverts_left - 1, next_row[:col] + (2,) + next_row[col + 1:]))

        return max_happiness

    return dfs(0, introvertsCount, extrovertsCount, (0,) * n)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    m, n, introvertsCount, extrovertsCount = 2, 3, 1, 2
    print(getMaxGridHappiness(m, n, introvertsCount, extrovertsCount))  # Expected Output: 240

    # Test Case 2
    m, n, introvertsCount, extrovertsCount = 3, 1, 2, 1
    print(getMaxGridHappiness(m, n, introvertsCount, extrovertsCount))  # Expected Output: 260

    # Test Case 3
    m, n, introvertsCount, extrovertsCount = 1, 1, 1, 0
    print(getMaxGridHappiness(m, n, introvertsCount, extrovertsCount))  # Expected Output: 120

# Time and Space Complexity Analysis
"""
Time Complexity:
The problem involves exploring all possible configurations of the grid, which is exponential in nature. The number of states is bounded by O(3^(m*n)) due to the three possible states for each cell (empty, introvert, extrovert). However, memoization significantly reduces redundant calculations.

Space Complexity:
The space complexity is determined by the memoization table, which stores results for each state. The size of the table is proportional to O(3^(m*n)), where m*n is the total number of cells in the grid.
"""

# Topic: Dynamic Programming (DP), Backtracking