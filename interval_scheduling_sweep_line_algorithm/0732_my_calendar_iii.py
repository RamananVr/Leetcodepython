"""
LeetCode Question #732: My Calendar III

Problem Statement:
A `MyCalendarThree` class is implemented to keep track of events and their maximum overlap. 
You are tasked with implementing the following methods:

1. `__init__()`:
   Initializes the object.

2. `book(start: int, end: int) -> int`:
   Adds an event with a start time `start` and an end time `end` (exclusive). 
   Returns an integer representing the maximum number of events that are simultaneously ongoing 
   at any point in time after the new event is added.

Constraints:
- 0 <= start < end <= 10^9
- At most 400 calls will be made to `book`.

Example:
Input:
    ["MyCalendarThree", "book", "book", "book", "book", "book"]
    [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10]]
Output:
    [null, 1, 1, 2, 3, 3]

Explanation:
    MyCalendarThree myCalendarThree = new MyCalendarThree();
    myCalendarThree.book(10, 20); // returns 1
    myCalendarThree.book(50, 60); // returns 1
    myCalendarThree.book(10, 40); // returns 2
    myCalendarThree.book(5, 15);  // returns 3
    myCalendarThree.book(5, 10);  // returns 3
"""

# Solution
from collections import defaultdict

class MyCalendarThree:
    def __init__(self):
        # Use a dictionary to store the changes in event counts at specific times
        self.timeline = defaultdict(int)

    def book(self, start: int, end: int) -> int:
        # Increment the count at the start time and decrement at the end time
        self.timeline[start] += 1
        self.timeline[end] -= 1
        
        # Calculate the maximum overlap using a running sum
        ongoing_events = 0
        max_overlap = 0
        for time in sorted(self.timeline.keys()):
            ongoing_events += self.timeline[time]
            max_overlap = max(max_overlap, ongoing_events)
        
        return max_overlap

# Example Test Cases
if __name__ == "__main__":
    # Initialize the MyCalendarThree object
    myCalendarThree = MyCalendarThree()
    
    # Test cases
    print(myCalendarThree.book(10, 20))  # Output: 1
    print(myCalendarThree.book(50, 60))  # Output: 1
    print(myCalendarThree.book(10, 40))  # Output: 2
    print(myCalendarThree.book(5, 15))   # Output: 3
    print(myCalendarThree.book(5, 10))   # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- The `book` method iterates over the keys of the `timeline` dictionary, which can grow with the number of calls to `book`.
- Sorting the keys takes O(K log K), where K is the number of unique timestamps in the `timeline`.
- Therefore, the time complexity for each `book` call is O(K log K).

Space Complexity:
- The `timeline` dictionary stores the changes in event counts at specific times. In the worst case, there can be up to 2 * N unique timestamps (start and end for each event), where N is the number of calls to `book`.
- Therefore, the space complexity is O(N).

Topic: Interval Scheduling / Sweep Line Algorithm
"""