"""
LeetCode Question #2668: Find Latest Salaries

Problem Statement:
Table: Salary
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| emp_id        | int     |
| firstname     | varchar |
| lastname      | varchar |
| salary        | int     |
| department_id | int     |
+---------------+---------+
(emp_id, salary) is the primary key (combination of columns with unique values) for this table.
Each row contains employee id, first name, last name, salary, and department id.

Write a solution to find the latest salary (i.e., the maximum salary) for each employee.

Return the result table ordered by emp_id in ascending order.

Examples:
Example 1:
Input: 
Salary table:
+--------+-----------+----------+--------+---------------+
| emp_id | firstname | lastname | salary | department_id |
+--------+-----------+----------+--------+---------------+
| 1      | Todd      | Wilson   | 110000 | 1             |
| 1      | Todd      | Wilson   | 106000 | 1             |
| 2      | Justin    | Garcia   | 90000  | 1             |
| 2      | Justin    | Garcia   | 85000  | 1             |
| 3      | Kelly     | Rosario  | 96000  | 1             |
| 3      | Kelly     | Rosario  | 89000  | 1             |
+--------+-----------+----------+--------+---------------+
Output: 
+--------+-----------+----------+--------+---------------+
| emp_id | firstname | lastname | salary | department_id |
+--------+-----------+----------+--------+---------------+
| 1      | Todd      | Wilson   | 110000 | 1             |
| 2      | Justin    | Garcia   | 90000  | 1             |
| 3      | Kelly     | Rosario  | 96000  | 1             |
+--------+-----------+----------+--------+---------------+
Explanation: 
For emp_id 1, the maximum salary is 110000.
For emp_id 2, the maximum salary is 90000.
For emp_id 3, the maximum salary is 96000.
"""

from typing import List, Dict, Any
import pandas as pd

def find_latest_salaries_pandas(salary_df: pd.DataFrame) -> pd.DataFrame:
    """
    Find the latest (maximum) salary for each employee using pandas.
    """
    # Group by emp_id and find the max salary, keeping all columns
    result = salary_df.loc[salary_df.groupby('emp_id')['salary'].idxmax()]
    
    # Sort by emp_id in ascending order
    result = result.sort_values('emp_id').reset_index(drop=True)
    
    return result

def find_latest_salaries_dict(salary_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Find the latest salary for each employee using dictionary approach.
    """
    # Dictionary to store the maximum salary record for each employee
    max_salary_records = {}
    
    for record in salary_data:
        emp_id = record['emp_id']
        salary = record['salary']
        
        if emp_id not in max_salary_records or salary > max_salary_records[emp_id]['salary']:
            max_salary_records[emp_id] = record
    
    # Sort by emp_id and return as list
    result = sorted(max_salary_records.values(), key=lambda x: x['emp_id'])
    return result

def find_latest_salaries_groupby(salary_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Find the latest salary using groupby approach.
    """
    from itertools import groupby
    
    # Sort by emp_id first
    sorted_data = sorted(salary_data, key=lambda x: x['emp_id'])
    
    result = []
    for emp_id, group in groupby(sorted_data, key=lambda x: x['emp_id']):
        # Find the record with maximum salary in this group
        max_record = max(group, key=lambda x: x['salary'])
        result.append(max_record)
    
    return result

# SQL Solution (for reference)
sql_solution = """
SELECT emp_id, firstname, lastname, salary, department_id
FROM Salary s1
WHERE salary = (
    SELECT MAX(salary)
    FROM Salary s2
    WHERE s1.emp_id = s2.emp_id
)
ORDER BY emp_id;
"""

# Alternative SQL with RANK()
sql_solution_rank = """
SELECT emp_id, firstname, lastname, salary, department_id
FROM (
    SELECT emp_id, firstname, lastname, salary, department_id,
           RANK() OVER (PARTITION BY emp_id ORDER BY salary DESC) as rn
    FROM Salary
) ranked
WHERE rn = 1
ORDER BY emp_id;
"""

# Test Cases
if __name__ == "__main__":
    # Test data
    salary_data = [
        {"emp_id": 1, "firstname": "Todd", "lastname": "Wilson", "salary": 110000, "department_id": 1},
        {"emp_id": 1, "firstname": "Todd", "lastname": "Wilson", "salary": 106000, "department_id": 1},
        {"emp_id": 2, "firstname": "Justin", "lastname": "Garcia", "salary": 90000, "department_id": 1},
        {"emp_id": 2, "firstname": "Justin", "lastname": "Garcia", "salary": 85000, "department_id": 1},
        {"emp_id": 3, "firstname": "Kelly", "lastname": "Rosario", "salary": 96000, "department_id": 1},
        {"emp_id": 3, "firstname": "Kelly", "lastname": "Rosario", "salary": 89000, "department_id": 1},
    ]
    
    expected = [
        {"emp_id": 1, "firstname": "Todd", "lastname": "Wilson", "salary": 110000, "department_id": 1},
        {"emp_id": 2, "firstname": "Justin", "lastname": "Garcia", "salary": 90000, "department_id": 1},
        {"emp_id": 3, "firstname": "Kelly", "lastname": "Rosario", "salary": 96000, "department_id": 1},
    ]
    
    print("Testing dictionary approach:")
    result1 = find_latest_salaries_dict(salary_data)
    print(f"Result: {result1}")
    print(f"Expected: {expected}")
    print(f"Match: {'✓' if result1 == expected else '✗'}")
    
    print("\nTesting groupby approach:")
    result2 = find_latest_salaries_groupby(salary_data)
    print(f"Result: {result2}")
    print(f"Expected: {expected}")
    print(f"Match: {'✓' if result2 == expected else '✗'}")
    
    print("\nTesting pandas approach:")
    df = pd.DataFrame(salary_data)
    result3_df = find_latest_salaries_pandas(df)
    result3 = result3_df.to_dict('records')
    print(f"Result: {result3}")
    print(f"Expected: {expected}")
    print(f"Match: {'✓' if result3 == expected else '✗'}")
    
    print(f"\nSQL Solution:\n{sql_solution}")
    print(f"\nSQL Solution with RANK:\n{sql_solution_rank}")

"""
Time and Space Complexity Analysis:

Dictionary Approach:
Time Complexity: O(n) - single pass through the data
Space Complexity: O(k) - where k is the number of unique employees

GroupBy Approach:
Time Complexity: O(n log n) - due to sorting
Space Complexity: O(n) - for storing sorted data

Pandas Approach:
Time Complexity: O(n) - groupby and idxmax operations
Space Complexity: O(n) - for intermediate results

Key Insights:
1. This is a classic "find maximum in each group" problem
2. Dictionary approach is most efficient for this specific case
3. SQL window functions (RANK/ROW_NUMBER) are ideal for database solutions
4. Pandas groupby with idxmax is elegant for data analysis

Topic: Database, Data Processing, Grouping
"""
