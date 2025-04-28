"""
LeetCode Question #1114: Print in Order

Problem Statement:
Suppose we have a class:

class Foo:
    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.

The same instance of Foo will be passed to three different threads. Thread A will call `first()`, thread B will call `second()`, and thread C will call `third()`. Design a mechanism to ensure that `second()` is executed after `first()`, and `third()` is executed after `second()`.

Note:
- We do not know how the threads will be scheduled in the operating system, even if the `first()`, `second()`, and `third()` methods are called in order.
- We must ensure that the output is always "firstsecondthird".

Constraints:
- The input to the methods is a callable function that outputs a string.
- There will be exactly three threads.
- The methods `first`, `second`, and `third` will be called exactly once.

"""

from threading import Lock

class Foo:
    def __init__(self):
        # Initialize two locks. Lock for second() is initially locked.
        self.lock2 = Lock()
        self.lock3 = Lock()
        self.lock2.acquire()  # Lock for second() is locked initially.
        self.lock3.acquire()  # Lock for third() is locked initially.

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        # Release the lock for second() so it can execute.
        self.lock2.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # Wait until first() releases the lock.
        with self.lock2:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            # Release the lock for third() so it can execute.
            self.lock3.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # Wait until second() releases the lock.
        with self.lock3:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()


# Example Test Cases
if __name__ == "__main__":
    import threading

    def printFirst():
        print("first", end="")

    def printSecond():
        print("second", end="")

    def printThird():
        print("third", end="")

    # Create an instance of Foo
    foo = Foo()

    # Create threads for first, second, and third
    thread1 = threading.Thread(target=foo.first, args=(printFirst,))
    thread2 = threading.Thread(target=foo.second, args=(printSecond,))
    thread3 = threading.Thread(target=foo.third, args=(printThird,))

    # Start threads in random order
    thread3.start()
    thread1.start()
    thread2.start()

    # Wait for all threads to complete
    thread1.join()
    thread2.join()
    thread3.join()

    # Expected Output: "firstsecondthird"

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each method (`first`, `second`, `third`) executes in O(1) time since they only perform a single operation (printing and releasing a lock).

Space Complexity:
- The space complexity is O(1) as we only use a constant amount of space for the locks.

Topic: Concurrency
"""