# LeetCode Problem #1731: Employees and Managers
# Problem Statement:
# For this problem, we will consider a manager an employee who has at least 1 other employee reporting to them.
# Write a solution to report the ids and the names of all managers, the number of employees who report directly to them, 
# and the average age of the reports rounded to the nearest integer.
# Return the result table ordered by employee_id.

# Note: This is a SQL problem, but since the request is for a Python solution, we will simulate the problem using Python.

from collections import defaultdict
from math import floor

class Solution:
    def getManagersInfo(self, employees):
        """
        Simulates the SQL query to find managers, their direct reports count, and average age of reports.

        :param employees: List of dictionaries, where each dictionary represents an employee with keys:
                          'employee_id', 'name', 'age', 'manager_id'.
        :return: List of dictionaries with keys: 'manager_id', 'manager_name', 'report_count', 'average_age'.
        """
        # Step 1: Create a mapping of manager_id to their direct reports
        manager_to_reports = defaultdict(list)
        employee_info = {}

        for emp in employees:
            employee_info[emp['employee_id']] = emp
            if emp['manager_id'] is not None:
                manager_to_reports[emp['manager_id']].append(emp)

        # Step 2: Calculate the required information for each manager
        result = []
        for manager_id, reports in manager_to_reports.items():
            manager_name = employee_info[manager_id]['name']
            report_count = len(reports)
            average_age = round(sum(report['age'] for report in reports) / report_count)
            result.append({
                'manager_id': manager_id,
                'manager_name': manager_name,
                'report_count': report_count,
                'average_age': average_age
            })

        # Step 3: Sort the result by manager_id
        result.sort(key=lambda x: x['manager_id'])
        return result

# Example Test Cases
if __name__ == "__main__":
    # Input: List of employees
    employees = [
        {'employee_id': 1, 'name': 'Alice', 'age': 45, 'manager_id': None},
        {'employee_id': 2, 'name': 'Bob', 'age': 30, 'manager_id': 1},
        {'employee_id': 3, 'name': 'Charlie', 'age': 25, 'manager_id': 1},
        {'employee_id': 4, 'name': 'David', 'age': 35, 'manager_id': 2},
        {'employee_id': 5, 'name': 'Eve', 'age': 28, 'manager_id': 2}
    ]

    # Create an instance of the solution
    solution = Solution()

    # Get the result
    result = solution.getManagersInfo(employees)

    # Print the result
    print("Managers Information:")
    for row in result:
        print(row)

# Expected Output:
# Managers Information:
# {'manager_id': 1, 'manager_name': 'Alice', 'report_count': 2, 'average_age': 28}
# {'manager_id': 2, 'manager_name': 'Bob', 'report_count': 2, 'average_age': 32}

# Time Complexity Analysis:
# - Building the `manager_to_reports` mapping: O(n), where n is the number of employees.
# - Calculating the report count and average age for each manager: O(m), where m is the number of managers.
# - Sorting the result: O(m log m).
# Overall: O(n + m log m).

# Space Complexity Analysis:
# - Space for `manager_to_reports` and `employee_info`: O(n).
# - Space for the result: O(m).
# Overall: O(n).

# Topic: Hash Map, Sorting, Simulation of SQL Queries