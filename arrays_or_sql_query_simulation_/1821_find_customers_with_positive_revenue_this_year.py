"""
LeetCode Question #1821: Find Customers With Positive Revenue this Year

Problem Statement:
You are given a table `Customers` with the following structure:

| Column Name | Type    |
|-------------|---------|
| customer_id | int     |
| revenue     | int     |

Write an SQL query to find the IDs of all customers who have a positive revenue this year. Return the result table in any order.

The query result format is in the following example:

Example:
Input:
Customers table:
| customer_id | revenue |
|-------------|---------|
| 1           | 100     |
| 2           | -50     |
| 3           | 0       |
| 4           | 200     |

Output:
| customer_id |
|-------------|
| 1           |
| 4           |

Explanation:
Customers with IDs 1 and 4 have positive revenue (100 and 200, respectively).
"""

# Python Solution:
# Since this is an SQL problem, we will simulate the solution using Python for demonstration purposes.

def find_customers_with_positive_revenue(customers):
    """
    Function to find customers with positive revenue.

    Args:
    customers (list of dict): A list of dictionaries where each dictionary represents a customer with 'customer_id' and 'revenue'.

    Returns:
    list: A list of customer IDs with positive revenue.
    """
    return [customer['customer_id'] for customer in customers if customer['revenue'] > 0]

# Example Test Cases:
if __name__ == "__main__":
    # Test Case 1
    customers = [
        {"customer_id": 1, "revenue": 100},
        {"customer_id": 2, "revenue": -50},
        {"customer_id": 3, "revenue": 0},
        {"customer_id": 4, "revenue": 200}
    ]
    print(find_customers_with_positive_revenue(customers))  # Output: [1, 4]

    # Test Case 2
    customers = [
        {"customer_id": 5, "revenue": 0},
        {"customer_id": 6, "revenue": -10},
        {"customer_id": 7, "revenue": 50}
    ]
    print(find_customers_with_positive_revenue(customers))  # Output: [7]

    # Test Case 3
    customers = []
    print(find_customers_with_positive_revenue(customers))  # Output: []

# Time and Space Complexity Analysis:
# Time Complexity: O(n), where n is the number of customers in the input list. We iterate through the list once.
# Space Complexity: O(k), where k is the number of customers with positive revenue. This is the size of the output list.

# Topic: Arrays (or SQL Query Simulation)