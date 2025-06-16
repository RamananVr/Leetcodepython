"""
LeetCode Question #2726: Calculator with Method Chaining

Problem Statement:
Design a `Calculator` class. The class should provide the mathematical operations of addition, subtraction, multiplication, division, and exponentiation. It should also allow consecutive operations to be performed using method chaining. The `Calculator` class constructor should accept a number which serves as the initial value.

Your Calculator class should have the following methods:
- `add` - This method adds the given number value to the result and returns a Calculator object.
- `subtract` - This method subtracts the given number value from the result and returns a Calculator object.
- `multiply` - This method multiplies the result by the given number value and returns a Calculator object.
- `divide` - This method divides the result by the given number value and returns a Calculator object. If the passed value is 0, an error "Division by zero is not allowed" should be thrown.
- `power` - This method raises the result to the power of the given number value and returns a Calculator object.
- `getResult` - This method returns the result.

Solutions within 10^-5 of the actual result are considered correct.

Constraints:
- Actions are valid mathematical operations
- Calculations with 0 division should return proper error
- `2 <= actions.length <= 2 * 10^5`
- `1 <= values.length <= 2 * 10^6`
- `-1000 <= actions[i] <= 1000`

Example:
Input: actions = ["Calculator", "add", "subtract", "getResult"], values = [10, 5, 7, null]
Output: 8
Explanation: 
new Calculator(10).add(5).subtract(7).getResult() // 10 + 5 - 7 = 8

Input: actions = ["Calculator", "multiply", "power", "getResult"], values = [2, 5, 2, null]
Output: 100
Explanation:
new Calculator(2).multiply(5).power(2).getResult() // (2 * 5) ^ 2 = 100

Input: actions = ["Calculator", "divide", "getResult"], values = [20, 0, null]
Output: "Division by zero is not allowed"
Explanation:
new Calculator(20).divide(0).getResult() // 20 / 0 => Error
"""

class Calculator:
    """
    Calculator class with method chaining support.
    """
    
    def __init__(self, value: float):
        """
        Initialize calculator with starting value.
        
        Args:
            value: Initial numeric value
        """
        self.result = value
    
    def add(self, value: float) -> 'Calculator':
        """
        Add value to current result.
        
        Args:
            value: Number to add
            
        Returns:
            Calculator instance for method chaining
        """
        self.result += value
        return self
    
    def subtract(self, value: float) -> 'Calculator':
        """
        Subtract value from current result.
        
        Args:
            value: Number to subtract
            
        Returns:
            Calculator instance for method chaining
        """
        self.result -= value
        return self
    
    def multiply(self, value: float) -> 'Calculator':
        """
        Multiply current result by value.
        
        Args:
            value: Number to multiply by
            
        Returns:
            Calculator instance for method chaining
        """
        self.result *= value
        return self
    
    def divide(self, value: float) -> 'Calculator':
        """
        Divide current result by value.
        
        Args:
            value: Number to divide by
            
        Returns:
            Calculator instance for method chaining
            
        Raises:
            ValueError: If value is 0 (division by zero)
        """
        if value == 0:
            raise ValueError("Division by zero is not allowed")
        self.result /= value
        return self
    
    def power(self, value: float) -> 'Calculator':
        """
        Raise current result to the power of value.
        
        Args:
            value: Exponent
            
        Returns:
            Calculator instance for method chaining
        """
        self.result = self.result ** value
        return self
    
    def getResult(self) -> float:
        """
        Get the current result.
        
        Returns:
            Current calculated value
        """
        return self.result

