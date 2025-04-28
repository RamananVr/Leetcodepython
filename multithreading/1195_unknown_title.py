"""
LeetCode Problem #1195: Fizz Buzz Multithreaded

Problem Statement:
You have the four functions:
- `printFizz` that prints the word "fizz" to the console.
- `printBuzz` that prints the word "buzz" to the console.
- `printFizzBuzz` that prints the word "fizzbuzz" to the console.
- `printNumber` that prints a given integer to the console.

You are given an instance of the class `FizzBuzz` that has four methods:
- `fizz`: Call `printFizz` if the number is divisible by 3 and not 5.
- `buzz`: Call `printBuzz` if the number is divisible by 5 and not 3.
- `fizzbuzz`: Call `printFizzBuzz` if the number is divisible by both 3 and 5.
- `number`: Call `printNumber` if the number is not divisible by 3 or 5.

The same instance of `FizzBuzz` will be passed to four different threads:
- Thread A will call `fizz()`.
- Thread B will call `buzz()`.
- Thread C will call `fizzbuzz()`.
- Thread D will call `number()`.

Modify the given class to ensure that the four methods work correctly in a multithreaded environment.

Constraints:
- 1 <= n <= 50
"""

from threading import Lock
from typing import Callable

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.current = 1
        self.lock = Lock()

    def fizz(self, printFizz: Callable[[], None]) -> None:
        while True:
            with self.lock:
                if self.current > self.n:
                    return
                if self.current % 3 == 0 and self.current % 5 != 0:
                    printFizz()
                    self.current += 1

    def buzz(self, printBuzz: Callable[[], None]) -> None:
        while True:
            with self.lock:
                if self.current > self.n:
                    return
                if self.current % 5 == 0 and self.current % 3 != 0:
                    printBuzz()
                    self.current += 1

    def fizzbuzz(self, printFizzBuzz: Callable[[], None]) -> None:
        while True:
            with self.lock:
                if self.current > self.n:
                    return
                if self.current % 3 == 0 and self.current % 5 == 0:
                    printFizzBuzz()
                    self.current += 1

    def number(self, printNumber: Callable[[int], None]) -> None:
        while True:
            with self.lock:
                if self.current > self.n:
                    return
                if self.current % 3 != 0 and self.current % 5 != 0:
                    printNumber(self.current)
                    self.current += 1


# Example Test Cases
if __name__ == "__main__":
    import threading

    def printFizz():
        print("fizz", end=" ")

    def printBuzz():
        print("buzz", end=" ")

    def printFizzBuzz():
        print("fizzbuzz", end=" ")

    def printNumber(x):
        print(x, end=" ")

    n = 15
    fizzbuzz = FizzBuzz(n)

    threads = [
        threading.Thread(target=fizzbuzz.fizz, args=(printFizz,)),
        threading.Thread(target=fizzbuzz.buzz, args=(printBuzz,)),
        threading.Thread(target=fizzbuzz.fizzbuzz, args=(printFizzBuzz,)),
        threading.Thread(target=fizzbuzz.number, args=(printNumber,))
    ]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

# Time and Space Complexity Analysis
# Time Complexity: O(n)
# - Each number from 1 to n is processed exactly once, and the operations performed for each number are constant time.

# Space Complexity: O(1)
# - The space used is constant, as we only use a few variables and locks, regardless of the input size.

# Topic: Multithreading