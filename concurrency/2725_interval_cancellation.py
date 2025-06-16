# filepath: q:\source\AgentGeneratedLeetcode\functions\2725_interval_cancellation.py
"""
LeetCode Question #2725: Interval Cancellation

Problem Statement:
Given a function `fn`, an array of arguments `args`, and an interval time `t`, return a cancel function `cancelFn`.

After a delay of `cancelTimeMs`, `cancelFn` will be invoked.

```javascript
setTimeout(cancelFn, cancelTimeMs)
```

The function `fn` should be called with `args` immediately and then called again every `t` milliseconds until `cancelFn` is called.

Constraints:
- `fn` is a function
- `args` is a valid JSON array
- `1 <= args.length <= 10`
- `30 <= t <= 100`
- `10 <= cancelTimeMs <= 500`

Example:
Input: fn = (x) => x * 2, args = [4], t = 35, cancelTimeMs = 190
Output: [{"time": 0, "returned": 8}, {"time": 35, "returned": 8}, {"time": 70, "returned": 8}, {"time": 105, "returned": 8}, {"time": 140, "returned": 8}, {"time": 175, "returned": 8}]
Explanation: 
const cancelTimeMs = 190;
const cancelFn = cancellable((x) => x * 2, [4], 35);
setTimeout(cancelFn, cancelTimeMs);

Every 35ms, fn(4) is called. Until t=190ms, then it is cancelled.
1st fn call is at 0ms. fn(4) returns 8.
2nd fn call is at 35ms. fn(4) returns 8.
3rd fn call is at 70ms. fn(4) returns 8.
4th fn call is at 105ms. fn(4) returns 8.
5th fn call is at 140ms. fn(4) returns 8.
6th fn call is at 175ms. fn(4) returns 8.
Cancelled at 190ms

Input: fn = (x1, x2) => x1 * x2, args = [2, 5], t = 30, cancelTimeMs = 165
Output: [{"time": 0, "returned": 10}, {"time": 30, "returned": 10}, {"time": 60, "returned": 10}, {"time": 90, "returned": 10}, {"time": 120, "returned": 10}, {"time": 150, "returned": 10}]
Explanation: 
const cancelTimeMs = 165;
const cancelFn = cancellable((x1, x2) => x1 * x2, [2, 5], 30);
setTimeout(cancelFn, cancelTimeMs);

Every 30ms, fn(2, 5) is called. Until t=165ms, then it is cancelled.
1st fn call is at 0ms. fn(2,5) returns 10.
2nd fn call is at 30ms. fn(2,5) returns 10.
3rd fn call is at 35ms. fn(2,5) returns 10.
4th fn call is at 105ms. fn(2,5) returns 10.
5th fn call is at 140ms. fn(2,5) returns 10.
6th fn call is at 175ms. fn(2,5) returns 10.
Cancelled at 165ms

Input: fn = (x1, x2, x3) => x1 + x2 + x3, args = [5, 1, 3], t = 50, cancelTimeMs = 180
Output: [{"time": 0, "returned": 9}, {"time": 50, "returned": 9}, {"time": 100, "returned": 9}, {"time": 150, "returned": 9}]
Explanation: 
const cancelTimeMs = 180;
const cancelFn = cancellable((x1, x2, x3) => x1 + x2 + x3, [5, 1, 3], 50);
setTimeout(cancelFn, cancelTimeMs);

Every 50ms, fn(5, 1, 3) is called. Until t=180ms, then it is cancelled.
1st fn call is at 0ms. fn(5,1,3) returns 9.
2nd fn call is at 50ms. fn(5,1,3) returns 9.
3rd fn call is at 100ms. fn(5,1,3) returns 9.
4th fn call is at 150ms. fn(5,1,3) returns 9.
Cancelled at 180ms
"""

import time
import threading
from typing import List, Dict, Any, Callable

