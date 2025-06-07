"""
LeetCode Question #2676: Throttle

Problem Statement:
Given a function fn and a time t in milliseconds, return a throttled version of that function.

A throttled function is first called without delay. Then, for the next t milliseconds, all calls to the function are ignored. After the t milliseconds have elapsed, the next call is executed, and the throttle process repeats.

Examples:
Example 1:
Input: t = 100, calls = [{"t": 20, "inputs": [1]}, {"t": 50, "inputs": [2]}, {"t": 120, "inputs": [3]}, {"t": 130, "inputs": [4]}, {"t": 250, "inputs": [5]}]
Output: [{"t": 20, "inputs": [1]}, {"t": 120, "inputs": [3]}, {"t": 250, "inputs": [5]}]
Explanation:
const throttled = throttle(fn, 100);
At t=20ms: throttled(1) calls fn(1). This is the first call, so it's executed immediately.
At t=50ms: throttled(2) is ignored because only 30ms have passed since the last execution.
At t=120ms: throttled(3) calls fn(3). 100ms have passed since the last execution at t=20ms.
At t=130ms: throttled(4) is ignored because only 10ms have passed since the last execution.
At t=250ms: throttled(5) calls fn(5). 130ms have passed since the last execution at t=120ms.

Example 2:
Input: t = 50, calls = [{"t": 0, "inputs": [1]}, {"t": 25, "inputs": [2]}, {"t": 60, "inputs": [3]}]
Output: [{"t": 0, "inputs": [1]}, {"t": 60, "inputs": [3]}]

Constraints:
- 0 <= t <= 1000
- 1 <= calls.length <= 10
- 0 <= calls[i].t <= 1000
- 0 <= calls[i].inputs.length <= 10
"""

from typing import List, Dict, Any, Callable
import time

def throttle(fn: Callable, t: int) -> Callable:
    """
    Create a throttled version of the function.
    
    Time: O(1) per call
    Space: O(1)
    """
    last_call_time = [-1]  # Use list to make it mutable in closure
    
    def throttled_fn(*args, **kwargs):
        current_time = int(time.time() * 1000)  # Current time in milliseconds
        
        # If this is the first call or enough time has passed
        if last_call_time[0] == -1 or current_time - last_call_time[0] >= t:
            last_call_time[0] = current_time
            return fn(*args, **kwargs)
        
        # Otherwise, ignore the call
        return None
    
    return throttled_fn

