"""
LeetCode Question #176: Second Highest Salary

Problem Statement:
Write an SQL query to get the second highest salary from the Employee table. If there is no second highest salary, the query should return null.

The Employee table is defined as follows:
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, the result should be null.

Expected Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

Note: Since this is an SQL problem, we will simulate the solution in Python for demonstration purposes.
"""

# Python Solution
def second_highest_salary(salaries):
    """
    Function to find the second highest salary from a list of salaries.
    If there is no second highest salary, return None.

    :param salaries: List[int] - A list of integers representing salaries.
    :return: int or None - The second highest salary or None if it doesn't exist.
    """
    # Remove duplicates and sort in descending order
    unique_salaries = sorted(set(salaries), reverse=True)
    
    # Check if there is a second highest salary
    if len(unique_salaries) < 2:
        return None
    return unique_salaries[1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Normal case with distinct salaries
    salaries1 = [100, 200, 300]
    print(second_highest_salary(salaries1))  # Expected Output: 200

    # Test Case 2: Case with duplicate salaries
    salaries2 = [100, 200, 200, 300]
    print(second_highest_salary(salaries2))  # Expected Output: 200

    # Test Case 3: Case with only one salary
    salaries3 = [100]
    print(second_highest_salary(salaries3))  # Expected Output: None

    # Test Case 4: Case with no salaries
    salaries4 = []
    print(second_highest_salary(salaries4))  # Expected Output: None

    # Test Case 5: Case with all salaries being the same
    salaries5 = [100, 100, 100]
    print(second_highest_salary(salaries5))  # Expected Output: None

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the unique salaries takes O(n log n), where n is the number of salaries.
- Removing duplicates using `set()` takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The `set()` operation and the sorted list both require O(n) space.
- Overall space complexity: O(n).

Topic: Arrays
"""