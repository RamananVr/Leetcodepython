"""
LeetCode Problem #933: Number of Recent Calls

Problem Statement:
You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:
- RecentCounter() Initializes the counter with an empty request log.
- int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that have happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].

It is guaranteed that every call to ping uses a strictly larger value of t than before.

Constraints:
- 1 <= t <= 10^9
- At most 10^4 calls will be made to ping.

Example:
Input:
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output:
[null, 1, 2, 3, 3]

Explanation:
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1,100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1,100,3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1,100,3001,3002], range is [2,3002], return 3
"""

# Solution
from collections import deque

class RecentCounter:
    def __init__(self):
        # Initialize a deque to store the timestamps of requests
        self.requests = deque()

    def ping(self, t: int) -> int:
        # Add the new request timestamp to the deque
        self.requests.append(t)
        
        # Remove timestamps that are outside the range [t - 3000, t]
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        
        # Return the number of requests within the range
        return len(self.requests)

# Example Test Cases
if __name__ == "__main__":
    # Initialize the RecentCounter object
    recentCounter = RecentCounter()
    
    # Test cases
    print(recentCounter.ping(1))     # Output: 1
    print(recentCounter.ping(100))   # Output: 2
    print(recentCounter.ping(3001))  # Output: 3
    print(recentCounter.ping(3002))  # Output: 3

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Each call to `ping` involves appending a timestamp to the deque (O(1)) and removing outdated timestamps from the front of the deque.
   - In the worst case, all timestamps in the deque are outdated and need to be removed, which takes O(k), where k is the number of timestamps in the deque.
   - Since the total number of calls to `ping` is limited to 10^4, the amortized time complexity for each call is O(1).

2. Space Complexity:
   - The deque stores at most 10^4 timestamps, so the space complexity is O(k), where k is the number of timestamps in the deque.

Topic: Queue
"""