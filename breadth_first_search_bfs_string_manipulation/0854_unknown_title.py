"""
LeetCode Problem #854: K-Similar Strings

Problem Statement:
Strings s1 and s2 are k-similar (where k is a non-negative integer) if we can swap the positions of two letters in s1 exactly k times so that the resulting string equals s2.

Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.

Example:
Input: s1 = "ab", s2 = "ba"
Output: 1
Explanation: Swap 'a' and 'b' in s1 to make s1 equal to s2.

Constraints:
- 1 <= s1.length <= 20
- s1.length == s2.length
- s1 and s2 contain only lowercase letters from the English alphabet.
- s1 and s2 are anagrams of each other.
"""

from collections import deque

def kSimilarity(s1: str, s2: str) -> int:
    """
    Returns the minimum number of swaps required to make s1 equal to s2.
    """
    def neighbors(s):
        """Generate all valid neighbors by swapping mismatched characters."""
        i = 0
        while s[i] == s2[i]:  # Find the first mismatch
            i += 1
        for j in range(i + 1, len(s)):
            if s[j] == s2[i] and s[j] != s2[j]:  # Swap only if it reduces mismatch
                yield s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]

    # BFS to find the shortest path
    queue = deque([s1])
    visited = {s1}
    steps = 0

    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()
            if current == s2:
                return steps
            for neighbor in neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        steps += 1

    return -1  # Should never reach here since s1 and s2 are anagrams

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "ab"
    s2 = "ba"
    print(kSimilarity(s1, s2))  # Output: 1

    # Test Case 2
    s1 = "abc"
    s2 = "bca"
    print(kSimilarity(s1, s2))  # Output: 2

    # Test Case 3
    s1 = "aabbcc"
    s2 = "ccbbaa"
    print(kSimilarity(s1, s2))  # Output: 3

    # Test Case 4
    s1 = "abcdef"
    s2 = "fedcba"
    print(kSimilarity(s1, s2))  # Output: 5

"""
Time and Space Complexity Analysis:

Time Complexity:
- The BFS explores all possible states of the string. In the worst case, the number of states is factorial in the length of the string (O(n!)), where n is the length of s1.
- However, due to pruning (only swapping mismatched characters), the actual number of states explored is much smaller.
- Generating neighbors takes O(n) time for each state, where n is the length of the string.
- Overall, the time complexity is difficult to express precisely but is bounded by O(n * n!).

Space Complexity:
- The space complexity is dominated by the size of the visited set and the queue, which can store up to O(n!) states in the worst case.
- Therefore, the space complexity is O(n!).

Topic: Breadth-First Search (BFS), String Manipulation
"""