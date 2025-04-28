"""
LeetCode Problem #2648: Generate Fibonacci Sequence

Problem Statement:
Write a generator function `fibonacciGenerator()` that returns a generator object which yields the Fibonacci sequence. 
The Fibonacci sequence is defined as follows:
- The first two numbers of the sequence are 0 and 1.
- The nth number is the sum of the (n-1)th and (n-2)th numbers (n >= 2).

The generator should be able to generate an infinite sequence of Fibonacci numbers.

Example:
    gen = fibonacciGenerator()
    print(next(gen))  # 0
    print(next(gen))  # 1
    print(next(gen))  # 1
    print(next(gen))  # 2
    print(next(gen))  # 3
    print(next(gen))  # 5
"""

# Solution
def fibonacciGenerator():
    """
    A generator function to yield the Fibonacci sequence indefinitely.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Example Test Cases
if __name__ == "__main__":
    gen = fibonacciGenerator()
    print(next(gen))  # 0
    print(next(gen))  # 1
    print(next(gen))  # 1
    print(next(gen))  # 2
    print(next(gen))  # 3
    print(next(gen))  # 5
    print(next(gen))  # 8
    print(next(gen))  # 13

"""
Time Complexity Analysis:
- Each call to `next()` in the generator performs a constant amount of work (updating two variables and yielding a value).
- Therefore, the time complexity for generating the next Fibonacci number is O(1).

Space Complexity Analysis:
- The generator maintains only two variables (`a` and `b`) to store the current and next Fibonacci numbers.
- Therefore, the space complexity is O(1).

Topic: Generators
"""