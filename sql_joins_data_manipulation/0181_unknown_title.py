"""
LeetCode Problem #181: Employees Earning More Than Their Managers

Problem Statement:
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key column for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.

Write an SQL query to find the employees who earn more than their managers.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+

Output:
+----------+
| Employee |
+----------+
| Joe      |
+----------+

Explanation:
Joe is the only employee who earns more than their manager.
"""

# Clean, Correct Python Solution
# Note: Since this is an SQL problem, we will use Python to simulate the SQL query using pandas.

import pandas as pd

def employees_earning_more_than_managers(employee_data):
    """
    Function to find employees earning more than their managers.

    Args:
    employee_data (list of dict): List of dictionaries representing the Employee table.

    Returns:
    pd.DataFrame: DataFrame containing employees who earn more than their managers.
    """
    # Convert the input data to a pandas DataFrame
    employee_df = pd.DataFrame(employee_data)

    # Perform a self-join to compare employees with their managers
    merged_df = employee_df.merge(
        employee_df, 
        left_on='managerId', 
        right_on='id', 
        suffixes=('_emp', '_mgr')
    )

    # Filter employees earning more than their managers
    result_df = merged_df[merged_df['salary_emp'] > merged_df['salary_mgr']]

    # Select only the employee names
    return result_df[['name_emp']].rename(columns={'name_emp': 'Employee'})

# Example Test Cases
if __name__ == "__main__":
    # Input data
    employee_data = [
        {"id": 1, "name": "Joe", "salary": 70000, "managerId": 3},
        {"id": 2, "name": "Henry", "salary": 80000, "managerId": 4},
        {"id": 3, "name": "Sam", "salary": 60000, "managerId": None},
        {"id": 4, "name": "Max", "salary": 90000, "managerId": None},
    ]

    # Expected Output: DataFrame with one row: Joe
    result = employees_earning_more_than_managers(employee_data)
    print(result)

"""
Time and Space Complexity Analysis:

Time Complexity:
- The merge operation (self-join) has a time complexity of O(n^2) in the worst case, where n is the number of rows in the employee table.
- Filtering the merged DataFrame has a time complexity of O(n).

Overall time complexity: O(n^2).

Space Complexity:
- The space complexity is O(n^2) due to the creation of the merged DataFrame.

Topic: SQL, Joins, Data Manipulation
"""