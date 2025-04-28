"""
LeetCode Problem #1875: Group Employees by Salary Range

Problem Statement:
You are given a table `Employee` with the following structure:

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| name        | varchar |
| salary      | int     |

id is the primary key for this table. Each row of this table indicates the ID, name, and salary of an employee.

Write an SQL query to group employees into salary ranges. The salary ranges are defined as follows:
- 'Low Salary' for salaries less than 20000.
- 'Average Salary' for salaries between 20000 and 50000 inclusive.
- 'High Salary' for salaries greater than 50000.

The query should return the following columns:
- `salary_range` - The salary range of the employees ('Low Salary', 'Average Salary', 'High Salary').
- `employee_count` - The number of employees in that salary range.

Return the result table ordered by `salary_range` in the order ('Low Salary', 'Average Salary', 'High Salary').

Example:
Input:
Employee table:
| id | name  | salary |
|----|-------|--------|
| 1  | Alice | 10000  |
| 2  | Bob   | 25000  |
| 3  | Carol | 55000  |
| 4  | Dave  | 50000  |

Output:
| salary_range   | employee_count |
|----------------|----------------|
| Low Salary     | 1              |
| Average Salary | 2              |
| High Salary    | 1              |

Explanation:
- Alice has a salary of 10000, which falls in the 'Low Salary' range.
- Bob and Dave have salaries of 25000 and 50000, respectively, which fall in the 'Average Salary' range.
- Carol has a salary of 55000, which falls in the 'High Salary' range.
"""

# Python Solution
def group_employees_by_salary(employee_data):
    """
    Groups employees into salary ranges and counts the number of employees in each range.

    Args:
    employee_data (list of dict): A list of dictionaries where each dictionary represents an employee
                                  with keys 'id', 'name', and 'salary'.

    Returns:
    list of dict: A list of dictionaries representing the salary ranges and the count of employees in each range.
    """
    # Initialize counters for each salary range
    salary_ranges = {
        "Low Salary": 0,
        "Average Salary": 0,
        "High Salary": 0
    }

    # Iterate through the employee data and classify salaries
    for employee in employee_data:
        salary = employee['salary']
        if salary < 20000:
            salary_ranges["Low Salary"] += 1
        elif 20000 <= salary <= 50000:
            salary_ranges["Average Salary"] += 1
        else:
            salary_ranges["High Salary"] += 1

    # Convert the result into a list of dictionaries
    result = [{"salary_range": key, "employee_count": value} for key, value in salary_ranges.items()]
    return result


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    employee_data = [
        {"id": 1, "name": "Alice", "salary": 10000},
        {"id": 2, "name": "Bob", "salary": 25000},
        {"id": 3, "name": "Carol", "salary": 55000},
        {"id": 4, "name": "Dave", "salary": 50000}
    ]
    print(group_employees_by_salary(employee_data))
    # Expected Output:
    # [
    #     {"salary_range": "Low Salary", "employee_count": 1},
    #     {"salary_range": "Average Salary", "employee_count": 2},
    #     {"salary_range": "High Salary", "employee_count": 1}
    # ]

    # Test Case 2
    employee_data = [
        {"id": 1, "name": "Eve", "salary": 15000},
        {"id": 2, "name": "Frank", "salary": 30000},
        {"id": 3, "name": "Grace", "salary": 60000}
    ]
    print(group_employees_by_salary(employee_data))
    # Expected Output:
    # [
    #     {"salary_range": "Low Salary", "employee_count": 1},
    #     {"salary_range": "Average Salary", "employee_count": 1},
    #     {"salary_range": "High Salary", "employee_count": 1}
    # ]

    # Test Case 3
    employee_data = []
    print(group_employees_by_salary(employee_data))
    # Expected Output:
    # [
    #     {"salary_range": "Low Salary", "employee_count": 0},
    #     {"salary_range": "Average Salary", "employee_count": 0},
    #     {"salary_range": "High Salary", "employee_count": 0}
    # ]


# Time and Space Complexity Analysis
# Time Complexity: O(n), where n is the number of employees in the input list. We iterate through the list once.
# Space Complexity: O(1), as we use a fixed amount of additional space for the salary_ranges dictionary.

# Topic: Arrays, Hash Table