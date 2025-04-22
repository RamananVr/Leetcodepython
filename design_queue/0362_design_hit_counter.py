"""
LeetCode Question #362: Design Hit Counter

Problem Statement:
Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Implement the `HitCounter` class:
- `HitCounter()` Initializes the object of the hit counter.
- `void hit(int timestamp)` Records a hit at the given `timestamp` (in seconds). Multiple hits may occur at the same timestamp.
- `int getHits(int timestamp)` Returns the number of hits in the past 5 minutes from the given `timestamp`.

Note:
- Each function call is guaranteed to be made with a strictly increasing timestamp.
- The timestamp is in seconds granularity.

Example:
Input:
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]

Output:
[null, null, null, null, 3, null, 4, 3]

Explanation:
HitCounter hitCounter = new HitCounter();
hitCounter.hit(1);       // hit at timestamp 1
hitCounter.hit(2);       // hit at timestamp 2
hitCounter.hit(3);       // hit at timestamp 3
hitCounter.getHits(4);   // get hits at timestamp 4, return 3
hitCounter.hit(300);     // hit at timestamp 300
hitCounter.getHits(300); // get hits at timestamp 300, return 4
hitCounter.getHits(301); // get hits at timestamp 301, return 3
"""

from collections import deque

class HitCounter:
    def __init__(self):
        """
        Initialize the HitCounter object.
        """
        self.hits = deque()  # A deque to store timestamps of hits

    def hit(self, timestamp: int) -> None:
        """
        Record a hit at the given timestamp.
        :param timestamp: int
        """
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes (300 seconds).
        :param timestamp: int
        :return: int
        """
        # Remove timestamps that are older than 300 seconds
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()
        return len(self.hits)


# Example Test Cases
if __name__ == "__main__":
    hitCounter = HitCounter()
    
    # Test Case 1
    hitCounter.hit(1)
    hitCounter.hit(2)
    hitCounter.hit(3)
    print(hitCounter.getHits(4))  # Expected Output: 3
    
    # Test Case 2
    hitCounter.hit(300)
    print(hitCounter.getHits(300))  # Expected Output: 4
    
    # Test Case 3
    print(hitCounter.getHits(301))  # Expected Output: 3

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - `hit(timestamp)`: O(1) - Appending to a deque is an O(1) operation.
   - `getHits(timestamp)`: O(k), where k is the number of timestamps in the deque that are older than 300 seconds. In the worst case, all timestamps in the deque are removed, but this is amortized over multiple calls.

2. Space Complexity:
   - The space complexity is O(n), where n is the number of timestamps stored in the deque. The deque only stores timestamps within the last 300 seconds.

Topic: Design, Queue
"""