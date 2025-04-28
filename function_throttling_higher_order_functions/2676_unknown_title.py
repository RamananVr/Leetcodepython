"""
LeetCode Problem #2676: Throttle Function

Problem Statement:
Implement a throttle function that limits the number of times a given function can be called within a specified time window.

The throttle function accepts two arguments:
1. `fn`: A function to be throttled.
2. `t`: A time window in milliseconds.

The throttle function should return a new function that, when invoked, will call `fn` at most once per `t` milliseconds. If the returned function is called multiple times within the same time window, only the first call should invoke `fn`. Subsequent calls within the same time window should be ignored.

Example:
Input:
    const throttled = throttle(console.log, 100);
    throttled("log1"); // logs "log1" immediately.
    throttled("log2"); // ignored.
    throttled("log3"); // ignored.
    // Wait 100ms.
    throttled("log4"); // logs "log4".

Constraints:
- `fn` is a function.
- `t` is a positive integer.
"""

import time
from typing import Callable

def throttle(fn: Callable, t: int) -> Callable:
    """
    Throttle a function to limit its execution to at most once per `t` milliseconds.

    Args:
        fn (Callable): The function to be throttled.
        t (int): The time window in milliseconds.

    Returns:
        Callable: A throttled version of the input function.
    """
    last_call_time = -float('inf')  # Initialize to negative infinity to allow the first call.

    def throttled(*args, **kwargs):
        nonlocal last_call_time
        current_time = time.time() * 1000  # Convert current time to milliseconds.
        if current_time - last_call_time >= t:
            last_call_time = current_time
            return fn(*args, **kwargs)

    return throttled

# Example Test Cases
if __name__ == "__main__":
    import time

    def test_fn(msg):
        print(f"{time.time() * 1000:.0f}: {msg}")

    print("Test Case 1:")
    throttled = throttle(test_fn, 100)
    throttled("log1")  # Should log immediately.
    throttled("log2")  # Should be ignored.
    throttled("log3")  # Should be ignored.
    time.sleep(0.1)    # Wait 100ms.
    throttled("log4")  # Should log after 100ms.

    print("\nTest Case 2:")
    throttled = throttle(test_fn, 200)
    throttled("logA")  # Should log immediately.
    time.sleep(0.1)    # Wait 100ms.
    throttled("logB")  # Should be ignored.
    time.sleep(0.1)    # Wait another 100ms (200ms total).
    throttled("logC")  # Should log after 200ms.

"""
Time and Space Complexity Analysis:

Time Complexity:
- The throttled function performs a constant amount of work (checking the time and comparing it to the last call time).
- Therefore, the time complexity is O(1) per call.

Space Complexity:
- The function uses a single variable `last_call_time` to store the timestamp of the last function call.
- No additional data structures are used, so the space complexity is O(1).

Topic: Function Throttling, Higher-Order Functions
"""