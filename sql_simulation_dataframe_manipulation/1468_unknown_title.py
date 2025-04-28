"""
LeetCode Problem #1468: Calculate Salaries of Employees After Taxes

Problem Statement:
You are given a table `Employee` with the following structure:

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| name        | varchar |
| salary      | int     |

id is the primary key for this table. Each row of this table contains information about the id, name, and salary of an employee.

Write an SQL query to calculate the salary of each employee after taxes. The tax rate is as follows:
- If the salary is less than or equal to $1000, the tax rate is 10%.
- If the salary is between $1001 and $2000 inclusive, the tax rate is 15%.
- If the salary is greater than $2000, the tax rate is 20%.

Return the result table in any order.

The result format should be:

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| name        | varchar |
| salary      | int     |

Where `salary` is the salary of the employee after taxes.

---

Note: Since this is an SQL problem, we will provide a Python solution to simulate the behavior of the query using pandas.
"""

# Python Solution Using Pandas
import pandas as pd

def calculate_salaries_after_taxes(employee: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the salary of each employee after applying the tax rate.

    Args:
    employee (pd.DataFrame): A DataFrame containing the columns 'id', 'name', and 'salary'.

    Returns:
    pd.DataFrame: A DataFrame with the columns 'id', 'name', and 'salary' (after taxes).
    """
    def apply_tax(salary):
        if salary <= 1000:
            return salary * 0.9  # 10% tax
        elif salary <= 2000:
            return salary * 0.85  # 15% tax
        else:
            return salary * 0.8  # 20% tax

    # Apply the tax calculation to the salary column
    employee['salary'] = employee['salary'].apply(apply_tax)
    return employee

# Example Test Cases
if __name__ == "__main__":
    # Input DataFrame
    data = {
        "id": [1, 2, 3, 4],
        "name": ["Alice", "Bob", "Charlie", "David"],
        "salary": [800, 1500, 2500, 1000]
    }
    employee_df = pd.DataFrame(data)

    # Expected Output:
    # id | name     | salary
    # 1  | Alice    | 720.0
    # 2  | Bob      | 1275.0
    # 3  | Charlie  | 2000.0
    # 4  | David    | 900.0

    result_df = calculate_salaries_after_taxes(employee_df)
    print(result_df)

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates over the 'salary' column once to apply the tax calculation.
- If there are `n` employees, the time complexity is O(n).

Space Complexity:
- The function modifies the DataFrame in place, so no additional space is required apart from the input DataFrame.
- Space complexity is O(1) (in-place modification).

Topic: SQL Simulation, DataFrame Manipulation
"""