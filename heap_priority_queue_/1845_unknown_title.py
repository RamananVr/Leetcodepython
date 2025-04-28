"""
LeetCode Problem #1845: Seat Reservation Manager

Problem Statement:
Design a system that manages the reservation of seats in a theater. The theater has a total of n seats, numbered from 1 to n. 
Implement the SeatManager class:

1. SeatManager(int n): Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
2. int reserve(): Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
3. void unreserve(int seatNumber): Unreserves the seat with the given seatNumber.

Constraints:
- 1 <= n <= 10^5
- 1 <= seatNumber <= n
- For each call to reserve, it is guaranteed that there will be at least one unreserved seat.
- For each call to unreserve, it is guaranteed that seatNumber will be reserved.

Example:
Input:
["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [5]]

Output:
[null, 1, 2, null, 2, 3, 4, null]

Explanation:
SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.
seatManager.reserve(); // All seats are available, so return the smallest seat number, which is 1.
seatManager.reserve(); // The smallest seat number is 2, so return 2.
seatManager.unreserve(2); // Unreserve seat 2, making it available again.
seatManager.reserve(); // Seat 2 is now available, so return 2.
seatManager.reserve(); // The smallest seat number is 3, so return 3.
seatManager.reserve(); // The smallest seat number is 4, so return 4.
seatManager.unreserve(5); // Unreserve seat 5, making it available again.
"""

import heapq

class SeatManager:
    def __init__(self, n: int):
        """
        Initializes the SeatManager with n seats.
        All seats are initially available.
        """
        self.available_seats = list(range(1, n + 1))
        heapq.heapify(self.available_seats)  # Min-heap to efficiently fetch the smallest seat number.

    def reserve(self) -> int:
        """
        Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
        """
        return heapq.heappop(self.available_seats)

    def unreserve(self, seatNumber: int) -> None:
        """
        Unreserves the seat with the given seatNumber, making it available again.
        """
        heapq.heappush(self.available_seats, seatNumber)


# Example Test Cases
if __name__ == "__main__":
    # Initialize SeatManager with 5 seats
    seatManager = SeatManager(5)
    
    # Test reserve
    print(seatManager.reserve())  # Output: 1
    print(seatManager.reserve())  # Output: 2
    
    # Test unreserve
    seatManager.unreserve(2)      # Unreserve seat 2
    
    # Test reserve again
    print(seatManager.reserve())  # Output: 2
    print(seatManager.reserve())  # Output: 3
    print(seatManager.reserve())  # Output: 4
    
    # Test unreserve
    seatManager.unreserve(5)      # Unreserve seat 5

    # Test reserve after unreserve
    print(seatManager.reserve())  # Output: 5


"""
Time and Space Complexity Analysis:

1. Initialization (__init__):
   - Time Complexity: O(n) to create the list of seats and heapify it.
   - Space Complexity: O(n) for storing the list of available seats.

2. Reserve:
   - Time Complexity: O(log n) for popping the smallest seat from the heap.
   - Space Complexity: O(1) (no additional space used).

3. Unreserve:
   - Time Complexity: O(log n) for pushing the seat back into the heap.
   - Space Complexity: O(1) (no additional space used).

Overall:
- Time Complexity: O(log n) for each reserve and unreserve operation.
- Space Complexity: O(n) for the heap storage.

Topic: Heap (Priority Queue)
"""