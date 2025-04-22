"""
LeetCode Question #626: Exchange Seats

Problem Statement:
A SQL problem where you are given a table `Seat` with the following structure:
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key column for this table.
Each row of this table indicates the name and the ID of a student.

Write an SQL query to swap seats for every two consecutive students. If the number of students is odd, the last student will keep his/her seat.

Return the result table ordered by `id`.

Example:
Input:
Seat table:
+----+---------+
| id | student |
+----+---------+
| 1  | Abbot   |
| 2  | Doris   |
| 3  | Emerson |
| 4  | Green   |
| 5  | Jeames  |
+----+---------+

Output:
+----+---------+
| id | student |
+----+---------+
| 1  | Doris   |
| 2  | Abbot   |
| 3  | Green   |
| 4  | Emerson |
| 5  | Jeames  |
+----+---------+

Explanation:
Note that if the number of students is odd, the last student keeps his/her seat.

Since this is a SQL problem, no Python solution is required.
However, for completeness, we will simulate the problem in Python.
"""

# Python Simulation of LeetCode #626: Exchange Seats

def exchange_seats(seat_table):
    """
    Simulates the swapping of seats for every two consecutive students.
    If the number of students is odd, the last student keeps their seat.

    Args:
    seat_table (list of tuples): A list of tuples where each tuple contains (id, student).

    Returns:
    list of tuples: The modified seat table after swapping.
    """
    n = len(seat_table)
    result = seat_table[:]
    
    for i in range(0, n - 1, 2):
        # Swap consecutive students
        result[i], result[i + 1] = result[i + 1], result[i]
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Odd number of students
    seat_table = [
        (1, "Abbot"),
        (2, "Doris"),
        (3, "Emerson"),
        (4, "Green"),
        (5, "Jeames")
    ]
    print(exchange_seats(seat_table))
    # Expected Output:
    # [(1, "Doris"), (2, "Abbot"), (3, "Green"), (4, "Emerson"), (5, "Jeames")]

    # Test Case 2: Even number of students
    seat_table = [
        (1, "Alice"),
        (2, "Bob"),
        (3, "Charlie"),
        (4, "David")
    ]
    print(exchange_seats(seat_table))
    # Expected Output:
    # [(1, "Bob"), (2, "Alice"), (3, "David"), (4, "Charlie")]

    # Test Case 3: Single student
    seat_table = [
        (1, "Eve")
    ]
    print(exchange_seats(seat_table))
    # Expected Output:
    # [(1, "Eve")]

    # Test Case 4: Empty table
    seat_table = []
    print(exchange_seats(seat_table))
    # Expected Output:
    # []

"""
Time and Space Complexity Analysis:

Time Complexity:
The function iterates through the list with a step of 2, swapping consecutive elements.
This results in O(n) time complexity, where n is the number of students.

Space Complexity:
The function creates a copy of the input list to avoid modifying the original list.
This results in O(n) space complexity, where n is the number of students.

Topic: Arrays
"""