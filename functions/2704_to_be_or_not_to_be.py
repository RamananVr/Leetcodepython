"""
LeetCode Problem #2704: To Be Or Not To Be

Problem Statement:
Write a function `expect` that helps with testing. It should return an object with the following two functions:
- `toBe(val)`: accepts another value and returns `true` if the two values are equal or throws the string "Not Equal" otherwise.
- `notToBe(val)`: accepts another value and returns `true` if the two values are not equal or throws the string "Equal" otherwise.

Constraints:
- 1 <= calls.length <= 15
- 1 <= calls[i].length <= 100
- All function calls are valid.

Note: This is a JavaScript problem but we'll implement it in Python for consistency.
"""

class ExpectObject:
    """
    Helper class that provides testing functionality similar to JavaScript's expect.
    """
    
    def __init__(self, actual_value):
        """
        Initialize with the actual value to be tested.
        
        :param actual_value: The value to be tested
        """
        self.actual_value = actual_value
    
    def toBe(self, expected_value):
        """
        Checks if actual value equals expected value.
        
        :param expected_value: The expected value
        :return: bool - True if values are equal
        :raises: Exception with "Not Equal" if values are not equal
        """
        if self.actual_value == expected_value:
            return True
        else:
            raise Exception("Not Equal")
    
    def notToBe(self, expected_value):
        """
        Checks if actual value does not equal expected value.
        
        :param expected_value: The value that should not equal actual
        :return: bool - True if values are not equal
        :raises: Exception with "Equal" if values are equal
        """
        if self.actual_value != expected_value:
            return True
        else:
            raise Exception("Equal")

def expect(val):
    """
    Creates an expect object for testing.
    
    :param val: The value to be tested
    :return: ExpectObject - Object with toBe and notToBe methods
    """
    return ExpectObject(val)

# Alternative functional implementation
def expectFunctional(val):
    """
    Functional implementation that returns a dictionary with functions.
    
    :param val: The value to be tested
    :return: dict - Dictionary with toBe and notToBe functions
    """
    def toBe(expected):
        if val == expected:
            return True
        else:
            raise Exception("Not Equal")
    
    def notToBe(expected):
        if val != expected:
            return True
        else:
            raise Exception("Equal")
    
    return {
        'toBe': toBe,
        'notToBe': notToBe
    }

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: toBe success
    try:
        result = expect(5).toBe(5)
        print(f"expect(5).toBe(5): {result}")  # Output: True
    except Exception as e:
        print(f"Error: {e}")

    # Test Case 2: toBe failure
    try:
        result = expect(5).toBe(null := None)
        print(f"expect(5).toBe(null): {result}")
    except Exception as e:
        print(f"expect(5).toBe(null): Error: {e}")  # Output: Error: Not Equal

    # Test Case 3: notToBe success
    try:
        result = expect(5).notToBe(null := None)
        print(f"expect(5).notToBe(null): {result}")  # Output: True
    except Exception as e:
        print(f"Error: {e}")

    # Test Case 4: notToBe failure
    try:
        result = expect(5).notToBe(5)
        print(f"expect(5).notToBe(5): {result}")
    except Exception as e:
        print(f"expect(5).notToBe(5): Error: {e}")  # Output: Error: Equal

    # Test Case 5: String comparison
    try:
        result = expect("hello").toBe("hello")
        print(f"expect('hello').toBe('hello'): {result}")  # Output: True
    except Exception as e:
        print(f"Error: {e}")

    # Test functional implementation
    print("\nTesting functional implementation:")
    try:
        result = expectFunctional(10)['toBe'](10)
        print(f"expectFunctional(10)['toBe'](10): {result}")  # Output: True
    except Exception as e:
        print(f"Error: {e}")

    try:
        result = expectFunctional(10)['notToBe'](5)
        print(f"expectFunctional(10)['notToBe'](5): {result}")  # Output: True
    except Exception as e:
        print(f"Error: {e}")

"""
Time Complexity Analysis:
- Time complexity: O(1) - All operations are constant time comparisons.

Space Complexity Analysis:
- Space complexity: O(1) - Only storing references to values.

Topic: Object-Oriented Programming, Testing, Functions
"""
