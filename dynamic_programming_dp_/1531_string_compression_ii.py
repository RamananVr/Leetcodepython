"""
LeetCode Question #1531: String Compression II

Problem Statement:
Given a string `s` and an integer `k`, you need to compress the string such that the length of the compressed string is as small as possible after removing exactly `k` characters.

The compression algorithm is as follows:
1. For a character `c` repeated `cnt` times consecutively, the contribution to the compressed string is:
   - `c` if `cnt == 1`
   - `c` followed by `cnt` if `cnt > 1`
2. For example, the string "aaabcccd" would be compressed to "a3bc3d". The length of this compressed string is 6.

Return the length of the smallest compressed string possible after removing exactly `k` characters.

Constraints:
- `1 <= s.length <= 100`
- `0 <= k <= s.length`
- `s` consists of lowercase English letters.
"""

# Solution
def getLengthOfOptimalCompression(s: str, k: int) -> int:
    from functools import lru_cache

    @lru_cache(None)
    def dp(index: int, prev_char: str, prev_count: int, remaining_k: int) -> int:
        # Base case: if we've processed the entire string
        if index == len(s):
            return 0

        # Option 1: Remove the current character
        if remaining_k > 0:
            remove_option = dp(index + 1, prev_char, prev_count, remaining_k - 1)
        else:
            remove_option = float('inf')

        # Option 2: Keep the current character
        if s[index] == prev_char:
            # If the current character matches the previous one, we may need to update the compression length
            add_option = dp(index + 1, prev_char, prev_count + 1, remaining_k)
            # Add 1 to the length only if the count changes from 1 to 2, 9 to 10, etc.
            if prev_count in {1, 9, 99}:
                add_option += 1
        else:
            # If the current character is different, start a new group
            add_option = dp(index + 1, s[index], 1, remaining_k) + 1

        return min(remove_option, add_option)

    return dp(0, '', 0, k)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aaabcccd"
    k1 = 2
    print(getLengthOfOptimalCompression(s1, k1))  # Expected Output: 4

    # Test Case 2
    s2 = "aabbaa"
    k2 = 2
    print(getLengthOfOptimalCompression(s2, k2))  # Expected Output: 2

    # Test Case 3
    s3 = "aaaaaaaaaaa"
    k3 = 0
    print(getLengthOfOptimalCompression(s3, k3))  # Expected Output: 4

    # Test Case 4
    s4 = "abc"
    k4 = 1
    print(getLengthOfOptimalCompression(s4, k4))  # Expected Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function uses memoization to store results for subproblems. The number of states is bounded by:
  - `len(s)` for the index
  - 27 for the previous character (26 letters + empty string)
  - `len(s)` for the previous count
  - `k` for the remaining characters to remove
- Thus, the total number of states is O(len(s) * 27 * len(s) * k).
- Each state computation takes O(1), so the overall time complexity is O(len(s)^2 * k).

Space Complexity:
- The space complexity is dominated by the memoization table, which has O(len(s) * 27 * len(s) * k) states.
- Additionally, the recursion stack can go up to O(len(s) + k) depth.
- Overall space complexity is O(len(s)^2 * k).
"""

# Topic: Dynamic Programming (DP)