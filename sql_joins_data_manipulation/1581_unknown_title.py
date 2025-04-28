"""
LeetCode Problem #1581: Customer Who Visited but Did Not Make Any Transactions

Problem Statement:
Table: Visits
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| visit_id    | int     |
| customer_id | int     |
+-------------+---------+
visit_id is the primary key for this table.
This table contains information about the customers who visited the store.

Table: Transactions
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| transaction_id | int     |
| visit_id       | int     |
| amount         | int     |
+----------------+---------+
transaction_id is the primary key for this table.
This table contains information about the transactions made during the store visits.

Write an SQL query to find the IDs of the customers who visited the store but did not make any transactions. Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Visits
+----------+-------------+
| visit_id | customer_id |
+----------+-------------+
| 1        | 23          |
| 2        | 9           |
| 4        | 30          |
| 5        | 54          |
+----------+-------------+

Transactions
+----------------+----------+--------+
| transaction_id | visit_id | amount |
+----------------+----------+--------+
| 2              | 5        | 310    |
| 3              | 5        | 300    |
| 9              | 1        | 200    |
+----------------+----------+--------+

Output:
+-------------+
| customer_id |
+-------------+
| 9           |
| 30          |
+-------------+

Explanation:
Customer with ID = 23 visited the store and made transactions during the visit with IDs = 9.
Customer with ID = 9 visited the store but did not make any transactions.
Customer with ID = 30 visited the store but did not make any transactions.
Customer with ID = 54 visited the store and made transactions during the visit with IDs = 2 and 3.
Hence, we only include customers with IDs 9 and 30 in the result table.
"""

# Python Solution (Simulating the SQL Query with Pandas for Testing)

import pandas as pd

def customers_without_transactions(visits, transactions):
    """
    Function to find customers who visited but did not make any transactions.

    :param visits: DataFrame containing visit_id and customer_id
    :param transactions: DataFrame containing transaction_id, visit_id, and amount
    :return: DataFrame containing customer_id of customers who visited but did not make any transactions
    """
    # Merge visits with transactions on visit_id using a left join
    merged = pd.merge(visits, transactions, on='visit_id', how='left')
    
    # Filter rows where transaction_id is null (no transaction made)
    no_transactions = merged[merged['transaction_id'].isnull()]
    
    # Select unique customer_id
    result = no_transactions[['customer_id']].drop_duplicates()
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Input DataFrames
    visits_data = {
        "visit_id": [1, 2, 4, 5],
        "customer_id": [23, 9, 30, 54]
    }
    transactions_data = {
        "transaction_id": [2, 3, 9],
        "visit_id": [5, 5, 1],
        "amount": [310, 300, 200]
    }
    
    visits_df = pd.DataFrame(visits_data)
    transactions_df = pd.DataFrame(transactions_data)
    
    # Expected Output: customer_id = [9, 30]
    print(customers_without_transactions(visits_df, transactions_df))

"""
Time Complexity Analysis:
- Merging the two DataFrames (visits and transactions) takes O(n + m), where n is the number of rows in visits and m is the number of rows in transactions.
- Filtering rows where transaction_id is null takes O(n).
- Dropping duplicates takes O(k), where k is the number of unique customer_ids in the filtered DataFrame.
Overall time complexity: O(n + m).

Space Complexity Analysis:
- The space complexity is O(n + m) for storing the merged DataFrame.
- Additional space is used for the filtered DataFrame and the result, but this is proportional to the input size.
Overall space complexity: O(n + m).

Topic: SQL, Joins, Data Manipulation
"""