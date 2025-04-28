"""
LeetCode Problem #2629: Function Composition

Problem Statement:
Given an array of functions [f1, f2, f3, ..., fn], return a new function fnc that is the function composition of the array of functions.
The function composition of [f(x), g(x), h(x)] is fnc(x) = f(g(h(x))).

If the array is empty, return the identity function f(x) = x.

Example:
Input: functions = [x => x + 1, x => 2 * x, x => x * x]
Output: fnc
Explanation:
fnc(4) = ((4 * 4) * 2) + 1 = 33

Constraints:
- `functions` is a valid array of functions.
- `functions` will have a length between [0, 1000].
- The input to all functions is a single integer `x`.
- The output of all functions is a single integer.

"""

from typing import List, Callable

def compose(functions: List[Callable[[int], int]]) -> Callable[[int], int]:
    """
    Returns a function that is the composition of the given list of functions.
    If the list is empty, returns the identity function f(x) = x.
    """
    def composed_function(x: int) -> int:
        for func in reversed(functions):
            x = func(x)
        return x
    
    return composed_function

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Example from the problem statement
    functions = [lambda x: x + 1, lambda x: 2 * x, lambda x: x * x]
    fnc = compose(functions)
    print(fnc(4))  # Expected Output: 33

    # Test Case 2: Empty list of functions
    functions = []
    fnc = compose(functions)
    print(fnc(10))  # Expected Output: 10 (identity function)

    # Test Case 3: Single function in the list
    functions = [lambda x: x - 5]
    fnc = compose(functions)
    print(fnc(15))  # Expected Output: 10

    # Test Case 4: Multiple functions
    functions = [lambda x: x * 2, lambda x: x + 3, lambda x: x - 1]
    fnc = compose(functions)
    print(fnc(5))  # Expected Output: 15

    # Test Case 5: Identity function behavior
    functions = [lambda x: x]
    fnc = compose(functions)
    print(fnc(42))  # Expected Output: 42

"""
Time Complexity Analysis:
- Let `n` be the number of functions in the list `functions`.
- For each call to the composed function, we iterate through the list of functions in reverse order, applying each function once.
- Therefore, the time complexity for a single call to the composed function is O(n).

Space Complexity Analysis:
- The space complexity is O(1) additional space, as we are not using any extra data structures apart from the input and the composed function.

Topic: Functional Programming
"""