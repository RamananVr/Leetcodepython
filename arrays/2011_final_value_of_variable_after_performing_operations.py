"""
LeetCode Question #2011: Final Value of Variable After Performing Operations

Problem Statement:
There is a programming language with only four operations and one variable X:
- ++X and X++ increments the value of the variable X by 1.
- --X and X-- decrements the value of the variable X by 1.

Initially, the value of X is 0.

Given an array of strings `operations` containing a list of operations, return the final value of X after performing all the operations.

Example:
Input: operations = ["--X", "X++", "X++"]
Output: 1
Explanation:
- Initially, X = 0.
- "--X" decrements X by 1: X = -1.
- "X++" increments X by 1: X = 0.
- "X++" increments X by 1: X = 1.

Constraints:
- 1 <= operations.length <= 100
- operations[i] will be either "++X", "X++", "--X", or "X--".
"""

# Clean, Correct Python Solution
def finalValueAfterOperations(operations):
    """
    Calculate the final value of X after performing all operations.

    :param operations: List[str] - List of operations to perform on X.
    :return: int - Final value of X.
    """
    X = 0
    for operation in operations:
        if operation in ("++X", "X++"):
            X += 1
        elif operation in ("--X", "X--"):
            X -= 1
    return X

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    operations = ["--X", "X++", "X++"]
    print(finalValueAfterOperations(operations))  # Output: 1

    # Test Case 2
    operations = ["++X", "++X", "X++"]
    print(finalValueAfterOperations(operations))  # Output: 3

    # Test Case 3
    operations = ["X--", "--X", "X--"]
    print(finalValueAfterOperations(operations))  # Output: -3

    # Test Case 4
    operations = ["++X", "X++", "--X", "X--"]
    print(finalValueAfterOperations(operations))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the `operations` list once, performing a constant-time operation for each element.
- Let n = len(operations). The time complexity is O(n).

Space Complexity:
- The function uses a single integer variable `X` to store the result, and no additional data structures are used.
- The space complexity is O(1).
"""

# Topic: Arrays