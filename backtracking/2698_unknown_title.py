"""
LeetCode Problem #2698: Find the Punishment Number of an Integer

Problem Statement:
Given a positive integer `n`, the punishment number of `n` is defined as the sum of all integers `i` (1 ≤ i ≤ n) such that the square of `i` can be split into one or more contiguous substrings, and the sum of these substrings equals `i`.

For example:
- For `n = 10`, the punishment number is calculated as follows:
  - `1^2 = 1` → sum of substrings = 1 → valid
  - `2^2 = 4` → sum of substrings = 4 → valid
  - `3^2 = 9` → sum of substrings = 9 → valid
  - `4^2 = 16` → sum of substrings = 1 + 6 = 7 → invalid
  - `5^2 = 25` → sum of substrings = 2 + 5 = 7 → invalid
  - `6^2 = 36` → sum of substrings = 3 + 6 = 9 → valid
  - `7^2 = 49` → sum of substrings = 4 + 9 = 13 → invalid
  - `8^2 = 64` → sum of substrings = 6 + 4 = 10 → invalid
  - `9^2 = 81` → sum of substrings = 8 + 1 = 9 → valid
  - `10^2 = 100` → sum of substrings = 1 + 0 + 0 = 1 → invalid
  - Punishment number = 1 + 4 + 9 + 36 + 81 = 131

Write a function `punishmentNumber(n: int) -> int` that calculates the punishment number for a given integer `n`.

Constraints:
- 1 ≤ n ≤ 1000
"""

def punishmentNumber(n: int) -> int:
    def can_split_to_sum(s: str, target: int) -> bool:
        """
        Helper function to check if the square of a number can be split into substrings
        that sum up to the original number.
        """
        def dfs(index: int, current_sum: int) -> bool:
            if index == len(s):
                return current_sum == target
            for i in range(index + 1, len(s) + 1):
                substring = s[index:i]
                current_sum += int(substring)
                if dfs(i, current_sum):
                    return True
                current_sum -= int(substring)
            return False
        
        return dfs(0, 0)
    
    punishment_sum = 0
    for i in range(1, n + 1):
        square = i * i
        if can_split_to_sum(str(square), i):
            punishment_sum += square
    return punishment_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 10
    print(f"Punishment Number for n={n}: {punishmentNumber(n)}")  # Expected Output: 131

    # Test Case 2
    n = 5
    print(f"Punishment Number for n={n}: {punishmentNumber(n)}")  # Expected Output: 14

    # Test Case 3
    n = 15
    print(f"Punishment Number for n={n}: {punishmentNumber(n)}")  # Expected Output: 276

    # Test Case 4
    n = 1
    print(f"Punishment Number for n={n}: {punishmentNumber(n)}")  # Expected Output: 1

    # Test Case 5
    n = 20
    print(f"Punishment Number for n={n}: {punishmentNumber(n)}")  # Expected Output: 442

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - For each number `i` from 1 to `n`, we calculate `i^2` and check if it can be split into substrings that sum to `i`.
   - The helper function `can_split_to_sum` uses a DFS approach to explore all possible splits of the square string.
   - In the worst case, the number of splits for a string of length `k` is `2^(k-1)`. Since the length of the square string is proportional to `log10(i^2)`, the complexity for each number is approximately `O(2^(log10(i^2)))`.
   - Summing this over all numbers from 1 to `n`, the overall complexity is exponential in the worst case.

2. Space Complexity:
   - The space complexity is dominated by the recursion depth in the DFS function, which is proportional to the length of the square string. This is `O(log10(i^2))` for each number.

Topic: Backtracking
"""