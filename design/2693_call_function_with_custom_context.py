"""
2693. Call Function with Custom Context

PROBLEM STATEMENT:
Implement a function that allows calling any function with a custom context (this binding).
The function should:
1. Accept a function and a context object
2. Allow calling the function with the provided context
3. Support passing arguments to the function
4. Return the result of the function call

This is similar to JavaScript's Function.prototype.call() and Function.prototype.apply() methods.

EXAMPLES:
Example 1:
function greet(name) { return `Hello ${name}, I'm ${this.name}`; }
const person = { name: "Alice" };
result = callWithContext(greet, person, ["Bob"]);
Output: "Hello Bob, I'm Alice"

Example 2:
function sum(a, b) { return a + b + this.offset; }
const context = { offset: 10 };
result = callWithContext(sum, context, [5, 3]);
Output: 18

CONSTRAINTS:
- The function can have any number of parameters
- The context can be any object
- Arguments should be passed as an array
"""

def call_function_with_custom_context():
    """
    Implementation of calling functions with custom context.
    """
    
    class ContextualFunction:
        def __init__(self, func, context):
            self.func = func
            self.context = context
        
        def call(self, *args):
            """Call function with bound context"""
            # Create a wrapper that injects context
            if hasattr(self.func, '__self__'):
                # It's already a bound method
                return self.func(*args)
            else:
                # Simulate 'this' binding by passing context as first argument
                # or by using a closure that captures the context
                return self._call_with_context(*args)
        
        def _call_with_context(self, *args):
            """Internal method to call function with context"""
            # For Python, we simulate 'this' by passing context as a parameter
            # or by monkey-patching the function temporarily
            
            # Save original function
            original_func = self.func
            
            # Create a new function that has access to context
            def bound_function(*args):
                # Inject context into function's local namespace
                # This is a simplified version - in real JS, 'this' would be available
                return original_func(self.context, *args)
            
            return bound_function(*args)
    
    def call_with_context(func, context, args=None):
        """
        Call a function with a custom context.
        
        Args:
            func: The function to call
            context: The context object (equivalent to 'this')
            args: List of arguments to pass to the function
        
        Returns:
            The result of the function call
        """
        if args is None:
            args = []
        
        # Create a contextual function
        contextual_func = ContextualFunction(func, context)
        return contextual_func.call(*args)
    
    # Alternative implementation using closures
    def bind_context(func, context):
        """
        Bind a context to a function, returning a new function.
        """
        def bound_function(*args, **kwargs):
            # Simulate JavaScript 'this' by passing context as first argument
            return func(context, *args, **kwargs)
        
        return bound_function
    
    # Implementation with method injection
    def apply_with_context(func, context, args=None):
        """
        Apply function with context (similar to Function.prototype.apply)
        """
        if args is None:
            args = []
        
        # Temporarily add method to context object
        method_name = f"_temp_method_{id(func)}"
        setattr(context, method_name, func)
        
        try:
            # Call the method
            method = getattr(context, method_name)
            if hasattr(func, '__code__') and func.__code__.co_argcount > 0:
                # Check if function expects 'self' parameter
                if len(args) == func.__code__.co_argcount - 1:
                    result = method(*args)
                else:
                    result = method(*args)
            else:
                result = method(*args)
            return result
        finally:
            # Clean up
            if hasattr(context, method_name):
                delattr(context, method_name)
    
    return call_with_context, bind_context, apply_with_context

def test_call_function_with_custom_context():
    """Test the context binding implementation."""
    call_with_context, bind_context, apply_with_context = call_function_with_custom_context()
    
    # Test 1: Simple function with context
    def greet(context, name):
        return f"Hello {name}, I'm {context['name']}"
    
    person = {"name": "Alice"}
    result = call_with_context(greet, person, ["Bob"])
    assert result == "Hello Bob, I'm Alice"
    
    # Test 2: Math function with context
    def add_with_offset(context, a, b):
        return a + b + context["offset"]
    
    math_context = {"offset": 10}
    result = call_with_context(add_with_offset, math_context, [5, 3])
    assert result == 18
    
    # Test 3: Bound function
    def multiply(context, x, y):
        return x * y * context["factor"]
    
    multiplier_context = {"factor": 3}
    bound_multiply = bind_context(multiply, multiplier_context)
    result = bound_multiply(4, 5)
    assert result == 60
    
    # Test 4: Function with no arguments
    def get_value(context):
        return context["value"]
    
    value_context = {"value": 42}
    result = call_with_context(get_value, value_context, [])
    assert result == 42
    
    # Test 5: Complex context object
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    def introduce(context, greeting="Hi"):
        return f"{greeting}, I'm {context.name} and I'm {context.age} years old"
    
    person_obj = Person("Charlie", 25)
    result = call_with_context(introduce, person_obj, ["Hello"])
    assert result == "Hello, I'm Charlie and I'm 25 years old"
    
    # Test 6: Apply with context
    def calculate_area(context, length, width):
        return length * width * context["scale"]
    
    area_context = {"scale": 2.5}
    result = apply_with_context(calculate_area, area_context, [4, 6])
    assert result == 60.0
    
    print("All test cases passed!")

# Additional utility functions for advanced context binding
def create_context_manager():
    """Create a context manager for function calls"""
    
    class ContextManager:
        def __init__(self):
            self.contexts = {}
        
        def register_context(self, name, context):
            """Register a named context"""
            self.contexts[name] = context
        
        def call_with_named_context(self, func, context_name, args=None):
            """Call function with a named context"""
            if context_name not in self.contexts:
                raise ValueError(f"Context '{context_name}' not found")
            
            context = self.contexts[context_name]
            return self._call_with_context(func, context, args or [])
        
        def _call_with_context(self, func, context, args):
            """Internal context calling logic"""
            def bound_func(*args):
                return func(context, *args)
            return bound_func(*args)
    
    return ContextManager

if __name__ == "__main__":
    test_call_function_with_custom_context()

"""
COMPLEXITY ANALYSIS:
- Time Complexity: O(1) for binding context, O(k) for function execution where k is function complexity
- Space Complexity: O(1) for context binding (not counting function execution space)

TOPICS: Design, Functional Programming, Context Binding, Closures

KEY INSIGHTS:
1. Context binding simulates JavaScript's 'this' mechanism in Python
2. Closures provide an elegant way to capture and bind context
3. Temporary method injection allows for true method-like behavior
4. Function introspection helps determine correct parameter passing
5. Context managers can provide organized access to multiple contexts
"""
