"""
2797. Partial Function with Placeholders

Problem Statement:
Given a function fn and an array args, return a partial function that can be called with 
remaining arguments. Use placeholders ("_") to indicate positions where arguments should 
be filled in later.

When the partial function is called, fill in the placeholders with the provided arguments 
in order, then call the original function with the complete argument list.

Constraints:
- fn is a function
- args is an array that may contain placeholders "_"
- 1 <= args.length <= 5
- The partial function will be called with the correct number of arguments to fill placeholders

Test Cases:
1. Input: fn = (a,b,c) => a+b+c, args = [1,"_",3]
   Call: partial(2)
   Output: 6
   
2. Input: fn = (...args) => args, args = ["_","_","_"]
   Call: partial(1,2,3)
   Output: [1,2,3]
"""

from typing import Any, Callable, List, Union

def partial(fn: Callable, args: List[Union[Any, str]]) -> Callable:
    """
    Create a partial function with placeholders.
    
    Algorithm:
    1. Store the original function and arguments template
    2. Return a new function that fills placeholders when called
    3. Replace placeholders with provided arguments in order
    
    Time Complexity: O(n) where n is number of arguments
    Space Complexity: O(n) for storing arguments
    """
    def partial_fn(*new_args):
        # Create a copy of the original args
        filled_args = args.copy()
        new_arg_index = 0
        
        # Fill in placeholders with new arguments
        for i in range(len(filled_args)):
            if filled_args[i] == "_":
                if new_arg_index < len(new_args):
                    filled_args[i] = new_args[new_arg_index]
                    new_arg_index += 1
        
        # Call original function with filled arguments
        return fn(*filled_args)
    
    return partial_fn

def partialAdvanced(fn: Callable, args: List[Union[Any, str]]) -> Callable:
    """
    Advanced partial function with validation and error handling.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    placeholder_count = sum(1 for arg in args if arg == "_")
    
    def partial_fn(*new_args):
        if len(new_args) != placeholder_count:
            raise ValueError(f"Expected {placeholder_count} arguments, got {len(new_args)}")
        
        filled_args = []
        new_arg_index = 0
        
        for arg in args:
            if arg == "_":
                filled_args.append(new_args[new_arg_index])
                new_arg_index += 1
            else:
                filled_args.append(arg)
        
        return fn(*filled_args)
    
    return partial_fn

def partialWithMultiplePlaceholders(fn: Callable, args: List[Union[Any, str]]) -> Callable:
    """
    Support multiple placeholder types and nested partial application.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def partial_fn(*new_args):
        filled_args = []
        new_arg_index = 0
        
        for arg in args:
            if isinstance(arg, str) and arg.startswith("_"):
                # Support numbered placeholders like "_1", "_2"
                if new_arg_index < len(new_args):
                    filled_args.append(new_args[new_arg_index])
                    new_arg_index += 1
                else:
                    filled_args.append(arg)  # Keep unfilled placeholder
            else:
                filled_args.append(arg)
        
        # If there are still placeholders, return another partial function
        if any(isinstance(arg, str) and arg.startswith("_") for arg in filled_args):
            return partialWithMultiplePlaceholders(fn, filled_args)
        else:
            return fn(*filled_args)
    
    return partial_fn

def partialFunctional(fn: Callable, args: List[Union[Any, str]]) -> Callable:
    """
    Functional programming style implementation.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def partial_fn(*new_args):
        def fill_placeholder(arg, new_args_iter):
            if arg == "_":
                try:
                    return next(new_args_iter)
                except StopIteration:
                    raise ValueError("Not enough arguments to fill placeholders")
            return arg
        
        new_args_iter = iter(new_args)
        filled_args = [fill_placeholder(arg, new_args_iter) for arg in args]
        
        # Check if all new args were used
        try:
            next(new_args_iter)
            raise ValueError("Too many arguments provided")
        except StopIteration:
            pass  # All args used, this is correct
        
        return fn(*filled_args)
    
    return partial_fn

class PartialFunction:
    """
    Class-based implementation for more complex partial function behavior.
    """
    
    def __init__(self, fn: Callable, args: List[Union[Any, str]]):
        self.fn = fn
        self.args = args
        self.placeholder_count = sum(1 for arg in args if arg == "_")
    
    def __call__(self, *new_args):
        if len(new_args) != self.placeholder_count:
            raise ValueError(f"Expected {self.placeholder_count} arguments, got {len(new_args)}")
        
        filled_args = []
        new_arg_index = 0
        
        for arg in self.args:
            if arg == "_":
                filled_args.append(new_args[new_arg_index])
                new_arg_index += 1
            else:
                filled_args.append(arg)
        
        return self.fn(*filled_args)
    
    def __repr__(self):
        return f"PartialFunction({self.fn.__name__}, {self.args})"

# Test functions for examples
def add_three(a, b, c):
    """Test function: sum of three numbers."""
    return a + b + c

def multiply_all(*args):
    """Test function: product of all arguments."""
    result = 1
    for arg in args:
        result *= arg
    return result

def concat_strings(*args):
    """Test function: concatenate all string arguments."""
    return ''.join(str(arg) for arg in args)

# Test cases
def test_partial_basic():
    # Test case 1: Basic partial with one placeholder
    partial_add = partial(add_three, [1, "_", 3])
    result1 = partial_add(2)
    print(f"Test 1 - Expected: 6, Got: {result1}")
    
    # Test case 2: Multiple placeholders
    partial_add2 = partial(add_three, ["_", "_", "_"])
    result2 = partial_add2(1, 2, 3)
    print(f"Test 2 - Expected: 6, Got: {result2}")
    
    # Test case 3: No placeholders
    partial_add3 = partial(add_three, [1, 2, 3])
    result3 = partial_add3()
    print(f"Test 3 - Expected: 6, Got: {result3}")

def test_partial_advanced():
    # Test with different functions
    partial_mult = partialAdvanced(multiply_all, [2, "_", "_", 3])
    result1 = partial_mult(4, 5)
    print(f"Multiply test - Expected: 120, Got: {result1}")
    
    # Test string concatenation
    partial_concat = partial(concat_strings, ["Hello", "_", "World", "_"])
    result2 = partial_concat(" ", "!")
    print(f"Concat test - Expected: 'Hello World!', Got: '{result2}'")

def test_class_based():
    # Test class-based implementation
    pf = PartialFunction(add_three, [10, "_", 20])
    result = pf(5)
    print(f"Class-based test - Expected: 35, Got: {result}")
    print(f"Partial function repr: {pf}")

def test_error_handling():
    # Test error cases
    try:
        partial_fn = partialAdvanced(add_three, [1, "_", 3])
        partial_fn(2, 4)  # Too many arguments
    except ValueError as e:
        print(f"Error handling test 1: {e}")
    
    try:
        partial_fn = partialAdvanced(add_three, [1, "_", "_"])
        partial_fn(2)  # Too few arguments
    except ValueError as e:
        print(f"Error handling test 2: {e}")

if __name__ == "__main__":
    test_partial_basic()
    print()
    test_partial_advanced()
    print()
    test_class_based()
    print()
    test_error_handling()

"""
Topic Classification: Functional Programming, Higher-Order Functions, Closures

Key Insights:
1. Partial application allows creating specialized functions from general ones
2. Placeholders indicate positions to be filled later
3. Closures capture the original function and argument template
4. Error handling important for robust implementation

Complexity Analysis:
- Time Complexity: O(n) where n is number of arguments
- Space Complexity: O(n) for storing argument template and filled values
"""
