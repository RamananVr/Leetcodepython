"""
LeetCode Question #1587: Bank Account Summary II

Problem Statement:
Table: Transactions
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| account_id     | int     |
| day            | int     |
| amount         | int     |
+----------------+---------+
(account_id, day) is the primary key for this table.
Each row contains information about the transactions in a bank account.

Write an SQL query to report the following for each account_id:
1. The maximum balance of this account during the period covered by the table.
2. The total number of transactions for each account_id.

The balance of an account is defined as the sum of the amounts of all transactions for that account before or on that day. The maximum balance is the highest balance ever recorded for an account.

Return the result table in any order.

The query result format is in the following example:

Transactions table:
+------------+-----+--------+
| account_id | day | amount |
+------------+-----+--------+
| 1          | 1   | 500    |
| 1          | 2   | -200   |
| 1          | 3   | 300    |
| 2          | 1   | 800    |
| 2          | 2   | 100    |
| 3          | 1   | 200    |
| 3          | 2   | 300    |
| 3          | 3   | -400   |
+------------+-----+--------+

Result table:
+------------+----------------+---------------------+
| account_id | max_balance    | num_transactions    |
+------------+----------------+---------------------+
| 1          | 600            | 3                   |
| 2          | 900            | 2                   |
| 3          | 500            | 3                   |
+------------+----------------+---------------------+
"""

# Clean, Correct Python Solution
# Note: Since this is an SQL problem, the solution is provided as an SQL query.

solution_sql = """
WITH RunningBalance AS (
    SELECT
        account_id,
        day,
        SUM(amount) OVER (PARTITION BY account_id ORDER BY day) AS balance
    FROM Transactions
),
MaxBalance AS (
    SELECT
        account_id,
        MAX(balance) AS max_balance
    FROM RunningBalance
    GROUP BY account_id
),
TransactionCount AS (
    SELECT
        account_id,
        COUNT(*) AS num_transactions
    FROM Transactions
    GROUP BY account_id
)
SELECT
    t.account_id,
    m.max_balance,
    tc.num_transactions
FROM MaxBalance m
JOIN TransactionCount tc
ON m.account_id = tc.account_id;
"""

# Example Test Cases
"""
Input:
Transactions table:
+------------+-----+--------+
| account_id | day | amount |
+------------+-----+--------+
| 1          | 1   | 500    |
| 1          | 2   | -200   |
| 1          | 3   | 300    |
| 2          | 1   | 800    |
| 2          | 2   | 100    |
| 3          | 1   | 200    |
| 3          | 2   | 300    |
| 3          | 3   | -400   |
+------------+-----+--------+

Output:
+------------+----------------+---------------------+
| account_id | max_balance    | num_transactions    |
+------------+----------------+---------------------+
| 1          | 600            | 3                   |
| 2          | 900            | 2                   |
| 3          | 500            | 3                   |
+------------+----------------+---------------------+
"""

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the running balance using a window function: O(n), where n is the number of rows in the Transactions table.
- Calculating the maximum balance for each account_id: O(n).
- Counting the number of transactions for each account_id: O(n).
- Joining the results: O(n).

Overall time complexity: O(n).

Space Complexity:
- The space required for the intermediate tables (RunningBalance, MaxBalance, TransactionCount) is proportional to the number of rows in the Transactions table.
- Overall space complexity: O(n).
"""

# Topic: SQL, Window Functions, Aggregation