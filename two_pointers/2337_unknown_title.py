"""
LeetCode Problem #2337: Move Pieces to Obtain a String

Problem Statement:
You are given two strings `start` and `target`, both of length `n`. Each string consists only of the characters `'L'`, `'R'`, and `'_'` where:

- The characters `'L'` and `'R'` represent pieces, where a piece `'L'` can move to the left only and a piece `'R'` can move to the right only.
- The character `'_'` represents an empty space that can be occupied by any piece.

The move rules are as follows:
- A piece `'L'` can only move to the left if there is an empty space directly to its left.
- A piece `'R'` can only move to the right if there is an empty space directly to its right.

You want to transform the string `start` into the string `target` using the above move rules. Return `True` if it is possible to achieve the transformation, or `False` otherwise.

Constraints:
- `n == start.length == target.length`
- `1 <= n <= 10^5`
- `start` and `target` consist of the characters `'L'`, `'R'`, and `'_'`.

"""

def canChange(start: str, target: str) -> bool:
    """
    Determines if it is possible to transform the string `start` into the string `target`
    using the given move rules for 'L' and 'R'.
    """
    # Remove all '_' from both strings and check if the remaining characters match
    if start.replace('_', '') != target.replace('_', ''):
        return False

    # Two pointers to traverse start and target
    i, j = 0, 0
    n = len(start)

    while i < n and j < n:
        # Skip '_' in start
        while i < n and start[i] == '_':
            i += 1
        # Skip '_' in target
        while j < n and target[j] == '_':
            j += 1

        # If both pointers are out of bounds, we are done
        if i == n and j == n:
            return True
        # If one pointer is out of bounds but the other is not, return False
        if i == n or j == n:
            return False

        # Check if the characters at i and j match
        if start[i] != target[j]:
            return False

        # Check movement rules
        if start[i] == 'L' and i < j:  # 'L' can only move left
            return False
        if start[i] == 'R' and i > j:  # 'R' can only move right
            return False

        # Move both pointers
        i += 1
        j += 1

    return True


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    start = "_L__R__R_"
    target = "L______RR"
    print(canChange(start, target))  # Output: True

    # Test Case 2
    start = "R_L_"
    target = "__LR"
    print(canChange(start, target))  # Output: False

    # Test Case 3
    start = "_R"
    target = "R_"
    print(canChange(start, target))  # Output: False

    # Test Case 4
    start = "L__R"
    target = "L__R"
    print(canChange(start, target))  # Output: True

    # Test Case 5
    start = "R_L__"
    target = "__RL_"
    print(canChange(start, target))  # Output: False


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the strings `start` and `target` once, skipping over the '_' characters.
- The replace operation also iterates through the strings once.
- Overall, the time complexity is O(n), where n is the length of the strings.

Space Complexity:
- The replace operation creates new strings without the '_' characters, which takes O(n) space.
- The rest of the algorithm uses constant space.
- Overall, the space complexity is O(n).

Topic: Two Pointers
"""