"""
LeetCode Problem #1226: The Dining Philosophers

Problem Statement:
Five silent philosophers sit at a round table with bowls of spaghetti. Forks are placed between each pair of adjacent philosophers.

Each philosopher must alternately think and eat. However, a philosopher can only eat spaghetti when they have both left and right forks. Each fork can be held by only one philosopher, and a fork can be picked up only if it is not being used.

Eating is not limited by the availability of spaghetti or stomach space; an infinite supply and infinite capacity are assumed.

Design a discipline of behavior (a concurrent algorithm) such that no philosopher will starve; i.e., each can forever continue to alternate between eating and thinking, assuming that no philosopher can know when others may want to eat or think.

The philosophers' behavior is defined by the following structure:

class DiningPhilosophers:
    def __init__(self):
        pass

    def wantsToEat(self, philosopher: int, 
                   pickLeftFork: 'Callable[[], None]', 
                   pickRightFork: 'Callable[[], None]', 
                   eat: 'Callable[[], None]', 
                   putLeftFork: 'Callable[[], None]', 
                   putRightFork: 'Callable[[], None]') -> None:
        pass

Implement the DiningPhilosophers class:

- DiningPhilosophers() Initializes the object of the dining philosophers.
- wantsToEat(philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork) 
  is called when a philosopher wants to eat. 
  - philosopher: The id of the philosopher who wants to eat (0-indexed).
  - pickLeftFork: An anonymous function to pick up the left fork.
  - pickRightFork: An anonymous function to pick up the right fork.
  - eat: An anonymous function to eat the food.
  - putLeftFork: An anonymous function to put down the left fork.
  - putRightFork: An anonymous function to put down the right fork.

The function should synchronize the philosophers such that no two philosophers access the same fork simultaneously.

Constraints:
- 1 <= calls to wantsToEat <= 10^4
"""

from threading import Lock

class DiningPhilosophers:
    def __init__(self):
        # Initialize a lock for each fork
        self.forks = [Lock() for _ in range(5)]

    def wantsToEat(self, philosopher: int, 
                   pickLeftFork: 'Callable[[], None]', 
                   pickRightFork: 'Callable[[], None]', 
                   eat: 'Callable[[], None]', 
                   putLeftFork: 'Callable[[], None]', 
                   putRightFork: 'Callable[[], None]') -> None:
        # Determine the left and right fork indices
        left_fork = philosopher
        right_fork = (philosopher + 1) % 5

        # To avoid deadlock, always pick up the lower-indexed fork first
        if left_fork < right_fork:
            first_fork, second_fork = left_fork, right_fork
        else:
            first_fork, second_fork = right_fork, left_fork

        # Acquire the locks in the correct order
        with self.forks[first_fork]:
            with self.forks[second_fork]:
                # Pick up forks, eat, and put down forks
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()

# Example Test Cases
if __name__ == "__main__":
    import threading

    # Initialize the DiningPhilosophers class
    dp = DiningPhilosophers()

    # Define the actions for testing
    def pickLeftFork():
        print("Picked up left fork")

    def pickRightFork():
        print("Picked up right fork")

    def eat():
        print("Eating")

    def putLeftFork():
        print("Put down left fork")

    def putRightFork():
        print("Put down right fork")

    # Simulate philosophers eating
    def philosopher_thread(philosopher_id):
        dp.wantsToEat(philosopher_id, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork)

    # Create threads for 5 philosophers
    threads = []
    for i in range(5):
        t = threading.Thread(target=philosopher_thread, args=(i,))
        threads.append(t)

    # Start all threads
    for t in threads:
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

"""
Time Complexity:
- Each philosopher's actions (picking up forks, eating, and putting down forks) are constant time operations.
- Therefore, the time complexity for each call to `wantsToEat` is O(1).

Space Complexity:
- We use an array of 5 locks, which is O(5) = O(1) space.

Topic: Concurrency, Multithreading
"""