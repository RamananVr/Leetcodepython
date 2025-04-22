"""
LeetCode Question #177: Nth Highest Salary

Problem Statement:
Write a SQL query to get the nth highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

For example, given the above Employee table, the nth highest salary where n = 2 should return 200 as the second highest salary.

If there is no nth highest salary, the query should return null.

Example:
Input:
Employee table:
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

n = 2

Output:
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+

Note:
- The `Salary` column is guaranteed to be unique.
- You are required to write a SQL query for this problem.
"""

# Python Solution:
# Since this is a SQL problem, we will simulate the solution in Python for demonstration purposes.

def get_nth_highest_salary(salaries, n):
    """
    Function to find the nth highest salary from a list of salaries.

    :param salaries: List[int] - A list of unique salaries.
    :param n: int - The rank of the salary to find.
    :return: int or None - The nth highest salary, or None if it doesn't exist.
    """
    # Sort the salaries in descending order
    sorted_salaries = sorted(salaries, reverse=True)
    
    # Check if n is within the range of the sorted salaries
    if n <= len(sorted_salaries):
        return sorted_salaries[n - 1]
    else:
        return None

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    salaries = [100, 200, 300]
    n = 2
    print(f"Test Case 1: {get_nth_highest_salary(salaries, n)}")  # Expected Output: 200

    # Test Case 2
    salaries = [100, 200, 300]
    n = 1
    print(f"Test Case 2: {get_nth_highest_salary(salaries, n)}")  # Expected Output: 300

    # Test Case 3
    salaries = [100, 200, 300]
    n = 4
    print(f"Test Case 3: {get_nth_highest_salary(salaries, n)}")  # Expected Output: None

    # Test Case 4
    salaries = [500, 400, 300, 200, 100]
    n = 3
    print(f"Test Case 4: {get_nth_highest_salary(salaries, n)}")  # Expected Output: 300

    # Test Case 5
    salaries = []
    n = 1
    print(f"Test Case 5: {get_nth_highest_salary(salaries, n)}")  # Expected Output: None

# Time and Space Complexity Analysis:
# Time Complexity: O(n log n), where n is the number of salaries. This is due to the sorting step.
# Space Complexity: O(n), as we create a new list to store the sorted salaries.

# Topic: Sorting