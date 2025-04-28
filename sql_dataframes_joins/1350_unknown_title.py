"""
LeetCode Problem #1350: Students With Invalid Departments

Problem Statement:
Table: Students
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
| department_id | int     |
+---------------+---------+
student_id is the primary key for this table.

Table: Departments
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| department_id | int     |
| department_name | varchar |
+---------------+---------+
department_id is the primary key for this table.

Write an SQL query to find the id and name of all students who are not enrolled in a valid department (i.e., their department_id does not exist in the Departments table).

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Students table:
+------------+--------------+---------------+
| student_id | student_name | department_id |
+------------+--------------+---------------+
| 1          | Alice        | 1             |
| 2          | Bob          | 2             |
| 3          | Charlie      | 3             |
| 4          | David        | 4             |
+------------+--------------+---------------+

Departments table:
+---------------+----------------+
| department_id | department_name|
+---------------+----------------+
| 1             | Engineering    |
| 3             | Math           |
+---------------+----------------+

Output:
+------------+--------------+
| student_id | student_name |
+------------+--------------+
| 2          | Bob          |
| 4          | David        |
+------------+--------------+

Explanation:
- Alice is in department 1, which exists in the Departments table.
- Bob is in department 2, which does not exist in the Departments table.
- Charlie is in department 3, which exists in the Departments table.
- David is in department 4, which does not exist in the Departments table.
"""

# Python Solution (Simulating SQL Query with Pandas)

import pandas as pd

def find_invalid_students(students: pd.DataFrame, departments: pd.DataFrame) -> pd.DataFrame:
    """
    Find students who are not enrolled in a valid department.

    Args:
    students (pd.DataFrame): DataFrame containing the Students table.
    departments (pd.DataFrame): DataFrame containing the Departments table.

    Returns:
    pd.DataFrame: DataFrame containing student_id and student_name of invalid students.
    """
    # Perform a left join between students and departments on department_id
    merged = students.merge(departments, on="department_id", how="left", indicator=True)
    
    # Filter rows where the department_id does not exist in the Departments table
    invalid_students = merged[merged["_merge"] == "left_only"]
    
    # Select only the required columns
    result = invalid_students[["student_id", "student_name"]]
    
    return result


# Example Test Cases
if __name__ == "__main__":
    # Input DataFrames
    students_data = {
        "student_id": [1, 2, 3, 4],
        "student_name": ["Alice", "Bob", "Charlie", "David"],
        "department_id": [1, 2, 3, 4]
    }
    departments_data = {
        "department_id": [1, 3],
        "department_name": ["Engineering", "Math"]
    }
    
    students_df = pd.DataFrame(students_data)
    departments_df = pd.DataFrame(departments_data)
    
    # Expected Output: DataFrame with Bob and David
    print(find_invalid_students(students_df, departments_df))


"""
Time and Space Complexity Analysis:

Time Complexity:
- The `merge` operation has a time complexity of O(n + m), where n is the number of rows in the Students table and m is the number of rows in the Departments table.
- Filtering the merged DataFrame is O(n) in the worst case.

Overall time complexity: O(n + m).

Space Complexity:
- The space complexity is O(n + m) due to the creation of the merged DataFrame.

Overall space complexity: O(n + m).

Topic: SQL, DataFrames, Joins
"""