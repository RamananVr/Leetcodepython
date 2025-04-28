"""
LeetCode Problem #2030: Smallest K-Length Subsequence With Occurrences of a Letter

Problem Statement:
You are given a string `s`, an integer `k`, a character `letter`, and an integer `repetition`.
Return the lexicographically smallest subsequence of `s` of length `k` that has the character `letter` 
appearing at least `repetition` times. The test cases are generated such that the `letter` appears in `s` 
at least `repetition` times.

A subsequence is a string that can be derived from another string by deleting some or no characters 
without changing the order of the remaining characters.

Example 1:
Input: s = "leet", k = 3, letter = "e", repetition = 1
Output: "eet"
Explanation: There are four subsequences of length 3 that have at least one 'e': "lee", "let", "eet", "et". 
The lexicographically smallest subsequence among them is "eet".

Example 2:
Input: s = "leetcode", k = 4, letter = "e", repetition = 2
Output: "ecde"
Explanation: "ecde" is the lexicographically smallest subsequence of length 4 that has at least two 'e's.

Example 3:
Input: s = "bb", k = 2, letter = "b", repetition = 2
Output: "bb"
Explanation: The only subsequence of length 2 that has at least two 'b's is "bb".

Constraints:
- 1 <= s.length <= 2 * 10^4
- 1 <= k <= s.length
- `letter` is a lowercase English letter.
- 1 <= repetition <= s.count(letter)
- The test cases are generated such that the `letter` appears in `s` at least `repetition` times.
"""

# Python Solution
def smallestSubsequence(s: str, k: int, letter: str, repetition: int) -> str:
    stack = []
    count_letter = s.count(letter)
    for i, char in enumerate(s):
        # While the stack is not empty, and the current character is smaller than the top of the stack,
        # and we can still form a valid subsequence after removing the top of the stack, pop the stack.
        while (stack and stack[-1] > char and 
               len(stack) + len(s) - i - 1 >= k and 
               (stack[-1] != letter or count_letter > repetition)):
            if stack[-1] == letter:
                repetition += 1
            stack.pop()
        
        # Add the current character to the stack if it doesn't exceed the required length.
        if len(stack) < k:
            if char == letter:
                stack.append(char)
                repetition -= 1
            elif k - len(stack) > repetition:
                stack.append(char)
        
        # Decrease the count of the current character if it's the target letter.
        if char == letter:
            count_letter -= 1
    
    return ''.join(stack)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "leet"
    k1 = 3
    letter1 = "e"
    repetition1 = 1
    print(smallestSubsequence(s1, k1, letter1, repetition1))  # Output: "eet"

    # Test Case 2
    s2 = "leetcode"
    k2 = 4
    letter2 = "e"
    repetition2 = 2
    print(smallestSubsequence(s2, k2, letter2, repetition2))  # Output: "ecde"

    # Test Case 3
    s3 = "bb"
    k3 = 2
    letter3 = "b"
    repetition3 = 2
    print(smallestSubsequence(s3, k3, letter3, repetition3))  # Output: "bb"

    # Additional Test Case
    s4 = "abcde"
    k4 = 3
    letter4 = "c"
    repetition4 = 1
    print(smallestSubsequence(s4, k4, letter4, repetition4))  # Output: "abc"

# Time and Space Complexity Analysis
# Time Complexity: O(n)
# - We iterate through the string `s` once, and each character is pushed and popped from the stack at most once.
# - Thus, the time complexity is O(n), where `n` is the length of the string `s`.

# Space Complexity: O(k)
# - The stack can hold at most `k` characters, so the space complexity is O(k).

# Topic: Stack, Greedy Algorithm