"""
LeetCode Problem #2746: Decremental String Concatenation

Problem Statement:
You are given an array of strings `words` and an integer `k`. You want to concatenate exactly `k` strings from the array into a single string such that the resulting string has the minimum possible length. To achieve this, you can remove characters from the end of any string before concatenating it.

Formally, for each string `s` in `words`, you can choose a non-negative integer `x` (where `x` is less than or equal to the length of `s`) and truncate the last `x` characters from `s`. After truncating, you concatenate exactly `k` strings in the order they appear in the array.

Return the minimum possible length of the resulting string.

Constraints:
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `1 <= k <= words.length`
- `words[i]` consists of lowercase English letters.
"""

# Solution
def minLength(words, k):
    from functools import lru_cache

    n = len(words)

    @lru_cache(None)
    def dp(index, remaining):
        # Base case: If no more strings are needed, return 0
        if remaining == 0:
            return 0
        # If we've run out of strings to consider, return infinity
        if index == n:
            return float('inf')

        # Option 1: Skip the current string
        skip = dp(index + 1, remaining)

        # Option 2: Use the current string
        use = len(words[index]) + dp(index + 1, remaining - 1)

        # Return the minimum of the two options
        return min(skip, use)

    return dp(0, k)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["abc", "def", "ghi"]
    k1 = 2
    print(minLength(words1, k1))  # Expected Output: 6

    # Test Case 2
    words2 = ["a", "b", "c", "d"]
    k2 = 3
    print(minLength(words2, k2))  # Expected Output: 3

    # Test Case 3
    words3 = ["abcd", "efgh", "ijkl"]
    k3 = 1
    print(minLength(words3, k3))  # Expected Output: 4

# Time Complexity Analysis:
# The time complexity of this solution is O(n * k), where `n` is the number of strings in the `words` array and `k` is the number of strings to concatenate. This is because the dynamic programming solution explores all combinations of indices and remaining strings to concatenate.
# The space complexity is O(n * k) due to the memoization table used to store intermediate results.

# Topic: Dynamic Programming