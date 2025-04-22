"""
LeetCode Question #175: Combine Two Tables

Problem Statement:
------------------
Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| personId    | int     |
| lastName    | varchar |
| firstName   | varchar |
+-------------+---------+
personId is the primary key column for this table.

Table: Address
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| addressId   | int     |
| personId    | int     |
| city        | varchar |
| state       | varchar |
+-------------+---------+
addressId is the primary key column for this table.

Write a SQL query for a report that provides the following information for each person in the Person table, 
regardless of whether they have an address:
- First Name
- Last Name
- City
- State

If a person does not have an address, their city and state should be NULL.

Expected Output:
The query should return the result in any order.

"""

# Solution:
# Since this is a SQL problem, we will write the SQL query as the solution.

"""
SQL Query:
----------
SELECT 
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM 
    Person p
LEFT JOIN 
    Address a
ON 
    p.personId = a.personId;
"""

# Example Test Cases:
# -------------------
# Input:
# Person Table:
# +----------+----------+-----------+
# | personId | lastName | firstName |
# +----------+----------+-----------+
# | 1        | Smith    | John      |
# | 2        | Johnson  | Jane      |
# +----------+----------+-----------+

# Address Table:
# +-----------+----------+----------+-------+
# | addressId | personId | city     | state |
# +-----------+----------+----------+-------+
# | 1         | 1        | New York| NY    |
# +-----------+----------+----------+-------+

# Output:
# +-----------+----------+----------+-------+
# | firstName | lastName | city     | state |
# +-----------+----------+----------+-------+
# | John      | Smith    | New York| NY    |
# | Jane      | Johnson  | NULL    | NULL  |
# +-----------+----------+----------+-------+

# Time and Space Complexity Analysis:
# -----------------------------------
# Time Complexity:
# - The time complexity of this query depends on the size of the `Person` and `Address` tables.
# - Let `n` be the number of rows in the `Person` table and `m` be the number of rows in the `Address` table.
# - The LEFT JOIN operation typically has a time complexity of O(n + m), assuming proper indexing on the `personId` column.

# Space Complexity:
# - The space complexity is O(n + m) for storing the intermediate results of the join operation.

# Topic: SQL, Joins