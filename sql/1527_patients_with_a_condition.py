"""
LeetCode Question #1527: Patients With a Condition

Problem Statement:
Table: Patients

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| patient_id   | int     |
| patient_name | varchar |
| conditions   | varchar |
+--------------+---------+
patient_id is the primary key for this table.
'conditions' contains a list of comma-separated strings.

Write an SQL query to find the names of all patients who have 'Diabetes' as one of their conditions.
Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Patients table:
+------------+--------------+-------------------------+
| patient_id | patient_name | conditions              |
+------------+--------------+-------------------------+
| 1          | John         | Diabetes,High Blood Pressure |
| 2          | Alice        | Asthma                  |
| 3          | Bob          | Diabetes                |
+------------+--------------+-------------------------+

Output:
+--------------+
| patient_name |
+--------------+
| John         |
| Bob          |
+--------------+
"""

# Python Solution
# Since this is an SQL-based problem, we will write the SQL query as the solution.

def sql_query():
    """
    Returns the SQL query to solve the problem.
    """
    query = """
    SELECT patient_name
    FROM Patients
    WHERE conditions LIKE '%Diabetes%';
    """
    return query

# Example Test Cases
def example_test_cases():
    """
    Example test cases for the SQL query.
    """
    print("Input:")
    print("+------------+--------------+-------------------------+")
    print("| patient_id | patient_name | conditions              |")
    print("+------------+--------------+-------------------------+")
    print("| 1          | John         | Diabetes,High Blood Pressure |")
    print("| 2          | Alice        | Asthma                  |")
    print("| 3          | Bob          | Diabetes                |")
    print("+------------+--------------+-------------------------+")
    
    print("\nExpected Output:")
    print("+--------------+")
    print("| patient_name |")
    print("+--------------+")
    print("| John         |")
    print("| Bob          |")
    print("+--------------+")

# Time and Space Complexity Analysis
"""
Time Complexity:
The time complexity of the SQL query depends on the number of rows in the Patients table.
If there are N rows, the LIKE operator will scan each row's 'conditions' column to check for the substring 'Diabetes'.
Thus, the time complexity is O(N * M), where M is the average length of the 'conditions' string.

Space Complexity:
The space complexity is O(1) since the query does not require any additional data structures.

Note: The actual performance may vary depending on the database engine and indexing.
"""

# Topic
# Topic: SQL