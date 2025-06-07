"""
LeetCode Problem #2648: Generate Fibonacci Sequence

Problem Statement:
Write a generator function that returns a generator object which yields the fibonacci sequence.

The fibonacci sequence is defined by the relation Xn = Xn-1 + Xn-2.

The first few numbers of the series are 0, 1, 1, 2, 3, 5, 8, 13, ...

Example 1:
Input: callCount = 5
Output: [0, 1, 1, 2, 3]
Explanation:
const gen = fibGenerator();
gen.next().value; // 0
gen.next().value; // 1
gen.next().value; // 1
gen.next().value; // 2
gen.next().value; // 3

Example 2:
Input: callCount = 0
Output: []
Explanation: gen.next() is never called so nothing is outputted

Constraints:
- 0 <= callCount <= 50
"""

from typing import Generator

def fibGenerator() -> Generator[int, None, None]:
    """
    Generator function that yields Fibonacci numbers indefinitely.
    
    Yields:
        int: Next Fibonacci number in sequence
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def fibGeneratorAlternative() -> Generator[int, None, None]:
    """
    Alternative implementation using explicit state tracking
    """
    prev, curr = 0, 1
    yield prev  # First Fibonacci number is 0
    
    while True:
        yield curr
        prev, curr = curr, prev + curr

def fibGeneratorWithLimit(limit: int) -> Generator[int, None, None]:
    """
    Generator with built-in limit for testing purposes
    
    Args:
        limit: Maximum number of Fibonacci numbers to generate
        
    Yields:
        int: Next Fibonacci number in sequence
    """
    if limit <= 0:
        return
    
    a, b = 0, 1
    count = 0
    
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

class FibonacciGenerator:
    """
    Class-based approach for Fibonacci generation
    """
    
    def __init__(self):
        self.prev = 0
        self.curr = 1
        self.started = False
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.started:
            self.started = True
            return self.prev
        
        result = self.curr
        self.prev, self.curr = self.curr, self.prev + self.curr
        return result

def fibGeneratorRecursive() -> Generator[int, None, None]:
    """
    Recursive approach (less efficient but demonstrates concept)
    """
    def fib(n: int) -> int:
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)
    
    n = 0
    while True:
        yield fib(n)
        n += 1

def fibGeneratorMemoized() -> Generator[int, None, None]:
    """
    Memoized version for better performance with recursive approach
    """
    cache = {0: 0, 1: 1}
    
    def fib_memo(n: int) -> int:
        if n not in cache:
            cache[n] = fib_memo(n - 1) + fib_memo(n - 2)
        return cache[n]
    
    n = 0
    while True:
        yield fib_memo(n)
        n += 1

# JavaScript-like implementation for comparison
def createFibGenerator():
    """
    Function that returns a generator object similar to JavaScript implementation
    """
    def generator():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    
    return generator()

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic usage
    print("Test Case 1: Basic Fibonacci generation")
    gen = fibGenerator()
    result = []
    for _ in range(5):
        result.append(next(gen))
    print(f"First 5 Fibonacci numbers: {result}")  # Expected: [0, 1, 1, 2, 3]
    
    # Test Case 2: Zero calls
    print("\nTest Case 2: Zero calls")
    gen2 = fibGenerator()
    result2 = []
    # No calls to next()
    print(f"Zero calls result: {result2}")  # Expected: []
    
    # Test Case 3: More numbers
    print("\nTest Case 3: First 10 Fibonacci numbers")
    gen3 = fibGenerator()
    result3 = [next(gen3) for _ in range(10)]
    print(f"First 10: {result3}")  # Expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    
    # Test Case 4: Class-based approach
    print("\nTest Case 4: Class-based generator")
    fib_gen = FibonacciGenerator()
    result4 = [next(fib_gen) for _ in range(8)]
    print(f"Class-based result: {result4}")  # Expected: [0, 1, 1, 2, 3, 5, 8, 13]
    
    # Test Case 5: Generator with limit
    print("\nTest Case 5: Generator with limit")
    limited_gen = fibGeneratorWithLimit(6)
    result5 = list(limited_gen)
    print(f"Limited to 6: {result5}")  # Expected: [0, 1, 1, 2, 3, 5]
    
    # Test Case 6: Performance comparison
    print("\nTest Case 6: Performance test")
    import time
    
    # Test iterative approach
    start_time = time.time()
    gen_iter = fibGenerator()
    for _ in range(30):
        next(gen_iter)
    iter_time = time.time() - start_time
    
    # Test memoized approach
    start_time = time.time()
    gen_memo = fibGeneratorMemoized()
    for _ in range(30):
        next(gen_memo)
    memo_time = time.time() - start_time
    
    print(f"Iterative approach time: {iter_time:.6f}s")
    print(f"Memoized approach time: {memo_time:.6f}s")
    
    # Test Case 7: Edge cases
    print("\nTest Case 7: Edge cases")
    gen7 = fibGenerator()
    print(f"First number: {next(gen7)}")  # Expected: 0
    print(f"Second number: {next(gen7)}")  # Expected: 1
    print(f"Third number: {next(gen7)}")  # Expected: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- fibGenerator(): O(1) per next() call, amortized constant time
- fibGeneratorRecursive(): O(2^n) per call due to exponential recursion
- fibGeneratorMemoized(): O(1) per call after initial computation, O(n) for first n calls
- Overall for iterative: O(k) for k calls

Space Complexity:
- fibGenerator(): O(1) - only stores two variables
- fibGeneratorRecursive(): O(n) - recursion stack depth
- fibGeneratorMemoized(): O(n) - memoization cache
- Class-based: O(1) - instance variables only

The iterative approach (fibGenerator) is most efficient with O(1) space and O(1) time per call.

Topic: Generator, Iterator, Mathematical Sequence, Dynamic Programming
"""
