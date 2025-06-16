"""
LeetCode Problem #2715: Timeout Cancellation

Problem Statement:
Given a function `fn`, an array of arguments `args`, and a timeout `t` in milliseconds, return a cancel function `cancelFn`.

After a delay of `cancelTimeMs`, `cancelFn` will be invoked.

```
setTimeout(cancelFn, cancelTimeMs)
```

Initially, the execution of the function `fn` should be delayed by `t` milliseconds.

If, before the timer of `t` milliseconds is up, the `cancelFn` is executed, then the original function `fn` should be prevented from execution. Otherwise, if the `cancelFn` is not invoked within the original delay, `fn` should be executed with the provided `args` as arguments.

Constraints:
- `fn` is a function
- `args` is a valid JSON array
- `1 <= args.length <= 10`
- `20 <= t <= 1000`
- `10 <= cancelTimeMs <= 1000`

Note: This is a JavaScript problem but we'll implement it in Python for consistency.
"""

import time
import threading
from typing import Callable, List, Any, Optional

def cancellable(fn: Callable, args: List[Any], t: int):
    """
    Creates a cancellable timeout function.
    
    :param fn: Function to execute after timeout
    :param args: Arguments to pass to the function
    :param t: Timeout in milliseconds
    :return: Cancel function
    """
    # Flag to track if the function has been cancelled
    cancelled = [False]
    result = [None]
    
    def execute_function():
        time.sleep(t / 1000.0)  # Convert milliseconds to seconds
        if not cancelled[0]:
            result[0] = fn(*args)
    
    def cancel_function():
        cancelled[0] = True
        return {"cancelled": True}
    
    # Start the timer in a separate thread
    timer_thread = threading.Thread(target=execute_function)
    timer_thread.daemon = True
    timer_thread.start()
    
    return cancel_function

def cancellableWithResult(fn: Callable, args: List[Any], t: int):
    """
    Enhanced version that returns both cancel function and result.
    
    :param fn: Function to execute after timeout
    :param args: Arguments to pass to the function
    :param t: Timeout in milliseconds
    :return: Tuple of (cancel_function, get_result_function)
    """
    cancelled = [False]
    result = [None]
    executed = [False]
    
    def execute_function():
        time.sleep(t / 1000.0)
        if not cancelled[0]:
            try:
                result[0] = fn(*args)
                executed[0] = True
            except Exception as e:
                result[0] = f"Error: {e}"
    
    def cancel_function():
        cancelled[0] = True
        return "cancelled"
    
    def get_result():
        return result[0] if executed[0] else None
    
    # Start the timer
    timer_thread = threading.Thread(target=execute_function)
    timer_thread.daemon = True
    timer_thread.start()
    
    return cancel_function, get_result

class CancellableTimer:
    """
    Class-based implementation of cancellable timer.
    """
    
    def __init__(self, fn: Callable, args: List[Any], t: int):
        self.fn = fn
        self.args = args
        self.timeout = t / 1000.0
        self.cancelled = False
        self.result = None
        self.executed = False
        self.timer = None
        
        self._start_timer()
    
    def _execute(self):
        if not self.cancelled:
            try:
                self.result = self.fn(*self.args)
                self.executed = True
            except Exception as e:
                self.result = f"Error: {e}"
    
    def _start_timer(self):
        self.timer = threading.Timer(self.timeout, self._execute)
        self.timer.start()
    
    def cancel(self):
        """Cancel the timer and prevent function execution."""
        if self.timer and not self.executed:
            self.timer.cancel()
            self.cancelled = True
            return "cancelled"
        return "already executed" if self.executed else "already cancelled"
    
    def get_result(self):
        """Get the result of the function execution."""
        return self.result if self.executed else None
    
    def is_cancelled(self):
        """Check if the timer was cancelled."""
        return self.cancelled
    
    def is_executed(self):
        """Check if the function was executed."""
        return self.executed

def simulateTimeoutCancellation(fn, args, t, cancelTimeMs):
    """
    Simulates the JavaScript timeout cancellation behavior.
    
    :param fn: Function to execute
    :param args: Arguments for the function
    :param t: Initial timeout in milliseconds
    :param cancelTimeMs: Time after which to cancel in milliseconds
    :return: Result of the operation
    """
    # Create cancellable timer
    timer = CancellableTimer(fn, args, t)
    
    # Wait for cancel time and then cancel
    time.sleep(cancelTimeMs / 1000.0)
    cancel_result = timer.cancel()
    
    # Wait a bit more to see if function would have executed
    time.sleep(max(0, (t - cancelTimeMs) / 1000.0) + 0.1)
    
    if timer.is_executed():
        return {"executed": True, "result": timer.get_result()}
    else:
        return {"cancelled": True}

# Example Test Cases
if __name__ == "__main__":
    # Helper functions for testing
    def add(a, b):
        return a + b
    
    def multiply(x, y):
        return x * y
    
    def greet(name):
        return f"Hello, {name}!"
    
    # Test Case 1: Function gets cancelled
    print("Test Case 1: Cancel before execution")
    cancel_fn = cancellable(add, [2, 3], 100)  # 100ms timeout
    time.sleep(0.05)  # Wait 50ms
    result1 = cancel_fn()  # Cancel after 50ms
    print(f"Cancelled: {result1}")
    time.sleep(0.1)  # Wait to see if function executes
    print()

    # Test Case 2: Function executes before cancellation
    print("Test Case 2: Execute before cancel")
    cancel_fn, get_result = cancellableWithResult(multiply, [4, 5], 50)  # 50ms timeout
    time.sleep(0.1)  # Wait 100ms (longer than timeout)
    result2 = get_result()
    print(f"Result: {result2}")
    cancel_result = cancel_fn()
    print(f"Cancel attempt: {cancel_result}")
    print()

    # Test Case 3: Using class-based approach
    print("Test Case 3: Class-based implementation")
    timer = CancellableTimer(greet, ["World"], 75)
    time.sleep(0.025)  # Wait 25ms
    cancel_result = timer.cancel()
    print(f"Cancel result: {cancel_result}")
    print(f"Is cancelled: {timer.is_cancelled()}")
    print(f"Is executed: {timer.is_executed()}")
    print()

    # Test Case 4: Simulate full scenario
    print("Test Case 4: Simulation - cancel after 20ms, function timeout 100ms")
    result4 = simulateTimeoutCancellation(add, [10, 15], 100, 20)
    print(f"Simulation result: {result4}")
    print()

    # Test Case 5: Simulate execution scenario
    print("Test Case 5: Simulation - cancel after 150ms, function timeout 100ms")
    result5 = simulateTimeoutCancellation(multiply, [6, 7], 100, 150)
    print(f"Simulation result: {result5}")

    print("All test cases completed!")

"""
Time Complexity Analysis:
- Time complexity: O(1) for creating the timer and cancel function.
- The actual execution depends on the timeout values.

Space Complexity Analysis:
- Space complexity: O(1) for storing the cancellation state and result.
- Additional O(1) space for the timer thread.

Topic: Concurrency, Threading, Timers, Asynchronous Programming
"""
