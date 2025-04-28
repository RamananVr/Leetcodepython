"""
LeetCode Problem #1532: The Most Recent Orders for Each Product

Problem Statement:
Table: Orders
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| product_id    | int     |
| quantity      | int     |
| order_date    | date    |
+---------------+---------+
(order_id, product_id) is the primary key for this table.

Write an SQL query to find the most recent order (by order_date) for each product. 
Return the product_id, quantity, and order_date of each product's most recent order.

The query result format is in the following example:

Orders table:
+----------+------------+----------+------------+
| order_id | product_id | quantity | order_date |
+----------+------------+----------+------------+
| 1        | 1          | 10       | 2020-07-01 |
| 2        | 1          | 15       | 2020-07-02 |
| 3        | 2          | 20       | 2020-07-01 |
| 4        | 2          | 30       | 2020-07-03 |
+----------+------------+----------+------------+

Result table:
+------------+----------+------------+
| product_id | quantity | order_date |
+------------+----------+------------+
| 1          | 15       | 2020-07-02 |
| 2          | 30       | 2020-07-03 |
+------------+----------+------------+
"""

# Python Solution (Simulating SQL Query Execution)

def most_recent_orders(orders):
    """
    Function to find the most recent order for each product.

    Args:
    orders (List[Dict]): A list of dictionaries representing the Orders table.

    Returns:
    List[Dict]: A list of dictionaries representing the result table.
    """
    from collections import defaultdict

    # Dictionary to store the most recent order for each product
    product_recent_order = defaultdict(lambda: {"quantity": 0, "order_date": None})

    for order in orders:
        product_id = order["product_id"]
        order_date = order["order_date"]

        # Update the most recent order for the product
        if product_recent_order[product_id]["order_date"] is None or order_date > product_recent_order[product_id]["order_date"]:
            product_recent_order[product_id] = {
                "quantity": order["quantity"],
                "order_date": order_date
            }

    # Convert the result to the desired format
    result = [{"product_id": product_id, "quantity": data["quantity"], "order_date": data["order_date"]} for product_id, data in product_recent_order.items()]
    return result

# Example Test Cases
if __name__ == "__main__":
    orders = [
        {"order_id": 1, "product_id": 1, "quantity": 10, "order_date": "2020-07-01"},
        {"order_id": 2, "product_id": 1, "quantity": 15, "order_date": "2020-07-02"},
        {"order_id": 3, "product_id": 2, "quantity": 20, "order_date": "2020-07-01"},
        {"order_id": 4, "product_id": 2, "quantity": 30, "order_date": "2020-07-03"},
    ]

    # Expected Output:
    # [
    #     {"product_id": 1, "quantity": 15, "order_date": "2020-07-02"},
    #     {"product_id": 2, "quantity": 30, "order_date": "2020-07-03"}
    # ]
    print(most_recent_orders(orders))

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the list of orders once, making the time complexity O(n), where n is the number of orders.

Space Complexity:
- The function uses a dictionary to store the most recent order for each product. In the worst case, the dictionary will have as many entries as there are unique products, making the space complexity O(p), where p is the number of unique products.

Topic: Hash Table
"""