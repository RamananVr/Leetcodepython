"""
LeetCode Problem #1741: Find Total Time Spent by Each Employee

Problem Statement:
SQL Schema:
The `Employees` table holds all employees' information. Each row of this table contains:
- `id` (int): The employee's ID.
- `event_day` (date): The day the event occurred.
- `in_time` (int): The time the employee entered the office (in minutes after midnight).
- `out_time` (int): The time the employee left the office (in minutes after midnight).

Write an SQL query to calculate the total time (in minutes) spent by each employee on each day. The result should be sorted by `id` and then by `event_day`.

Return the result table in any order.

Example:
Input:
Employees table:
+-----+------------+---------+----------+
| id  | event_day  | in_time | out_time |
+-----+------------+---------+----------+
| 1   | 2020-11-28 | 4       | 32       |
| 1   | 2020-11-28 | 55      | 200      |
| 1   | 2020-12-03 | 1       | 42       |
| 2   | 2020-11-28 | 3       | 33       |
+-----+------------+---------+----------+

Output:
+-----+------------+------------+
| id  | event_day  | total_time |
+-----+------------+------------+
| 1   | 2020-11-28 | 173        |
| 1   | 2020-12-03 | 41         |
| 2   | 2020-11-28 | 30         |
+-----+------------+------------+

Explanation:
- Employee 1 on 2020-11-28: (32 - 4) + (200 - 55) = 28 + 145 = 173.
- Employee 1 on 2020-12-03: (42 - 1) = 41.
- Employee 2 on 2020-11-28: (33 - 3) = 30.

Note:
This is an SQL problem, but we will solve it in Python for the sake of this exercise.
"""

# Python Solution
from collections import defaultdict
from typing import List, Tuple

def total_time_spent(employees: List[Tuple[int, str, int, int]]) -> List[Tuple[int, str, int]]:
    """
    Calculate the total time spent by each employee on each day.

    Args:
    employees: A list of tuples where each tuple contains:
        - id (int): Employee ID
        - event_day (str): The day the event occurred
        - in_time (int): Time the employee entered the office (in minutes after midnight)
        - out_time (int): Time the employee left the office (in minutes after midnight)

    Returns:
    A list of tuples where each tuple contains:
        - id (int): Employee ID
        - event_day (str): The day the event occurred
        - total_time (int): Total time spent by the employee on that day
    """
    time_spent = defaultdict(int)

    for emp_id, event_day, in_time, out_time in employees:
        time_spent[(emp_id, event_day)] += (out_time - in_time)

    result = [(emp_id, event_day, total_time) for (emp_id, event_day), total_time in time_spent.items()]
    result.sort(key=lambda x: (x[0], x[1]))  # Sort by id and then by event_day
    return result

# Example Test Cases
if __name__ == "__main__":
    employees = [
        (1, "2020-11-28", 4, 32),
        (1, "2020-11-28", 55, 200),
        (1, "2020-12-03", 1, 42),
        (2, "2020-11-28", 3, 33)
    ]

    expected_output = [
        (1, "2020-11-28", 173),
        (1, "2020-12-03", 41),
        (2, "2020-11-28", 30)
    ]

    output = total_time_spent(employees)
    print("Output:", output)
    print("Expected:", expected_output)
    assert output == expected_output, "Test case failed!"

"""
Time and Space Complexity Analysis:

Time Complexity:
- O(n): We iterate through the list of employees once to calculate the total time spent for each (id, event_day) pair.
- O(m log m): Sorting the result list, where m is the number of unique (id, event_day) pairs.
- Overall: O(n + m log m), where n is the number of rows in the input and m is the number of unique (id, event_day) pairs.

Space Complexity:
- O(m): We use a dictionary to store the total time spent for each (id, event_day) pair, where m is the number of unique pairs.

Topic: Hash Table, Sorting
"""