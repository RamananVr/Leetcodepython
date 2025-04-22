"""
LeetCode Question #579: Find Total Employees Who Worked in All Departments

Problem Statement:
A company has a table `Employee` with the following columns:
- `id`: The employee's ID.
- `name`: The employee's name.

Another table `Department` has the following columns:
- `id`: The department's ID.
- `name`: The department's name.

A third table `EmployeeDepartment` has the following columns:
- `employee_id`: The ID of the employee.
- `department_id`: The ID of the department.

Write a SQL query to find the total number of employees who have worked in all the departments.

Note:
- The result should be a single number.
- Assume that the tables are properly populated with data.

Since this is a SQL problem, we will simulate the solution in Python using pandas for demonstration purposes.
"""

import pandas as pd

# Solution
def find_total_employees_worked_in_all_departments(employee_df, department_df, employee_department_df):
    """
    Function to find the total number of employees who worked in all departments.

    Args:
    - employee_df (pd.DataFrame): DataFrame containing employee data.
    - department_df (pd.DataFrame): DataFrame containing department data.
    - employee_department_df (pd.DataFrame): DataFrame containing employee-department mapping.

    Returns:
    - int: Total number of employees who worked in all departments.
    """
    # Count the total number of departments
    total_departments = department_df['id'].nunique()

    # Count the number of departments each employee has worked in
    employee_department_count = employee_department_df.groupby('employee_id')['department_id'].nunique()

    # Find employees who have worked in all departments
    employees_in_all_departments = employee_department_count[employee_department_count == total_departments]

    # Return the total number of such employees
    return len(employees_in_all_departments)

# Example Test Cases
if __name__ == "__main__":
    # Example data
    employee_data = {'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']}
    department_data = {'id': [1, 2, 3], 'name': ['HR', 'Engineering', 'Sales']}
    employee_department_data = {
        'employee_id': [1, 1, 1, 2, 2, 3],
        'department_id': [1, 2, 3, 1, 2, 1]
    }

    # Create DataFrames
    employee_df = pd.DataFrame(employee_data)
    department_df = pd.DataFrame(department_data)
    employee_department_df = pd.DataFrame(employee_department_data)

    # Find total employees who worked in all departments
    result = find_total_employees_worked_in_all_departments(employee_df, department_df, employee_department_df)
    print(f"Total employees who worked in all departments: {result}")

"""
Time and Space Complexity Analysis:
- Time Complexity:
  - Counting unique departments: O(D), where D is the number of departments.
  - Grouping and counting unique departments per employee: O(E), where E is the number of employee-department mappings.
  - Filtering employees who worked in all departments: O(E).
  - Overall: O(D + E).

- Space Complexity:
  - Space used for intermediate groupings and counts: O(E).
  - Overall: O(E).

Topic: SQL Simulation / Relational Data
"""