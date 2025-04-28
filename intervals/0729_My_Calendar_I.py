"""
LeetCode Problem #729: My Calendar I

Problem Statement:
You are implementing a program to manage a calendar of events. Each event is represented as a pair of integers [start, end], 
where `start` represents the start time and `end` represents the end time. The program should support adding new events to the calendar.

A new event can be added if and only if it does not overlap with any existing events in the calendar. Specifically, an event [start, end) 
is considered to overlap with another event [s, e) if `start < e` and `s < end`.

Implement the `MyCalendar` class:
- `MyCalendar()` Initializes the calendar object.
- `bool book(int start, int end)` Adds a new event [start, end) to the calendar. Returns `true` if the event can be added successfully 
  without overlapping with any existing events, and `false` otherwise.

Constraints:
- 0 <= start < end <= 10^9
- At most 1000 calls will be made to the `book` function.
"""

class MyCalendar:
    def __init__(self):
        # Initialize an empty list to store events
        self.events = []

    def book(self, start: int, end: int) -> bool:
        # Check for overlap with existing events
        for s, e in self.events:
            if start < e and s < end:  # Overlap condition
                return False
        # If no overlap, add the event to the calendar
        self.events.append((start, end))
        return True


# Example Test Cases
if __name__ == "__main__":
    # Initialize the calendar
    my_calendar = MyCalendar()

    # Test case 1: Booking an event that does not overlap
    print(my_calendar.book(10, 20))  # Expected: True

    # Test case 2: Booking an event that overlaps with an existing event
    print(my_calendar.book(15, 25))  # Expected: False

    # Test case 3: Booking an event that does not overlap
    print(my_calendar.book(20, 30))  # Expected: True

    # Test case 4: Booking an event that overlaps with multiple existing events
    print(my_calendar.book(5, 15))   # Expected: False

    # Test case 5: Booking an event that does not overlap with any existing events
    print(my_calendar.book(30, 40))  # Expected: True


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The `book` method iterates through the list of existing events to check for overlaps.
   - In the worst case, there are `n` events already in the calendar, where `n` is the number of successful bookings so far.
   - Therefore, the time complexity of the `book` method is O(n).
   - Since there are at most 1000 calls to the `book` method, the overall time complexity is O(n^2) in the worst case.

2. Space Complexity:
   - The `events` list stores all successfully booked events.
   - In the worst case, there can be up to 1000 events stored in the list.
   - Each event is represented as a tuple of two integers, so the space complexity is O(n), where `n` is the number of events.

Topic: Intervals
"""