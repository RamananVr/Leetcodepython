"""
LeetCode Problem #1322: Ads Performance

Problem Statement:
Table: Ads

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| ad_id         | int     |
| user_id       | int     |
| action        | enum    |
+---------------+---------+
(ad_id, user_id) is the primary key for this table.
The table contains information about ads clicked by users.
The action column is an ENUM type with the following possible values: ('Clicked', 'Viewed', 'Ignored').

Write an SQL query to find the percentage of users who viewed and then clicked each ad. 
The percentage should be rounded to two decimal places.

Return the result table in any order.

The query result format is in the following example.

Example Input:
Ads table:
+-------+---------+---------+
| ad_id | user_id | action  |
+-------+---------+---------+
| 1     | 1       | Viewed  |
| 1     | 1       | Clicked |
| 1     | 2       | Viewed  |
| 1     | 2       | Ignored |
| 2     | 3       | Viewed  |
| 2     | 3       | Clicked |
| 2     | 4       | Viewed  |
| 2     | 4       | Ignored |
+-------+---------+---------+

Output:
+-------+-------------------+
| ad_id | view_click_ratio  |
+-------+-------------------+
| 1     | 50.00             |
| 2     | 50.00             |
+-------+-------------------+
"""

# Python Solution
# Note: Since this is an SQL-based problem, the solution is provided as an SQL query.

sql_query = """
SELECT
    ad_id,
    ROUND(
        (COUNT(DISTINCT CASE WHEN action = 'Clicked' THEN user_id END) * 100.0) /
        NULLIF(COUNT(DISTINCT CASE WHEN action IN ('Viewed', 'Clicked') THEN user_id END), 0),
        2
    ) AS view_click_ratio
FROM Ads
GROUP BY ad_id;
"""

# Example Test Cases
# Note: Test cases for SQL problems are typically run in a database environment.
# Below is a representation of how the Ads table would look and the expected output.

ads_table = [
    {"ad_id": 1, "user_id": 1, "action": "Viewed"},
    {"ad_id": 1, "user_id": 1, "action": "Clicked"},
    {"ad_id": 1, "user_id": 2, "action": "Viewed"},
    {"ad_id": 1, "user_id": 2, "action": "Ignored"},
    {"ad_id": 2, "user_id": 3, "action": "Viewed"},
    {"ad_id": 2, "user_id": 3, "action": "Clicked"},
    {"ad_id": 2, "user_id": 4, "action": "Viewed"},
    {"ad_id": 2, "user_id": 4, "action": "Ignored"},
]

expected_output = [
    {"ad_id": 1, "view_click_ratio": 50.00},
    {"ad_id": 2, "view_click_ratio": 50.00},
]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The query involves a GROUP BY operation on the `ad_id` column, which is O(n), where n is the number of rows in the Ads table.
- COUNT and CASE operations are performed within each group, which are O(k), where k is the number of rows in each group.
- Overall complexity is O(n).

Space Complexity:
- The space complexity is O(m), where m is the number of unique `ad_id` values, as we store the results for each group.

Note: The complexity assumes the database engine optimizes the query execution efficiently.
"""

# Topic: SQL