class CalculatorWithHistory:
    """
    Calculator with operation history tracking.
    """
    
    def __init__(self, value: float):
        self.result = value
        self.history = [("init", value)]
    
    def add(self, value: float) -> 'CalculatorWithHistory':
        self.result += value
        self.history.append(("add", value))
        return self
    
    def subtract(self, value: float) -> 'CalculatorWithHistory':
        self.result -= value
        self.history.append(("subtract", value))
        return self
    
    def multiply(self, value: float) -> 'CalculatorWithHistory':
        self.result *= value
        self.history.append(("multiply", value))
        return self
    
    def divide(self, value: float) -> 'CalculatorWithHistory':
        if value == 0:
            raise ValueError("Division by zero is not allowed")
        self.result /= value
        self.history.append(("divide", value))
        return self
    
    def power(self, value: float) -> 'CalculatorWithHistory':
        self.result = self.result ** value
        self.history.append(("power", value))
        return self
    
    def getResult(self) -> float:
        return self.result
    
    def getHistory(self) -> list:
        """Get operation history."""
        return self.history.copy()
    
    def undo(self) -> 'CalculatorWithHistory':
        """Undo the last operation."""
        if len(self.history) <= 1:
            return self
        
        # Remove last operation
        self.history.pop()
        
        # Recalculate from beginning
        self.result = self.history[0][1]  # Initial value
        for operation, value in self.history[1:]:
            if operation == "add":
                self.result += value
            elif operation == "subtract":
                self.result -= value
            elif operation == "multiply":
                self.result *= value
            elif operation == "divide":
                self.result /= value
            elif operation == "power":
                self.result = self.result ** value
        
        return self

class CalculatorWithPrecision:
    """
    Calculator with configurable precision.
    """
    
    def __init__(self, value: float, precision: int = 5):
        self.result = value
        self.precision = precision
    
    def _round_result(self):
        """Round result to specified precision."""
        self.result = round(self.result, self.precision)
    
    def add(self, value: float) -> 'CalculatorWithPrecision':
        self.result += value
        self._round_result()
        return self
    
    def subtract(self, value: float) -> 'CalculatorWithPrecision':
        self.result -= value
        self._round_result()
        return self
    
    def multiply(self, value: float) -> 'CalculatorWithPrecision':
        self.result *= value
        self._round_result()
        return self
    
    def divide(self, value: float) -> 'CalculatorWithPrecision':
        if value == 0:
            raise ValueError("Division by zero is not allowed")
        self.result /= value
        self._round_result()
        return self
    
    def power(self, value: float) -> 'CalculatorWithPrecision':
        self.result = self.result ** value
        self._round_result()
        return self
    
    def getResult(self) -> float:
        return self.result

