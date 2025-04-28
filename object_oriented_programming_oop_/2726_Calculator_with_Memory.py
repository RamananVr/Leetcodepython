"""
LeetCode Problem #2726: Calculator with Memory

Problem Statement:
You are tasked with implementing a simple calculator with memory functionality. The calculator should support the following operations:
1. Addition: `add(x)` - Adds the value `x` to the current value.
2. Subtraction: `subtract(x)` - Subtracts the value `x` from the current value.
3. Multiplication: `multiply(x)` - Multiplies the current value by `x`.
4. Division: `divide(x)` - Divides the current value by `x`. If `x` is 0, the operation should throw an error.
5. Reset: `reset()` - Resets the current value to 0.
6. Get Value: `get_value()` - Returns the current value.

The calculator starts with an initial value of 0. Implement a class `Calculator` that supports these operations.

Constraints:
- All operations should be implemented as methods of the `Calculator` class.
- Division by zero should raise a `ZeroDivisionError`.
- The `x` values for all operations will be integers or floats.

Your task is to implement the `Calculator` class with the above functionality.
"""

class Calculator:
    def __init__(self):
        """Initialize the calculator with a value of 0."""
        self.value = 0

    def add(self, x):
        """Add x to the current value."""
        self.value += x

    def subtract(self, x):
        """Subtract x from the current value."""
        self.value -= x

    def multiply(self, x):
        """Multiply the current value by x."""
        self.value *= x

    def divide(self, x):
        """Divide the current value by x. Raise ZeroDivisionError if x is 0."""
        if x == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        self.value /= x

    def reset(self):
        """Reset the current value to 0."""
        self.value = 0

    def get_value(self):
        """Return the current value."""
        return self.value


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic operations
    calc = Calculator()
    calc.add(10)
    assert calc.get_value() == 10, "Test Case 1 Failed"
    calc.subtract(5)
    assert calc.get_value() == 5, "Test Case 1 Failed"
    calc.multiply(3)
    assert calc.get_value() == 15, "Test Case 1 Failed"
    calc.divide(5)
    assert calc.get_value() == 3, "Test Case 1 Failed"

    # Test Case 2: Division by zero
    try:
        calc.divide(0)
    except ZeroDivisionError:
        pass
    else:
        assert False, "Test Case 2 Failed"

    # Test Case 3: Reset functionality
    calc.reset()
    assert calc.get_value() == 0, "Test Case 3 Failed"

    # Test Case 4: Chained operations
    calc.add(20)
    calc.multiply(2)
    calc.subtract(10)
    calc.divide(5)
    assert calc.get_value() == 6, "Test Case 4 Failed"

    print("All test cases passed!")


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Each operation (add, subtract, multiply, divide, reset, get_value) is O(1) since they involve a constant number of operations.

2. Space Complexity:
   - The space complexity is O(1) because the calculator only stores a single value (`self.value`) and does not use any additional data structures.

Topic: Object-Oriented Programming (OOP)
"""