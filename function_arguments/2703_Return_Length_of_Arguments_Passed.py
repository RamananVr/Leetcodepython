"""
LeetCode Problem #2703: Return Length of Arguments Passed

Problem Statement:
Write a function `argumentsLength` that returns the count of arguments passed to it.

Example 1:
Input: argumentsLength(5)
Output: 1
Explanation: The function was called with one argument, so it returns 1.

Example 2:
Input: argumentsLength({}, null, "3")
Output: 3
Explanation: The function was called with three arguments, so it returns 3.

Example 3:
Input: argumentsLength()
Output: 0
Explanation: The function was called with zero arguments, so it returns 0.

Constraints:
- The function can be called with any number of arguments.
- The arguments can be of any type.
"""

# Solution
def argumentsLength(*args):
    """
    Returns the number of arguments passed to the function.

    :param args: Variable-length argument list.
    :return: Integer count of arguments.
    """
    return len(args)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    print(argumentsLength(5))  # Output: 1

    # Test Case 2
    print(argumentsLength({}, None, "3"))  # Output: 3

    # Test Case 3
    print(argumentsLength())  # Output: 0

    # Test Case 4
    print(argumentsLength(1, 2, 3, 4, 5))  # Output: 5

    # Test Case 5
    print(argumentsLength("a", "b", "c", "d", "e", "f", "g"))  # Output: 7

"""
Time Complexity Analysis:
- The function uses the built-in `len()` function to count the number of arguments in the `args` tuple.
- Let n be the number of arguments passed to the function.
- Time complexity: O(1), as the `len()` function operates in constant time for tuples.

Space Complexity Analysis:
- The function does not use any additional space apart from the input arguments.
- Space complexity: O(1), as no extra data structures are created.

Topic: Function Arguments
"""