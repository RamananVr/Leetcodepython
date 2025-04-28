"""
LeetCode Problem #1398: Customers Who Bought Products A and B but Not C

Problem Statement:
Table: Customers

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| customer_id | int     |
| product_key | char(1) |
+-------------+---------+
(customer_id, product_key) is the primary key for this table.
This table contains data about the IDs of customers and the products they bought (A, B, or C).

Write an SQL query to report the customer_id of customers who bought products A and B but did not buy product C since we want to recommend them product C.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Customers table:
+-------------+-------------+
| customer_id | product_key |
+-------------+-------------+
| 1           | A           |
| 2           | A           |
| 1           | B           |
| 1           | C           |
| 3           | A           |
| 3           | B           |
| 3           | C           |
| 4           | A           |
| 4           | B           |
+-------------+-------------+

Output:
+-------------+
| customer_id |
+-------------+
| 4           |
+-------------+

Explanation:
- The customer with ID=1 bought products A, B, and C.
- The customer with ID=2 bought only product A.
- The customer with ID=3 bought products A, B, and C.
- The customer with ID=4 bought products A and B but not C.
Thus, we recommend product C to the customer with ID=4.
"""

# Clean, Correct Python Solution
def customers_who_bought_a_and_b_but_not_c(customers):
    """
    This function simulates the SQL query for the problem using Python.
    It takes a list of tuples representing the Customers table and returns
    a list of customer IDs who bought products A and B but not C.
    """
    from collections import defaultdict

    # Create a dictionary to store the products bought by each customer
    customer_products = defaultdict(set)
    for customer_id, product_key in customers:
        customer_products[customer_id].add(product_key)

    # Find customers who bought A and B but not C
    result = []
    for customer_id, products in customer_products.items():
        if 'A' in products and 'B' in products and 'C' not in products:
            result.append(customer_id)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Input: Customers table as a list of tuples
    customers = [
        (1, 'A'),
        (2, 'A'),
        (1, 'B'),
        (1, 'C'),
        (3, 'A'),
        (3, 'B'),
        (3, 'C'),
        (4, 'A'),
        (4, 'B')
    ]

    # Expected Output: [4]
    print(customers_who_bought_a_and_b_but_not_c(customers))  # Output: [4]

# Time and Space Complexity Analysis
"""
Time Complexity:
- O(n), where n is the number of rows in the input list. We iterate through the list once to populate the dictionary
  and then iterate through the dictionary to check the conditions.

Space Complexity:
- O(m), where m is the number of unique customer IDs. We store the products bought by each customer in a dictionary.

Overall, the solution is efficient for the given problem.

Topic: Hash Table
"""