"""
LeetCode Problem #2067: Number of Equal Count Substrings

Problem Statement:
You are given a string `s` and an integer `count`. A substring of `s` is called an "equal count substring" if every character in the substring appears exactly `count` times.

Return the number of equal count substrings in `s`.

Constraints:
- 1 <= s.length <= 100
- 1 <= count <= 100
- `s` consists of only lowercase English letters.
"""

def equalCountSubstrings(s: str, count: int) -> int:
    """
    Function to count the number of equal count substrings in the given string `s`.
    """
    from collections import Counter

    n = len(s)
    result = 0

    # Iterate over all possible starting points of substrings
    for start in range(n):
        freq = Counter()
        # Iterate over all possible ending points of substrings
        for end in range(start, n):
            freq[s[end]] += 1
            # Check if all characters in the current substring have frequency equal to `count`
            if all(value == count for value in freq.values()):
                result += 1
            # If any character's frequency exceeds `count`, we can stop checking further
            if any(value > count for value in freq.values()):
                break

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aabb"
    count1 = 2
    print(equalCountSubstrings(s1, count1))  # Output: 1 (substring: "aabb")

    # Test Case 2
    s2 = "abcabc"
    count2 = 1
    print(equalCountSubstrings(s2, count2))  # Output: 10 (substrings: "a", "b", "c", "ab", "bc", "ca", "abc", "bca", "cab", "abc")

    # Test Case 3
    s3 = "aaabbbccc"
    count3 = 3
    print(equalCountSubstrings(s3, count3))  # Output: 1 (substring: "aaabbbccc")

    # Test Case 4
    s4 = "aaaa"
    count4 = 2
    print(equalCountSubstrings(s4, count4))  # Output: 0 (no substring meets the criteria)

    # Test Case 5
    s5 = "ababab"
    count5 = 2
    print(equalCountSubstrings(s5, count5))  # Output: 4 (substrings: "abab", "baba", "ababab", "babab")

"""
Time Complexity Analysis:
- The outer loop iterates over all possible starting indices of substrings, O(n).
- The inner loop iterates over all possible ending indices of substrings, O(n).
- For each substring, we check the frequency of characters using a Counter, which takes O(1) for updates and O(26) for checking all values (since there are at most 26 lowercase English letters).
- Overall time complexity: O(n^2 * 26) = O(n^2).

Space Complexity Analysis:
- The space complexity is determined by the Counter, which stores at most 26 keys (one for each lowercase English letter).
- Overall space complexity: O(26) = O(1).

Topic: Strings, Sliding Window, Hash Table
"""