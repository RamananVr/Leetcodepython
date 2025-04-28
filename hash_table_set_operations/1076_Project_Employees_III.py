"""
LeetCode Problem #1076: Project Employees III

Problem Statement:
You are given a table `Employee` with the following structure:

| Column Name | Type    |
|-------------|---------|
| employee_id | int     |
| project_id  | int     |

employee_id is the primary key for this table.
Each row of this table indicates that the employee with employee_id is working on the project with project_id.

Write an SQL query to find the employees who are working on all the projects.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Employee table:
| employee_id | project_id |
|-------------|------------|
| 1           | 1          |
| 2           | 1          |
| 3           | 1          |
| 1           | 2          |
| 2           | 2          |

Output:
| employee_id |
|-------------|
| 1           |
| 2           |

Explanation:
- The total number of projects is 2.
- Employee 1 works on both project 1 and project 2.
- Employee 2 works on both project 1 and project 2.
- Employee 3 works only on project 1.
Hence, we return employees 1 and 2 as they work on all the projects.
"""

# Python Solution:
# Since this is an SQL problem, we will simulate the solution using Python for demonstration purposes.

from collections import defaultdict

def employees_working_on_all_projects(employee_project_list):
    """
    Function to find employees who are working on all the projects.

    Args:
    employee_project_list (List[Tuple[int, int]]): A list of tuples where each tuple represents
                                                   (employee_id, project_id).

    Returns:
    List[int]: A list of employee IDs who are working on all the projects.
    """
    # Step 1: Find all unique projects
    projects = set()
    employee_projects = defaultdict(set)

    for employee_id, project_id in employee_project_list:
        projects.add(project_id)
        employee_projects[employee_id].add(project_id)

    # Step 2: Find employees who are working on all projects
    all_projects = set(projects)
    result = []

    for employee_id, project_set in employee_projects.items():
        if project_set == all_projects:
            result.append(employee_id)

    return result


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    employee_project_list = [
        (1, 1),
        (2, 1),
        (3, 1),
        (1, 2),
        (2, 2)
    ]
    print(employees_working_on_all_projects(employee_project_list))  # Output: [1, 2]

    # Test Case 2
    employee_project_list = [
        (1, 1),
        (2, 1),
        (1, 2),
        (2, 2),
        (1, 3)
    ]
    print(employees_working_on_all_projects(employee_project_list))  # Output: [1]

    # Test Case 3
    employee_project_list = [
        (1, 1),
        (2, 1),
        (3, 1),
        (1, 2),
        (2, 2),
        (3, 2),
        (1, 3),
        (2, 3),
        (3, 3)
    ]
    print(employees_working_on_all_projects(employee_project_list))  # Output: [1, 2, 3]


# Time and Space Complexity Analysis:
# Time Complexity:
# - O(n): We iterate through the employee_project_list once to populate the projects and employee_projects.
# - O(m): We iterate through the employee_projects dictionary to check if each employee works on all projects.
# - Overall: O(n + m), where n is the number of entries in employee_project_list and m is the number of employees.

# Space Complexity:
# - O(p): Space for the `projects` set, where p is the number of unique projects.
# - O(e): Space for the `employee_projects` dictionary, where e is the number of employees.
# - Overall: O(p + e).

# Topic: Hash Table, Set Operations