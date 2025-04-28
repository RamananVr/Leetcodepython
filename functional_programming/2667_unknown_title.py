"""
LeetCode Problem #2667: Create Hello World Function

Problem Statement:
Write a function `createHelloWorld` that returns a new function. The new function, when called, should return the string "Hello World".

Example:
Input: args = []
Output: "Hello World"

Explanation:
The function returned by `createHelloWorld` does not take any arguments and always returns "Hello World".

Constraints:
- The returned function should not take any arguments.
- The returned function should always return the string "Hello World".
"""

# Solution
def createHelloWorld():
    """
    Returns a function that, when called, returns the string "Hello World".
    """
    def hello_world():
        return "Hello World"
    return hello_world

# Example Test Cases
if __name__ == "__main__":
    # Create the function
    hello = createHelloWorld()
    
    # Test Case 1
    # Call the returned function and check the output
    assert hello() == "Hello World", "Test Case 1 Failed"
    
    # Test Case 2
    # Call the returned function multiple times
    assert hello() == "Hello World", "Test Case 2 Failed"
    assert hello() == "Hello World", "Test Case 2 Failed"
    
    print("All test cases passed!")

"""
Time Complexity Analysis:
- The `createHelloWorld` function itself runs in O(1) time since it only defines and returns a function.
- The returned `hello_world` function also runs in O(1) time since it simply returns a string.

Space Complexity Analysis:
- The space complexity is O(1) as no additional data structures are used, and the returned function does not store any state.

Topic: Functional Programming
"""