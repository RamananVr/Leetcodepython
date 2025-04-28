"""
LeetCode Question #2618: Check if Object is a Function

Problem Statement:
You are given an object obj. Write a function to check if obj is a function. 
Return true if obj is a function, otherwise return false.

Constraints:
- obj can be of any type.
- You may assume that the input is valid and does not require additional validation.

Example:
Input: obj = lambda x: x + 1
Output: true

Input: obj = 42
Output: false

Input: obj = "hello"
Output: false
"""

# Solution
def is_function(obj):
    """
    This function checks if the given object is a function.

    Args:
    obj: Any type of object.

    Returns:
    bool: True if obj is a function, False otherwise.
    """
    return callable(obj)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: obj is a lambda function
    obj1 = lambda x: x + 1
    print(is_function(obj1))  # Expected Output: True

    # Test Case 2: obj is an integer
    obj2 = 42
    print(is_function(obj2))  # Expected Output: False

    # Test Case 3: obj is a string
    obj3 = "hello"
    print(is_function(obj3))  # Expected Output: False

    # Test Case 4: obj is a built-in function
    obj4 = len
    print(is_function(obj4))  # Expected Output: True

    # Test Case 5: obj is a list
    obj5 = [1, 2, 3]
    print(is_function(obj5))  # Expected Output: False

    # Test Case 6: obj is a user-defined function
    def custom_function():
        return "I am a function"
    print(is_function(custom_function))  # Expected Output: True

# Time and Space Complexity Analysis
"""
Time Complexity:
- The callable() function in Python runs in O(1) time since it simply checks the type of the object.

Space Complexity:
- The space complexity is O(1) as no additional data structures are used.

Overall, the solution is highly efficient.

Topic: Type Checking
"""