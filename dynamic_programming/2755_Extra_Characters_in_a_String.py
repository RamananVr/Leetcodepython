"""
LeetCode Problem #2755: "Extra Characters in a String"

Problem Statement:
You are given a string `s` and a dictionary of words `dictionary`. You want to determine the minimum number of extra characters left in `s` after you construct a string by concatenating words from the dictionary.

- A word can be used multiple times.
- A word can appear anywhere in the string `s`.

Return the minimum number of extra characters left in `s` after constructing the string.

Constraints:
- `1 <= s.length <= 50`
- `1 <= dictionary.length <= 50`
- `1 <= dictionary[i].length <= 50`
- `dictionary[i]` and `s` consist of only lowercase English letters.
"""

def minExtraChar(s: str, dictionary: list[str]) -> int:
    """
    Dynamic Programming solution to find the minimum number of extra characters
    left in the string `s` after constructing it using words from `dictionary`.
    """
    # Convert dictionary to a set for O(1) lookups
    word_set = set(dictionary)
    n = len(s)
    
    # dp[i] represents the minimum extra characters for the prefix s[:i]
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Base case: no extra characters for an empty prefix
    
    for i in range(1, n + 1):
        # Case 1: Treat s[i-1] as an extra character
        dp[i] = dp[i - 1] + 1
        
        # Case 2: Check all substrings ending at index i-1
        for j in range(i):
            if s[j:i] in word_set:
                dp[i] = min(dp[i], dp[j])
    
    return dp[n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "leetscode"
    dictionary1 = ["leet", "code", "leetcode"]
    print(minExtraChar(s1, dictionary1))  # Output: 1 (extra 's')

    # Test Case 2
    s2 = "sayhelloworld"
    dictionary2 = ["hello", "world"]
    print(minExtraChar(s2, dictionary2))  # Output: 3 (extra 'say')

    # Test Case 3
    s3 = "applepenapple"
    dictionary3 = ["apple", "pen"]
    print(minExtraChar(s3, dictionary3))  # Output: 0 (no extra characters)

    # Test Case 4
    s4 = "abc"
    dictionary4 = ["a", "b", "c"]
    print(minExtraChar(s4, dictionary4))  # Output: 0 (no extra characters)

    # Test Case 5
    s5 = "abcd"
    dictionary5 = ["a", "bc"]
    print(minExtraChar(s5, dictionary5))  # Output: 1 (extra 'd')

"""
Time Complexity:
- Let `n` be the length of the string `s` and `m` be the maximum length of a word in the dictionary.
- For each index `i` in `s`, we check all substrings ending at `i`, which takes O(n^2) in the worst case.
- Checking if a substring is in the dictionary takes O(1) due to the set lookup.
- Overall time complexity: O(n^2).

Space Complexity:
- The `dp` array takes O(n) space.
- The `word_set` takes O(k) space, where `k` is the total number of characters in the dictionary.
- Overall space complexity: O(n + k).

Topic: Dynamic Programming
"""