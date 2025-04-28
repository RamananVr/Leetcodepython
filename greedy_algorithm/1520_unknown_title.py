"""
LeetCode Problem #1520: Maximum Number of Non-Overlapping Substrings

Problem Statement:
Given a string `s` of lowercase English letters, you need to find the maximum number of non-overlapping substrings of `s` that satisfy the following conditions:
1. The substring is a non-empty substring of `s`.
2. For each character `c` in the substring, all occurrences of `c` in `s` must be contained within it.

Return the maximum number of such substrings. If there are multiple solutions with the same number of substrings, return the one with the smallest lexicographical order of starting indices.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "adefaddaccc"
Output: ["e","f","ccc"]

Example 2:
Input: s = "abbaccd"
Output: ["bb","cc","d"]

Constraints:
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.
"""

# Python Solution
def maxNumOfSubstrings(s: str):
    # Step 1: Find the first and last occurrence of each character
    first = {}
    last = {}
    for i, c in enumerate(s):
        if c not in first:
            first[c] = i
        last[c] = i

    # Step 2: Expand intervals for each character
    intervals = []
    for c in set(s):
        start, end = first[c], last[c]
        i = start
        while i <= end:
            if first[s[i]] < start:
                start = first[s[i]]
            if last[s[i]] > end:
                end = last[s[i]]
            i += 1
        intervals.append((start, end))

    # Step 3: Sort intervals by their end points
    intervals.sort(key=lambda x: x[1])

    # Step 4: Select non-overlapping intervals
    result = []
    prev_end = -1
    for start, end in intervals:
        if start > prev_end:
            result.append(s[start:end + 1])
            prev_end = end

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "adefaddaccc"
    print(maxNumOfSubstrings(s1))  # Output: ["e", "f", "ccc"]

    # Test Case 2
    s2 = "abbaccd"
    print(maxNumOfSubstrings(s2))  # Output: ["bb", "cc", "d"]

    # Test Case 3
    s3 = "abab"
    print(maxNumOfSubstrings(s3))  # Output: ["abab"]

    # Test Case 4
    s4 = "a"
    print(maxNumOfSubstrings(s4))  # Output: ["a"]

    # Test Case 5
    s5 = "abcabc"
    print(maxNumOfSubstrings(s5))  # Output: ["abcabc"]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Finding the first and last occurrence of each character takes O(n), where n is the length of the string.
- Expanding intervals for each character takes O(n) in total since each character is processed at most once.
- Sorting the intervals takes O(k log k), where k is the number of unique characters in the string (k <= 26 for lowercase English letters).
- Selecting non-overlapping intervals takes O(k).
Overall, the time complexity is O(n + k log k), which simplifies to O(n) since k is bounded by 26.

Space Complexity:
- The space used for the `first` and `last` dictionaries is O(k), where k is the number of unique characters.
- The space used for the `intervals` list is O(k).
- The result list uses O(k) space.
Overall, the space complexity is O(k), which is O(1) since k is bounded by 26.

Topic: Greedy Algorithm
"""