class CalculatorSafe:
    """
    Calculator with safe error handling that doesn't raise exceptions.
    """
    
    def __init__(self, value: float):
        self.result = value
        self.error = None
    
    def add(self, value: float) -> 'CalculatorSafe':
        if self.error:
            return self
        self.result += value
        return self
    
    def subtract(self, value: float) -> 'CalculatorSafe':
        if self.error:
            return self
        self.result -= value
        return self
    
    def multiply(self, value: float) -> 'CalculatorSafe':
        if self.error:
            return self
        self.result *= value
        return self
    
    def divide(self, value: float) -> 'CalculatorSafe':
        if self.error:
            return self
        if value == 0:
            self.error = "Division by zero is not allowed"
            return self
        self.result /= value
        return self
    
    def power(self, value: float) -> 'CalculatorSafe':
        if self.error:
            return self
        try:
            self.result = self.result ** value
        except (OverflowError, ValueError) as e:
            self.error = str(e)
        return self
    
    def getResult(self):
        if self.error:
            return self.error
        return self.result
    
    def hasError(self) -> bool:
        return self.error is not None

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1 - Basic operations
    calc = Calculator(10)
    result = calc.add(5).subtract(7).getResult()
    print(f"Test 1 - Expected: 8, Got: {result}")
    assert result == 8
    
    # Test Case 2 - Multiplication and power
    calc = Calculator(2)
    result = calc.multiply(5).power(2).getResult()
    print(f"Test 2 - Expected: 100, Got: {result}")
    assert result == 100
    
    # Test Case 3 - Division by zero
    calc = Calculator(20)
    try:
        result = calc.divide(0).getResult()
        assert False, "Should have raised exception"
    except ValueError as e:
        print(f"Test 3 - Expected error: {e}")
        assert str(e) == "Division by zero is not allowed"
    
    # Test Case 4 - Complex chain
    calc = Calculator(5)
    result = calc.add(3).multiply(2).subtract(4).divide(2).getResult()
    expected = ((5 + 3) * 2 - 4) / 2  # (8 * 2 - 4) / 2 = 12 / 2 = 6
    print(f"Test 4 - Expected: {expected}, Got: {result}")
    assert result == expected
    
    # Test Case 5 - Power operations
    calc = Calculator(3)
    result = calc.power(3).add(2).power(0.5).getResult()
    expected = ((3 ** 3) + 2) ** 0.5  # (27 + 2) ** 0.5 = 29 ** 0.5 ≈ 5.385
    print(f"Test 5 - Expected: ~{expected:.3f}, Got: {result:.3f}")
    assert abs(result - expected) < 1e-5
    
    # Test Case 6 - Negative numbers
    calc = Calculator(-10)
    result = calc.add(15).subtract(20).multiply(-1).getResult()
    expected = ((-10 + 15) - 20) * -1  # (5 - 20) * -1 = 15
    print(f"Test 6 - Expected: {expected}, Got: {result}")
    assert result == expected
    
    # Test Case 7 - Decimal operations
    calc = Calculator(1.5)
    result = calc.multiply(2.5).add(1.25).divide(2).getResult()
    expected = ((1.5 * 2.5) + 1.25) / 2  # (3.75 + 1.25) / 2 = 2.5
    print(f"Test 7 - Expected: {expected}, Got: {result}")
    assert abs(result - expected) < 1e-10
    
    # Test Calculator with History
    calc_hist = CalculatorWithHistory(10)
    result = calc_hist.add(5).multiply(2).undo().getResult()
    print(f"Test 8 - History with undo - Expected: 15, Got: {result}")
    assert result == 15  # 10 + 5 = 15 (multiply undone)
    
    # Test Calculator with Precision
    calc_prec = CalculatorWithPrecision(1, precision=2)
    result = calc_prec.divide(3).getResult()
    print(f"Test 9 - Precision - Expected: 0.33, Got: {result}")
    assert result == 0.33
    
    # Test Safe Calculator
    calc_safe = CalculatorSafe(10)
    result = calc_safe.divide(0).add(5).getResult()
    print(f"Test 10 - Safe calculator - Expected: error message, Got: {result}")
    assert result == "Division by zero is not allowed"
    
    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

Basic Calculator:
1. Time Complexity: O(1) per operation
   - Each mathematical operation (add, subtract, multiply, divide, power) is O(1)
   - Method chaining doesn't add overhead
   - getResult() is O(1)

2. Space Complexity: O(1)
   - Only stores current result value
   - No additional data structures

Calculator with History:
1. Time Complexity: 
   - Operations: O(1) per operation
   - Undo: O(n) where n is number of operations (requires recalculation)
   - getHistory: O(n) for copying history

2. Space Complexity: O(n)
   - Stores history of all operations
   - Each operation tuple is constant size

Calculator with Precision:
1. Time Complexity: O(1) per operation
   - Rounding operation is O(1)
   - Same as basic calculator with small constant overhead

2. Space Complexity: O(1)
   - Only additional precision setting stored

Safe Calculator:
1. Time Complexity: O(1) per operation
   - Error checking adds minimal overhead
   - Early return on error state

2. Space Complexity: O(1)
   - Additional error string storage (constant)

Key Design Patterns:
1. Method Chaining (Fluent Interface):
   - Each method returns 'self' for chaining
   - Enables readable operation sequences
   - Maintains object state throughout chain

2. Error Handling Strategies:
   - Exception throwing (standard approach)
   - Error state tracking (safe approach)
   - Both prevent invalid calculations

3. State Management:
   - Immutable operations (could return new instance)
   - Mutable operations (modifies current instance)
   - History tracking for undo functionality

Real-world Considerations:
- Floating-point precision issues
- Overflow handling for large numbers
- Complex number support
- Thread safety for concurrent access
- Validation of input parameters

Topic: Object-Oriented Design, Method Chaining, Error Handling, State Management
"""
