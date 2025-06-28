"""
LeetCode Problem 2803: Factorial Generator

Write a generator function that yields the factorial of numbers starting from n.

The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.

Constraints:
- 0 <= n <= 18

Example 1:
Input: n = 5
Output: [120, 720, 5040, 40320, 362880]
Explanation: 
factorial(5) = 120
factorial(6) = 720
factorial(7) = 5040
factorial(8) = 40320
factorial(9) = 362880

Example 2:
Input: n = 2
Output: [2, 6, 24, 120, 720]
Explanation:
factorial(2) = 2
factorial(3) = 6
factorial(4) = 24
factorial(5) = 120
factorial(6) = 720

Example 3:
Input: n = 0
Output: [1, 1, 2, 6, 24]
Explanation:
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2
factorial(3) = 6
factorial(4) = 24
"""

def factorial_generator(n):
    """
    Approach 1: Generator with Incremental Calculation
    
    Calculate factorial incrementally to avoid recomputation.
    
    Time Complexity: O(1) per yield after first calculation
    Space Complexity: O(1)
    """
    if n == 0:
        factorial = 1
        current = 0
    else:
        # Calculate initial factorial
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        current = n
    
    while True:
        yield factorial
        current += 1
        factorial *= current

def factorial_generator_recursive(n):
    """
    Approach 2: Generator with Memoization
    
    Use memoization to cache factorial values.
    
    Time Complexity: O(k) for k-th factorial (if not cached)
    Space Complexity: O(k) for memoization
    """
    memo = {}
    
    def factorial(num):
        if num in memo:
            return memo[num]
        if num <= 1:
            return 1
        memo[num] = num * factorial(num - 1)
        return memo[num]
    
    current = n
    while True:
        yield factorial(current)
        current += 1

def factorial_generator_iterative(n):
    """
    Approach 3: Pure Iterative Generator
    
    Calculate each factorial from scratch (less efficient but simpler).
    
    Time Complexity: O(k) for k-th factorial
    Space Complexity: O(1)
    """
    def factorial(num):
        if num <= 1:
            return 1
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result
    
    current = n
    while True:
        yield factorial(current)
        current += 1

def factorial_generator_optimized(n):
    """
    Approach 4: Optimized with Precomputed Values
    
    Use precomputed factorials for small numbers.
    
    Time Complexity: O(1) for precomputed, O(k) for larger values
    Space Complexity: O(1)
    """
    # Precomputed factorials for 0-18
    precomputed = [
        1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 
        3628800, 39916800, 479001600, 6227020800, 87178291200,
        1307674368000, 20922789888000, 355687428096000, 6402373705728000
    ]
    
    current = n
    if current < len(precomputed):
        factorial = precomputed[current]
    else:
        # Calculate from the last precomputed value
        factorial = precomputed[-1]
        for i in range(len(precomputed), current + 1):
            factorial *= i
    
    while True:
        if current < len(precomputed):
            yield precomputed[current]
        else:
            yield factorial
        
        current += 1
        if current < len(precomputed):
            factorial = precomputed[current]
        else:
            factorial *= current

class FactorialGenerator:
    """
    Approach 5: Class-based Generator
    
    Object-oriented approach with state management.
    """
    def __init__(self, n):
        self.current = n
        if n == 0:
            self.factorial = 1
        else:
            self.factorial = 1
            for i in range(1, n + 1):
                self.factorial *= i
    
    def __iter__(self):
        return self
    
    def __next__(self):
        result = self.factorial
        self.current += 1
        self.factorial *= self.current
        return result
    
    def next(self):
        """For Python 2 compatibility"""
        return self.__next__()

def factorial_generator_async():
    """
    Approach 6: Async Generator (Python 3.6+)
    
    Asynchronous generator for concurrent scenarios.
    """
    async def async_factorial_gen(n):
        factorial = 1
        if n > 0:
            for i in range(1, n + 1):
                factorial *= i
        
        current = n
        while True:
            yield factorial
            current += 1
            factorial *= current
    
    return async_factorial_gen

# Test cases
def test_factorial_generator():
    test_cases = [
        (5, [120, 720, 5040, 40320, 362880]),
        (2, [2, 6, 24, 120, 720]),
        (0, [1, 1, 2, 6, 24]),
        (1, [1, 2, 6, 24, 120]),
        (3, [6, 24, 120, 720, 5040])
    ]
    
    for n, expected in test_cases:
        # Test different approaches
        gen1 = factorial_generator(n)
        gen2 = factorial_generator_recursive(n)
        gen3 = factorial_generator_iterative(n)
        gen4 = factorial_generator_optimized(n)
        gen5 = FactorialGenerator(n)
        
        results1 = [next(gen1) for _ in range(len(expected))]
        results2 = [next(gen2) for _ in range(len(expected))]
        results3 = [next(gen3) for _ in range(len(expected))]
        results4 = [next(gen4) for _ in range(len(expected))]
        results5 = [next(gen5) for _ in range(len(expected))]
        
        print(f"Input: n={n}")
        print(f"Expected: {expected}")
        print(f"Incremental: {results1}")
        print(f"Memoized: {results2}")
        print(f"Iterative: {results3}")
        print(f"Optimized: {results4}")
        print(f"Class-based: {results5}")
        
        all_correct = (results1 == expected and results2 == expected and 
                      results3 == expected and results4 == expected and 
                      results5 == expected)
        print(f"✓ Passed: {all_correct}\n")

def test_large_factorials():
    """Test with larger numbers to verify efficiency"""
    gen = factorial_generator(10)
    
    # Get first 5 factorials starting from 10!
    factorials = [next(gen) for _ in range(5)]
    expected = [3628800, 39916800, 479001600, 6227020800, 87178291200]
    
    print("Large factorial test:")
    print(f"Results: {factorials}")
    print(f"Expected: {expected}")
    print(f"✓ Passed: {factorials == expected}")

if __name__ == "__main__":
    test_factorial_generator()
    test_large_factorials()

"""
Topics: Math, Generator, Iterator Pattern
Difficulty: Easy

Key Insights:
1. Generators provide memory-efficient lazy evaluation
2. Incremental calculation avoids recomputation
3. Memoization trades space for time
4. Precomputed values optimize common cases
5. Class-based generators offer more control

Companies: Microsoft, Google, Amazon
"""
