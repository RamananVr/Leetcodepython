"""
LeetCode Problem #1131: Maximum of Absolute Value Expression

Problem Statement:
Given two arrays `arr1` and `arr2` of equal length `n`, the absolute value expression is defined as:

    |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

where `|x|` denotes the absolute value of `x`.

Find the maximum value of the absolute value expression over all pairs of indices `(i, j)` (0 <= i, j < n).

Constraints:
- `2 <= arr1.length == arr2.length <= 40000`
- `-10^6 <= arr1[i], arr2[i] <= 10^6`

---

Solution:
The problem can be solved by observing that the absolute value expression can be rewritten in terms of four possible cases based on the signs of the terms. This allows us to reduce the problem to finding the maximum and minimum values for each case, which can be done in O(n) time.

---

Python Solution:
"""

def maxAbsValExpr(arr1, arr2):
    """
    Calculate the maximum value of the absolute value expression.

    :param arr1: List[int] - First array
    :param arr2: List[int] - Second array
    :return: int - Maximum value of the absolute value expression
    """
    n = len(arr1)
    max_val = float('-inf')

    # Evaluate the expression for all 4 cases
    for sign1, sign2 in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        max_term = float('-inf')
        min_term = float('inf')

        for i in range(n):
            term = sign1 * arr1[i] + sign2 * arr2[i] + i
            max_term = max(max_term, term)
            min_term = min(min_term, term)

        # Update the maximum value
        max_val = max(max_val, max_term - min_term)

    return max_val

"""
Example Test Cases:
"""

if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 2, 3, 4]
    arr2 = [-1, 4, 5, 6]
    print(maxAbsValExpr(arr1, arr2))  # Expected Output: 13

    # Test Case 2
    arr1 = [1, -2, -5, 0, 10]
    arr2 = [0, -2, -1, -7, -4]
    print(maxAbsValExpr(arr1, arr2))  # Expected Output: 20

    # Test Case 3
    arr1 = [1, 1, 1]
    arr2 = [1, 1, 1]
    print(maxAbsValExpr(arr1, arr2))  # Expected Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the array 4 times (once for each case).
- Each iteration is O(n), where n is the length of the arrays.
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space for variables like `max_term`, `min_term`, and `max_val`.
- Therefore, the space complexity is O(1).

---

Topic: Arrays
"""