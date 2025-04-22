"""
LeetCode Question #601: Human Traffic of Stadium

Problem Statement:
X city built a new stadium, each day many people visit it. The data table `Stadium` stores the information of the people who visited the stadium. Write an SQL query to display the records with three or more consecutive rows with people having an attendance greater than or equal to 100.

The `Stadium` table is defined as follows:
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| visit_date    | date    |
| people        | int     |
+---------------+---------+
id is the primary key for this table.
Each row of this table contains the visit date and the number of people that visited the stadium on that day.

Return the result table ordered by `visit_date` in ascending order.

Example:
Input:
Stadium table:
+----+------------+--------+
| id | visit_date | people |
+----+------------+--------+
| 1  | 2023-01-01 | 10     |
| 2  | 2023-01-02 | 109    |
| 3  | 2023-01-03 | 150    |
| 4  | 2023-01-04 | 99     |
| 5  | 2023-01-05 | 145    |
| 6  | 2023-01-06 | 145    |
| 7  | 2023-01-07 | 145    |
| 8  | 2023-01-08 | 10     |
+----+------------+--------+

Output:
+----+------------+--------+
| id | visit_date | people |
+----+------------+--------+
| 5  | 2023-01-05 | 145    |
| 6  | 2023-01-06 | 145    |
| 7  | 2023-01-07 | 145    |
+----+------------+--------+

Explanation:
The output table contains rows with three or more consecutive days where the number of people is greater than or equal to 100.
"""

# Python Solution:
# Since this is an SQL problem, we will simulate the solution using Python for demonstration purposes.

from typing import List, Tuple

def human_traffic_of_stadium(stadium: List[Tuple[int, str, int]]) -> List[Tuple[int, str, int]]:
    """
    Simulates the SQL query to find rows with three or more consecutive days
    where the number of people is greater than or equal to 100.
    
    Args:
    stadium (List[Tuple[int, str, int]]): List of tuples representing the stadium table.
    
    Returns:
    List[Tuple[int, str, int]]: Filtered rows meeting the condition.
    """
    # Sort the input by visit_date (assuming it's already sorted in the input)
    stadium.sort(key=lambda x: x[1])
    
    result = []
    n = len(stadium)
    
    for i in range(n - 2):
        # Check if three consecutive rows have people >= 100
        if (stadium[i][2] >= 100 and 
            stadium[i + 1][2] >= 100 and 
            stadium[i + 2][2] >= 100):
            result.append(stadium[i])
            result.append(stadium[i + 1])
            result.append(stadium[i + 2])
    
    # Remove duplicates while maintaining order
    seen = set()
    filtered_result = []
    for row in result:
        if row not in seen:
            filtered_result.append(row)
            seen.add(row)
    
    return filtered_result

# Example Test Cases
if __name__ == "__main__":
    stadium_data = [
        (1, "2023-01-01", 10),
        (2, "2023-01-02", 109),
        (3, "2023-01-03", 150),
        (4, "2023-01-04", 99),
        (5, "2023-01-05", 145),
        (6, "2023-01-06", 145),
        (7, "2023-01-07", 145),
        (8, "2023-01-08", 10),
    ]
    
    expected_output = [
        (5, "2023-01-05", 145),
        (6, "2023-01-06", 145),
        (7, "2023-01-07", 145),
    ]
    
    assert human_traffic_of_stadium(stadium_data) == expected_output
    print("All test cases passed!")

"""
Time Complexity Analysis:
- Sorting the input list takes O(n log n), where n is the number of rows in the stadium table.
- The loop to check consecutive rows runs in O(n).
- Removing duplicates runs in O(n).
Overall time complexity: O(n log n).

Space Complexity Analysis:
- The space complexity is O(n) for storing the result and the seen set.
Overall space complexity: O(n).

Topic: SQL Simulation, Sliding Window
"""