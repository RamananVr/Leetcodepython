"""
LeetCode Question #1541: Minimum Insertions to Balance a Parentheses String

Problem Statement:
Given a parentheses string `s` containing only the characters '(' and ')'. A parentheses string is balanced if:
1. Any left parenthesis '(' must have a corresponding two consecutive right parentheses '))'.
2. Left parenthesis '(' must go before the corresponding two consecutive right parentheses '))'.

In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

- For example, "())", "())(())))" and "(())())))" are not balanced, but "()())" and "(()))" are balanced.

You can insert the characters '(' and ')' at any position of the string to balance it if needed.

Return the minimum number of insertions needed to make `s` balanced.

Constraints:
- `1 <= s.length <= 10^5`
- `s` consists of '(' and ')' only.
"""

def minInsertions(s: str) -> int:
    """
    Function to calculate the minimum number of insertions needed to balance a parentheses string.
    """
    insertions = 0  # Tracks the number of insertions needed
    open_count = 0  # Tracks the number of unmatched '('

    i = 0
    while i < len(s):
        if s[i] == '(':
            open_count += 1
        else:  # s[i] == ')'
            # Check if this ')' is part of a pair '))'
            if i + 1 < len(s) and s[i + 1] == ')':
                # Consume this pair of '))'
                i += 1
            else:
                # Single ')' needs one more ')' to form a valid '))'
                insertions += 1

            # Match this '))' with an open '(' if available
            if open_count > 0:
                open_count -= 1
            else:
                # No '(' available, so we need to insert one
                insertions += 1

        i += 1

    # Any unmatched '(' will need two ')' each to balance
    insertions += open_count * 2

    return insertions

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "(()))"
    print(f"Minimum insertions for '{s1}': {minInsertions(s1)}")  # Expected: 1

    # Test Case 2
    s2 = "())"
    print(f"Minimum insertions for '{s2}': {minInsertions(s2)}")  # Expected: 0

    # Test Case 3
    s3 = "))())("
    print(f"Minimum insertions for '{s3}': {minInsertions(s3)}")  # Expected: 3

    # Test Case 4
    s4 = "(((((("
    print(f"Minimum insertions for '{s4}': {minInsertions(s4)}")  # Expected: 12

    # Test Case 5
    s5 = ")))))))"
    print(f"Minimum insertions for '{s5}': {minInsertions(s5)}")  # Expected: 8

"""
Time Complexity Analysis:
- The algorithm processes each character of the string exactly once, making it O(n), where n is the length of the string.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space, making it O(1).

Topic: String
"""