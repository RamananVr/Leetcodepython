"""
LeetCode Question #2666: Allow One Function Call

Problem Statement:
Given a function fn, return a new function that is identical to the original function except that it ensures fn is called at most once.

The first time the returned function is called, it should return the same result as fn.
Every subsequent time it's called, it should return undefined.

Examples:
Example 1:
Input: fn = (a,b,c) => (a + b + c), calls = [[1,2,3],[2,3,6]]
Output: [{"calls":1,"value":6}]
Explanation:
const onceFn = once(fn);
onceFn(1, 2, 3); // 6
onceFn(2, 3, 6); // undefined, fn was not called

Example 2:
Input: fn = (a,b,c) => (a * b * c), calls = [[5,7,4],[2,3,6],[4,6,8]]
Output: [{"calls":1,"value":140}]
Explanation:
const onceFn = once(fn);
onceFn(5, 7, 4); // 140
onceFn(2, 3, 6); // undefined, fn was not called
onceFn(4, 6, 8); // undefined, fn was not called

Constraints:
- calls is a valid JSON array
- 1 <= calls.length <= 10
- 1 <= calls[i].length <= 100
- 2 <= JSON.stringify(calls).length <= 1000
"""

from typing import Any, Callable, List, Dict, Union

def once(fn: Callable[..., Any]) -> Callable[..., Union[Any, None]]:
    """
    Return a function that can only be called once.
    
    The first call returns the result of fn, subsequent calls return None.
    """
    called = False
    result = None
    
    def wrapper(*args, **kwargs):
        nonlocal called, result
        if not called:
            called = True
            result = fn(*args, **kwargs)
            return result
        return None
    
    return wrapper

def once_with_closure(fn: Callable[..., Any]) -> Callable[..., Union[Any, None]]:
    """
    Alternative implementation using closure properties.
    """
    def wrapper(*args, **kwargs):
        if hasattr(wrapper, '_called'):
            return None
        wrapper._called = True
        return fn(*args, **kwargs)
    
    return wrapper

def once_with_exception(fn: Callable[..., Any]) -> Callable[..., Union[Any, None]]:
    """
    Implementation that raises exception on subsequent calls.
    """
    called = False
    
    def wrapper(*args, **kwargs):
        nonlocal called
        if called:
            raise RuntimeError("Function can only be called once")
        called = True
        return fn(*args, **kwargs)
    
    return wrapper

class OnceWrapper:
    """
    Class-based implementation of once function.
    """
    def __init__(self, fn: Callable[..., Any]):
        self.fn = fn
        self.called = False
        self.result = None
    
    def __call__(self, *args, **kwargs):
        if self.called:
            return None
        self.called = True
        self.result = self.fn(*args, **kwargs)
        return self.result

def simulate_function_calls(fn: Callable, calls: List[List[Any]]) -> List[Dict[str, Any]]:
    """
    Simulate function calls and return results in LeetCode format.
    """
    once_fn = once(fn)
    results = []
    actual_calls = 0
    
    for call_args in calls:
        result = once_fn(*call_args)
        if result is not None:
            actual_calls += 1
            results.append({"calls": actual_calls, "value": result})
    
    return results

def simulate_function_calls_detailed(fn: Callable, calls: List[List[Any]]) -> Dict[str, Any]:
    """
    Detailed simulation showing all call results.
    """
    once_fn = once(fn)
    results = []
    call_count = 0
    
    for i, call_args in enumerate(calls):
        result = once_fn(*call_args)
        if result is not None:
            call_count += 1
        results.append({
            "call_index": i,
            "args": call_args,
            "result": result,
            "was_executed": result is not None
        })
    
    return {
        "total_calls": len(calls),
        "executed_calls": call_count,
        "results": results
    }

# Test Cases
if __name__ == "__main__":
    # Test functions
    def add_three(a, b, c):
        return a + b + c
    
    def multiply_three(a, b, c):
        return a * b * c
    
    def identity(x):
        return x
    
    test_cases = [
        (add_three, [[1, 2, 3], [2, 3, 6]], [{"calls": 1, "value": 6}]),
        (multiply_three, [[5, 7, 4], [2, 3, 6], [4, 6, 8]], [{"calls": 1, "value": 140}]),
        (identity, [[42], [100]], [{"calls": 1, "value": 42}]),
        (lambda: "hello", [[], []], [{"calls": 1, "value": "hello"}])
    ]
    
    print("Testing main once implementation:")
    for fn, calls, expected in test_cases:
        result = simulate_function_calls(fn, calls)
        print(f"once({fn.__name__}) with calls {calls}")
        print(f"  Result: {result}")
        print(f"  Expected: {expected}")
        print(f"  {'✓' if result == expected else '✗'}\n")
    
    print("Testing alternative implementations:")
    
    # Test once_with_closure
    print("Testing once_with_closure:")
    fn = lambda a, b: a + b
    once_fn = once_with_closure(fn)
    print(f"First call: {once_fn(3, 4)}")  # Should return 7
    print(f"Second call: {once_fn(5, 6)}")  # Should return None
    
    # Test class-based implementation
    print("\nTesting OnceWrapper class:")
    once_wrapper = OnceWrapper(lambda x: x * 2)
    print(f"First call: {once_wrapper(5)}")  # Should return 10
    print(f"Second call: {once_wrapper(7)}")  # Should return None
    
    # Detailed simulation
    print("\nDetailed simulation for add_three:")
    detailed_result = simulate_function_calls_detailed(add_three, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    for key, value in detailed_result.items():
        print(f"{key}: {value}")

"""
Time and Space Complexity Analysis:

Main Implementation (once):
Time Complexity: O(1) - constant time for each call
Space Complexity: O(1) - stores only a boolean flag and result

Closure Implementation:
Time Complexity: O(1) - constant time for each call
Space Complexity: O(1) - uses function attribute to track state

Class-based Implementation:
Time Complexity: O(1) - constant time for each call
Space Complexity: O(1) - stores state in instance variables

Key Insights:
1. The once pattern is a common functional programming concept
2. Need to track if function has been called before
3. Store and return the original result on first call
4. Return None (or undefined in JavaScript) on subsequent calls
5. Can be implemented with closures, classes, or function attributes

Use Cases:
- Initialization functions that should only run once
- Event handlers that should only fire once
- Resource allocation that should happen only once
- Memoization for functions with no parameters

Design Patterns:
- Decorator pattern: wrapping original function with additional behavior
- Singleton pattern: ensuring single execution
- Proxy pattern: controlling access to the original function

Topic: Functional Programming, Closures, Decorators, Design Patterns
"""
