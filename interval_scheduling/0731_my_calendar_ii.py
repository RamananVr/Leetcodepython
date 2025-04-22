"""
LeetCode Question #731: My Calendar II

Problem Statement:
Implement a class `MyCalendarTwo` to simulate a calendar system that can book events with possible double bookings but no triple bookings.

Your class will have one method, `book(int start, int end)`, which adds a new event (start, end) to the calendar. The event can be added if it does not result in a triple booking. A triple booking happens when three events overlap at any point.

An event is represented as a pair of integers [start, end), where `start` is inclusive and `end` is exclusive. The `book` method returns `True` if the event can be added to the calendar successfully without causing a triple booking, and `False` otherwise.

Constraints:
- The values of `start` and `end` are integers in the range [0, 10^9].
- Calls to `book` will be made at most 1000 times.

Example:
    MyCalendarTwo myCalendar = new MyCalendarTwo();
    myCalendar.book(10, 20); // returns True
    myCalendar.book(50, 60); // returns True
    myCalendar.book(10, 40); // returns True
    myCalendar.book(5, 15);  // returns False
    myCalendar.book(5, 10);  // returns True
    myCalendar.book(25, 55); // returns True
"""

# Python Solution
class MyCalendarTwo:
    def __init__(self):
        self.bookings = []  # Stores all single bookings
        self.overlaps = []  # Stores all double bookings

    def book(self, start: int, end: int) -> bool:
        # Check if the new booking would cause a triple booking
        for overlap_start, overlap_end in self.overlaps:
            if max(start, overlap_start) < min(end, overlap_end):
                return False  # Triple booking detected

        # Update overlaps with new double bookings
        for booking_start, booking_end in self.bookings:
            if max(start, booking_start) < min(end, booking_end):
                self.overlaps.append((max(start, booking_start), min(end, booking_end)))

        # Add the new booking to the list of single bookings
        self.bookings.append((start, end))
        return True

# Example Test Cases
if __name__ == "__main__":
    myCalendar = MyCalendarTwo()
    print(myCalendar.book(10, 20))  # True
    print(myCalendar.book(50, 60))  # True
    print(myCalendar.book(10, 40))  # True
    print(myCalendar.book(5, 15))   # False
    print(myCalendar.book(5, 10))   # True
    print(myCalendar.book(25, 55))  # True

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each call to `book` iterates through the `overlaps` and `bookings` lists.
- In the worst case, there are O(n) bookings and O(n) overlaps, where n is the number of calls to `book`.
- Thus, the time complexity for each `book` call is O(n).

Space Complexity:
- The `bookings` list stores all single bookings, and the `overlaps` list stores all double bookings.
- In the worst case, the space complexity is O(n) for `bookings` and O(n) for `overlaps`, resulting in a total space complexity of O(n).

Topic: Interval Scheduling
"""