"""
LeetCode Problem #1117: Building H2O

Problem Statement:
There are two kinds of threads: oxygen and hydrogen. Your goal is to group these threads to form water molecules. 
There is a barrier where each thread has to wait until a complete molecule can be formed. Hydrogen and oxygen threads 
will be given a releaseHydrogen and releaseOxygen method respectively, which will allow them to pass the barrier. 
These threads should pass the barrier in groups of three: two hydrogen threads and one oxygen thread. 

Write a class `H2O` that has the following methods:
- `hydrogen(releaseHydrogen: Callable[[], None]) -> None`: This method is called when a hydrogen thread is ready to 
  release hydrogen. It accepts a callable `releaseHydrogen` that outputs "H".
- `oxygen(releaseOxygen: Callable[[], None]) -> None`: This method is called when an oxygen thread is ready to 
  release oxygen. It accepts a callable `releaseOxygen` that outputs "O".

Your solution must ensure that:
- If an oxygen thread calls `releaseOxygen`, then exactly two hydrogen threads have also called `releaseHydrogen` 
  before the oxygen thread can pass the barrier.
- If a hydrogen thread calls `releaseHydrogen`, then there must be an oxygen thread and another hydrogen thread 
  that have also called the respective methods before the hydrogen thread can pass the barrier.

Constraints:
- Total number of threads will be less than 20.
- There will be an equal number of hydrogen and oxygen threads.

Example:
Input: "HOH"
Output: "HHO" or "HOH" (any valid combination that forms water molecules is acceptable)
"""

from threading import Semaphore, Barrier
from typing import Callable

class H2O:
    def __init__(self):
        # Semaphores to control the number of hydrogen and oxygen threads
        self.hydrogen_semaphore = Semaphore(2)  # Allow up to 2 hydrogen threads
        self.oxygen_semaphore = Semaphore(1)   # Allow 1 oxygen thread
        # Barrier to ensure exactly 2 hydrogen and 1 oxygen threads are released together
        self.barrier = Barrier(3)

    def hydrogen(self, releaseHydrogen: Callable[[], None]) -> None:
        # Acquire hydrogen semaphore
        self.hydrogen_semaphore.acquire()
        # Wait for the barrier to synchronize with other threads
        self.barrier.wait()
        # Release hydrogen
        releaseHydrogen()
        # Release the hydrogen semaphore for the next thread
        self.hydrogen_semaphore.release()

    def oxygen(self, releaseOxygen: Callable[[], None]) -> None:
        # Acquire oxygen semaphore
        self.oxygen_semaphore.acquire()
        # Wait for the barrier to synchronize with other threads
        self.barrier.wait()
        # Release oxygen
        releaseOxygen()
        # Release the oxygen semaphore for the next thread
        self.oxygen_semaphore.release()

# Example Test Cases
if __name__ == "__main__":
    import threading

    def releaseHydrogen():
        print("H", end="")

    def releaseOxygen():
        print("O", end="")

    # Test case 1: Input "HOH"
    h2o = H2O()
    threads = []
    for char in "HOH":
        if char == "H":
            threads.append(threading.Thread(target=h2o.hydrogen, args=(releaseHydrogen,)))
        elif char == "O":
            threads.append(threading.Thread(target=h2o.oxygen, args=(releaseOxygen,)))

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print()  # Output: "HHO" or "HOH"

    # Test case 2: Input "OOHHHH"
    h2o = H2O()
    threads = []
    for char in "OOHHHH":
        if char == "H":
            threads.append(threading.Thread(target=h2o.hydrogen, args=(releaseHydrogen,)))
        elif char == "O":
            threads.append(threading.Thread(target=h2o.oxygen, args=(releaseOxygen,)))

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print()  # Output: Any valid combination like "HHOHHO"

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each thread acquires a semaphore and waits at the barrier. The barrier ensures synchronization, 
  and the semaphore ensures that only the required number of threads proceed. 
  The operations are constant time, so the time complexity is O(1) per thread.

Space Complexity:
- The space complexity is O(1) because we use a fixed number of semaphores and a barrier, 
  regardless of the number of threads.

Topic: Concurrency, Multithreading
"""