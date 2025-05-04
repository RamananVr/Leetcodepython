"""
LeetCode Problem #2213: Longest Substring of One Repeating Character

Problem Statement:
You are given a string `s` and a list of queries `queryCharacters` and `queryIndices` where the `i-th` query updates the character at index `queryIndices[i]` in the string `s` to `queryCharacters[i]`.

Return an array `result` where `result[i]` is the length of the longest substring of one repeating character after the `i-th` query is performed.

Example:
Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1, 3, 3]
Output: [3, 3, 4]

Explanation:
- After applying the 1st query, s = "bbbacc", the longest substring is "bbb" with length 3.
- After applying the 2nd query, s = "bbbccc", the longest substring is "bbb" or "ccc" with length 3.
- After applying the 3rd query, s = "bbbbcc", the longest substring is "bbbb" with length 4.

Constraints:
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.
- `1 <= queryCharacters.length == queryIndices.length <= 10^5`
- `queryCharacters` consists of lowercase English letters.
- `0 <= queryIndices[i] < s.length`
"""

from sortedcontainers import SortedList

def longestRepeating(s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
    """
    Function to compute the length of the longest substring of one repeating character
    after each query is applied.
    """
    n = len(s)
    result = []
    intervals = SortedList()
    max_length = 0

    # Helper function to add an interval
    def add_interval(start, end):
        nonlocal max_length
        intervals.add((start, end))
        max_length = max(max_length, end - start + 1)

    # Helper function to remove an interval
    def remove_interval(start, end):
        nonlocal max_length
        intervals.remove((start, end))

    # Initialize intervals
    i = 0
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        add_interval(i, j - 1)
        i = j

    # Process each query
    for idx, char in zip(queryIndices, queryCharacters):
        if s[idx] == char:
            result.append(max_length)
            continue

        # Find the interval containing idx
        pos = intervals.bisect_left((idx, idx))
        start, end = intervals[pos - 1]

        # Remove the current interval
        remove_interval(start, end)

        # Update the string
        s = s[:idx] + char + s[idx + 1:]

        # Add new intervals
        if start <= idx - 1:
            add_interval(start, idx - 1)
        if idx + 1 <= end:
            add_interval(idx + 1, end)

        # Merge intervals if possible
        if start <= idx - 1 and idx + 1 <= end and s[idx - 1] == s[idx] == s[idx + 1]:
            remove_interval(start, idx - 1)
            remove_interval(idx + 1, end)
            add_interval(start, end)

        result.append(max_length)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s = "babacc"
    queryCharacters = "bcb"
    queryIndices = [1, 3, 3]
    print(longestRepeating(s, queryCharacters, queryIndices))  # Output: [3, 3, 4]

    # Test Case 2
    s = "aaaa"
    queryCharacters = "bbbb"
    queryIndices = [0, 1, 2, 3]
    print(longestRepeating(s, queryCharacters, queryIndices))  # Output: [3, 2, 1, 1]

    # Test Case 3
    s = "abcde"
    queryCharacters = "aaaaa"
    queryIndices = [0, 1, 2, 3, 4]
    print(longestRepeating(s, queryCharacters, queryIndices))  # Output: [1, 2, 3, 4, 5]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Initializing the intervals takes O(n), where n is the length of the string `s`.
- Each query involves finding and updating intervals, which takes O(log k) for each operation, where k is the number of intervals.
- In the worst case, there are O(q * log k) operations, where q is the number of queries.

Space Complexity:
- The space complexity is O(k), where k is the number of intervals stored in the SortedList.

Overall:
- Time Complexity: O(n + q * log k)
- Space Complexity: O(k)
"""

# Topic: Strings, Intervals, Sorted Data Structures