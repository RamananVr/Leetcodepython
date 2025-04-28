"""
LeetCode Question #1237: Find Positive Integer Solution for a Given Function

Problem Statement:
Given a callable function `f(x, y)` that returns a non-negative integer, find all pairs `(x, y)` of positive integers 
such that `f(x, y) == z`. You are given the function `f` and the target integer `z`.

The function `f` is defined as a custom class `CustomFunction` with a method `f(x, y)`:
- `CustomFunction.f(x, y)` is increasing with respect to both `x` and `y` (i.e., `f(x, y) < f(x + 1, y)` and `f(x, y) < f(x, y + 1)`).

Your task is to return a list of all pairs `(x, y)` such that `f(x, y) == z`. The pairs should be returned in sorted order 
by their first element `x`, and if two pairs have the same `x`, then by their second element `y`.

Constraints:
- 1 <= x, y <= 1000
- 1 <= z <= 1000
- The function `f` is increasing with respect to both `x` and `y`.

Example:
Input: customfunction = CustomFunction(), z = 5
Output: [[1,4],[2,3],[3,2],[4,1]]
Explanation: customfunction.f(x, y) is defined as x + y, and there are four solutions for f(x, y) == 5.

"""

# Solution
def findSolution(customfunction, z):
    """
    Finds all pairs (x, y) such that customfunction.f(x, y) == z.

    Args:
    customfunction (CustomFunction): A callable function with method f(x, y).
    z (int): Target integer.

    Returns:
    List[List[int]]: List of pairs (x, y) satisfying the condition.
    """
    result = []
    x, y = 1, 1000  # Start with the smallest x and largest y
    while x <= 1000 and y >= 1:
        value = customfunction.f(x, y)
        if value == z:
            result.append([x, y])
            x += 1
            y -= 1
        elif value < z:
            x += 1  # Increase x to make f(x, y) larger
        else:
            y -= 1  # Decrease y to make f(x, y) smaller
    return result


# Example Test Cases
class CustomFunction:
    """
    Example implementation of CustomFunction for testing purposes.
    """
    def f(self, x, y):
        return x + y  # Example: f(x, y) = x + y

# Test Case 1
customfunction = CustomFunction()
z = 5
print(findSolution(customfunction, z))  # Expected Output: [[1, 4], [2, 3], [3, 2], [4, 1]]

# Test Case 2
z = 10
print(findSolution(customfunction, z))  # Expected Output: [[1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1]]

# Test Case 3
z = 2
print(findSolution(customfunction, z))  # Expected Output: [[1, 1]]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses a two-pointer approach, where x starts at 1 and y starts at 1000.
- In the worst case, the loop runs at most 1000 iterations (since x and y are bounded by 1000).
- Therefore, the time complexity is O(1000), which is effectively O(1) given the constraints.

Space Complexity:
- The space complexity is O(k), where k is the number of valid pairs (x, y) that satisfy f(x, y) == z.
- The result list stores these pairs, but no additional space is used beyond that.
- Therefore, the space complexity is O(k).

Topic: Two Pointers
"""