"""
LeetCode Question #577: Employee Bonus

Problem Statement:
Table: Employee
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| empId       | int     |
| name        | varchar |
| supervisor  | int     |
| salary      | int     |
+-------------+---------+
empId is the primary key column for this table.
Each row of this table indicates the ID of an employee, their name, the ID of their supervisor, and their salary.

Table: Bonus
+-------------+------+
| Column Name | Type |
+-------------+------+
| empId       | int  |
| bonus       | int  |
+-------------+------+
empId is the primary key column for this table.
empId is a foreign key to empId from the Employee table.
Each row of this table contains the bonus amount of an employee.

Write an SQL query to report the name and bonus amount of each employee with a bonus less than 1000.
Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Employee table:
+-------+--------+------------+--------+
| empId | name   | supervisor | salary |
+-------+--------+------------+--------+
| 3     | Brad   | null       | 4000   |
| 1     | John   | 3          | 1000   |
| 2     | Dan    | 3          | 2000   |
| 4     | Thomas | 3          | 4000   |
+-------+--------+------------+--------+

Bonus table:
+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+

Output:
+--------+-------+
| name   | bonus |
+--------+-------+
| Brad   | null  |
| John   | null  |
| Dan    | 500   |
+--------+-------+
"""

# Python Solution:
# Since this is an SQL problem, we will write the SQL query as a string in Python.

def employee_bonus_query():
    """
    Returns the SQL query to solve LeetCode Question #577.
    """
    query = """
    SELECT e.name, b.bonus
    FROM Employee e
    LEFT JOIN Bonus b
    ON e.empId = b.empId
    WHERE b.bonus < 1000 OR b.bonus IS NULL;
    """
    return query

# Example Test Cases:
def test_employee_bonus_query():
    """
    Test cases for the SQL query.
    Note: These test cases assume the query is run in a database environment.
    """
    # Input:
    # Employee table:
    # +-------+--------+------------+--------+
    # | empId | name   | supervisor | salary |
    # +-------+--------+------------+--------+
    # | 3     | Brad   | null       | 4000   |
    # | 1     | John   | 3          | 1000   |
    # | 2     | Dan    | 3          | 2000   |
    # | 4     | Thomas | 3          | 4000   |
    # +-------+--------+------------+--------+
    #
    # Bonus table:
    # +-------+-------+
    # | empId | bonus |
    # +-------+-------+
    # | 2     | 500   |
    # | 4     | 2000  |
    # +-------+-------+
    #
    # Expected Output:
    # +--------+-------+
    # | name   | bonus |
    # +--------+-------+
    # | Brad   | null  |
    # | John   | null  |
    # | Dan    | 500   |
    # +--------+-------+

    print("Test cases for the SQL query should be run in a database environment.")

# Time and Space Complexity Analysis:
# Time Complexity:
# - The query involves a LEFT JOIN between the Employee and Bonus tables, which has a time complexity of O(N * M),
#   where N is the number of rows in the Employee table and M is the number of rows in the Bonus table.
# - The WHERE clause filters the results, which is O(K), where K is the number of rows in the joined table.
# - Overall time complexity: O(N * M).

# Space Complexity:
# - The query does not use any additional space apart from the result set.
# - Space complexity: O(K), where K is the number of rows in the result set.

# Topic: SQL, Joins