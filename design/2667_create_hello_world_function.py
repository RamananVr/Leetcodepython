"""
LeetCode Question #2667: Create Hello World Function

Problem Statement:
Write a function createHelloWorld. It should return a new function that always returns "Hello World".

Examples:
Example 1:
Input: args = []
Output: "Hello World"
Explanation:
const f = createHelloWorld();
f(); // "Hello World"

The function returned by createHelloWorld should always return "Hello World", regardless of arguments.

Example 2:
Input: args = [{},null,42]
Output: "Hello World"
Explanation: Any arguments passed to the function are ignored.

Constraints:
- 0 <= args.length <= 10
"""

from typing import List, Any, Callable

def createHelloWorld() -> Callable[..., str]:
    """
    Creates a function that always returns "Hello World".
    """
    def hello_world(*args) -> str:
        return "Hello World"
    
    return hello_world

def createHelloWorldLambda() -> Callable[..., str]:
    """
    Lambda version of the function.
    """
    return lambda *args: "Hello World"

def createHelloWorldClosure() -> Callable[..., str]:
    """
    Using closure to demonstrate the concept.
    """
    message = "Hello World"
    
    def inner(*args) -> str:
        return message
    
    return inner

# Test Cases
if __name__ == "__main__":
    test_cases = [
        ([], "Hello World"),
        ([{}], "Hello World"),
        ([None, 42], "Hello World"),
        ([1, 2, 3, 4, 5], "Hello World"),
        (["test", True, {"key": "value"}], "Hello World")
    ]
    
    print("Testing main approach:")
    f = createHelloWorld()
    for args, expected in test_cases:
        result = f(*args)
        print(f"f({args}) = '{result}', expected = '{expected}', {'✓' if result == expected else '✗'}")
    
    print("\nTesting lambda approach:")
    f_lambda = createHelloWorldLambda()
    for args, expected in test_cases:
        result = f_lambda(*args)
        print(f"f_lambda({args}) = '{result}', expected = '{expected}', {'✓' if result == expected else '✗'}")
    
    print("\nTesting closure approach:")
    f_closure = createHelloWorldClosure()
    for args, expected in test_cases:
        result = f_closure(*args)
        print(f"f_closure({args}) = '{result}', expected = '{expected}', {'✓' if result == expected else '✗'}")

"""
Time and Space Complexity Analysis:

All Approaches:
Time Complexity: O(1) - constant time to return the string
Space Complexity: O(1) - only storing the constant string

Key Insights:
1. This is a basic closure/function factory pattern
2. The returned function ignores all arguments
3. Demonstrates how functions can return other functions
4. Useful for understanding JavaScript-style function creation in Python

Topic: Design, Functional Programming, Closures
"""
