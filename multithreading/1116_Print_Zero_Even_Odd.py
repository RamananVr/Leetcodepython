"""
LeetCode Problem #1116: Print Zero Even Odd

Problem Statement:
You have a function `printNumber` that can be called to output any integer to the console. 
You are given an instance of the class `ZeroEvenOdd` that has three functions: `zero`, `even`, and `odd`. 
The same instance of `ZeroEvenOdd` will be passed to three different threads:

1. Thread A will call `zero()` which should only output the number 0.
2. Thread B will call `even()` which should only output even numbers.
3. Thread C will call `odd()` which should only output odd numbers.

Each of these threads is given a `printNumber` function to output the number. 
Modify the given class to ensure that the output sequence is correct and that every number is output exactly once.

Constraints:
- 1 <= n <= 1000

Example:
Input: n = 2
Output: "0102"
Explanation: There are three threads being fired asynchronously. One of them calls zero(), 
the other calls even(), and the last one calls odd(). "0102" is the correct output.

Input: n = 5
Output: "0102030405"
"""

from threading import Lock

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_lock = Lock()
        self.odd_lock = Lock()
        self.even_lock = Lock()
        
        # Initially, only zero_lock is unlocked
        self.odd_lock.acquire()
        self.even_lock.acquire()

    def zero(self, printNumber):
        for i in range(1, self.n + 1):
            self.zero_lock.acquire()
            printNumber(0)
            # Release the appropriate lock based on whether the next number is odd or even
            if i % 2 == 1:
                self.odd_lock.release()
            else:
                self.even_lock.release()

    def even(self, printNumber):
        for i in range(2, self.n + 1, 2):
            self.even_lock.acquire()
            printNumber(i)
            self.zero_lock.release()

    def odd(self, printNumber):
        for i in range(1, self.n + 1, 2):
            self.odd_lock.acquire()
            printNumber(i)
            self.zero_lock.release()


# Example Test Cases
if __name__ == "__main__":
    import threading

    def printNumber(x):
        print(x, end="")

    # Test Case 1
    n = 2
    zero_even_odd = ZeroEvenOdd(n)
    threads = [
        threading.Thread(target=zero_even_odd.zero, args=(printNumber,)),
        threading.Thread(target=zero_even_odd.even, args=(printNumber,)),
        threading.Thread(target=zero_even_odd.odd, args=(printNumber,))
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print()  # Output: "0102"

    # Test Case 2
    n = 5
    zero_even_odd = ZeroEvenOdd(n)
    threads = [
        threading.Thread(target=zero_even_odd.zero, args=(printNumber,)),
        threading.Thread(target=zero_even_odd.even, args=(printNumber,)),
        threading.Thread(target=zero_even_odd.odd, args=(printNumber,))
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print()  # Output: "0102030405"


"""
Time and Space Complexity Analysis:

Time Complexity:
- The `zero` function runs a loop from 1 to n, so its time complexity is O(n).
- The `even` function runs a loop for all even numbers up to n, so its time complexity is O(n/2), which simplifies to O(n).
- The `odd` function runs a loop for all odd numbers up to n, so its time complexity is O(n/2), which simplifies to O(n).
- Overall, the time complexity is O(n).

Space Complexity:
- The space complexity is O(1) as we are only using a few locks and no additional data structures.

Topic: Multithreading
"""