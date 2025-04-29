"""
LeetCode Problem #1421: NPV Queries

Table: NPV
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| year          | int     |
| npv           | int     |
+---------------+---------+
(id, year) is the primary key (combination of columns with unique values) of this table.
The table has information about the id and the year of each inventory and the corresponding net present value.

Table: Queries
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| year          | int     |
+---------------+---------+
(id, year) is the primary key (combination of columns with unique values) of this table.
The table has information about the id and the year of each inventory query.

Write a solution to find the npv of each query of the Queries table.
Return the result table in any order.
"""

# Problem Statement:
"""
Join the `Queries` table with the `NPV` table based on the composite key (id, year).
For each row in the `Queries` table, retrieve the corresponding `npv` from the `NPV` table.
If a specific (id, year) pair from `Queries` does not exist in the `NPV` table, the `npv` for that query should be considered 0.

Example 1:
Input: 
NPV table:
+------+--------+--------+
| id   | year   | npv    |
+------+--------+--------+
| 1    | 2018   | 100    |
| 7    | 2020   | 30     |
| 13   | 2019   | 40     |
| 1    | 2019   | 113    |
| 2    | 2008   | 121    |
| 3    | 2009   | 12     |
| 11   | 2020   | 99     |
| 7    | 2019   | 0      |
+------+--------+--------+
Queries table:
+------+--------+
| id   | year   |
+------+--------+
| 1    | 2019   |
| 2    | 2008   |
| 3    | 2009   |
| 7    | 2018   |
| 7    | 2019   |
| 7    | 2020   |
| 13   | 2019   |
+------+--------+
Output: 
+------+--------+--------+
| id   | year   | npv    |
+------+--------+--------+
| 1    | 2019   | 113    |
| 2    | 2008   | 121    |
| 3    | 2009   | 12     |
| 7    | 2018   | 0      |  <- Note: (7, 2018) not in NPV, so npv is 0
| 7    | 2019   | 0      |
| 7    | 2020   | 30     |
| 13   | 2019   | 40     |
+------+--------+--------+
Explanation: 
The npv value of (7, 2018) is not present in the NPV table, we consider it 0.
The npv values of all other queries can be found in the NPV table.
"""

# SQL Solution:
"""
-- Use LEFT JOIN to keep all rows from Queries and match corresponding rows from NPV.
-- Join on both id and year.
-- Use COALESCE (or IFNULL in MySQL) to replace NULL npv values (where no match was found) with 0.

SELECT
    q.id,
    q.year,
    COALESCE(n.npv, 0) AS npv
FROM
    Queries q
LEFT JOIN
    NPV n ON q.id = n.id AND q.year = n.year;

-- Alternative using IFNULL (MySQL specific):
-- SELECT
--     q.id,
--     q.year,
--     IFNULL(n.npv, 0) AS npv
-- FROM
--     Queries q
-- LEFT JOIN
--     NPV n ON q.id = n.id AND q.year = n.year;

"""

# Example Usage (Conceptual - cannot run SQL directly in this Python script)
# Assume you have a database connection `conn` and cursor `cur`

# Sample Data Creation (for illustration)
# cur.execute("CREATE TABLE NPV (id INT, year INT, npv INT, PRIMARY KEY (id, year));")
# cur.execute("INSERT INTO NPV (id, year, npv) VALUES (1, 2018, 100), (7, 2020, 30), (13, 2019, 40), (1, 2019, 113), (2, 2008, 121), (3, 2009, 12), (11, 2020, 99), (7, 2019, 0);")
# cur.execute("CREATE TABLE Queries (id INT, year INT, PRIMARY KEY (id, year));")
# cur.execute("INSERT INTO Queries (id, year) VALUES (1, 2019), (2, 2008), (3, 2009), (7, 2018), (7, 2019), (7, 2020), (13, 2019);")
# conn.commit()

# Execution
# query = """
# SELECT
#     q.id,
#     q.year,
#     COALESCE(n.npv, 0) AS npv
# FROM
#     Queries q
# LEFT JOIN
#     NPV n ON q.id = n.id AND q.year = n.year;
# """
# cur.execute(query)
# results = cur.fetchall()
# print("Query Results:")
# for row in results:
#     print(row)

# Expected Output from Example:
# (1, 2019, 113)
# (2, 2008, 121)
# (3, 2009, 12)
# (7, 2018, 0)
# (7, 2019, 0)
# (7, 2020, 30)
# (13, 2019, 40)

# Time and Space Complexity Analysis:
"""
Time Complexity: Depends on the database implementation, indexing, and table sizes. Typically, a hash join or merge join would be used.
- If indexes exist on the join columns (id, year) for both tables, the complexity is often closer to O(Q + N) or O(Q log N) or O(N log Q), where Q is the number of rows in Queries and N is the number of rows in NPV.
- Without indexes, it could degrade to O(Q * N) in the worst case (nested loop join).

Space Complexity: O(Q) in the worst case to store the result set. The join operation might require intermediate space depending on the join algorithm used by the database (e.g., for hashing or sorting).
"""

# Topic: Database
"""
Topic: Database, SQL, Join
"""