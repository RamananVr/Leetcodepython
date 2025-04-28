"""
LeetCode Problem #1209: Remove All Adjacent Duplicates in String II

Problem Statement:
You are given a string `s` and an integer `k`, a k duplicate removal consists of choosing `k` adjacent and equal letters from `s` and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on `s` until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Constraints:
- 1 <= s.length <= 10^5
- 2 <= k <= 10^4
- s consists of lowercase English letters.

Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa".

Example 3:
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"

Follow-up:
Can you solve it without using extra space for another string?
"""

# Solution
def removeDuplicates(s: str, k: int) -> str:
    stack = []  # Stack to store pairs of (character, count)

    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1  # Increment the count of the top character
            if stack[-1][1] == k:  # If count reaches k, pop the element
                stack.pop()
        else:
            stack.append([char, 1])  # Push a new character with count 1

    # Reconstruct the string from the stack
    result = ''.join(char * count for char, count in stack)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abcd"
    k1 = 2
    print(removeDuplicates(s1, k1))  # Output: "abcd"

    # Test Case 2
    s2 = "deeedbbcccbdaa"
    k2 = 3
    print(removeDuplicates(s2, k2))  # Output: "aa"

    # Test Case 3
    s3 = "pbbcggttciiippooaais"
    k3 = 2
    print(removeDuplicates(s3, k3))  # Output: "ps"

    # Test Case 4 (Edge Case: No duplicates)
    s4 = "a"
    k4 = 2
    print(removeDuplicates(s4, k4))  # Output: "a"

    # Test Case 5 (Edge Case: Entire string removed)
    s5 = "aaaa"
    k5 = 2
    print(removeDuplicates(s5, k5))  # Output: ""

# Time Complexity Analysis:
# The algorithm processes each character in the string once, and each character is pushed and popped from the stack at most once.
# Therefore, the time complexity is O(n), where n is the length of the string `s`.

# Space Complexity Analysis:
# The space complexity is O(n) in the worst case, where the stack could store all characters of the string if no duplicates are removed.

# Topic: Stack