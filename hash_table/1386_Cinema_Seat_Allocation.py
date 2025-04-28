"""
LeetCode Problem #1386: Cinema Seat Allocation

Problem Statement:
A cinema has `n` rows of seats, numbered from 1 to `n` and there are ten seats in each row, labeled from 1 to 10. 
Given the array `reservedSeats` containing the numbers of seats already reserved, for example, `reservedSeats[i] = [3,8]` 
means the seat located in row 3 and column 8 is already reserved.

Return the maximum number of four-person families you can assign on the cinema seats. A four-person family occupies 
four adjacent seats in one row. Seats across an aisle (such as between seats 4 and 5) are not considered to be adjacent, 
but it is permissible for the family to be separated by an aisle.

A four-person family can sit in the following configurations:
1. Seats 2, 3, 4, and 5.
2. Seats 4, 5, 6, and 7.
3. Seats 6, 7, 8, and 9.

Constraints:
- 1 <= n <= 10^9
- 1 <= reservedSeats.length <= min(10^4, 10 * n)
- reservedSeats[i].length == 2
- 1 <= reservedSeats[i][0] <= n
- 1 <= reservedSeats[i][1] <= 10
- All `reservedSeats[i]` are unique.

"""

from collections import defaultdict

def maxNumberOfFamilies(n: int, reservedSeats: list[list[int]]) -> int:
    # Dictionary to store reserved seats for each row
    reserved_map = defaultdict(set)
    for row, seat in reservedSeats:
        reserved_map[row].add(seat)
    
    # Maximum families that can fit in a row
    max_families_per_row = 2
    
    # Count the number of rows with reserved seats
    rows_with_reserved = len(reserved_map)
    
    # Initialize the total number of families
    total_families = (n - rows_with_reserved) * max_families_per_row
    
    # Check each row with reserved seats
    for row, reserved in reserved_map.items():
        # Check the three possible configurations
        left_block = all(seat not in reserved for seat in range(2, 6))
        middle_block = all(seat not in reserved for seat in range(4, 8))
        right_block = all(seat not in reserved for seat in range(6, 10))
        
        if left_block and right_block:
            total_families += 2
        elif left_block or middle_block or right_block:
            total_families += 1
    
    return total_families

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 3
    reservedSeats1 = [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]
    print(maxNumberOfFamilies(n1, reservedSeats1))  # Output: 4

    # Test Case 2
    n2 = 2
    reservedSeats2 = [[2, 1], [1, 8], [2, 6]]
    print(maxNumberOfFamilies(n2, reservedSeats2))  # Output: 2

    # Test Case 3
    n3 = 4
    reservedSeats3 = []
    print(maxNumberOfFamilies(n3, reservedSeats3))  # Output: 8

    # Test Case 4
    n4 = 1
    reservedSeats4 = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9]]
    print(maxNumberOfFamilies(n4, reservedSeats4))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Let `m` be the length of `reservedSeats`.
- Constructing the `reserved_map` takes O(m).
- Iterating through the rows with reserved seats and checking the three configurations takes O(m).
- Calculating the families for rows without reserved seats is O(1) since it is a simple arithmetic operation.
- Overall time complexity: O(m).

Space Complexity:
- The `reserved_map` dictionary stores up to `m` entries, where each entry is a set of reserved seats.
- Space complexity: O(m).

Topic: Hash Table
"""