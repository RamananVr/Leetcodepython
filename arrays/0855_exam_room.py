"""
LeetCode Question #855: Exam Room

Problem Statement:
In an exam room, there are `n` seats in a single row, numbered `0, 1, 2, ..., n-1`.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person. 
If there are multiple such seats, they sit in the seat with the lowest number. 
If no one is in the room, the student sits at seat `0`.

Design a class `ExamRoom` that simulates the exam room.

Implement the following methods:
1. `ExamRoom(n: int)` Initializes the object with `n` seats.
2. `seat() -> int` Returns the seat number where the student sat.
3. `leave(p: int) -> None` Indicates that the student at seat `p` has left the room. It is guaranteed that `p` is occupied.

Constraints:
- `1 <= n <= 10^9`
- It is guaranteed that `seat()` and `leave()` will be called at most `10^4` times.

Example:
Input:
["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
[[10], [], [], [], [], [4], []]

Output:
[null, 0, 9, 4, 2, null, 5]

Explanation:
ExamRoom examRoom = new ExamRoom(10);
examRoom.seat(); // return 0, since no one is in the room.
examRoom.seat(); // return 9, since the student sits at the last seat.
examRoom.seat(); // return 4, since the student sits at the position with the maximum distance to the closest person.
examRoom.seat(); // return 2, since the student sits at the position with the maximum distance to the closest person.
examRoom.leave(4);
examRoom.seat(); // return 5, since the student sits at the position with the maximum distance to the closest person.

"""

# Python Solution
import bisect

class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.seats = []  # List to store occupied seats

    def seat(self) -> int:
        if not self.seats:
            # If no one is seated, the first student sits at seat 0
            self.seats.append(0)
            return 0

        max_distance = self.seats[0]  # Distance from seat 0 to the first occupied seat
        seat_to_sit = 0

        # Check the gaps between consecutive occupied seats
        for i in range(len(self.seats) - 1):
            prev_seat = self.seats[i]
            next_seat = self.seats[i + 1]
            distance = (next_seat - prev_seat) // 2
            if distance > max_distance:
                max_distance = distance
                seat_to_sit = prev_seat + distance

        # Check the distance from the last occupied seat to the last seat
        if self.n - 1 - self.seats[-1] > max_distance:
            seat_to_sit = self.n - 1

        # Insert the seat into the sorted list of occupied seats
        bisect.insort(self.seats, seat_to_sit)
        return seat_to_sit

    def leave(self, p: int) -> None:
        self.seats.remove(p)

# Example Test Cases
if __name__ == "__main__":
    examRoom = ExamRoom(10)
    print(examRoom.seat())  # Output: 0
    print(examRoom.seat())  # Output: 9
    print(examRoom.seat())  # Output: 4
    print(examRoom.seat())  # Output: 2
    examRoom.leave(4)
    print(examRoom.seat())  # Output: 5

"""
Time and Space Complexity Analysis:

1. `seat()`:
   - Time Complexity: O(k), where k is the number of currently occupied seats. This is because we iterate through the list of occupied seats to find the maximum distance and use `bisect.insort` to insert the new seat in sorted order.
   - Space Complexity: O(k), where k is the number of currently occupied seats.

2. `leave()`:
   - Time Complexity: O(k), where k is the number of currently occupied seats. This is because we use `remove()` to delete a seat from the list.
   - Space Complexity: O(1), as no additional space is used.

Overall, the space complexity of the class is O(k), where k is the number of occupied seats.

Topic: Arrays
"""