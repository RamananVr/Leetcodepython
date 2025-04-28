"""
LeetCode Problem #2375: Construct Smallest Number From DI String

Problem Statement:
You are given a string `pattern` of length `n` consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

You need to construct the lexicographically smallest permutation of the numbers [1, 2, ..., n + 1] that satisfies the pattern.

Return the lexicographically smallest permutation as a string.

Example 1:
Input: pattern = "IDID"
Output: "13254"

Example 2:
Input: pattern = "III"
Output: "1234"

Example 3:
Input: pattern = "DDI"
Output: "3214"

Constraints:
- 1 <= pattern.length <= 8
- pattern consists of only the characters 'I' and 'D'.
"""

def smallestNumber(pattern: str) -> str:
    """
    Constructs the lexicographically smallest permutation of numbers [1, 2, ..., n + 1]
    that satisfies the given pattern of 'I' (increasing) and 'D' (decreasing).
    """
    stack = []
    result = []
    for i in range(len(pattern) + 1):
        stack.append(i + 1)
        if i == len(pattern) or pattern[i] == 'I':
            while stack:
                result.append(stack.pop())
    return ''.join(map(str, result))


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    pattern = "IDID"
    print(smallestNumber(pattern))  # Output: "13254"

    # Test Case 2
    pattern = "III"
    print(smallestNumber(pattern))  # Output: "1234"

    # Test Case 3
    pattern = "DDI"
    print(smallestNumber(pattern))  # Output: "3214"

    # Additional Test Case 4
    pattern = "D"
    print(smallestNumber(pattern))  # Output: "21"

    # Additional Test Case 5
    pattern = "IID"
    print(smallestNumber(pattern))  # Output: "1243"


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the `pattern` string once, and for each character, it may push and pop elements from the stack.
- Pushing and popping from the stack are O(1) operations.
- Therefore, the overall time complexity is O(n), where n is the length of the `pattern`.

Space Complexity:
- The stack can hold up to n + 1 elements, and the result list also holds n + 1 elements.
- Thus, the space complexity is O(n), where n is the length of the `pattern`.

Topic: Stack
"""