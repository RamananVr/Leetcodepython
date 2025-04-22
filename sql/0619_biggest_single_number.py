"""
LeetCode Question #619: Biggest Single Number

Problem Statement:
Table: MyNumbers

+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
+-------------+------+
The num column is the primary key for this table.
Each row of this table contains one number.

Write an SQL query to find the biggest number in the table that only appears once.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 3   |
| 3   |
| 1   |
| 4   |
| 5   |
| 5   |
+-----+

Output:
+-----+
| num |
+-----+
| 4   |
+-----+

Explanation:
The number 4 is the only number in the table that appears exactly once.
"""

# Python Solution
# Since this is an SQL problem, we will write the SQL query as part of the solution.

def biggest_single_number_query():
    """
    Returns the SQL query to find the biggest number in the table that only appears once.
    """
    query = """
    SELECT MAX(num) AS num
    FROM MyNumbers
    WHERE num IN (
        SELECT num
        FROM MyNumbers
        GROUP BY num
        HAVING COUNT(num) = 1
    );
    """
    return query

# Example Test Cases
def example_test_cases():
    """
    Example test cases for the SQL query.
    """
    print("Example Input:")
    print("""
    MyNumbers table:
    +-----+
    | num |
    +-----+
    | 8   |
    | 8   |
    | 3   |
    | 3   |
    | 1   |
    | 4   |
    | 5   |
    | 5   |
    +-----+
    """)

    print("Expected Output:")
    print("""
    +-----+
    | num |
    +-----+
    | 4   |
    +-----+
    """)

# Time And Space Complexity Analysis
"""
Time Complexity:
- The query involves a GROUP BY operation to group numbers and calculate their counts, which takes O(n) time, where n is the number of rows in the table.
- The MAX operation scans the filtered results, which also takes O(m) time, where m is the number of unique numbers that appear exactly once.
- Overall, the time complexity is O(n).

Space Complexity:
- The space complexity is O(k), where k is the number of unique numbers in the table, as the GROUP BY operation may store intermediate results.
- The space used by the final result is negligible compared to the intermediate storage.
- Overall, the space complexity is O(k).

Topic: SQL
"""

# Run Example Test Cases
if __name__ == "__main__":
    print("SQL Query:")
    print(biggest_single_number_query())
    example_test_cases()