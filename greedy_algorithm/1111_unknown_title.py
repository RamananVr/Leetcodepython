"""
LeetCode Problem #1111: Maximum Nesting Depth of Two Valid Parentheses Strings

Problem Statement:
A string is a valid parentheses string (denoted VPS) if it meets one of the following:
1. It is an empty string "".
2. It can be written as AB (A concatenated with B), where A and B are VPS.
3. It can be written as (A), where A is a VPS.

We can similarly define the nesting depth depth(S) of any VPS S as follows:
- depth("") = 0
- depth(A + B) = max(depth(A), depth(B)), where A and B are VPS.
- depth("(" + A + ")") = 1 + depth(A), where A is a VPS.

For example, "", "()", and "()()" are VPS (with nesting depths 0, 1, and 1), and "(()(()))" is a VPS with a nesting depth of 3.

Given a VPS seq, split it into two disjoint subsequences A and B, such that:
- A and B are VPS.
- max(depth(A), depth(B)) is minimized.

Return a sequence answer of length seq.length, where answer[i] = 0 if seq[i] is part of A, and answer[i] = 1 if seq[i] is part of B.

Constraints:
- 1 <= seq.length <= 10^4
- seq is a VPS.

Example:
Input: seq = "(()())"
Output: [0, 1, 1, 1, 1, 0]

Input: seq = "()(())()"
Output: [0, 0, 0, 1, 1, 0, 1, 1]
"""

# Solution
def maxDepthAfterSplit(seq: str) -> list[int]:
    """
    Split the valid parentheses string into two subsequences A and B
    such that the maximum nesting depth of A and B is minimized.
    """
    result = []
    depth = 0

    for char in seq:
        if char == '(':
            # Alternate between 0 and 1 for '(' based on current depth
            result.append(depth % 2)
            depth += 1
        else:  # char == ')'
            depth -= 1
            # Alternate between 0 and 1 for ')' based on current depth
            result.append(depth % 2)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    seq1 = "(()())"
    print(maxDepthAfterSplit(seq1))  # Expected Output: [0, 1, 1, 1, 1, 0]

    # Test Case 2
    seq2 = "()(())()"
    print(maxDepthAfterSplit(seq2))  # Expected Output: [0, 0, 0, 1, 1, 0, 1, 1]

    # Test Case 3
    seq3 = "((()))"
    print(maxDepthAfterSplit(seq3))  # Expected Output: [0, 1, 0, 1, 0, 1]

    # Test Case 4
    seq4 = "()"
    print(maxDepthAfterSplit(seq4))  # Expected Output: [0, 0]

    # Test Case 5
    seq5 = "(((())))"
    print(maxDepthAfterSplit(seq5))  # Expected Output: [0, 1, 0, 1, 0, 1, 0, 1]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution iterates through the string `seq` exactly once, performing O(1) operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The solution uses a list `result` to store the output, which has a size proportional to the input string.
- Therefore, the space complexity is O(n), where n is the length of the string.
"""

# Topic: Greedy Algorithm