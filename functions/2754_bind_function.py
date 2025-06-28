"""
LeetCode Problem 2754: Bind Function

Write a function that accepts a function fn and returns a new function that is identical to the original function except that it ensures the function is called with a given argument as its first parameter.

The returned function should maintain the original function's behavior for additional arguments.

Example 1:
Input: fn = function add(a, b) { return a + b; }, args = [5]
Output: function(b) { return add(5, b); }
Explanation: 
const boundAdd = bindFunc(add, [5]);
boundAdd(10); // returns 15 (5 + 10)

Example 2:  
Input: fn = function multiply(a, b, c) { return a * b * c; }, args = [2, 3]
Output: function(c) { return multiply(2, 3, c); }
Explanation:
const boundMultiply = bindFunc(multiply, [2, 3]);
boundMultiply(4); // returns 24 (2 * 3 * 4)

Example 3:
Input: fn = function greet(greeting, name) { return greeting + " " + name; }, args = ["Hello"]
Output: function(name) { return greet("Hello", name); }
Explanation:
const boundGreet = bindFunc(greet, ["Hello"]);
boundGreet("World"); // returns "Hello World"

Constraints:
- args is an array of 0 or more arguments
- 1 <= args.length + additionalArgs.length <= 10
- The returned function should work with any number of additional arguments
"""

from typing import Any, Callable, List
from functools import partial


def bind_function(fn: Callable, args: List[Any]) -> Callable:
    """
    Bind arguments to a function, returning a new function with pre-filled parameters.
    
    This is similar to JavaScript's Function.prototype.bind() or Python's functools.partial.
    
    Args:
        fn: The function to bind arguments to
        args: List of arguments to pre-fill
        
    Returns:
        New function with bound arguments
        
    Time Complexity: O(1) for binding, O(k) for each call where k is total args
    Space Complexity: O(n) where n is number of bound arguments
    """
    def bound_function(*additional_args):
        """The returned bound function."""
        # Combine bound arguments with additional arguments
        all_args = args + list(additional_args)
        return fn(*all_args)
    
    return bound_function


def bind_function_partial(fn: Callable, args: List[Any]) -> Callable:
    """
    Implementation using Python's built-in functools.partial.
    
    Args:
        fn: The function to bind arguments to
        args: List of arguments to pre-fill
        
    Returns:
        Partially applied function
        
    Time Complexity: O(1) for binding
    Space Complexity: O(n) where n is number of bound arguments
    """
    return partial(fn, *args)


def bind_function_closure(fn: Callable, args: List[Any]) -> Callable:
    """
    Implementation using closure to capture bound arguments.
    
    Args:
        fn: The function to bind arguments to
        args: List of arguments to pre-fill
        
    Returns:
        New function with closure over bound arguments
        
    Time Complexity: O(1) for binding
    Space Complexity: O(n) where n is number of bound arguments
    """
    bound_args = args.copy()  # Create a copy to avoid mutation issues
    
    def bound_function(*additional_args):
        return fn(*(bound_args + list(additional_args)))
    
    return bound_function


def bind_function_class(fn: Callable, args: List[Any]) -> Callable:
    """
    Implementation using a class to store bound arguments.
    
    Args:
        fn: The function to bind arguments to
        args: List of arguments to pre-fill
        
    Returns:
        Callable class instance
        
    Time Complexity: O(1) for binding
    Space Complexity: O(n) where n is number of bound arguments
    """
    class BoundFunction:
        def __init__(self, func, bound_args):
            self.func = func
            self.bound_args = bound_args
        
        def __call__(self, *additional_args):
            return self.func(*(self.bound_args + list(additional_args)))
    
    return BoundFunction(fn, args)


def bind_function_with_kwargs(fn: Callable, args: List[Any], kwargs: dict = None) -> Callable:
    """
    Enhanced version that supports both positional and keyword arguments.
    
    Args:
        fn: The function to bind arguments to
        args: List of positional arguments to pre-fill
        kwargs: Dictionary of keyword arguments to pre-fill
        
    Returns:
        Function with bound positional and keyword arguments
        
    Time Complexity: O(1) for binding
    Space Complexity: O(n + m) where n is bound args, m is bound kwargs
    """
    if kwargs is None:
        kwargs = {}
    
    def bound_function(*additional_args, **additional_kwargs):
        # Merge arguments
        all_args = args + list(additional_args)
        all_kwargs = {**kwargs, **additional_kwargs}
        return fn(*all_args, **all_kwargs)
    
    return bound_function


# Test functions for demonstration
def add(a, b):
    """Simple addition function."""
    return a + b


def multiply(a, b, c):
    """Multiply three numbers."""
    return a * b * c


def greet(greeting, name):
    """Create a greeting message."""
    return f"{greeting} {name}"


def complex_function(a, b, c=10, d=20, *args, **kwargs):
    """Function with various parameter types."""
    result = a + b + c + d
    for arg in args:
        result += arg
    for value in kwargs.values():
        if isinstance(value, (int, float)):
            result += value
    return result