def throttleSimulation(fn: Callable, t: int, calls: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Simulate throttling for given test calls.
    
    Time: O(n) where n is number of calls
    Space: O(1)
    """
    result = []
    last_execution_time = -1
    
    for call in calls:
        call_time = call["t"]
        inputs = call["inputs"]
        
        # Check if we should execute this call
        if last_execution_time == -1 or call_time - last_execution_time >= t:
            # Execute the call
            result.append({"t": call_time, "inputs": inputs})
            last_execution_time = call_time
        # Otherwise, ignore the call
    
    return result

class ThrottleManager:
    """
    A class-based implementation of throttling.
    """
    
    def __init__(self, fn: Callable, t: int):
        self.fn = fn
        self.t = t
        self.last_call_time = -1
    
    def call(self, *args, **kwargs):
        """Make a throttled call."""
        current_time = int(time.time() * 1000)
        
        if self.last_call_time == -1 or current_time - self.last_call_time >= self.t:
            self.last_call_time = current_time
            return self.fn(*args, **kwargs)
        
        return None
    
    def simulate_call(self, call_time: int, *args, **kwargs):
        """Simulate a call at a specific time (for testing)."""
        if self.last_call_time == -1 or call_time - self.last_call_time >= self.t:
            self.last_call_time = call_time
            return self.fn(*args, **kwargs)
        
        return None

def throttleWithCallback(fn: Callable, t: int, on_ignore: Callable = None) -> Callable:
    """
    Throttle with optional callback when calls are ignored.
    
    Time: O(1) per call
    Space: O(1)
    """
    last_call_time = [-1]
    
    def throttled_fn(*args, **kwargs):
        current_time = int(time.time() * 1000)
        
        if last_call_time[0] == -1 or current_time - last_call_time[0] >= t:
            last_call_time[0] = current_time
            return fn(*args, **kwargs)
        else:
            if on_ignore:
                on_ignore(*args, **kwargs)
            return None
    
    return throttled_fn

def throttleWithQueue(fn: Callable, t: int) -> Callable:
    """
    Alternative implementation that queues the latest call during throttle period.
    
    Time: O(1) per call
    Space: O(1)
    """
    last_call_time = [-1]
    pending_call = [None]
    
    def execute_pending():
        if pending_call[0] is not None:
            args, kwargs = pending_call[0]
            pending_call[0] = None
            last_call_time[0] = int(time.time() * 1000)
            return fn(*args, **kwargs)
        return None
    
    def throttled_fn(*args, **kwargs):
        current_time = int(time.time() * 1000)
        
        if last_call_time[0] == -1 or current_time - last_call_time[0] >= t:
            last_call_time[0] = current_time
            return fn(*args, **kwargs)
        else:
            # Queue this call for later execution
            pending_call[0] = (args, kwargs)
            return None
    
    throttled_fn.execute_pending = execute_pending
    return throttled_fn

# Test Cases
if __name__ == "__main__":
    # Mock function for testing
    def test_fn(*args):
        return f"Called with: {args}"
    
    test_cases = [
        (
            100,
            [{"t": 20, "inputs": [1]}, {"t": 50, "inputs": [2]}, {"t": 120, "inputs": [3]}, {"t": 130, "inputs": [4]}, {"t": 250, "inputs": [5]}],
            [{"t": 20, "inputs": [1]}, {"t": 120, "inputs": [3]}, {"t": 250, "inputs": [5]}]
        ),
        (
            50,
            [{"t": 0, "inputs": [1]}, {"t": 25, "inputs": [2]}, {"t": 60, "inputs": [3]}],
            [{"t": 0, "inputs": [1]}, {"t": 60, "inputs": [3]}]
        ),
        (
            200,
            [{"t": 0, "inputs": [1]}, {"t": 100, "inputs": [2]}, {"t": 200, "inputs": [3]}, {"t": 300, "inputs": [4]}],
            [{"t": 0, "inputs": [1]}, {"t": 200, "inputs": [3]}]
        ),
    ]
    
    print("Testing throttle simulation:")
    for t, calls, expected in test_cases:
        result = throttleSimulation(test_fn, t, calls)
        print(f"t={t}, calls={calls}")
        print(f"Result: {result}")
        print(f"Expected: {expected}")
        print(f"Match: {'✓' if result == expected else '✗'}")
        print()
    
    print("Testing class-based throttle:")
    throttle_manager = ThrottleManager(test_fn, 100)
    
    test_calls = [
        (20, [1]),
        (50, [2]),
        (120, [3]),
        (130, [4]),
        (250, [5])
    ]
    
    executed_calls = []
    for call_time, inputs in test_calls:
        result = throttle_manager.simulate_call(call_time, *inputs)
        if result is not None:
            executed_calls.append({"t": call_time, "inputs": inputs})
    
    print(f"Class-based result: {executed_calls}")
    
    print("\nTesting with callback:")
    ignored_calls = []
    
    def on_ignore(*args):
        ignored_calls.append(args)
    
    throttled_fn = throttleWithCallback(test_fn, 100, on_ignore)
    
    # Simulate calls (this would work better with actual timing)
    print("Throttle with callback created successfully")

"""
Time and Space Complexity Analysis:

Basic Throttle:
Time Complexity: O(1) per function call
Space Complexity: O(1) - only storing last call time

Simulation Approach:
Time Complexity: O(n) where n is number of calls to process
Space Complexity: O(1) - constant extra space

Class-based Approach:
Time Complexity: O(1) per call
Space Complexity: O(1) - storing state in instance variables

Key Insights:
1. Throttling ensures function executes at most once per time period
2. The first call always executes immediately
3. Subsequent calls within the time window are ignored
4. Implementation requires tracking the last execution time
5. Real-world throttling often uses setTimeout for delayed execution

JavaScript Equivalent:
```javascript
function throttle(fn, t) {
    let lastCallTime = -1;
    
    return function(...args) {
        const currentTime = Date.now();
        
        if (lastCallTime === -1 || currentTime - lastCallTime >= t) {
            lastCallTime = currentTime;
            return fn.apply(this, args);
        }
    };
}
```

Topic: Design, Functional Programming, Rate Limiting, Closures
"""