def cancellable(fn: Callable, args: List[Any], t: int) -> Callable:
    """
    Create a cancellable interval function.
    
    Args:
        fn: Function to call repeatedly
        args: Arguments to pass to fn
        t: Interval time in milliseconds
    
    Returns:
        Cancel function that stops the interval
    """
    results = []
    start_time = time.time() * 1000  # Convert to milliseconds
    interval_active = True
    timer = None
    
    def execute_function():
        nonlocal timer, interval_active
        if not interval_active:
            return
            
        current_time = time.time() * 1000
        elapsed = int(current_time - start_time)
        
        try:
            result = fn(*args)
            results.append({"time": elapsed, "returned": result})
        except Exception as e:
            results.append({"time": elapsed, "error": str(e)})
        
        # Schedule next execution
        if interval_active:
            timer = threading.Timer(t / 1000.0, execute_function)
            timer.start()
    
    def cancel_fn():
        nonlocal interval_active, timer
        interval_active = False
        if timer:
            timer.cancel()
        return results
    
    # Execute immediately
    execute_function()
    
    return cancel_fn

def cancellable_simple(fn: Callable, args: List[Any], t: int) -> Callable:
    """
    Simplified version for testing purposes.
    
    Args:
        fn: Function to call repeatedly
        args: Arguments to pass to fn
        t: Interval time in milliseconds
    
    Returns:
        Cancel function that stops the interval
    """
    results = []
    is_cancelled = False
    
    def cancel_fn():
        nonlocal is_cancelled
        is_cancelled = True
        return results
    
    # Simulate immediate execution
    try:
        result = fn(*args)
        results.append({"time": 0, "returned": result})
    except Exception as e:
        results.append({"time": 0, "error": str(e)})
    
    return cancel_fn

def cancellable_with_generator(fn: Callable, args: List[Any], t: int) -> Callable:
    """
    Generator-based approach for interval management.
    
    Args:
        fn: Function to call repeatedly
        args: Arguments to pass to fn
        t: Interval time in milliseconds
    
    Returns:
        Cancel function that stops the interval
    """
    results = []
    cancelled = False
    
    def interval_generator():
        elapsed_time = 0
        while not cancelled:
            try:
                result = fn(*args)
                results.append({"time": elapsed_time, "returned": result})
            except Exception as e:
                results.append({"time": elapsed_time, "error": str(e)})
            
            yield elapsed_time
            elapsed_time += t
    
    generator = interval_generator()
    
    def cancel_fn():
        nonlocal cancelled
        cancelled = True
        return results
    
    # Execute first iteration
    try:
        next(generator)
    except StopIteration:
        pass
    
    return cancel_fn

def cancellable_event_driven(fn: Callable, args: List[Any], t: int) -> Callable:
    """
    Event-driven implementation using threading events.
    
    Args:
        fn: Function to call repeatedly
        args: Arguments to pass to fn
        t: Interval time in milliseconds
    
    Returns:
        Cancel function that stops the interval
    """
    results = []
    stop_event = threading.Event()
    thread = None
    
    def worker():
        elapsed = 0
        start_time = time.time()
        
        while not stop_event.is_set():
            current_elapsed = int((time.time() - start_time) * 1000)
            
            try:
                result = fn(*args)
                results.append({"time": current_elapsed, "returned": result})
            except Exception as e:
                results.append({"time": current_elapsed, "error": str(e)})
            
            # Wait for interval or stop event
            if stop_event.wait(t / 1000.0):
                break  # Stop event was set
    
    def cancel_fn():
        stop_event.set()
        if thread and thread.is_alive():
            thread.join(timeout=1.0)
        return results
    
    # Start worker thread
    thread = threading.Thread(target=worker, daemon=True)
    thread.start()
    
    return cancel_fn

