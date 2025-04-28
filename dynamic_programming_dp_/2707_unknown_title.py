"""
LeetCode Problem #2707: Extra Characters in a String

Problem Statement:
You are given a string `s` and a dictionary of strings `dictionary`. You want to break `s` into one or more non-overlapping substrings such that each substring is in the dictionary. There may be some extra characters in `s` which are not part of any substring in the dictionary.

Return the minimum number of extra characters left over if you break up `s` optimally.

Constraints:
- `1 <= s.length <= 50`
- `1 <= dictionary.length <= 50`
- `1 <= dictionary[i].length <= 50`
- `dictionary[i]` and `s` consist of only lowercase English letters.
- `dictionary` contains distinct strings.

Example:
Input: s = "leetscode", dictionary = ["leet", "code", "leetcode"]
Output: 1
Explanation: We can break "leetscode" into "leet" and "code", leaving 1 extra character 's'.

Input: s = "sayhelloworld", dictionary = ["hello", "world"]
Output: 3
Explanation: We can break "sayhelloworld" into "hello" and "world", leaving 3 extra characters "say".
"""

# Solution
def minExtraChar(s: str, dictionary: list[str]) -> int:
    # Convert dictionary to a set for O(1) lookups
    word_set = set(dictionary)
    n = len(s)
    
    # dp[i] represents the minimum extra characters needed for the substring s[0:i]
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Base case: no extra characters for an empty string
    
    for i in range(1, n + 1):
        # Assume the current character is extra
        dp[i] = dp[i - 1] + 1
        
        # Check all possible substrings ending at index i
        for j in range(i):
            if s[j:i] in word_set:
                dp[i] = min(dp[i], dp[j])
    
    return dp[n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "leetscode"
    dictionary1 = ["leet", "code", "leetcode"]
    print(minExtraChar(s1, dictionary1))  # Output: 1

    # Test Case 2
    s2 = "sayhelloworld"
    dictionary2 = ["hello", "world"]
    print(minExtraChar(s2, dictionary2))  # Output: 3

    # Test Case 3
    s3 = "applepenapple"
    dictionary3 = ["apple", "pen"]
    print(minExtraChar(s3, dictionary3))  # Output: 0

    # Test Case 4
    s4 = "abcd"
    dictionary4 = ["a", "abc", "d"]
    print(minExtraChar(s4, dictionary4))  # Output: 1

    # Test Case 5
    s5 = "abcde"
    dictionary5 = ["a", "b", "c", "d"]
    print(minExtraChar(s5, dictionary5))  # Output: 1

"""
Time Complexity:
- Let `n` be the length of the string `s` and `m` be the maximum length of a word in the dictionary.
- For each index `i` in `s`, we check all substrings ending at `i`, which takes O(n) in the worst case.
- Checking if a substring is in the dictionary takes O(1) due to the set lookup.
- Overall time complexity: O(n^2).

Space Complexity:
- The `dp` array takes O(n) space.
- The dictionary set takes O(k), where `k` is the total length of all words in the dictionary.
- Overall space complexity: O(n + k).

Topic: Dynamic Programming (DP)
"""