"""
LeetCode Problem #1965: Employees With Missing Information

Problem Statement:
Table: Employees
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
+-------------+---------+
employee_id is the primary key for this table.
Each row of this table indicates the ID and name of an employee.

Table: Salaries
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| salary      | int     |
+-------------+---------+
employee_id is the primary key for this table.
Each row of this table indicates the ID and salary of an employee.

Write an SQL query to report the IDs of employees missing information. 
The information missing is either the employee's name or salary.

Return the result table ordered by employee_id.

The query result format is in the following example.

Example:
Input:
Employees table:
+-------------+----------+
| employee_id | name     |
+-------------+----------+
| 2           | Crew     |
| 4           | NULL     |
| 5           | NULL     |
+-------------+----------+

Salaries table:
+-------------+--------+
| employee_id | salary |
+-------------+--------+
| 2           | 1000   |
| 4           | 2000   |
| 5           | NULL   |
+-------------+--------+

Output:
+-------------+
| employee_id |
+-------------+
| 4           |
| 5           |
+-------------+
"""

# Python Solution (Simulating SQL Query Execution)

# Import pandas for simulating SQL-like operations
import pandas as pd

def employees_with_missing_information(employees, salaries):
    """
    Function to find employees with missing information (either name or salary).
    
    Args:
    employees (pd.DataFrame): DataFrame containing employee_id and name.
    salaries (pd.DataFrame): DataFrame containing employee_id and salary.
    
    Returns:
    pd.DataFrame: DataFrame containing employee_id of employees with missing information.
    """
    # Merge the two tables on employee_id
    merged = pd.merge(employees, salaries, on="employee_id", how="outer")
    
    # Filter rows where either name or salary is missing
    missing_info = merged[(merged["name"].isnull()) | (merged["salary"].isnull())]
    
    # Select only the employee_id column and sort by employee_id
    result = missing_info[["employee_id"]].sort_values(by="employee_id").reset_index(drop=True)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Example Input DataFrames
    employees_data = {
        "employee_id": [2, 4, 5],
        "name": ["Crew", None, None]
    }
    salaries_data = {
        "employee_id": [2, 4, 5],
        "salary": [1000, 2000, None]
    }
    
    employees_df = pd.DataFrame(employees_data)
    salaries_df = pd.DataFrame(salaries_data)
    
    # Call the function and print the result
    result = employees_with_missing_information(employees_df, salaries_df)
    print(result)

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The merge operation has a time complexity of O(n + m), where n is the number of rows in the `employees` table and m is the number of rows in the `salaries` table.
   - Filtering rows with missing information has a time complexity of O(n), where n is the number of rows in the merged table.
   - Sorting the result has a time complexity of O(k log k), where k is the number of rows with missing information.
   - Overall time complexity: O(n + m + k log k).

2. Space Complexity:
   - The merged table requires O(n + m) space.
   - The result table requires O(k) space.
   - Overall space complexity: O(n + m).

Topic: SQL Simulation / DataFrames
"""