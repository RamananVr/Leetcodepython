"""
LeetCode Problem #1898: Maximum Number of Removable Characters

Problem Statement:
You are given two strings `s` and `p` where `p` is a subsequence of `s`. You are also given an array of integers `removable` where `removable[i]` represents the index of a character in `s` that can be removed.

The goal is to find the maximum number of characters you can remove from `s` such that `p` is still a subsequence of `s`. After removing a character, the remaining characters will shift left to fill the gap and the relative order of characters in `s` remains the same.

Return the maximum number of characters you can remove.

Constraints:
1. `1 <= p.length <= s.length <= 10^5`
2. `0 <= removable.length <= s.length`
3. `0 <= removable[i] < s.length`
4. The elements in `removable` are distinct.
5. `p` is a subsequence of `s`.

Example:
Input: s = "abcacb", p = "ab", removable = [3, 1, 0]
Output: 2
Explanation: After removing the characters at indices 3 and 1, "abcacb" becomes "accb". "ab" is still a subsequence of "accb".

"""

def maximumRemovals(s: str, p: str, removable: list[int]) -> int:
    def is_subsequence(s: str, p: str, removed: set[int]) -> bool:
        """Helper function to check if p is a subsequence of s with removed indices."""
        p_index = 0
        for i in range(len(s)):
            if i in removed:
                continue
            if p_index < len(p) and s[i] == p[p_index]:
                p_index += 1
            if p_index == len(p):
                return True
        return p_index == len(p)

    left, right = 0, len(removable)
    max_removals = 0

    while left <= right:
        mid = (left + right) // 2
        removed_set = set(removable[:mid])
        if is_subsequence(s, p, removed_set):
            max_removals = mid
            left = mid + 1
        else:
            right = mid - 1

    return max_removals

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abcacb"
    p1 = "ab"
    removable1 = [3, 1, 0]
    print(maximumRemovals(s1, p1, removable1))  # Output: 2

    # Test Case 2
    s2 = "abcbddddd"
    p2 = "abcd"
    removable2 = [3, 2, 1, 4, 5, 6]
    print(maximumRemovals(s2, p2, removable2))  # Output: 1

    # Test Case 3
    s3 = "abcab"
    p3 = "abc"
    removable3 = [0, 1, 2, 3, 4]
    print(maximumRemovals(s3, p3, removable3))  # Output: 0

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The binary search runs in O(log(n)) iterations, where n is the length of the `removable` array.
   - For each iteration, the `is_subsequence` function is called, which takes O(s) time, where s is the length of the string `s`.
   - Therefore, the overall time complexity is O(s * log(n)).

2. Space Complexity:
   - The space complexity is O(n) due to the `removed_set` used in the `is_subsequence` function.

Topic: Binary Search, Strings
"""