"""
LeetCode Problem #2630: Memoize

Problem Statement:
Given a function `fn`, return a memoized version of that function.

A memoized function is a function that will never be called twice with the same inputs. Instead, it will return a cached value.

The function `fn` can be assumed to be a pure function, meaning that:
- The return value of `fn` is only determined by its input values.
- It does not produce side effects.

The inputs to the memoized function will always be primitives.

Example 1:
Input:
fn = lambda a, b: a + b
inputs = [[2, 3], [2, 3], [1, 2]]
Output: [5, 5, 3]
Explanation:
- The inputs [2, 3] are called twice, so the second call returns the cached value.
- The inputs [1, 2] are called once, so the result is computed.

Example 2:
Input:
fn = lambda a, b: a * b
inputs = [[2, 3], [4, 5], [2, 3]]
Output: [6, 20, 6]
Explanation:
- The inputs [2, 3] are called twice, so the second call returns the cached value.
- The inputs [4, 5] are called once, so the result is computed.

Example 3:
Input:
fn = lambda a: a + 1
inputs = [[0], [0], [1]]
Output: [1, 1, 2]
Explanation:
- The inputs [0] are called twice, so the second call returns the cached value.
- The inputs [1] are called once, so the result is computed.

Constraints:
- 1 <= inputs.length <= 10^5
- 0 <= inputs[i][j] <= 10^9
- `fn` accepts at most 2 arguments.
"""

from typing import Callable, List

def memoize(fn: Callable) -> Callable:
    """
    Returns a memoized version of the given function `fn`.
    """
    cache = {}

    def memoized_function(*args):
        if args in cache:
            return cache[args]
        result = fn(*args)
        cache[args] = result
        return result

    return memoized_function

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    fn1 = lambda a, b: a + b
    memoized_fn1 = memoize(fn1)
    inputs1 = [[2, 3], [2, 3], [1, 2]]
    outputs1 = [memoized_fn1(*args) for args in inputs1]
    print(outputs1)  # Expected: [5, 5, 3]

    # Test Case 2
    fn2 = lambda a, b: a * b
    memoized_fn2 = memoize(fn2)
    inputs2 = [[2, 3], [4, 5], [2, 3]]
    outputs2 = [memoized_fn2(*args) for args in inputs2]
    print(outputs2)  # Expected: [6, 20, 6]

    # Test Case 3
    fn3 = lambda a: a + 1
    memoized_fn3 = memoize(fn3)
    inputs3 = [[0], [0], [1]]
    outputs3 = [memoized_fn3(*args) for args in inputs3]
    print(outputs3)  # Expected: [1, 1, 2]

"""
Time Complexity Analysis:
- Let `n` be the number of calls to the memoized function.
- Each call to the memoized function involves a dictionary lookup, which is O(1) on average.
- If the result is not cached, the function `fn` is called, which takes O(1) for the given examples.
- Therefore, the overall time complexity is O(n).

Space Complexity Analysis:
- The space complexity is determined by the size of the cache.
- In the worst case, all `n` inputs are unique, so the cache will store `n` entries.
- Each entry in the cache requires space proportional to the size of the input arguments and the result.
- Therefore, the space complexity is O(n).

Topic: Hashing
"""