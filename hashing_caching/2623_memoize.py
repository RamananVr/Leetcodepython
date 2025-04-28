"""
LeetCode Question #2623: Memoize

Problem Statement:
Design a function that allows you to memoize another function. A memoized function is a function that will never be called twice with the same inputs. Instead, it will return a cached value.

Implement the `memoize` function:
    def memoize(fn: Callable) -> Callable

Once `memoize` is called with a function `fn`, it returns a memoized version of `fn`.

The memoized function should:
1. Accept any number of arguments.
2. Cache the results of calls with unique arguments.
3. Return the cached result if the same arguments are passed again.

Example:
    const memoizedAdd = memoize((a, b) => a + b);
    memoizedAdd(2, 3) // 5
    memoizedAdd(2, 3) // 5 (from cache)
    memoizedAdd(3, 3) // 6
"""

# Solution
from typing import Callable

def memoize(fn: Callable) -> Callable:
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
    # Example 1: Memoizing addition
    memoized_add = memoize(lambda a, b: a + b)
    print(memoized_add(2, 3))  # Output: 5
    print(memoized_add(2, 3))  # Output: 5 (from cache)
    print(memoized_add(3, 3))  # Output: 6

    # Example 2: Memoizing multiplication
    memoized_multiply = memoize(lambda a, b: a * b)
    print(memoized_multiply(2, 3))  # Output: 6
    print(memoized_multiply(2, 3))  # Output: 6 (from cache)
    print(memoized_multiply(4, 5))  # Output: 20

    # Example 3: Memoizing a single-argument function
    memoized_square = memoize(lambda x: x * x)
    print(memoized_square(4))  # Output: 16
    print(memoized_square(4))  # Output: 16 (from cache)
    print(memoized_square(5))  # Output: 25

# Time and Space Complexity Analysis
"""
Time Complexity:
- For each unique set of arguments, the function `fn` is called once, which takes O(T) time where T is the time complexity of `fn`.
- For repeated calls with the same arguments, the result is retrieved from the cache in O(1) time.
- Overall, the time complexity for N calls is O(U * T), where U is the number of unique argument sets.

Space Complexity:
- The space complexity is O(U * S), where U is the number of unique argument sets and S is the size of each cached result.
- The cache dictionary grows with the number of unique argument sets.

In summary:
Time Complexity: O(U * T)
Space Complexity: O(U * S)
"""

# Topic: Hashing / Caching