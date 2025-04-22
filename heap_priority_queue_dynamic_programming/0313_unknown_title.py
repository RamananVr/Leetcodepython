"""
LeetCode Problem #313: Super Ugly Number

Problem Statement:
A super ugly number is a positive integer whose prime factors are in the array `primes`.
Given an integer `n` and an array of integers `primes`, return the `n`-th super ugly number.

The `n`-th super ugly number is guaranteed to fit in a 32-bit signed integer.

Constraints:
- 1 <= n <= 10^5
- 1 <= primes.length <= 100
- 2 <= primes[i] <= 1000
- primes[i] is guaranteed to be a prime number.
- All the values of primes are unique, and the list is sorted in ascending order.

Example:
Input: n = 12, primes = [2,7,13,19]
Output: 32
Explanation: [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers.

Input: n = 1, primes = [2,3,5]
Output: 1
Explanation: The first super ugly number is always 1.
"""

# Solution
import heapq

def nthSuperUglyNumber(n, primes):
    # Min-heap to store the next potential super ugly numbers
    heap = [1]
    seen = set(heap)  # To avoid duplicates
    ugly_number = 1  # Initialize the first super ugly number

    for _ in range(n):
        # Extract the smallest number from the heap
        ugly_number = heapq.heappop(heap)
        # Generate the next super ugly numbers by multiplying with primes
        for prime in primes:
            next_ugly = ugly_number * prime
            if next_ugly not in seen:
                heapq.heappush(heap, next_ugly)
                seen.add(next_ugly)

    return ugly_number

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 12
    primes1 = [2, 7, 13, 19]
    print(f"Test Case 1: {nthSuperUglyNumber(n1, primes1)}")  # Expected Output: 32

    # Test Case 2
    n2 = 1
    primes2 = [2, 3, 5]
    print(f"Test Case 2: {nthSuperUglyNumber(n2, primes2)}")  # Expected Output: 1

    # Test Case 3
    n3 = 15
    primes3 = [3, 5, 7]
    print(f"Test Case 3: {nthSuperUglyNumber(n3, primes3)}")  # Expected Output: 45

    # Test Case 4
    n4 = 10
    primes4 = [2, 3, 5]
    print(f"Test Case 4: {nthSuperUglyNumber(n4, primes4)}")  # Expected Output: 12

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let k = len(primes) and n = the input value for the nth super ugly number.
- Each number is pushed and popped from the heap exactly once. The heap operations (push and pop) take O(log(n)).
- For each number popped, we generate k new numbers (one for each prime), so the total number of heap operations is O(n * log(n)).
- Therefore, the time complexity is O(n * k * log(n)).

Space Complexity:
- The heap can grow up to size n, so the space complexity for the heap is O(n).
- The `seen` set also stores up to n numbers, so its space complexity is O(n).
- The total space complexity is O(n).
"""

# Topic: Heap (Priority Queue), Dynamic Programming