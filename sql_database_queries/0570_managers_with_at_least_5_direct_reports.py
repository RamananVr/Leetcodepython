"""
LeetCode Question #570: Managers with at Least 5 Direct Reports

Problem Statement:
The `Employee` table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

+-----+-------+--------+-----------+
| Id  | Name  | Salary | ManagerId |
+-----+-------+--------+-----------+
| 1   | Joe   | 70000  | 3         |
| 2   | Henry | 80000  | 4         |
| 3   | Sam   | 60000  | NULL      |
| 4   | Max   | 90000  | NULL      |
+-----+-------+--------+-----------+

Write a SQL query to find the managers who have at least 5 direct reports.

For the above table, no manager has at least 5 direct reports, so the result is empty.

Expected Output:
The output should be a table with a single column `Name` that lists the names of managers with at least 5 direct reports.

+------+
| Name |
+------+

Solution:
Since this is a SQL problem, the solution involves writing a SQL query. However, as a Python expert, I will demonstrate how to execute this query using Python and SQLite.

"""

import sqlite3

# Step 1: Create the database and table
def setup_database():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    
    # Create Employee table
    cursor.execute("""
    CREATE TABLE Employee (
        Id INTEGER PRIMARY KEY,
        Name TEXT,
        Salary INTEGER,
        ManagerId INTEGER
    )
    """)
    
    # Insert sample data
    cursor.executemany("""
    INSERT INTO Employee (Id, Name, Salary, ManagerId)
    VALUES (?, ?, ?, ?)
    """, [
        (1, "Joe", 70000, 3),
        (2, "Henry", 80000, 4),
        (3, "Sam", 60000, None),
        (4, "Max", 90000, None)
    ])
    
    return connection, cursor

# Step 2: Write the SQL query
def find_managers_with_at_least_5_reports(cursor):
    query = """
    SELECT Name
    FROM Employee
    WHERE Id IN (
        SELECT ManagerId
        FROM Employee
        GROUP BY ManagerId
        HAVING COUNT(*) >= 5
    )
    """
    cursor.execute(query)
    return cursor.fetchall()

# Step 3: Example test cases
def test_find_managers_with_at_least_5_reports():
    connection, cursor = setup_database()
    result = find_managers_with_at_least_5_reports(cursor)
    connection.close()
    
    # Expected output: []
    print("Test Case 1: ", result)

# Step 4: Time and Space Complexity Analysis
"""
Time Complexity:
- The query involves a GROUP BY operation on the `ManagerId` column, which takes O(n) time where n is the number of rows in the table.
- The HAVING clause filters the grouped results, which is O(k), where k is the number of unique `ManagerId` values.
- The outer query performs a lookup on the `Id` column, which is O(m), where m is the number of rows in the table.
- Overall, the time complexity is O(n + k + m), which simplifies to O(n) for large datasets.

Space Complexity:
- The space complexity is O(k), where k is the number of unique `ManagerId` values stored during the GROUP BY operation.
- The result set size is O(r), where r is the number of managers with at least 5 direct reports.
- Overall, the space complexity is O(k + r), which simplifies to O(k) for large datasets.

Topic: SQL, Database Queries
"""

# Run the test cases
if __name__ == "__main__":
    test_find_managers_with_at_least_5_reports()