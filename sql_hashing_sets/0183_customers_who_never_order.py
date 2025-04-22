"""
LeetCode Question #183: Customers Who Never Order

Problem Statement:
Table: Customers
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| Id          | int     |
| Name        | varchar |
+-------------+---------+
Id is the primary key column for this table.

Table: Orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| Id          | int  |
| CustomerId  | int  |
+-------------+------+
Id is the primary key column for this table.

Write an SQL query to find all customers who never order anything.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Customers table:
+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+

Orders table:
+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 4          |
+----+------------+

Output:
+-------+
| Name  |
+-------+
| Joe   |
| Henry |
+-------+
"""

# Python Solution
# Since this is an SQL problem, we will write the SQL query as part of the solution.

def customers_who_never_order(customers, orders):
    """
    Simulates the SQL query to find customers who never placed an order.

    Args:
    customers (list of dict): List of customer records, where each record is a dictionary with keys 'Id' and 'Name'.
    orders (list of dict): List of order records, where each record is a dictionary with keys 'Id' and 'CustomerId'.

    Returns:
    list of str: List of customer names who never placed an order.
    """
    # Extract customer IDs who have placed orders
    ordered_customer_ids = {order['CustomerId'] for order in orders}

    # Find customers whose IDs are not in the ordered_customer_ids set
    result = [customer['Name'] for customer in customers if customer['Id'] not in ordered_customer_ids]

    return result

# Example Test Cases
if __name__ == "__main__":
    # Input data
    customers = [
        {"Id": 1, "Name": "Joe"},
        {"Id": 2, "Name": "Henry"},
        {"Id": 3, "Name": "Sam"},
        {"Id": 4, "Name": "Max"}
    ]

    orders = [
        {"Id": 1, "CustomerId": 3},
        {"Id": 2, "CustomerId": 4}
    ]

    # Expected Output: ['Joe', 'Henry']
    print(customers_who_never_order(customers, orders))

    # Additional Test Case
    customers = [
        {"Id": 1, "Name": "Alice"},
        {"Id": 2, "Name": "Bob"},
        {"Id": 3, "Name": "Charlie"}
    ]

    orders = [
        {"Id": 1, "CustomerId": 2}
    ]

    # Expected Output: ['Alice', 'Charlie']
    print(customers_who_never_order(customers, orders))

# Time and Space Complexity Analysis
"""
Time Complexity:
- Extracting ordered_customer_ids: O(m), where m is the number of orders.
- Filtering customers: O(n), where n is the number of customers.
- Overall: O(n + m).

Space Complexity:
- Space used for the ordered_customer_ids set: O(m).
- Space used for the result list: O(n).
- Overall: O(n + m).
"""

# Topic: SQL, Hashing, Sets