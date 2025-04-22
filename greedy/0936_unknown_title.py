"""
LeetCode Problem #936: Stamping The Sequence

Problem Statement:
You are given two strings `stamp` and `target`. Initially, `target` is a string of lowercase letters, and `stamp` is a string of lowercase letters. You can place `stamp` over `target` and replace every letter in the `stamp` with a `?` in `target`.

For example, if `stamp = "abc"` and `target = "ababc"`, you can place `stamp` at index 0 and replace the first three letters with `?`, making `target = "??abc"`. Then you can place `stamp` at index 2 and replace the next three letters, making `target = "?????"`.

The goal is to make `target` a string of only `?`s. You can only place `stamp` over `target` if the letters in `stamp` match the corresponding letters in `target` and the rest of the letters in `stamp` are already `?`. For example, if `stamp = "abc"` and `target = "ababc"`, you cannot place `stamp` at index 1 because the second letter in `stamp` does not match the second letter in `target`.

Return an array of the indices of the `target` where `stamp` is placed to achieve the goal. If it is not possible to achieve the goal, return an empty array.

Example 1:
Input: stamp = "abc", target = "ababc"
Output: [0, 2]
Explanation: Initially target = "ababc".
- Place stamp at index 0, target becomes "??abc".
- Place stamp at index 2, target becomes "?????".

Example 2:
Input: stamp = "abca", target = "aabcaca"
Output: [0, 3, 1]

Constraints:
- `1 <= stamp.length <= target.length <= 1000`
- `stamp` and `target` consist of lowercase English letters.
"""

# Python Solution
def movesToStamp(stamp: str, target: str) -> list[int]:
    m, n = len(stamp), len(target)
    target = list(target)
    result = []
    visited = [False] * n
    replaced_count = 0

    def can_stamp(start):
        """Check if we can stamp at the given start index."""
        for i in range(m):
            if target[start + i] != '?' and target[start + i] != stamp[i]:
                return False
        return True

    def do_stamp(start):
        """Perform the stamping operation."""
        nonlocal replaced_count
        for i in range(m):
            if target[start + i] != '?':
                target[start + i] = '?'
                replaced_count += 1

    while replaced_count < n:
        stamped = False
        for i in range(n - m + 1):
            if not visited[i] and can_stamp(i):
                do_stamp(i)
                visited[i] = True
                stamped = True
                result.append(i)
        if not stamped:
            return []
    
    return result[::-1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    stamp = "abc"
    target = "ababc"
    print(movesToStamp(stamp, target))  # Output: [0, 2]

    # Test Case 2
    stamp = "abca"
    target = "aabcaca"
    print(movesToStamp(stamp, target))  # Output: [0, 3, 1]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates over the target string multiple times until all characters are replaced with '?'.
- In the worst case, we iterate over the target string O(n) times, and for each iteration, we check O(n - m) positions.
- Thus, the time complexity is O(n * (n - m)).

Space Complexity:
- The space complexity is O(n) due to the `visited` array and the `target` list.
- The result list also takes O(n) space in the worst case.
- Overall space complexity is O(n).
"""

# Topic: Greedy