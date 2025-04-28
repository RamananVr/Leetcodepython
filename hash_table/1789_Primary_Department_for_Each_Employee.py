"""
LeetCode Problem #1789: Primary Department for Each Employee

Problem Statement:
You are given a list of employees, where each employee is represented as a list of strings. 
Each string in the list represents a department that the employee is a part of. 
An employee can belong to multiple departments, but there is always one "primary" department 
for each employee. The primary department is the one that is unique to that employee 
(i.e., no other employee belongs to that department). If there is no such unique department 
for an employee, then that employee does not have a primary department.

Write a function `findPrimaryDepartment(employees: List[List[str]]) -> List[str]` that takes 
a list of employees and returns a list of strings, where the i-th string is the primary 
department of the i-th employee. If an employee does not have a primary department, 
return an empty string for that employee.

Constraints:
- 1 <= len(employees) <= 1000
- 1 <= len(employees[i]) <= 100
- 1 <= len(employees[i][j]) <= 20
- All department names consist of lowercase English letters.

Example:
Input: employees = [["a", "b", "c"], ["b", "c", "d"], ["e", "f"]]
Output: ["a", "d", "e"]

Explanation:
- Employee 0 has departments ["a", "b", "c"]. "a" is unique to this employee, so it is their primary department.
- Employee 1 has departments ["b", "c", "d"]. "d" is unique to this employee, so it is their primary department.
- Employee 2 has departments ["e", "f"]. "e" is unique to this employee, so it is their primary department.
"""

from typing import List
from collections import Counter

def findPrimaryDepartment(employees: List[List[str]]) -> List[str]:
    # Step 1: Count the frequency of each department across all employees
    department_count = Counter(dept for employee in employees for dept in employee)
    
    # Step 2: Determine the primary department for each employee
    result = []
    for employee in employees:
        primary_department = ""
        for dept in employee:
            if department_count[dept] == 1:  # Unique department
                primary_department = dept
                break
        result.append(primary_department)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    employees1 = [["a", "b", "c"], ["b", "c", "d"], ["e", "f"]]
    print(findPrimaryDepartment(employees1))  # Output: ["a", "d", "e"]

    # Test Case 2
    employees2 = [["a", "b"], ["b", "c"], ["c", "d"]]
    print(findPrimaryDepartment(employees2))  # Output: ["a", "d", ""]

    # Test Case 3
    employees3 = [["a"], ["b"], ["c"]]
    print(findPrimaryDepartment(employees3))  # Output: ["a", "b", "c"]

    # Test Case 4
    employees4 = [["a", "b"], ["a", "b"], ["a", "b"]]
    print(findPrimaryDepartment(employees4))  # Output: ["", "", ""]

    # Test Case 5
    employees5 = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
    print(findPrimaryDepartment(employees5))  # Output: ["a", "d", "g"]

"""
Time Complexity Analysis:
- Counting the frequency of all departments: O(n * m), where n is the number of employees and m is the average number of departments per employee.
- Determining the primary department for each employee: O(n * m).
- Overall time complexity: O(n * m).

Space Complexity Analysis:
- The Counter object stores the frequency of all departments, which requires O(d) space, where d is the total number of unique departments.
- The result list requires O(n) space.
- Overall space complexity: O(d + n).

Topic: Hash Table
"""