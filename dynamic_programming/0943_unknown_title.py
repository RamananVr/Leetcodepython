"""
LeetCode Problem #943: Find the Shortest Superstring

Problem Statement:
You are given an array of strings `words`. A string `s` is called a superstring of `words` if each string in `words` 
is a substring of `s`. A superstring can contain other characters not in `words`, but each string in `words` must 
appear as a substring of `s`.

Return any shortest superstring `s` that contains all the strings in `words` as substrings. If there are multiple 
valid shortest superstrings, you can return any of them.

Example 1:
Input: words = ["alex", "loves", "leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex", "loves", and "leetcode" would also be accepted.

Example 2:
Input: words = ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]
Output: "gctaagttcatgcatc"

Constraints:
- 1 <= words.length <= 12
- 1 <= words[i].length <= 20
- All the strings of `words` are unique.
"""

from itertools import permutations

def shortestSuperstring(words):
    """
    Finds the shortest superstring that contains all the strings in the input list as substrings.

    :param words: List[str] - List of unique strings
    :return: str - Shortest superstring
    """
    n = len(words)

    # Precompute the overlap between every pair of words
    def calculate_overlap(a, b):
        max_overlap = 0
        for i in range(1, len(a) + 1):
            if b.startswith(a[-i:]):
                max_overlap = i
        return max_overlap

    overlap = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                overlap[i][j] = calculate_overlap(words[i], words[j])

    # Use dynamic programming to find the shortest superstring
    dp = [[float('inf')] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]

    # Base case: starting with each word
    for i in range(n):
        dp[1 << i][i] = len(words[i])

    # Iterate over all subsets of words
    for mask in range(1 << n):
        for i in range(n):
            if not (mask & (1 << i)):
                continue
            for j in range(n):
                if mask & (1 << j):
                    continue
                next_mask = mask | (1 << j)
                cost = dp[mask][i] + len(words[j]) - overlap[i][j]
                if cost < dp[next_mask][j]:
                    dp[next_mask][j] = cost
                    parent[next_mask][j] = i

    # Find the minimum cost to cover all words
    min_cost = float('inf')
    last = -1
    final_mask = (1 << n) - 1
    for i in range(n):
        if dp[final_mask][i] < min_cost:
            min_cost = dp[final_mask][i]
            last = i

    # Reconstruct the shortest superstring
    result = []
    mask = final_mask
    while last != -1:
        result.append(last)
        next_last = parent[mask][last]
        mask ^= (1 << last)
        last = next_last

    result.reverse()
    superstring = words[result[0]]
    for i in range(1, len(result)):
        overlap_len = overlap[result[i - 1]][result[i]]
        superstring += words[result[i]][overlap_len:]

    return superstring


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["alex", "loves", "leetcode"]
    print(shortestSuperstring(words1))  # Output: "alexlovesleetcode"

    # Test Case 2
    words2 = ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]
    print(shortestSuperstring(words2))  # Output: "gctaagttcatgcatc"

    # Test Case 3
    words3 = ["abc", "bca", "cab"]
    print(shortestSuperstring(words3))  # Output: "abcab"

    # Test Case 4
    words4 = ["a", "b", "c"]
    print(shortestSuperstring(words4))  # Output: "abc"


"""
Time Complexity:
- Calculating overlaps: O(n^2 * m), where n is the number of words and m is the average length of a word.
- Dynamic programming: O(2^n * n^2), as we iterate over all subsets of words and transitions between pairs of words.
- Reconstructing the superstring: O(n * m).
Overall: O(2^n * n^2 + n^2 * m).

Space Complexity:
- Overlap matrix: O(n^2).
- DP table and parent table: O(2^n * n).
Overall: O(2^n * n + n^2).

Topic: Dynamic Programming
"""