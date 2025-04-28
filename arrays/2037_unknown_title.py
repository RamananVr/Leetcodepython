"""
LeetCode Problem #2037: Minimum Number of Moves to Seat Everyone

Problem Statement:
There are n seats and n students in a room. You are given an array `seats` of length n, 
where `seats[i]` is the position of the i-th seat. You are also given the array `students` 
of length n, where `students[j]` is the position of the j-th student.

You may perform the following move any number of times:
- Increase or decrease the position of the i-th student by 1 (i.e., move the student from position x to x + 1 or x - 1).

Return the minimum number of moves required to make every student sit in a seat such that no two students are in the same seat.

Constraints:
- n == seats.length == students.length
- 1 <= n <= 100
- 1 <= seats[i], students[j] <= 100
"""

# Python Solution
def minMovesToSeat(seats, students):
    """
    Calculate the minimum number of moves required to seat all students.

    :param seats: List[int] - Positions of the seats
    :param students: List[int] - Positions of the students
    :return: int - Minimum number of moves required
    """
    # Sort both arrays to minimize the distance between corresponding elements
    seats.sort()
    students.sort()
    
    # Calculate the total moves by summing the absolute differences
    return sum(abs(seat - student) for seat, student in zip(seats, students))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    seats = [3, 1, 5]
    students = [2, 7, 4]
    print(minMovesToSeat(seats, students))  # Output: 4

    # Test Case 2
    seats = [4, 1, 5, 9]
    students = [1, 3, 2, 6]
    print(minMovesToSeat(seats, students))  # Output: 7

    # Test Case 3
    seats = [2, 2, 6, 6]
    students = [1, 3, 2, 6]
    print(minMovesToSeat(seats, students))  # Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the `seats` and `students` arrays takes O(n log n), where n is the number of elements.
- Calculating the sum of absolute differences takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- Sorting is done in-place, and no additional data structures are used.
- Overall space complexity: O(1).

Topic: Arrays
"""