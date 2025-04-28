"""
LeetCode Problem #1115: Print FooBar Alternately

Problem Statement:
Suppose you are given the following code:

class FooBar:
    def __init__(self, n: int):
        pass

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        pass

    def bar(self, printBar: 'Callable[[], None]') -> None:
        pass

The same instance of FooBar will be passed to two different threads. Thread A will call foo() while thread B will call bar(). 
Modify the given class to output "foobar" n times. 

Specifically, output "foo" followed by "bar" n times.

Example 1:
Input: n = 1
Output: "foobar"

Example 2:
Input: n = 2
Output: "foobarfoobar"

Constraints:
- 1 <= n <= 1000
"""

from threading import Lock

class FooBar:
    def __init__(self, n: int):
        self.n = n
        self.foo_lock = Lock()
        self.bar_lock = Lock()
        self.bar_lock.acquire()  # Initially lock bar so foo can run first

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            self.foo_lock.acquire()  # Wait for foo_lock to be available
            printFoo()  # Print "foo"
            self.bar_lock.release()  # Allow bar to run

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            self.bar_lock.acquire()  # Wait for bar_lock to be available
            printBar()  # Print "bar"
            self.foo_lock.release()  # Allow foo to run


# Example Test Cases
if __name__ == "__main__":
    import threading

    def printFoo():
        print("foo", end="")

    def printBar():
        print("bar", end="")

    # Test Case 1
    n = 1
    foobar = FooBar(n)
    thread1 = threading.Thread(target=foobar.foo, args=(printFoo,))
    thread2 = threading.Thread(target=foobar.bar, args=(printBar,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print()  # Output: "foobar"

    # Test Case 2
    n = 2
    foobar = FooBar(n)
    thread1 = threading.Thread(target=foobar.foo, args=(printFoo,))
    thread2 = threading.Thread(target=foobar.bar, args=(printBar,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print()  # Output: "foobarfoobar"

    # Test Case 3
    n = 5
    foobar = FooBar(n)
    thread1 = threading.Thread(target=foobar.foo, args=(printFoo,))
    thread2 = threading.Thread(target=foobar.bar, args=(printBar,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print()  # Output: "foobarfoobarfoobarfoobarfoobar"


"""
Time and Space Complexity Analysis:

Time Complexity:
- Each thread runs `n` iterations, and each iteration involves acquiring and releasing a lock.
- Acquiring and releasing a lock are O(1) operations.
- Therefore, the time complexity is O(n).

Space Complexity:
- The space complexity is O(1) since we are only using two locks and no additional data structures.

Topic: Multithreading, Concurrency
"""