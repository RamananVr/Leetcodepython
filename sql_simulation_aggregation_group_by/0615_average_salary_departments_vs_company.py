"""
LeetCode Question #615: Average Salary: Departments VS Company

Problem Statement:
A company's employees are represented in a table, `Employee`, with the following schema:

Table: Employee
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| department  | varchar |
+-------------+---------+
id is the primary key for this table.
Each row of this table indicates the id, name, salary, and department of an employee.

Write an SQL query to find the departments where the average salary is higher than the average salary of the company.

Return the result table in any order.

The query result format is in the following example:

Employee table:
+----+-------+--------+------------+
| id | name  | salary | department |
+----+-------+--------+------------+
| 1  | Joe   | 70000  | IT         |
| 2  | Henry | 80000  | IT         |
| 3  | Sam   | 60000  | HR         |
| 4  | Max   | 90000  | HR         |
+----+-------+--------+------------+

Result table:
+------------+
| department |
+------------+
| IT         |
+------------+
The average salary of the company is (70000 + 80000 + 60000 + 90000) / 4 = 75000.
The average salary of the IT department is (70000 + 80000) / 2 = 75000.
The average salary of the HR department is (60000 + 90000) / 2 = 75000.
Since the average salary of the IT department is not higher than the company average, it is not included in the result.
"""

# Clean, Correct Python Solution
# Note: Since this is an SQL problem, we will simulate the solution using Python and pandas.

import pandas as pd

def departments_with_higher_avg_salary(employee_data):
    """
    Function to find departments where the average salary is higher than the company's average salary.

    :param employee_data: List of dictionaries representing the Employee table.
    :return: List of departments meeting the criteria.
    """
    # Convert the input data to a pandas DataFrame
    df = pd.DataFrame(employee_data)

    # Calculate the company's average salary
    company_avg_salary = df['salary'].mean()

    # Calculate the average salary per department
    department_avg_salary = df.groupby('department')['salary'].mean()

    # Filter departments where the average salary is higher than the company's average salary
    result = department_avg_salary[department_avg_salary > company_avg_salary].index.tolist()

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    employee_data = [
        {"id": 1, "name": "Joe", "salary": 70000, "department": "IT"},
        {"id": 2, "name": "Henry", "salary": 80000, "department": "IT"},
        {"id": 3, "name": "Sam", "salary": 60000, "department": "HR"},
        {"id": 4, "name": "Max", "salary": 90000, "department": "HR"}
    ]
    print(departments_with_higher_avg_salary(employee_data))  # Output: []

    # Test Case 2
    employee_data = [
        {"id": 1, "name": "Alice", "salary": 100000, "department": "Engineering"},
        {"id": 2, "name": "Bob", "salary": 120000, "department": "Engineering"},
        {"id": 3, "name": "Charlie", "salary": 50000, "department": "Sales"},
        {"id": 4, "name": "David", "salary": 60000, "department": "Sales"}
    ]
    print(departments_with_higher_avg_salary(employee_data))  # Output: ['Engineering']

    # Test Case 3
    employee_data = [
        {"id": 1, "name": "Eve", "salary": 50000, "department": "Marketing"},
        {"id": 2, "name": "Frank", "salary": 50000, "department": "Marketing"},
        {"id": 3, "name": "Grace", "salary": 50000, "department": "Finance"},
        {"id": 4, "name": "Hank", "salary": 50000, "department": "Finance"}
    ]
    print(departments_with_higher_avg_salary(employee_data))  # Output: []

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the company's average salary: O(n), where n is the number of employees.
- Grouping by department and calculating average salary: O(n).
- Filtering departments: O(d), where d is the number of unique departments.
Overall: O(n + d).

Space Complexity:
- Storing the DataFrame: O(n).
- Storing the grouped department averages: O(d).
Overall: O(n + d).
"""

# Topic: SQL Simulation, Aggregation, Group By