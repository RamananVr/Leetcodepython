"""
LeetCode Problem #2102: Sequentially Ordinal Rank Tracker

Problem Statement:
Design a system that manages the ranking of items with a score. Each item has a unique name and a score. Implement the SORTracker class:

- SORTracker() Initializes the tracker system.
- void add(string name, int score) Adds an item with the given name and score to the system.
- string get() Returns the name of the item with the highest rank, then increases the number of times the get method has been called.

The ranking is determined by the following rules:
1. Higher score items are ranked higher.
2. If two items have the same score, the lexicographically smaller name is ranked higher.

Constraints:
- name consists of lowercase English letters, and its length is between 1 and 50, inclusive.
- 1 <= score <= 10^9
- At any moment, the number of calls to add and get will not exceed 4 * 10^4 in total.
"""

from sortedcontainers import SortedList

class SORTracker:
    def __init__(self):
        # Use a sorted list to maintain the items in sorted order
        # Each element in the list is a tuple (-score, name) to sort by score descending and name lexicographically
        self.items = SortedList()
        self.rank = 0  # Tracks the number of times `get` has been called

    def add(self, name: str, score: int) -> None:
        # Add the item to the sorted list
        # Use (-score, name) to sort by descending score and lexicographical order
        self.items.add((-score, name))

    def get(self) -> str:
        # Retrieve the item at the current rank and increment the rank
        result = self.items[self.rank][1]
        self.rank += 1
        return result


# Example Test Cases
if __name__ == "__main__":
    tracker = SORTracker()
    tracker.add("bravo", 2)
    tracker.add("alpha", 2)
    tracker.add("charlie", 1)
    print(tracker.get())  # Output: "alpha" (highest rank: score=2, lexicographically smallest)
    print(tracker.get())  # Output: "bravo" (next highest rank: score=2, next lexicographically smallest)
    tracker.add("delta", 3)
    print(tracker.get())  # Output: "delta" (highest rank: score=3)


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - `add`: The `add` operation inserts an element into the `SortedList`, which takes O(log n) time.
   - `get`: The `get` operation retrieves an element at a specific index, which takes O(1) time.
   - Overall, for `m` operations (where m is the total number of `add` and `get` calls), the time complexity is O(m log n), where n is the number of elements in the tracker.

2. Space Complexity:
   - The `SortedList` stores all the items, so the space complexity is O(n), where n is the number of items added.

Topic: Data Structures (SortedList, Priority Queue)
"""