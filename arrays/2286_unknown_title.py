"""
LeetCode Problem #2286: Booking Concert Tickets in Groups

Problem Statement:
You are managing a concert venue and want to sell tickets to groups of people. The venue consists of `n` rows of seats, 
and each row contains `m` seats. You need to implement a system that can handle the following operations:

1. `gather(k, maxRow)`: Find a single row such that at least `k` consecutive seats are available in that row, and the row 
   index is less than or equal to `maxRow`. If such a row is found, allocate those seats to the group and return an array 
   `[row, seatNumber]` where `row` is the row index, and `seatNumber` is the starting seat number of the allocated seats. 
   If no such row is found, return an empty array `[]`.

2. `scatter(k, maxRow)`: Allocate `k` seats across multiple rows (starting from row 0 to `maxRow`) such that no row is 
   allocated seats beyond its capacity. If it is possible to allocate all `k` seats, return `True`. Otherwise, return `False`.

Implement the `BookMyShow` class:
- `BookMyShow(n: int, m: int)` Initializes the object with `n` rows and `m` seats per row.
- `gather(k: int, maxRow: int) -> List[int]` Handles the gather operation as described above.
- `scatter(k: int, maxRow: int) -> bool` Handles the scatter operation as described above.

Constraints:
- `1 <= n, m <= 10^5`
- `0 <= k <= m`
- `0 <= maxRow < n`
- At most `10^4` calls will be made to `gather` and `scatter`.

"""

from typing import List

class BookMyShow:
    def __init__(self, n: int, m: int):
        # Initialize the number of rows and seats per row
        self.n = n
        self.m = m
        self.rows = [m] * n  # Each row starts with `m` available seats
        self.total_seats = n * m  # Total seats available in the venue

    def gather(self, k: int, maxRow: int) -> List[int]:
        # Find a single row with at least `k` consecutive seats available
        for row in range(maxRow + 1):
            if self.rows[row] >= k:
                start_seat = self.m - self.rows[row]
                self.rows[row] -= k
                self.total_seats -= k
                return [row, start_seat]
        return []

    def scatter(self, k: int, maxRow: int) -> bool:
        # Check if we can allocate `k` seats across multiple rows
        if k > self.total_seats:
            return False

        for row in range(maxRow + 1):
            if k == 0:
                break
            if self.rows[row] > 0:
                allocated = min(self.rows[row], k)
                self.rows[row] -= allocated
                self.total_seats -= allocated
                k -= allocated

        return k == 0


# Example Test Cases
if __name__ == "__main__":
    # Initialize the BookMyShow system
    bms = BookMyShow(3, 5)  # 3 rows, 5 seats per row

    # Test gather
    print(bms.gather(4, 2))  # Expected: [0, 0] (4 seats allocated in row 0 starting at seat 0)
    print(bms.gather(2, 2))  # Expected: [0, 4] (2 seats allocated in row 0 starting at seat 4)
    print(bms.gather(3, 2))  # Expected: [1, 0] (3 seats allocated in row 1 starting at seat 0)

    # Test scatter
    print(bms.scatter(4, 2))  # Expected: True (4 seats allocated across rows 1 and 2)
    print(bms.scatter(6, 2))  # Expected: False (Not enough seats available in rows 0 to 2)


"""
Time and Space Complexity Analysis:

1. `gather(k, maxRow)`:
   - Time Complexity: O(maxRow) in the worst case, as we iterate through rows up to `maxRow`.
   - Space Complexity: O(1), as we only use a constant amount of extra space.

2. `scatter(k, maxRow)`:
   - Time Complexity: O(maxRow) in the worst case, as we iterate through rows up to `maxRow`.
   - Space Complexity: O(1), as we only use a constant amount of extra space.

Overall:
- Time Complexity: O(maxRow) per operation.
- Space Complexity: O(n), where `n` is the number of rows (to store the `rows` array).

Topic: Arrays
"""