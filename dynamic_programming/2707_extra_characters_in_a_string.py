"""
LeetCode Problem #2707: Extra Characters in a String

Problem Statement:
You are given a 0-indexed string `s` and a dictionary of words `dictionary`. You have to break `s` into one or more non-overlapping substrings such that each substring is present in `dictionary`. There may be some extra characters in `s` which are not part of any substring.

Return the minimum number of extra characters left over if you break up `s` optimally.

Constraints:
- 1 <= s.length <= 50
- 1 <= dictionary.length <= 50
- 1 <= dictionary[i].length <= 50
- `dictionary[i]` and `s` consists only of lowercase English letters
- `dictionary` has distinct words
"""

def minExtraChar(s, dictionary):
    """
    Finds the minimum number of extra characters using dynamic programming.
    
    :param s: str - The input string to break
    :param dictionary: List[str] - Dictionary of valid words
    :return: int - Minimum number of extra characters
    """
    n = len(s)
    word_set = set(dictionary)
    
    # dp[i] represents minimum extra characters for s[0:i]
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Empty string has 0 extra characters
    
    for i in range(1, n + 1):
        # Option 1: Consider s[i-1] as an extra character
        dp[i] = dp[i - 1] + 1
        
        # Option 2: Try to match ending substrings with dictionary words
        for j in range(i):
            substring = s[j:i]
            if substring in word_set:
                dp[i] = min(dp[i], dp[j])
    
    return dp[n]

def minExtraCharMemoization(s, dictionary):
    """
    Solution using memoization (top-down DP).
    
    :param s: str - The input string to break
    :param dictionary: List[str] - Dictionary of valid words
    :return: int - Minimum number of extra characters
    """
    word_set = set(dictionary)
    memo = {}
    
    def dfs(index):
        if index >= len(s):
            return 0
        
        if index in memo:
            return memo[index]
        
        # Option 1: Skip current character (count as extra)
        result = 1 + dfs(index + 1)
        
        # Option 2: Try to match substring starting from current index
        for end in range(index + 1, len(s) + 1):
            substring = s[index:end]
            if substring in word_set:
                result = min(result, dfs(end))
        
        memo[index] = result
        return result
    
    return dfs(0)

def minExtraCharOptimized(s, dictionary):
    """
    Optimized solution with early termination.
    
    :param s: str - The input string to break
    :param dictionary: List[str] - Dictionary of valid words
    :return: int - Minimum number of extra characters
    """
    n = len(s)
    word_set = set(dictionary)
    max_word_len = max(len(word) for word in dictionary) if dictionary else 0
    
    # dp[i] represents minimum extra characters for s[0:i]
    dp = [i for i in range(n + 1)]  # Initialize with worst case
    
    for i in range(1, n + 1):
        # Check substrings ending at position i
        for j in range(max(0, i - max_word_len), i):
            substring = s[j:i]
            if substring in word_set:
                dp[i] = min(dp[i], dp[j])
    
    return dp[n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s = "leetscode"
    dictionary = ["leet", "code", "leetcode"]
    print(f"s: '{s}', dictionary: {dictionary}")
    print(f"minExtraChar: {minExtraChar(s, dictionary)}")  # Output: 1
    print(f"minExtraCharMemoization: {minExtraCharMemoization(s, dictionary)}")  # Output: 1
    print(f"minExtraCharOptimized: {minExtraCharOptimized(s, dictionary)}")  # Output: 1
    print()

    # Test Case 2
    s = "sayhelloworld"
    dictionary = ["hello", "world"]
    print(f"s: '{s}', dictionary: {dictionary}")
    print(f"minExtraChar: {minExtraChar(s, dictionary)}")  # Output: 3
    print(f"minExtraCharMemoization: {minExtraCharMemoization(s, dictionary)}")  # Output: 3
    print(f"minExtraCharOptimized: {minExtraCharOptimized(s, dictionary)}")  # Output: 3
    print()

    # Test Case 3
    s = "abcdef"
    dictionary = ["abc", "def"]
    print(f"s: '{s}', dictionary: {dictionary}")
    print(f"minExtraChar: {minExtraChar(s, dictionary)}")  # Output: 0
    print(f"minExtraCharMemoization: {minExtraCharMemoization(s, dictionary)}")  # Output: 0
    print(f"minExtraCharOptimized: {minExtraCharOptimized(s, dictionary)}")  # Output: 0
    print()

    # Test Case 4
    s = "xyz"
    dictionary = ["abc", "def"]
    print(f"s: '{s}', dictionary: {dictionary}")
    print(f"minExtraChar: {minExtraChar(s, dictionary)}")  # Output: 3
    print(f"minExtraCharMemoization: {minExtraCharMemoization(s, dictionary)}")  # Output: 3
    print(f"minExtraCharOptimized: {minExtraCharOptimized(s, dictionary)}")  # Output: 3
    print()

    # Test Case 5
    s = "aaaaaa"
    dictionary = ["aa", "aaa"]
    print(f"s: '{s}', dictionary: {dictionary}")
    print(f"minExtraChar: {minExtraChar(s, dictionary)}")  # Output: 0
    print(f"minExtraCharMemoization: {minExtraCharMemoization(s, dictionary)}")  # Output: 0
    print(f"minExtraCharOptimized: {minExtraCharOptimized(s, dictionary)}")  # Output: 0

    # Validation
    assert minExtraChar("leetscode", ["leet", "code", "leetcode"]) == 1
    assert minExtraCharMemoization("sayhelloworld", ["hello", "world"]) == 3
    assert minExtraCharOptimized("abcdef", ["abc", "def"]) == 0
    print("All test cases passed!")

"""
Time Complexity Analysis:
Bottom-up DP:
- Time complexity: O(n^2 * m) where n is length of string and m is average word length.

Memoization:
- Time complexity: O(n^2 * m) in the worst case.

Optimized:
- Time complexity: O(n * max_word_len * m) which is better when max_word_len << n.

Space Complexity Analysis:
- Space complexity: O(n) for the DP array plus O(total_dict_chars) for the word set.

Topic: Dynamic Programming, String, Hash Set
"""
