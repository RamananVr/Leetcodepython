"""
LeetCode Problem #2620: Counter

Problem Statement:
Write a function `createCounter`. It should accept an initial integer `n` and return a function. 
This returned function, when called, should return the next integer (starting from `n`) in an 
incremental sequence (n, n + 1, n + 2, ...).

Example:
Input: 
    const counter = createCounter(10)
    counter() # 10
    counter() # 11
    counter() # 12

Constraints:
- The initial integer `n` is guaranteed to be a valid integer.
- The returned function should maintain its state across multiple calls.
"""

# Solution
def createCounter(n: int):
    """
    Creates a counter function that starts from the given integer `n` and increments by 1
    each time the returned function is called.
    
    :param n: The starting integer for the counter.
    :return: A function that returns the next integer in the sequence when called.
    """
    def counter():
        nonlocal n
        current = n
        n += 1
        return current
    
    return counter

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    counter1 = createCounter(10)
    print(counter1())  # Output: 10
    print(counter1())  # Output: 11
    print(counter1())  # Output: 12

    # Test Case 2
    counter2 = createCounter(0)
    print(counter2())  # Output: 0
    print(counter2())  # Output: 1
    print(counter2())  # Output: 2

    # Test Case 3
    counter3 = createCounter(-5)
    print(counter3())  # Output: -5
    print(counter3())  # Output: -4
    print(counter3())  # Output: -3

# Time and Space Complexity Analysis
"""
Time Complexity:
- Each call to the returned function `counter` takes O(1) time since it simply increments a variable and returns a value.

Space Complexity:
- The space complexity is O(1) as we only store a single integer `n` in memory for the counter's state.
"""

# Topic: Closures, Functions