"""
LeetCode Question #584: Find Customer Referee

Problem Statement:
Table: Customer

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
id is the primary key for this table.
Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.

Write an SQL query to return the names of customers whose referee_id is not 2.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Customer table:
+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+

Output:
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+
Explanation: 
The customers whose referee_id is not 2 are Will, Jane, Bill, and Zack.
"""

# Python Solution
# Since this is an SQL problem, the solution is provided as an SQL query.

def find_customer_referee():
    """
    SQL Query to solve the problem:
    """
    query = """
    SELECT name
    FROM Customer
    WHERE referee_id != 2 OR referee_id IS NULL;
    """
    return query

# Example Test Cases
def example_test_cases():
    """
    Example test cases for the SQL query.
    """
    input_table = [
        {"id": 1, "name": "Will", "referee_id": None},
        {"id": 2, "name": "Jane", "referee_id": None},
        {"id": 3, "name": "Alex", "referee_id": 2},
        {"id": 4, "name": "Bill", "referee_id": None},
        {"id": 5, "name": "Zack", "referee_id": 1},
        {"id": 6, "name": "Mark", "referee_id": 2},
    ]

    expected_output = [
        {"name": "Will"},
        {"name": "Jane"},
        {"name": "Bill"},
        {"name": "Zack"},
    ]

    print("Input Table:", input_table)
    print("Expected Output:", expected_output)
    print("SQL Query:", find_customer_referee())

# Time And Space Complexity Analysis
"""
Time Complexity:
The time complexity of the SQL query depends on the number of rows in the Customer table. 
If there are N rows, the query will perform a scan of all rows, resulting in O(N) time complexity.

Space Complexity:
The space complexity is O(1) since the query does not use any additional data structures and operates directly on the database.

Note: The actual performance may vary depending on the database engine and indexing.
"""

# Topic
"""
Topic: SQL
"""

# Run Example Test Cases
if __name__ == "__main__":
    example_test_cases()