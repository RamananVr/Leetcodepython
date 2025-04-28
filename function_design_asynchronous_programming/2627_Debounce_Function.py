"""
LeetCode Problem #2627: Debounce Function

Problem Statement:
Write a function `debounce` that accepts a function `fn` and a delay time in milliseconds `t` as arguments. 
The `debounce` function should return a new function that delays the execution of `fn` until after `t` milliseconds 
have elapsed since the last time the returned function was invoked. If the returned function is called again 
before `t` milliseconds have passed, the timer should reset.

The returned function can be called multiple times, and the `fn` function should only be executed once 
the delay has passed without any new calls.

Example:
Input:
    const log = debounce(console.log, 100);
    log('Hello'); // Will not log immediately.
    log('Hello again'); // Resets the timer.
    // After 100ms from the last call, logs: 'Hello again'

Constraints:
- `fn` is a function.
- `t` is a non-negative integer.
"""

import threading
from typing import Callable

def debounce(fn: Callable, t: int) -> Callable:
    """
    Returns a debounced version of the input function `fn` that delays its execution
    until `t` milliseconds have passed since the last invocation.
    
    Args:
        fn (Callable): The function to debounce.
        t (int): The delay time in milliseconds.
    
    Returns:
        Callable: A debounced version of `fn`.
    """
    timer = None

    def debounced(*args, **kwargs):
        nonlocal timer
        if timer is not None:
            timer.cancel()
        timer = threading.Timer(t / 1000, lambda: fn(*args, **kwargs))
        timer.start()

    return debounced

# Example Test Cases
if __name__ == "__main__":
    import time

    def print_message(message):
        print(message)

    # Create a debounced version of the print_message function
    debounced_print = debounce(print_message, 200)

    # Test Case 1: Call the debounced function multiple times
    debounced_print("Hello")  # This call will be ignored
    time.sleep(0.1)           # Wait 100ms
    debounced_print("World")  # This call will reset the timer
    time.sleep(0.3)           # Wait 300ms (enough time for the last call to execute)

    # Expected Output:
    # "World" (printed after 200ms from the last call)

    # Test Case 2: Single call
    debounced_print("Single Call Test")
    time.sleep(0.3)           # Wait 300ms
    # Expected Output:
    # "Single Call Test" (printed after 200ms)

# Time and Space Complexity Analysis
"""
Time Complexity:
- The time complexity of the `debounce` function is O(1) for each call to the debounced function. 
  The actual execution of `fn` happens only once after the delay, so the cost of executing `fn` 
  depends on its own complexity.

Space Complexity:
- The space complexity is O(1) for maintaining the timer reference. However, the memory usage 
  depends on the size of the arguments passed to `fn` and the internal implementation of the 
  threading.Timer class.
"""

# Topic: Function Design, Asynchronous Programming