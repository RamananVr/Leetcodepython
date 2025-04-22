"""
LeetCode Problem #607: Sales Person

Problem Statement:
Table: SalesPerson
+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| sales_id        | int     |
| name            | varchar |
| salary          | int     |
| commission_rate | int     |
| hire_date       | date    |
+-----------------+---------+
sales_id is the primary key column for this table.

Table: Company
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| com_id      | int     |
| name        | varchar |
| city        | varchar |
+-------------+---------+
com_id is the primary key column for this table.

Table: Orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| order_date  | date |
| com_id      | int  |
| sales_id    | int  |
| amount      | int  |
+-------------+------+
order_id is the primary key column for this table.
com_id is a foreign key to the Company table.
sales_id is a foreign key to the SalesPerson table.

Write an SQL query to find the names of all the salespersons who did not have any orders related to the company with the name "RED".

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
SalesPerson table:
+----------+------+--------+----------------+------------+
| sales_id | name | salary | commission_rate| hire_date  |
+----------+------+--------+----------------+------------+
| 1        | John | 100000 | 6              | 2006-04-01 |
| 2        | Amy  | 12000  | 5              | 2010-05-01 |
| 3        | Mark | 65000  | 12             | 2008-12-25 |
| 4        | Pam  | 25000  | 25             | 2005-01-01 |
+----------+------+--------+----------------+------------+

Company table:
+--------+------+----------+
| com_id | name | city     |
+--------+------+----------+
| 1      | RED  | Boston   |
| 2      | ORANGE| New York|
| 3      | YELLOW| Boston  |
+--------+------+----------+

Orders table:
+----------+------------+--------+----------+--------+
| order_id | order_date | com_id | sales_id | amount |
+----------+------------+--------+----------+--------+
| 1        | 2014-01-01 | 3      | 1        | 10000  |
| 2        | 2014-01-02 | 1      | 2        | 5000   |
| 3        | 2014-01-03 | 3      | 3        | 50000  |
| 4        | 2014-01-04 | 2      | 4        | 25000  |
+----------+------------+--------+----------+--------+

Output:
+------+
| name |
+------+
| John |
| Mark |
| Pam  |
+------+
"""

# Python Solution
def find_salespersons_without_red_orders(salesperson, company, orders):
    """
    Function to find salespersons who did not have any orders related to the company named "RED".
    
    Args:
    salesperson (list of dict): List of salespersons with their details.
    company (list of dict): List of companies with their details.
    orders (list of dict): List of orders with their details.
    
    Returns:
    list: Names of salespersons who did not have any orders related to "RED".
    """
    # Step 1: Find the com_id of the company named "RED"
    red_com_id = None
    for com in company:
        if com['name'] == 'RED':
            red_com_id = com['com_id']
            break
    
    # Step 2: Find sales_ids that have orders related to "RED"
    sales_ids_with_red_orders = set()
    for order in orders:
        if order['com_id'] == red_com_id:
            sales_ids_with_red_orders.add(order['sales_id'])
    
    # Step 3: Find salespersons who are not in sales_ids_with_red_orders
    result = []
    for sp in salesperson:
        if sp['sales_id'] not in sales_ids_with_red_orders:
            result.append(sp['name'])
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Input Data
    SalesPerson = [
        {"sales_id": 1, "name": "John", "salary": 100000, "commission_rate": 6, "hire_date": "2006-04-01"},
        {"sales_id": 2, "name": "Amy", "salary": 12000, "commission_rate": 5, "hire_date": "2010-05-01"},
        {"sales_id": 3, "name": "Mark", "salary": 65000, "commission_rate": 12, "hire_date": "2008-12-25"},
        {"sales_id": 4, "name": "Pam", "salary": 25000, "commission_rate": 25, "hire_date": "2005-01-01"},
    ]

    Company = [
        {"com_id": 1, "name": "RED", "city": "Boston"},
        {"com_id": 2, "name": "ORANGE", "city": "New York"},
        {"com_id": 3, "name": "YELLOW", "city": "Boston"},
    ]

    Orders = [
        {"order_id": 1, "order_date": "2014-01-01", "com_id": 3, "sales_id": 1, "amount": 10000},
        {"order_id": 2, "order_date": "2014-01-02", "com_id": 1, "sales_id": 2, "amount": 5000},
        {"order_id": 3, "order_date": "2014-01-03", "com_id": 3, "sales_id": 3, "amount": 50000},
        {"order_id": 4, "order_date": "2014-01-04", "com_id": 2, "sales_id": 4, "amount": 25000},
    ]

    # Expected Output: ["John", "Mark", "Pam"]
    print(find_salespersons_without_red_orders(SalesPerson, Company, Orders))

# Time and Space Complexity Analysis
"""
Time Complexity:
- Finding the com_id of "RED": O(n), where n is the number of companies.
- Iterating through orders to find sales_ids related to "RED": O(m), where m is the number of orders.
- Iterating through salespersons to filter out those with "RED" orders: O(p), where p is the number of salespersons.
Overall: O(n + m + p)

Space Complexity:
- Storage for sales_ids_with_red_orders: O(k), where k is the number of unique sales_ids related to "RED".
- Storage for result: O(p), where p is the number of salespersons.
Overall: O(k + p)

Topic: SQL, Database Queries
"""