"""
LeetCode Problem #2626: Array Reduce Transformation

Problem Statement:
Given an integer array `nums`, a function `fn`, and an initial value `init`, 
implement a function `reduce` that applies the given function `fn` to reduce 
the array to a single value. The function should work as follows:

1. The `reduce` function takes four arguments:
   - `nums`: A list of integers.
   - `fn`: A function that takes two arguments and returns a single value.
   - `init`: The initial value to start the reduction.
   - `index`: (Optional) The current index in the array (default is 0).

2. The function should iterate through the array `nums` and apply the function `fn` 
   to the current accumulated value and the current element of the array.

3. The result of applying `fn` should be used as the accumulated value for the next iteration.

4. If the array is empty, the function should return the initial value `init`.

Write the function `reduce` to implement this behavior.

Constraints:
- The `nums` array will have a length of at most 1000.
- The `fn` function will always return a value.
- The `init` value will be a valid input for the `fn` function.

Example:
Input: nums = [1, 2, 3, 4], fn = lambda acc, curr: acc + curr, init = 0
Output: 10
Explanation: (0 + 1) -> (1 + 2) -> (3 + 3) -> (6 + 4) -> 10
"""

# Solution
from typing import List, Callable

def reduce(nums: List[int], fn: Callable[[int, int], int], init: int) -> int:
    """
    Reduces the array `nums` to a single value using the function `fn` and the initial value `init`.

    Args:
    nums (List[int]): The list of integers to reduce.
    fn (Callable[[int, int], int]): The function to apply for reduction.
    init (int): The initial value for the reduction.

    Returns:
    int: The reduced value.
    """
    result = init
    for num in nums:
        result = fn(result, num)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Sum of elements
    nums = [1, 2, 3, 4]
    fn = lambda acc, curr: acc + curr
    init = 0
    print(reduce(nums, fn, init))  # Output: 10

    # Test Case 2: Product of elements
    nums = [1, 2, 3, 4]
    fn = lambda acc, curr: acc * curr
    init = 1
    print(reduce(nums, fn, init))  # Output: 24

    # Test Case 3: Maximum element
    nums = [1, 2, 3, 4]
    fn = lambda acc, curr: max(acc, curr)
    init = float('-inf')
    print(reduce(nums, fn, init))  # Output: 4

    # Test Case 4: Empty array
    nums = []
    fn = lambda acc, curr: acc + curr
    init = 10
    print(reduce(nums, fn, init))  # Output: 10

    # Test Case 5: Subtraction
    nums = [10, 5, 1]
    fn = lambda acc, curr: acc - curr
    init = 20
    print(reduce(nums, fn, init))  # Output: 4

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the array `nums` once, applying the function `fn` to each element.
- Let `n` be the length of the array. The time complexity is O(n).

Space Complexity:
- The function uses a constant amount of extra space for the `result` variable.
- The space complexity is O(1).
"""

# Topic: Arrays