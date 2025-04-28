"""
LeetCode Problem #2666: Allow One Function Call

Problem Statement:
You are given a function `fn` and a value `t`. Implement a function `once` that takes `fn` and `t` as arguments and returns a new function. The new function allows the original function `fn` to be called at most once. If the new function is called more than once, it should return the value `t` from the first call.

Example 1:
Input:
fn = (x) => x * 2
t = 10
const onceFn = once(fn, t)
onceFn(5) // 10
onceFn(10) // 10

Example 2:
Input:
fn = (x, y) => x + y
t = 0
const onceFn = once(fn, t)
onceFn(2, 3) // 5
onceFn(4, 5) // 5

Constraints:
- `fn` is a function.
- `t` is the return value of the first call to `fn`.
- The returned function should return the same value `t` for all subsequent calls.
"""

def once(fn, t):
    """
    Returns a function that allows the given function `fn` to be called at most once.
    Subsequent calls return the value `t` from the first call.

    :param fn: The function to be called at most once.
    :param t: The value to return for subsequent calls.
    :return: A new function that wraps `fn` with the described behavior.
    """
    called = False
    result = None

    def wrapper(*args, **kwargs):
        nonlocal called, result
        if not called:
            result = fn(*args, **kwargs)
            called = True
        return result

    return wrapper

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    def multiply(x):
        return x * 2

    once_multiply = once(multiply, 10)
    print(once_multiply(5))  # Expected output: 10
    print(once_multiply(10))  # Expected output: 10

    # Test Case 2
    def add(x, y):
        return x + y

    once_add = once(add, 0)
    print(once_add(2, 3))  # Expected output: 5
    print(once_add(4, 5))  # Expected output: 5

    # Test Case 3
    def greet(name):
        return f"Hello, {name}!"

    once_greet = once(greet, "Hello, World!")
    print(once_greet("Alice"))  # Expected output: "Hello, Alice!"
    print(once_greet("Bob"))  # Expected output: "Hello, Alice!"

"""
Time Complexity Analysis:
- The time complexity of the `once` function is O(1) for each call to the returned function. 
  The first call executes the original function `fn`, and subsequent calls simply return the cached result.
- The time complexity of the first call depends on the complexity of `fn`.

Space Complexity Analysis:
- The space complexity is O(1) for storing the `called` flag and the `result`.

Topic: Function Wrapping, Closures
"""