# Test cases
def test_bind_function():
    """Test the bind_function with various scenarios."""
    
    test_cases = [
        {
            "fn": add,
            "args": [5],
            "additional_args": [10],
            "expected": 15,
            "description": "Bind first argument to add function"
        },
        {
            "fn": multiply,
            "args": [2, 3],
            "additional_args": [4],
            "expected": 24,
            "description": "Bind first two arguments to multiply function"
        },
        {
            "fn": greet,
            "args": ["Hello"],
            "additional_args": ["World"],
            "expected": "Hello World",
            "description": "Bind greeting to greet function"
        },
        {
            "fn": lambda x, y, z: x + y * z,
            "args": [1, 2],
            "additional_args": [3],
            "expected": 7,
            "description": "Bind arguments to lambda function"
        },
        {
            "fn": max,
            "args": [5],
            "additional_args": [3, 7, 2],
            "expected": 7,
            "description": "Bind first argument to built-in max function"
        }
    ]
    
    for i, test in enumerate(test_cases):
        fn = test["fn"]
        args = test["args"]
        additional_args = test["additional_args"]
        expected = test["expected"]
        
        print(f"Test {i+1}: {test['description']}")
        print(f"  Original function: {fn}")
        print(f"  Bound arguments: {args}")
        print(f"  Additional arguments: {additional_args}")
        print(f"  Expected: {expected}")
        
        # Test main implementation
        bound_fn1 = bind_function(fn, args)
        result1 = bound_fn1(*additional_args)
        print(f"  Basic binding: {result1}")
        
        # Test partial implementation
        bound_fn2 = bind_function_partial(fn, args)
        result2 = bound_fn2(*additional_args)
        print(f"  Partial binding: {result2}")
        
        # Test closure implementation
        bound_fn3 = bind_function_closure(fn, args)
        result3 = bound_fn3(*additional_args)
        print(f"  Closure binding: {result3}")
        
        # Test class implementation
        bound_fn4 = bind_function_class(fn, args)
        result4 = bound_fn4(*additional_args)
        print(f"  Class binding: {result4}")
        
        # Verify results
        assert result1 == expected, f"Basic binding failed for test {i+1}"
        assert result2 == expected, f"Partial binding failed for test {i+1}"
        assert result3 == expected, f"Closure binding failed for test {i+1}"
        assert result4 == expected, f"Class binding failed for test {i+1}"
        
        print(f"  ✓ All implementations passed!")
        print()
    
    # Test enhanced version with kwargs
    print("Testing enhanced version with keyword arguments:")
    
    def test_kwargs_fn(a, b, c=100, name="default"):
        return f"a={a}, b={b}, c={c}, name={name}"
    
    bound_kwargs_fn = bind_function_with_kwargs(
        test_kwargs_fn, 
        [1, 2], 
        {"c": 200}
    )
    
    result = bound_kwargs_fn(name="test")
    expected = "a=1, b=2, c=200, name=test"
    print(f"  Kwargs binding result: {result}")
    print(f"  Expected: {expected}")
    assert result == expected
    print("  ✓ Kwargs binding passed!")
    
    # Test with no bound arguments
    print("\nTesting with no bound arguments:")
    identity_bound = bind_function(lambda x: x * 2, [])
    result = identity_bound(5)
    print(f"  No args bound: {result}")
    assert result == 10
    print("  ✓ No args binding passed!")


if __name__ == "__main__":
    test_bind_function()

"""
Complexity Analysis:

1. Basic Binding (bind_function):
   - Time Complexity: O(1) for creating bound function, O(k) per call where k is total arguments
   - Space Complexity: O(n) where n is number of bound arguments

2. Partial Binding (bind_function_partial):
   - Time Complexity: O(1) for binding (uses built-in optimization)
   - Space Complexity: O(n) for storing bound arguments

3. Closure Binding (bind_function_closure):
   - Time Complexity: O(1) for binding, O(k) per call
   - Space Complexity: O(n) for closure variables

4. Class Binding (bind_function_class):
   - Time Complexity: O(1) for binding, O(k) per call
   - Space Complexity: O(n) for instance variables

Key Insights:
- Function binding is a form of partial application
- Creates a new function with some arguments pre-filled
- Useful for creating specialized versions of general functions
- Common pattern in functional programming

Implementation Strategies:
1. Simple closure: Capture bound arguments in closure
2. functools.partial: Use Python's built-in partial application
3. Class-based: Store arguments as instance variables
4. Enhanced: Support both positional and keyword arguments

Use Cases:
- Event handlers with pre-filled parameters
- Configuration functions with default settings
- API clients with pre-filled authentication
- Mathematical functions with fixed coefficients

JavaScript Equivalent:
// function bindFunc(fn, args) {
//     return function(...additionalArgs) {
//         return fn(...args, ...additionalArgs);
//     };
// }

Topics: Functional Programming, Closures, Higher-Order Functions, Partial Application
"""