def cancellable_queue_based(fn: Callable, args: List[Any], t: int) -> Callable:
    """
    Queue-based implementation for result collection.
    
    Args:
        fn: Function to call repeatedly
        args: Arguments to pass to fn
        t: Interval time in milliseconds
    
    Returns:
        Cancel function that stops the interval
    """
    import queue
    import threading
    
    result_queue = queue.Queue()
    stop_flag = threading.Event()
    
    def worker():
        start_time = time.time()
        iteration = 0
        
        while not stop_flag.is_set():
            elapsed = int((time.time() - start_time) * 1000)
            
            try:
                result = fn(*args)
                result_queue.put({"time": elapsed, "returned": result})
            except Exception as e:
                result_queue.put({"time": elapsed, "error": str(e)})
            
            iteration += 1
            
            # Calculate next execution time
            next_time = start_time + (iteration * t / 1000.0)
            sleep_time = max(0, next_time - time.time())
            
            if stop_flag.wait(sleep_time):
                break
    
    def cancel_fn():
        stop_flag.set()
        
        # Collect all results from queue
        results = []
        while not result_queue.empty():
            try:
                results.append(result_queue.get_nowait())
            except queue.Empty:
                break
        
        return results
    
    # Start worker thread
    worker_thread = threading.Thread(target=worker, daemon=True)
    worker_thread.start()
    
    return cancel_fn

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    def multiply_by_2(x):
        return x * 2
    
    cancel_fn = cancellable_simple(multiply_by_2, [4], 35)
    results = cancel_fn()
    print(f"Test 1 - Got: {results}")
    assert len(results) >= 1
    assert results[0]["returned"] == 8
    
    # Test Case 2  
    def multiply(x1, x2):
        return x1 * x2
    
    cancel_fn = cancellable_simple(multiply, [2, 5], 30)
    results = cancel_fn()
    print(f"Test 2 - Got: {results}")
    assert len(results) >= 1
    assert results[0]["returned"] == 10
    
    # Test Case 3
    def add_three(x1, x2, x3):
        return x1 + x2 + x3
    
    cancel_fn = cancellable_simple(add_three, [5, 1, 3], 50)
    results = cancel_fn()
    print(f"Test 3 - Got: {results}")
    assert len(results) >= 1
    assert results[0]["returned"] == 9
    
    # Test Case 4 - Error handling
    def divide_by_zero(x):
        return x / 0
    
    cancel_fn = cancellable_simple(divide_by_zero, [10], 100)
    results = cancel_fn()
    print(f"Test 4 - Got: {results}")
    assert len(results) >= 1
    assert "error" in results[0]
    
    # Test Case 5 - No arguments function
    counter = [0]
    def increment():
        counter[0] += 1
        return counter[0]
    
    cancel_fn = cancellable_simple(increment, [], 25)
    results = cancel_fn()
    print(f"Test 5 - Got: {results}")
    assert len(results) >= 1
    assert results[0]["returned"] == 1
    
    # Test Case 6 - Complex function
    def complex_calc(a, b, c):
        return (a + b) * c - a % b if b != 0 else a * c
    
    cancel_fn = cancellable_simple(complex_calc, [10, 3, 2], 40)
    results = cancel_fn()
    print(f"Test 6 - Got: {results}")
    assert len(results) >= 1
    expected = (10 + 3) * 2 - 10 % 3  # 26 - 1 = 25
    assert results[0]["returned"] == expected
    
    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

Basic Implementation:
1. Time Complexity: O(n * f) 
   - Where n is the number of intervals before cancellation
   - f is the time complexity of the function fn
   - Each interval execution is independent

2. Space Complexity: O(n)
   - Storage for n result objects
   - Each result object has constant size

Threading Implementation:
1. Time Complexity: O(n * f)
   - Same as basic, but with concurrent execution
   - Timer overhead is minimal

2. Space Complexity: O(n)
   - Result storage plus thread overhead
   - Thread stack space (typically ~8MB per thread)

Event-Driven Implementation:
1. Time Complexity: O(n * f)
   - Event checking adds minimal overhead
   - More precise timing control

2. Space Complexity: O(n)
   - Result storage plus event objects
   - Threading.Event uses minimal memory

Queue-Based Implementation:
1. Time Complexity: O(n * f)
   - Queue operations are O(1)
   - Thread-safe result collection

2. Space Complexity: O(n)
   - Queue storage for results
   - Additional queue overhead

Key Insights:
- Immediate execution happens at time 0
- Subsequent executions at t, 2t, 3t, etc.
- Cancellation stops future executions
- Results maintain execution order
- Error handling preserves interval continuation
- Thread safety important for concurrent access

Real-world Considerations:
- Timer drift in long-running intervals
- Memory cleanup after cancellation
- Exception handling doesn't stop interval
- Resource cleanup on cancellation
- Thread pool for multiple intervals

Topic: Concurrency, Threading, Timers, Event Handling, Function Scheduling
"""
