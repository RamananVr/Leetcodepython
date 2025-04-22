"""
LeetCode Question #660: Remove 9

Problem Statement:
------------------
Start from integer 1, remove all integers that contain the digit '9'. For example, 9, 19, 29, etc. are removed, and the sequence becomes: 
1, 2, 3, 4, 5, 6, 7, 8, 10, 11, ...

Given an integer n, return the nth integer in the sequence.

Example 1:
Input: n = 9
Output: 10

Example 2:
Input: n = 10
Output: 11

Constraints:
1 <= n <= 8 * 10^4
"""

# Solution
def newInteger(n: int) -> int:
    """
    This function returns the nth integer in the sequence where all integers containing the digit '9' are removed.
    """
    result = 0
    base = 1
    while n > 0:
        result += (n % 9) * base
        n //= 9
        base *= 10
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 9
    print(newInteger(n))  # Output: 10

    # Test Case 2
    n = 10
    print(newInteger(n))  # Output: 11

    # Test Case 3
    n = 1
    print(newInteger(n))  # Output: 1

    # Test Case 4
    n = 18
    print(newInteger(n))  # Output: 20

    # Test Case 5
    n = 100
    print(newInteger(n))  # Output: 121

"""
Time and Space Complexity Analysis:
-----------------------------------
Time Complexity:
The function processes the input `n` by repeatedly dividing it by 9. The number of divisions is proportional to the number of digits in the base-9 representation of `n`. 
For a given `n`, the number of digits in base-9 is approximately O(log9(n)), which is equivalent to O(log(n)).

Space Complexity:
The function uses a constant amount of space for variables like `result` and `base`. Therefore, the space complexity is O(1).

Topic: Math, Number Conversion
"""