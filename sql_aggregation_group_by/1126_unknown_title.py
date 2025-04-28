"""
LeetCode Problem #1126: Active Businesses

Problem Statement:
You are given a table `Activity` with the following schema:

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| business_id | int     |
| event_type  | varchar |
| occurences  | int     |
+-------------+---------+
(business_id, event_type) is the primary key for this table.
Each row in the table logs the info that an event of some type occurred at some business for a certain number of times.

Write an SQL query to find all businesses that have more than one type of event with occurences greater than 10.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Activity table:
+-------------+------------+------------+
| business_id | event_type | occurences |
+-------------+------------+------------+
| 1           | A          | 12         |
| 1           | B          | 8          |
| 2           | A          | 20         |
| 2           | B          | 15         |
| 3           | A          | 5          |
| 3           | B          | 7          |
+-------------+------------+------------+

Output:
+-------------+
| business_id |
+-------------+
| 2           |
+-------------+

Explanation:
- Business 1 has only one event type (A) with occurences > 10.
- Business 2 has two event types (A and B) with occurences > 10.
- Business 3 does not have any event type with occurences > 10.
Thus, only business 2 is returned.
"""

# Python Solution:
# Since this is an SQL-based problem, we will write the SQL query as the solution.

"""
SQL Query Solution:

SELECT DISTINCT business_id
FROM Activity
WHERE occurences > 10
GROUP BY business_id
HAVING COUNT(DISTINCT event_type) > 1;
"""

# Example Test Cases:
# The test cases are based on the SQL query and the given example.

"""
Input:
Activity table:
+-------------+------------+------------+
| business_id | event_type | occurences |
+-------------+------------+------------+
| 1           | A          | 12         |
| 1           | B          | 8          |
| 2           | A          | 20         |
| 2           | B          | 15         |
| 3           | A          | 5          |
| 3           | B          | 7          |
+-------------+------------+------------+

Output:
+-------------+
| business_id |
+-------------+
| 2           |
+-------------+
"""

# Time and Space Complexity Analysis:
# Time Complexity: O(n), where n is the number of rows in the Activity table. The query involves filtering rows with occurences > 10, grouping by business_id, and counting distinct event types.
# Space Complexity: O(k), where k is the number of unique business_ids in the table. This is due to the grouping operation.

# Topic: SQL, Aggregation, Group By