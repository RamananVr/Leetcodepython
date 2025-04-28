"""
LeetCode Problem #1441: Build an Array With Stack Operations

Problem Statement:
Given an array `target` and an integer `n`, you have an empty stack with the following operations available:
- "Push": Push an integer onto the stack.
- "Pop": Remove the top integer from the stack.

You are tasked to build the array `target` (in the same order) using the stack operations. The integers you can push onto the stack are in the range [1, n].

Return a list of the stack operations needed to build `target`. If there are multiple valid answers, return any of them.

Constraints:
- 1 <= target.length <= 100
- 1 <= target[i] <= n
- target is strictly increasing.
- 1 <= n <= 100
"""

# Python Solution
def buildArray(target, n):
    """
    Generate the stack operations to build the target array.

    :param target: List[int] - The target array to build.
    :param n: int - The maximum integer that can be pushed onto the stack.
    :return: List[str] - The list of stack operations.
    """
    operations = []
    current = 1  # Start with the smallest number (1)

    for num in target:
        # Push all numbers up to the current target number
        while current < num:
            operations.append("Push")
            operations.append("Pop")  # Pop the numbers not in the target
            current += 1
        # Push the current target number
        operations.append("Push")
        current += 1

    return operations

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    target = [1, 3]
    n = 3
    print(buildArray(target, n))  # Output: ["Push", "Push", "Pop", "Push"]

    # Test Case 2
    target = [1, 2, 3]
    n = 3
    print(buildArray(target, n))  # Output: ["Push", "Push", "Push"]

    # Test Case 3
    target = [1, 2]
    n = 4
    print(buildArray(target, n))  # Output: ["Push", "Push"]

    # Test Case 4
    target = [2, 3, 4]
    n = 4
    print(buildArray(target, n))  # Output: ["Push", "Pop", "Push", "Push", "Push"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the `target` array and performs operations for each number up to the maximum value in `target`.
- In the worst case, we iterate through all numbers from 1 to max(target), which is O(n), where n is the maximum value in `target`.

Space Complexity:
- The space complexity is O(m), where m is the length of the `target` array, as we store the operations in a list.

Overall:
- Time Complexity: O(n)
- Space Complexity: O(m)
"""

# Topic: Arrays, Simulation