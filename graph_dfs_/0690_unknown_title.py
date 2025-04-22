"""
LeetCode Problem #690: Employee Importance

Problem Statement:
You have a data structure of employee information, which includes the employee's unique ID, their importance value, 
and their direct subordinates' IDs.

You are given an array of employees where:
- `employees[i].id` is the ID of the `i-th` employee.
- `employees[i].importance` is the importance value of the `i-th` employee.
- `employees[i].subordinates` is a list of IDs of the direct subordinates of the `i-th` employee.

Given an integer `id` that represents an employee's ID, return the total importance value of this employee and all their subordinates.

Example:
Input: employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], id = 1
Output: 11
Explanation:
Employee 1 has an importance value of 5 and has two direct subordinates: employee 2 and employee 3.
They each have an importance value of 3. So, the total importance value is 5 + 3 + 3 = 11.

Constraints:
1. One employee has at most one direct leader and may have several subordinates.
2. The maximum number of employees is 2000.
3. The maximum importance value of any employee is 1000.
4. The ID of each employee is unique.
"""

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: list[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

# Solution
class Solution:
    def getImportance(self, employees: list[Employee], id: int) -> int:
        # Create a dictionary to map employee ID to the Employee object for quick access
        employee_map = {employee.id: employee for employee in employees}
        
        # Helper function to calculate total importance using DFS
        def dfs(emp_id: int) -> int:
            employee = employee_map[emp_id]
            total_importance = employee.importance
            for sub_id in employee.subordinates:
                total_importance += dfs(sub_id)
            return total_importance
        
        # Start DFS from the given employee ID
        return dfs(id)

# Example Test Cases
if __name__ == "__main__":
    # Create employees
    employees = [
        Employee(1, 5, [2, 3]),
        Employee(2, 3, []),
        Employee(3, 3, [])
    ]
    
    # Create solution instance
    solution = Solution()
    
    # Test case 1
    id = 1
    print(solution.getImportance(employees, id))  # Output: 11
    
    # Test case 2
    id = 2
    print(solution.getImportance(employees, id))  # Output: 3
    
    # Test case 3
    id = 3
    print(solution.getImportance(employees, id))  # Output: 3

"""
Time Complexity Analysis:
- Let `n` be the number of employees and `m` be the total number of subordinates across all employees.
- Building the `employee_map` takes O(n) time.
- The DFS traversal visits each employee and their subordinates exactly once, so it takes O(n + m) time.
- Overall time complexity: O(n + m).

Space Complexity Analysis:
- The `employee_map` dictionary takes O(n) space.
- The recursion stack in the DFS can go as deep as the number of employees in the worst case, which is O(n).
- Overall space complexity: O(n).

Topic: Graph (DFS)
"""